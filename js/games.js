
function getopengames(username) {
    var url = '/get_opengames';
    var opentablehtml = '<h3>Available Games</h3><table id="opengamelist"><tr bgcolor = "#B9B9B9"><th>Game</th><th>Competitor</th><th>Join</th></tr>';
    var pendingtablehtml = '<h3>Waiting for Opponent</h3><table id="pendinggamelist"><tr bgcolor = "#B9B9B9"><th>Game</th></tr>';
    $.getJSON(url, function(data) {
        var i;
        for (i = 0; i < data.length; i++) {
            if (data[i][1] == username){
                pendingtablehtml += '<tr bgcolor="#EDEDED"><td>' + data[i][0] + '</td>';
            } else {
                opentablehtml += '<tr bgcolor="#EDEDED"><td>' + data[i][0] + '</td><td>' + data[i][1] + '</td><td><div class="button join" onclick="joingame(' + data[i][0] + ')">Join</div></td></r>';
            }
        }
        opentablehtml += '</table>';
        pendingtablehtml += '</table>';
        var opentableshtml = opentablehtml + pendingtablehtml;
        document.getElementById('opengametables').innerHTML = opentableshtml;
    });

}

function getcurrentgames(username) {
    var url = '/get_currentgames'; // data received is of the form [idnum, player1, player2, move]
    var yourmovetablehtml = '<h3>Your Move</h3><table id="opengamelist"><tr bgcolor = "#B9B9B9"><th>Game</th><th>Opponent</th></tr>';
    var theirmovetablehtml = '<h3>Their Move</h3><table id="opengamelist"><tr bgcolor = "#B9B9B9"><th>Game</th><th>Opponent</th></tr>';
    $.getJSON(url, function(data) {
        var i;
        for (i = 0; i < data.length; i++) {
            if (data[i][1] == username){
                if (data[i][3] == 1) {
                    yourmovetablehtml += '<tr bgcolor="#EDEDED"><td>' + data[i][0] + '</td><td>' + data[i][2] + '</td></r>';
                } else if (data[i][3] == -1) {
                    theirmovetablehtml += '<tr bgcolor="#EDEDED"><td>' + data[i][0] + '</td><td>' + data[i][2] + '</td></r>';
                }
            } else if (data[i][2] == username){
                if (data[i][3] == 1) {
                    theirmovetablehtml += '<tr bgcolor="#EDEDED"><td>' + data[i][0] + '</td><td>' + data[i][1] + '</td></r>';
                } else if (data[i][3] == -1) {
                    yourmovetablehtml += '<tr bgcolor="#EDEDED"><td>' + data[i][0] + '</td><td>' + data[i][1] + '</td></r>';
                }
            }
        }
        yourmovetablehtml += '</table>';
        theirmovetablehtml += '</table>';
        var tablehtml = yourmovetablehtml + theirmovetablehtml;
        document.getElementById('currentgametable').innerHTML = tablehtml;
    });
}