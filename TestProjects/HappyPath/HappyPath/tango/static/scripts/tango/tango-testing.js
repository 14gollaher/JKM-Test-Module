$(function () {
    $('#pass-button').hide();
    $('#fail-button').hide();
    updateNoCases();
    getStoredCases();
});

$("#test-case-button").click(function () {
    $('#test-case-button').hide();
    $('#pass-button').show();
    $('#fail-button').show();
    runTestCase();
    updateCurrentCase();
});

$("#pass-button").click(function () {
    runTestCase();
    updateCurrentCase();

    cases[0]['status'] = 'Pass';
    updateCases();
    passedCaseNotification();
});

$("#fail-button").click(function () {
    $('#pass-button').hide();
    $('#fail-button').hide();
    $('#test-case-button').show();
    $("#case-fail-notes").val("");
});

$("#update-fail-button").click(function () {
    cases[0]['status'] = 'Fail';
    updateCases();
    
    updateFailedCase();
    updateCasesTable();
    updateStoredCases();
    failedCaseNotification();
});

$("#add-case-button").click(function () {
    submitCustomCase();
    updateCasesTable();
    updateCurrentCase();
    updateCasesExist();
});

$("#update-notes-button").click(function () {
    updateCurrentNote();
});

$("#results-table").on("click", "tr", function () {
    selectedPermutationIndex = $(this).index() - 1;
    updateSelectedPermutation(selectedPermutationIndex);
});

$("#generate-manual-case-button").click(function () {
    let newCaseId = createCustomCase();
    createCustomCaseTable(newCaseId);
});

$("#edit-selectors-button").click(function () {
    UIkit.modal('#edit-selectors-modal').show();
    updateSelectorsTable();
});

UIkit.util.on('#generate-cases-button', 'click', function (e) {
    e.preventDefault();
    e.target.blur();
    if (cases.length > 0) {
        UIkit.modal.confirm('Previous unsaved cases will be overwritten!').then(function () {
            generatePermutationsAjax();
        }, function () {
        });
    }
    else {
        generatePermutationsAjax();
    }
});

function generatePermutationsAjax() {
    let requestUrl = window.location.origin + "/tango/generate-permutations";
    $.get(requestUrl, { viewName: viewName },
        function (data) {
            createCases(data);
            updateCasesTable();
            updateCurrentCase();
            updateCasesExist();
        });
}

function passedCaseNotification() {
    UIkit.notification({
        message: 'Test Passed!',
        status: 'success',
        pos: 'bottom-right',
        timeout: 1000
    });
}

function failedCaseNotification() {
    UIkit.notification({
        message: 'Test Failed!',
        status: 'danger',
        pos: 'bottom-right',
        timeout: 1000
    });
}

function runTestCase() {
    for (i in cases[0]['test_data']) {
        $("#tango-frame").contents().find(cases[0]['test_data'][i]['selector']).val(cases[0]['test_data'][i]['test_value']);
    }
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth() + 1;

    let yyyy = today.getFullYear();
    if (dd < 10) {
        dd = '0' + dd;
    }
    if (mm < 10) {
        mm = '0' + mm;
    }
    today = dd + '/' + mm + '/' + yyyy;
    cases[0]['last_ran'] = today

}

function updateCases() {
    cases.push(cases.splice(0, 1)[0]); // Moves array position 0 to back
    updateCasesTable();
    updateStoredCases();
}

// TODO: Make this work as a POST
function updateStoredCases() {
    let requestUrl = window.location.origin + "/tango/save-cases";

    let savedCases = cases.filter(function (item) {
        return item['save'] == "true";
    });

    $.get(requestUrl, { cases: JSON.stringify(savedCases), viewName: viewName })
}

function getStoredCases() {
    let requestUrl = window.location.origin + "/tango/get-cases";
    $.get(requestUrl, { viewName: viewName },
        function (data) {
            cases = data;
            updateCasesTable();
            updateCurrentCase();
            if (cases.length) updateCasesExist()
        });
}

function createCustomCase() {
    newTestCase['id'] = createNewId();
    newTestCase['last_ran'] = "-";
    newTestCase['importance'] = "1";
    newTestCase['notes'] = "";
    newTestCase['status'] = "Not Ran";
    newTestCase['save'] = false;
    return newTestCase["id"];
}

function createCustomCaseTable(caseId) {
    let html = '<h3 class="uk-heading-divider">New Case - ' + caseId + '</h1>';
    html += '<table class="uk-table uk-table-striped">';

    html += '<tr>';
    html += '<th>Field Name</th>';
    html += '<th>Value</th>';
    html += '</tr>';
    for (i in fieldNames) {
        html += '<tr>';
        html += '<td>' + fieldNames[i] + '</td>';
        html += '<td> <input id="custom-case-new-' + fieldNames[i] + '" class="uk-input" type="text" placeholder="Input"> </td>';
        html += '</tr>';
    }

    html += '</table>';
    document.getElementById('custom-case-details').innerHTML = html;
}

