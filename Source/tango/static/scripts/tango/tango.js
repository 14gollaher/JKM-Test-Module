var turn = 0;
$(function () {
    $('#passButton').hide();
    $('#failButton').hide();
});

$('#testButton').click(function () {
    if (turn === 0) {
        turn0();
        turn = turn + 1;
    }
    else if (turn === 1){
        turn1();
        turn = turn + 1;
    }
    else if(turn === 2){
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
    $("#viewTestIFrame").contents().find("#emailInput").val("email@gmail.com");
    $("#viewTestIFrame").contents().find("#numberInput").val("10");
    $("#viewTestIFrame").contents().find("#textInput").val("Hello");
}

function turn1() {
    $("#viewTestIFrame").contents().find("#emailInput").val("532");
    $("#viewTestIFrame").contents().find("#numberInput").val("-11");
    $("#viewTestIFrame").contents().find("#textInput").val("150");
}

function turn2() {
    $("#viewTestIFrame").contents().find("#emailInput").val("Hello");
    $("#viewTestIFrame").contents().find("#numberInput").val("Hello");
    $("#viewTestIFrame").contents().find("#textInput").val("email@gmail.com");
}

