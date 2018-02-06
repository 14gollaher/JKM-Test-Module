$("#test-case-button").click(function () {
    $('#test-case-button').hide();
    $('#pass-button').show();
    $('#fail-button').show();
    runTestCase();
});

$(function () {
    $('#pass-button').hide();
    $('#fail-button').hide();
});

$("#pass-button").click(function () {
    $('#pass-button').hide();
    $('#fail-button').hide();
    $('#test-case-button').show();

});

$("#fail-button").click(function () {
    $('#pass-button').hide();
    $('#fail-button').hide();
    $('#test-case-button').show();
});

$("#generate-permutations-button").click(function () {
    generatePermutations();
});


function runTestCase() {
    updateCurrentPermutation();
    for (var i = 0; i < form.length; i++) {
        $("#tango-frame").contents().find("#id_" + form[i]['tango_name']).val(permutations[0][form[i]['tango_name']]); 
        permutations.push(permutations.splice(0, 1)[0]);
    }
}

function generatePermutations() {
    let requestUrl = window.location.origin + "/tango/generate-permutations";
    $.get(requestUrl, { form: JSON.stringify(form) },
        function (data) {
            allocatePermutations(data);
            updatePermutationsTable();
            $("#test-case-button").prop('disabled', false);
        });
}

function allocatePermutations(data) {
    permutations = [];
    while (!isEmpty(data)) {
        let permutation = {}
        $.each(data, function (key, value) {
            permutation[key] = value[0];
            value.shift();
        });
        permutation['tango_id'] = createNewId();
        permutation['tango_last_ran'] = "-"
        permutation['tango_notes'] = ""
        permutation['tango_test_data'] = "!"
        permutation['tango_status'] = "Not Ran"
        permutations.push(permutation);
    }
}

function isEmpty(object) {
    for (var key in object) {
        if (object[key].length) {
            return false;
        }
    }
    return true;
}

function updatePermutationsTable() {

    var html = '<h3 class="uk-heading-divider">All Permutations</h1>';
    html += '<table class="uk-table uk-table-striped">';
    html += '<tr>';

    html += '<th>ID</th>';
    html += '<th>Last Ran</th>';
    html += '<th>Notes</th>';
    html += '<th>Test Data</th>';

    html += '</tr>';
    for (var i = 0; i < permutations.length; i++) {
        html += '<tr>';
        html += '<td>' + permutations[i]['tango_id'] + '</td>';
        html += '<td>' + permutations[i]['tango_last_ran'] + '</td>';
        html += '<td>' + permutations[i]['tango_notes'] + '</td>';
        html += '<td>' + permutations[i]['tango_test_data'] + '</td>';
        html += '</tr>';
    }
    html += '</table>';
    document.getElementById('results-table').innerHTML = html;
}

function updateCurrentPermutation() {

    var html = '<h3 class="uk-heading-divider">Current Permutation</h1>';

    html += '<ul class="uk-list uk-list-striped">';

    for (i in permutations[0]) {
        if (!isTangoProperty(i)) {
            html += '<li>' + i + '  -  ' + permutations[0][i] + '</li>';
        }
    }

    html += '</ul';
    document.getElementById('current-permutation').innerHTML = html;
}

function isTangoProperty(property) {
    let tangoProperties = ['tango_id', 'tango_last_ran', 'tango_notes', 'tango_test_data', 'tango_status'];

    return tangoProperties.indexOf(property) > -1;
}

function createNewId() {
    return Math.random().toString(36).substr(2, 8);
}