function createCases(permutations) {
    cases = cases.filter(function (item) {
        return item['save'] == "true";
    });

    while (isMoreTestValues(permutations)) {
        for (i in permutations) {
            let testCase = {}
            testCase['id'] = createNewId();
            testCase['last_ran'] = "-";
            testCase['importance'] = "1";
            testCase['notes'] = "";
            testCase['status'] = "Not Ran";
            testCase['save'] = 'false';
            testCase['test_data'] = getTestData(permutations);
            cases.push(testCase);
        }
    }

    function getTestData(permutations) {
        let test_data = []

        for (i in permutations) {
            let test_input = {}
            if (permutations[i]['test_values'].length > 0) {
                test_input['test_value'] = permutations[i]['test_values'][0];
            }
            else {
                test_input['test_value'] = ''
            }
            test_input['name'] = permutations[i]['name'];

            if (cases.length > 0) {
                test_input['selector'] = cases[0]['test_data'][i]['selector'];
            }
            else {
                test_input['selector'] = permutations[i]['selector'];
            }
            test_data.push(test_input);
            permutations[i]['test_values'].shift();
        }

        return test_data;
    }

    function isMoreTestValues(permutations) {
        for (i in permutations) {
            if (permutations[i]['test_values'].length > 0) {
                return true;
            }
        }
        return false;
    }
}

function updateCaseSaveStatus(data) {
    let caseIndex = data.parent().parent().index() - 1;

    if (data[0].checked) cases[caseIndex]['save'] = "true";
    else cases[caseIndex]['save'] = "false";

    updateStoredCases();
}

function openNotesModal(data) {
    var caseIndex = data.parent().parent().index() - 1;
    let html = '<h3 class="uk-heading-divider">Notes for Case - ' + cases[caseIndex]['id'] + '</h1>';
    document.getElementById('notes-text').innerHTML = html;

    html = ' <button onclick= "updateCurrentNote(' + caseIndex + ')" style= "float: left"class="uk-button uk-button-default uk-modal-close uk-button-primary" type= "button" id= "update-notes-button" > Update</button >';
    html += ' <button class="uk-button uk-button-default uk-modal-close" type="button">Close</button>';
    document.getElementById('notes-footer').innerHTML = html;

    $('#notes-textarea').val(cases[caseIndex]['notes']);

    UIkit.modal('#case-notes-modal').show();
}

function submitCustomCase() {
    let newTestData = [];

    for (i in fieldNames) {
        let newFieldValue = {};
        newFieldValue['name'] = fieldNames[i];
        newFieldValue['test_value'] = $('#custom-case-new-' + newFieldValue['name']).val();

        if (cases.length > 0) {
            newFieldValue['selector'] = cases[0]['test_data'][i]['selector'];
        }
        else {
            newFieldValue['selector'] = '#id_' + newFieldValue['name'];
        }
        newTestData.push(newFieldValue);
    }
    newTestCase['test_data'] = newTestData;
    console.log(newTestCase);
    cases.unshift(newTestCase);
    console.log(cases);
    newTestCase = {};
}

function updateCasesTable() {
    if (cases.length === 0) {
        document.getElementById('results-table').innerHTML = "";
        return;
    }

    var html = '<h3 class="uk-heading-divider">All Cases</h1>';
    html += '<table class="uk-table uk-table-striped ">';

    html += '<tr>';
    html += '<th>ID</th>';
    html += '<th>Last Ran</th>';
    html += '<th>Importance</th>';
    html += '<th>Notes</th>';
    html += '<th>Save</th>';
    html += '</tr>';

    for (let i = 0; i < cases.length; i++) {
        if (cases[i]['status'] == "Pass") {
            html += '<tr style="background-color: #CCFFCC; cursor: pointer" href="#case-details-modal" uk-toggle>';
        }
        else if (cases[i]['status'] == "Fail") {
            html += '<tr style="background-color: #FFAD99; cursor: pointer" href="#case-details-modal" uk-toggle>';
        }
        else {
            html += '<tr href="#case-details-modal" style="cursor: pointer" uk-toggle>';
        }
        html += '<td>' + cases[i]['id'] + '</td>';
        html += '<td>' + cases[i]['last_ran'] + '</td>';
        html += '<td>' + cases[i]['importance'] + '</td>';
        html += '<td> <a uk-icon="warning" onclick= "openNotesModal($(this)); event.stopPropagation()" /> </td > ';

        if (cases[i]['save'] == "true") html += '<td> <input checked '
        else html += '<td> <input '

        html += 'class="uk-checkbox" type= "checkbox" onclick= "updateCaseSaveStatus($(this)); event.stopPropagation()" /> </td > ';
        html += '</tr>';
    }

    html += '</table>';
    document.getElementById('results-table').innerHTML = html;
}

