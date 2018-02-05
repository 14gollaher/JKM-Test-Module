$("#testButton").click(function () {
    //getPermutations();
    generatePermutation();
});

function generatePermutation() {
    for (var i = 0; i < forms.length; i++) {
        $("#tango-frame").contents().find("#id_" + forms[i].name).val(chance.string()); 
    }
}

function getPermutations() {
    var requestUrl = window.location.origin + "/tango/permutations";
    $.get(requestUrl, function (data) {
        var existingsTests = data;
    });
}



