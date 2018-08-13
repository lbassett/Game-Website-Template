
function rendergame(gameid, player) {
    var url = "/get_game_status/" + gameid;
    var playercardshtml = "";
    $.getJSON(url, function(data) {
        
        var playernum;
        if (player == "player1") {
            playernum = 1;
        }
        else if (player == "player2") {
            playernum = 2
        }

        var alertmessage = "";

        var i;
        colorcodes = ["Blue", "Yellow", "Orange", "Green", "Red", "Purple"];
        for (i = 0; i < 7; i++) {
            var cardstring = data[playernum+8][i];
            if (cardstring != "None") {
                var card = Number(cardstring);
                var cardcolornum = Math.floor(card / 10);
                var color = colorcodes[cardcolornum];
                var cardnum = (card % 10) + 1;
                playercardshtml += "<div class ='card' background-color='" + color + "'>" + cardnum.toString() + "</div>";
                alertmessage+= cardnum.toString() + ", ";
            }
            else {
                playercardshtml += "<div class ='card' background-color='white'>None</div>";

            }
        


        }



    });  

    alert(playercardshtml);
    document.getElementById('PlayerCards').innerHTML = playercardshtml;
}