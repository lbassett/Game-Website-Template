function rendergame(gameid) {
    var url = "/get_game_status/" + gameid;
    var playercardshtml = ""
    $.getJSON(url, function(data) {


    });   
    document.getElementById('PlayerCards').innerHTML = playercardshtml;
}