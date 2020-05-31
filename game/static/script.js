$("#send").click(function() {
    var tittle =  $("#quest").text();
    var answer = $('input[name="option1"]:checked').val();
    $.ajax({
        type: "GET",
        url: "game/",
        data: {
            "tittle": tittle,
            "answer": answer
        },
        dataType: "text",
        cache: false,

        success:function(url){
            document.location.href = url
        }
    });
});