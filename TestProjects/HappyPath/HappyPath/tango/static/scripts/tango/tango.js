$(function () {
    $('#pass-button').hide();
    $('#fail-button').hide();
});

$("#test-case-button").click(function () {
    $('#test-case-button').hide();
    $('#pass-button').show();
    $('#fail-button').show();
    runTestCase();
    updateCurrentCase();
});

$("#pass-button").click(function () {
    $('#pass-button').hide();
    $('#fail-button').hide();
    $('#test-case-button').show();

    cases[0]['tango_status'] = 'Pass';
    updateCases();
});

$("#fail-button").click(function () {
    $('#pass-button').hide();
    $('#fail-button').hide();
    $('#test-case-button').show();

    cases[0]['tango_status'] = 'Fail';
    updateCases();
});

$("#generate-cases-button").click(function () {
    let requestUrl = window.location.origin + "/tango/generate-cases";
    $.get(requestUrl, { form: JSON.stringify(form) },
        function (data) {
            allocateCases(data);
            updateCasesTable();
            $("#test-case-button").prop('disabled', false);
            updateCurrentCase();
    });
});

$("#add-case-button").click(function () {
    submitCustomCase();
    updateCasesTable();
    $("#test-case-button").prop('disabled', false);
    updateCurrentCase();
});

$("#results-table").on("click", "tr", function () {
    selectedPermutationIndex = $(this).index() - 1;
    updateSelectedPermutation(selectedPermutationIndex);
});

$("#delete-case-button").click(function () {
    cases.splice(selectedPermutationIndex, 1);
    updateCasesTable();
    updateStoredCases();
    updateCurrentCase();
});

$("#generate-manual-case-button").click(function () {
    let newCaseId = createCustomCase();
    createCustomCaseTable(newCaseId);
});

function runTestCase() {
    for (var i = 0; i < form.length; i++) {
        $("#tango-frame").contents().find("#id_" + form[i]['tango_name']).val(cases[0][form[i]['tango_name']]);
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
        return item['tango_save'];
    });

    $.get(requestUrl, { cases: JSON.stringify(savedCases), viewName: viewName })
}

function createCustomCase() {

    //TODO: Don't make Id's this way....maybe. it's easy but bad. Or at least check if the id exists first in the function
    newTestCase['tango_id'] = createNewId();
    newTestCase['tango_last_ran'] = "-";
    newTestCase['tango_importance'] = "-";
    newTestCase['tango_notes'] = "-";
    newTestCase['tango_test_data'] = "!";
    newTestCase['tango_status'] = "Not Ran";
    newTestCase['tango_save'] = false;

    for (let i = 0; i < form.length; i++) {
        newTestCase[form[i]['tango_name']] = form[i]['tango_name'];
    }

    return newTestCase["tango_id"];
}

function allocateCases(data) {
    cases = [];
    while (!isEmpty(data)) {
        let testCase = {}
        $.each(data, function (key, value) {
            testCase[key] = value[0];
            value.shift();
        });
        //TODO: Don't make Id's this way....maybe. it's easy but bad. Or at least check if the id exists first in the function
        testCase['tango_id'] = createNewId();
        testCase['tango_last_ran'] = "-";
        testCase['tango_importance'] = "-";
        testCase['tango_notes'] = "-";
        testCase['tango_test_data'] = "!";
        testCase['tango_status'] = "Not Ran";
        testCase['tango_save'] = false;
        cases.push(testCase);
    }

    function isEmpty(object) {
        for (var key in object) {
            if (object[key].length) {
                return false;
            }
        }
        return true;
    }
}

function updateCaseSaveStatus(data) {
    let caseIndex = data.parent().parent().index();

    if (data[0].checked) cases[caseIndex]['tango_save'] = true;
    else cases[caseIndex]['tango_save'] = false;

    updateStoredCases();
}

