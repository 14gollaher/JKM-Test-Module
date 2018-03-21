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
            if (cases.length) $("#test-case-button").prop('disabled', false);
        });
}

function createCustomCase() {
    newTestCase['id'] = createNewId();
    newTestCase['last_ran'] = "-";
    newTestCase['importance'] = "1";
    newTestCase['notes'] = "";
    newTestCase['status'] = "Not Ran";
    newTestCase['save'] = false;

    for (i in cases[selectedPermutationIndex]['test_data']) {
        let html = '<tr>';
        html += '<td>' + cases[selectedPermutationIndex]['test_data'][i]['name'] + '</td>';
        html += '<td class="uk-panel uk-panel-box uk-text-truncate">' + cases[selectedPermutationIndex]['test_data'][i]['test_value'] + '</td>';
        html += '</tr>';
    }

    return newTestCase["id"];
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
            test_input['selector'] = permutations[i]['selector'];
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
    for (let i = 0; i < components.length; i++) {
        newTestCase[component[i]['name']] = $('#custom_value_' + component[i]['name']).val();
    }
    cases.unshift(newTestCase);
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
        html += '<td class="uk-panel uk-panel-box uk-text-truncate">' + cases[selectedPermutationIndex]['test_data'][i]['test_value'] + '</td>';
        html += '</tr>';
    }

    html += '</table>';
    document.getElementById('selected-case-details').innerHTML = html;

    //html generated for the footer of the modal
    html = '<button onclick="deleteCase()" style="float: left" class="uk-button uk-button-default uk-modal-close uk-button-danger" type="button">Delete Case</button>'
    html += ' <button style="margin-right:10px" onclick= "updateSelectedCase(' + selectedPermutationIndex + ')" class="uk-button uk-button-default uk-modal-close uk-button-primary" type= "button" id= "update-case-button" > Apply</button >'
    html += '<button class="uk-button uk-button-default uk-modal-close" type= "button" > Close </button>'

    document.getElementById('selected-case-footer').innerHTML = html;
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
        html += '<td>' + cases[0]['test_data'][i]['selector'] + '</td>';
        html += '</tr>';
    }
    html += '</table>';
    document.getElementById('selectors-table').innerHTML = html;
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
    updateCasesTable();
    updateStoredCases();
}

function updateCurrentNote(data) {
    cases[data]['notes']  = $('#notes-textarea').val();
}