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
        $("#tango-frame").contents().find("#id_" + form[i].name).val(chance.string()); 
    }
}

function generatePermutations() {
    var requestUrl = window.location.origin + "/tango/generate-permutations";

    //$.get(requestUrl, { form: form })
    //    .done(function (data) {
    //        alert("Data Loaded: " + data);
    //    });

    $.ajax({
        "type": "GET",
        "dataType": "json",
        "url": requestUrl,
        "data": JSON.stringify(form),
        "success": function (result) {
            alert("yay!");
        },
    });
}





