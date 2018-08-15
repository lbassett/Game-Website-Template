
function rendergame(gameid, player) {
    var url = "/get_game_status/" + gameid;
    var playercardshtml = "";
    var handshtml = "";
    $.getJSON(url, function(data) {
        
        var playernum;
        if (player == "player1") {
            playernum = 1;
        } else if (player == "player2") {
            playernum = 2
        }

        var i;
        colorcodes = ["Blue", "Yellow", "Orange", "Green", "Red", "Purple"];
        for (i = 0; i < 7; i++) {
            var cardstring = data[playernum+8][i];
            if (cardstring != "None") {
                var card = Number(cardstring);
                var cardcolornum = Math.floor(card / 10);
                var color = colorcodes[cardcolornum];
                var cardnum = (card % 10) + 1;
                playercardshtml += "<div class ='card' style = 'background-color:" + color + "'>" + cardnum.toString() + "</div>";
            } else {
                playercardshtml += "<div class ='card' background-color='white'>None</div>";
            }
        }
        document.getElementById('PlayerCards').innerHTML = playercardshtml;
        var j;
        for (j = 0; j < 9; j++) {
            var handlist = data[j];
            var p1cards = "";
            var p2cards = "";
            var k;
            for (k = 0; k<3; k++) {
                var cardstring = handlist[k];
                if (cardstring != "None") {
                    var card = Number(cardstring);
                    var cardcolornum = Math.floor(card / 10);
                    var color = colorcodes[cardcolornum];
                    var cardnum = (card % 10) + 1;
                    p1cards += "<div class ='card' style = 'background-color:" + color + "'>" + cardnum.toString() + "</div>";
                } else {
                    p1cards += "<div class ='card' background-color='white'>None</div>";
                }
            }
            var l;
            for (l = 4; l<6; l++) {
                var cardstring = handlist[l];
                if (cardstring != "None") {
                    var card = Number(cardstring);
                    var cardcolornum = Math.floor(card / 10);
                    var color = colorcodes[cardcolornum];
                    var cardnum = (card % 10) + 1;
                    p2cards += "<div class ='card' style = 'background-color:" + color + "'>" + cardnum.toString() + "</div>";
                } else {
                    p2cards += "<div class ='card' background-color='white'>None</div>";
                }
            }
            var flaghtml = "";
            if (handlist[3] == 1) {
                flaghtml += ;

            } else if (handlist[3] == 2) {

            }



            if (playernum == 1) {
                handshtml += "<div class = 'hand'><div class = 'tophand'>"+p2cards+"</div><div class= 'bottomhand'>"+ p1cards +"</div></div>";
            } else {
                handshtml += "<div class = 'hand'><div class = 'tophand'>"+p1cards+"</div><div class= 'bottomhand'>"+ p2cards +"</div></div>";
            }

        }



        document.getElementById('hands').innerHTML = ;
    });  
}