function createCustomCaseTable(caseId) {
    let html = '<h3 class="uk-heading-divider">Selected Case - ' + caseId + '</h1>';
    html += '<table class="uk-table uk-table-striped">';

    html += '<tr>';
    html += '<th>Form Item</th>';
    html += '<th>Test Value</th>';
    html += '</tr>';
    console.log(form);
    let j = 1;
    for (i in newTestCase) {
        if (!isTangoProperty(i)) {
            html += '<tr>';
            html += '<td>' + i + '</td>';
            html += '<td> <input id="testValue' + j + '" class="uk-input" type="text" placeholder="Input"> </td>';
            html += '</tr>';
            j = j + 1;
        }
    }

    html += '</table>';
    document.getElementById('custom-case-details').innerHTML = html;
}

function submitCustomCase() {
   
}

function updateCasesTable() {
    if (cases.length === 0) {
        document.getElementById('results-table').innerHTML = "";
        return;
    }

    var html = '<h3 class="uk-heading-divider">All Cases</h1>';
    html += '<table class="uk-table uk-table-striped">';

    html += '<tr>';
    html += '<th>ID</th>';
    html += '<th>Last Ran</th>';
    html += '<th>Importance</th>';
    html += '<th>Notes</th>';
    html += '<th>Save</th>';
    html += '</tr>';

    for (let i = 0; i < cases.length; i++) {
        if (cases[i]['tango_status'] == "Pass") {
            html += '<tr style="background-color: #CCFFCC; cursor: pointer" href="#case-details-modal" uk-toggle>';
        }
        else if (cases[i]['tango_status'] == "Fail") {
            html += '<tr style="background-color: #FFAD99; cursor: pointer" href="#case-details-modal" uk-toggle>';
        }
        else {
            html += '<tr href="#case-details-modal" style="cursor: pointer" uk-toggle>';
        }
        html += '<td>' + cases[i]['tango_id'] + '</td>';
        html += '<td>' + cases[i]['tango_last_ran'] + '</td>';
        html += '<td>' + cases[i]['tango_importance'] + '</td>';
        html += '<td>' + cases[i]['tango_notes'] + '</td>';
        html += '<td> <input class="uk-checkbox" type="checkbox" onclick="updateCaseSaveStatus($(this)); event.stopPropagation()"/> </td>';
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

    var html = '<h3 class="uk-heading-divider">Current Case - ' + cases[0]['tango_id'] + '</h1>';
    html += '<table class="uk-table uk-table-striped">';

    html += '<tr>';
    html += '<th>Form Item</th>';
    html += '<th>Test Value</th>';
    html += '</tr>';
    for (i in cases[0]) {
        if (!isTangoProperty(i)) {
            html += '<tr>';
            html += '<td>' + i + '</td>';
            html += '<td>' + cases[0][i] + '</td>';
            html += '</tr>';
        }
    }

    html += '</table>';
    document.getElementById('current-case').innerHTML = html;
}

function updateSelectedPermutation() {

    var html = '<h3 class="uk-heading-divider">Selected Case - ' + cases[selectedPermutationIndex]['tango_id'] + '</h1>';
    html += '<table class="uk-table uk-table-striped">';

    html += '<tr>';
    html += '<th>Form Item</th>';
    html += '<th>Test Value</th>';
    html += '</tr>';

    for (i in cases[selectedPermutationIndex]) {
        if (!isTangoProperty(i)) {
            html += '<tr>';
            html += '<td>' + i + '</td>';
            html += '<td>' + cases[selectedPermutationIndex][i] + '</td>';
            html += '</tr>';
        }
    }

    html += '</table>';
    document.getElementById('selected-case-details').innerHTML = html;
}

function isTangoProperty(property) {
    let tangoProperties
        = ['tango_id', 'tango_last_ran', 'tango_notes', 'tango_test_data', 'tango_status', 'tango_importance', 'tango_save', 'tango_name'];

    return tangoProperties.indexOf(property) > -1;
}

function createNewId() {
    return Math.random().toString(36).substr(2, 8);
}