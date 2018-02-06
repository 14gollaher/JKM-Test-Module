$("#testButton").click(function () {
    //getPermutations();
    generatePermutations();
    $('#testButton').hide();
    $('#passButton').show();
    $('#failButton').show();
});

$(function () {
    $('#passButton').hide();
    $('#failButton').hide();
});

$("#passButton").click(function () {
    $('#passButton').hide();
    $('#failButton').hide();
    $('#testButton').show();
});

$("#failButton").click(function () {
    $('#passButton').hide();
    $('#failButton').hide();
    $('#testButton').show();
});


function generatePermutation() {
    for (var i = 0; i < form.length; i++) {
        let caseValue = getCaseValue(form[i].name);
        $("#tango-frame").contents().find("#id_" + form[i].name).val(caseValue); 
    }
}

function generatePermutations() {

    let requestUrl = window.location.origin + "/tango/generate-permutations";
    $.get(requestUrl, { form: JSON.stringify(form) },
        function (data) {
            var permutations = data;
        });
}

function





