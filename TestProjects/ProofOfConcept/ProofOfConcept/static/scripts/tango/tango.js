var turn = 0;

$('#testButton').click(function () {
    if (turn === 0) {
        turn0();
        turn = turn + 1;
    }
    else if (turn === 1) {
        turn1();
        turn = turn + 1;
    }
    else if (turn === 2) {
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
    $(".tango-frame").contents().find("#input-email").val("email@gmail.com");
    $(".tango-frame").contents().find("#input-number").val("10");
    $(".tango-frame").contents().find("#input-text").val("Hello");
    $(".tango-frame").contents().find("#submitbutton").click();
}

function turn1() {
    $(".tango-frame").contents().find("#input-email").val("532");
    $(".tango-frame").contents().find("#input-number").val("-11");
    $(".tango-frame").contents().find("#input-text").val("150");
    $(".tango-frame").contents().find("#submitbutton").click();

}

function turn2() {
    $(".tango-frame").contents().find("#input-email").val("Hello");
    $(".tango-frame").contents().find("#input-number").val("Hello");
    $(".tango-frame").contents().find("#input-text").val("email@gmail.com");
    $(".tango-frame").contents().find("#submitbutton").click();

}

