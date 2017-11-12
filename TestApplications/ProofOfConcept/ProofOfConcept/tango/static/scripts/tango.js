var turn = 0;
$(function () {
    $('#passButton').hide();
    $('#failButton').hide();
});

$('#testButton').click(function () {
    if (turn == 0) {
        turn0();
        turn = turn + 1;
    }
    else if (turn == 1){
        turn1();
        turn = turn + 1;
    }
    else if(turn == 2){
        turn2();
        turn = 0;
    }

    $('#passButton').show();
    $('#failButton').show();
    $('#testButton').hide();
    
});

$('#passButton').click(function () {
    $('#passButton').hide();
    $('#failButton').hide();
    $('#testButton').show();
});

$('#failButton').click(function () {
    $('#passButton').hide();
    $('#failButton').hide();
    $('#testButton').show();
});

function turn0() {
    $("#userAppIframe").contents().find("#emailInput").val("email@gmail.com");
    $("#userAppIframe").contents().find("#numberInput").val("10");
    $("#userAppIframe").contents().find("#textInput").val("Hello");
}

function turn1() {
    $("#userAppIframe").contents().find("#emailInput").val("532");
    $("#userAppIframe").contents().find("#numberInput").val("-11");
    $("#userAppIframe").contents().find("#textInput").val("150");
}

function turn2() {
    $("#userAppIframe").contents().find("#emailInput").val("Hello");
    $("#userAppIframe").contents().find("#numberInput").val("Hello");
    $("#userAppIframe").contents().find("#textInput").val("email@gmail.com");
}

