
function rendergame(gameid, player) {
    var url = "/get_game_status/" + gameid;
    var playercardshtml = "";
    $.getJSON(url, function(data) {
        
        var i;
        colorcodes = ["Blue", "Yellow", "Orange", "Green", "Red", "Purple"];
        for (i = 0; i < 9; i++) {
            var cardstring = data[9][i];
            if (cardstring != "None") {
                var card = Number(cardstring);
                var cardcolornum = Math.floor(card / 10);
                var color = colorcodes[cardcolornum];
                var cardnum = (card % 10) + 1;
                playercardshtml += "<div class ='card' background-color='" + color + "'>" + cardnum.toString() + "</div>";
            }
            else {
                playercardshtml += "<div class ='card' background-color='white'>None</div>";

            }
        
        }





    });   
    document.getElementById('PlayerCards').innerHTML = playercardshtml;
}