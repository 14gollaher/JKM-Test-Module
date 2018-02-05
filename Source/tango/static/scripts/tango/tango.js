$("#testButton").click(function () {
    getPermutations();
    generatePermutation();
});

formFieldNames = ['firstName', 'lastName', 'emailAddress', 'age']
formFieldTypes = ['string', 'string', 'email', 'integer']

function generatePermutation() {
    for (var i = 0; i < formFieldNames.length; i++) {
        $("#tango-frame").contents().find("#id_" + formFieldNames[i]).val(chance.string()); 
    }
}

function getPermutations() {
    var requestUrl = window.location.origin + "/tango/permutations";
    $.get(requestUrl, function (data) {
        var existingsTests = data;
    });
}



