$("#new_game_btn").click(function (){

    console.log('test');

    $.ajax({

        type: "GET",
        url: "redir/",

    });
});

$("#send").click(function() {

    $.ajax({

        type: "GET",

        url: "game/",

        data: {

            'tittle': $("#quest").text(),
            "answer": $('input[name="option1"]:checked').val()
        },

        success: function (data) {
            $("#quest").html("<p id='quest'><b>{{ quest.quest }}</b></p>");
        }


    });

});