function updateCurrentCase() {
    if (cases.length === 0) {
        document.getElementById('current-case').innerHTML = "";
        return;
    }

    var html = '<h3 class="uk-heading-divider">Current Case - ' + cases[0]['id'] + '</h1>';
    html += '<table class="uk-table uk-table-striped">';

    html += '<tr>';
    html += '<th>Field Name</th>';
    html += '<th>Test Value</th>';
    html += '</tr>';
    for (i in cases[selectedPermutationIndex]['test_data']) {
        html += '<tr>';
        html += '<td>' + cases[selectedPermutationIndex]['test_data'][i]['name'] + '</td>';
        html += '<td class="uk-panel uk-panel-box uk-text-truncate">' + cases[selectedPermutationIndex]['test_data'][i]['test_value'] + '</td>';
        html += '</tr>';
    }
    html += '</table>';
    document.getElementById('current-case').innerHTML = html;
}

function updateSelectedPermutation(selectedPermutationIndex) {
    var html = '<h3 class="uk-heading-divider">Selected Case - ' + cases[selectedPermutationIndex]['id'] + '</h1>';
    html += '<table class="uk-table uk-table-striped">';

    html += '<tr>';
    html += '<th>Field Name</th>';
    html += '<th>Test Value</th>';
    html += '</tr>';

    for (i in cases[selectedPermutationIndex]['test_data']) {
        html += '<tr>';
        html += '<td>' + cases[selectedPermutationIndex]['test_data'][i]['name'] + '</td>';
        html += '<td> <input id="custom-case-update-' + cases[selectedPermutationIndex]['test_data'][i]['name'] + '" class="uk-input" type="text" value="' + cases[selectedPermutationIndex]['test_data'][i]['test_value'] + '"></td>';
        html += '</tr>'; 
    }

    html += '</table>';

    document.getElementById('selected-case-details').innerHTML = html;

    // generated for the footer of the modal
    html = '<button onclick="deleteCase()" style="float: left" class="uk-button uk-button-default uk-modal-close uk-button-danger" type="button">Delete Case</button>'
    html += ' <button style="margin-right:10px" onclick= "updateSelectedCase(' + selectedPermutationIndex + ')" class="uk-button uk-button-default uk-modal-close uk-button-primary" type= "button" id= "update-case-button" > Apply</button >'
    html += '<button class="uk-button uk-button-default uk-modal-close" type= "button" > Close </button>'

    document.getElementById('selected-case-footer').innerHTML = html;
    
    let number = cases[selectedPermutationIndex]['importance'];
    $('#importanceRating' + number).prop('checked', true);
}

function updateSelectorsTable() {
    var html = '<h3 class="uk-heading-divider">Selectors</h1>';
    html += '<table class="uk-table uk-table-striped">';
    html += '<tr>';
    html += '<th>Field Name</th>';
    html += '<th>Selector</th>';
    html += '</tr>';
    for (i in cases[0]['test_data']) {
        html += '<tr>';
        html += '<td>' + cases[0]['test_data'][i]['name'] + '</td>';
        html += '<td> <input id="custom-selector' + i + '" class="uk-input" type="text" value="' + cases[0]['test_data'][i]['selector'] + '"></td>';
        html += '</tr>';
    }
    html += '</table>';
    document.getElementById('selectors-table').innerHTML = html;

    //TODO: Move me to HTML since I'm static
    html = '<button style="margin-right:10px" onclick= "updateSelectors()" class="uk-button uk-button-default uk-modal-close uk-button-primary" type= "button" id= "update-case-button" > Apply</button >'
    html += '<button class="uk-button uk-button-default uk-modal-close" type= "button" > Close </button>'
    document.getElementById('edit-selectors-footer').innerHTML = html;
}

function deleteCase() {
    cases.splice(selectedPermutationIndex, 1);
    updateCasesTable();
    updateStoredCases();
    updateCurrentCase();
    updateCasesExist();
    if (cases.length) updateNoCases();
}

function updateNoCases() {
    $("#test-case-button").prop('disabled', true);
    $("#edit-selectors-button").prop('disabled', true);

}

function updateCasesExist() {
    $("#test-case-button").prop('disabled', false);
    $("#edit-selectors-button").prop('disabled', false);
}

function createNewId() {
    return Math.random().toString(36).substr(2, 8);
}

function updateFailedCase() {
    cases[cases.length - 1]['importance'] = $("input[name=importanceRating]:checked").val()
    cases[cases.length - 1]['notes'] = $("#case-fail-notes").val()
}

function updateSelectedCase(data) {
    cases[data]['importance'] = $("input[name=importanceRating]:checked").val()
    for (i in cases[data]['test_data']) {
        cases[data]['test_data'][i]['test_value'] = document.getElementById("custom-case-update-" + cases[data]['test_data'][i]['name']).value;
    }
    updateCasesTable();
    updateStoredCases();
    updateCurrentCase();
}

function updateCurrentNote(data) {
    cases[data]['notes'] = $('#notes-textarea').val();
}

function updateSelectors() {
    for (i in cases) {
        for (j in cases[i]['test_data']) {
            cases[i]['test_data'][j]['selector'] = document.getElementById("custom-selector" + j).value;
        }
    }

    updateCasesTable();
    updateStoredCases();
    updateCurrentCase();
}