from flask import Flask
from flask import redirect
from flask import jsonify
import json
from flask import request
from flask import session
from flask import render_template
from flask import send_from_directory
from flask import send_file
from jinja2 import Template
from flask import escape
import threading
import os
import csv
import global_var
from game import *
from passlib.hash import pbkdf2_sha256
import base64

app = Flask(__name__)
app.secret_key = 'SecretKey'

def do_login(user):
    if user is not None:
        session['user'] = user
        return(redirect('/'))
    else:
        return(redirect('/login'))

def register(username, password):
    with open('usernamepassword.csv', 'a') as csvfile:
        w = csv.DictWriter(csvfile,['username','password'])
        w.writerow({'username': username, 'password': password})
    

@app.route('/')
def index():
    if 'user' in session:
        return(render_template('main.html', user = session['user']))
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return(render_template('login.html'))
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
        with open('usernamepassword.csv') as csvfile:
            r = csv.DictReader(csvfile,['username','password'])
            for row in r:
                if row['username'] == username:
                    if pbkdf2_sha256.verify(password,row['password']):
                        return(do_login(username))
    return(do_login(None))

@app.route('/make_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'GET':
        return(render_template('Createaccount.html'))
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cont = True
        with open('usernamepassword.csv') as csvfile:
            r = csv.DictReader(csvfile,['username','password'])
            for row in r:
                if row['username'] == username:
                    cont = False
        if cont:
            hashedpass = pbkdf2_sha256.hash(password)
            register(username, hashedpass)
            global_var.usergamesdict[username] = []
            return(redirect('/login'))
        else:
            return(redirect('/make_account'))
    else:
        return(redirect('/make_account'))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect('/login')

@app.route('/get_opengames')
def get_othergames():
    gamelist = []
    for x in global_var.opengamedict:
        gamelist.append([x,global_var.opengamedict[x].player1,global_var.opengamedict[x].name])
    return(json.dumps(gamelist))

@app.route('/get_currentgames')
def get_currentgames():
    gamelist = []
    username = session['user']
    for x in global_var.usergamesdict[username]:
        game1 = global_var.currentgamedict[x]
        gamelist.append([x,game1.player1, game1.player2, game1.move, game1.name])
    return(json.dumps(gamelist))


@app.route('/new_game/<gamename>', methods=['POST'])
def new_game(gamename):
    if gamename in global_var.realgames:
        username = session['user']
        game1 = game(username,global_var.gameid, gamename)
        global_var.opengamedict[global_var.gameid] = game1
        global_var.gameid += 1
        return(redirect('/'))
    else:
        return(redirect('/'))


@app.route('/join_game/<gameid>', methods = ['POST'])
def join_game(gameid):
    username = session['user']
    gameidnum = int(gameid)
    if gameidnum in global_var.opengamedict:
        game1 = global_var.opengamedict[gameidnum]
        if game1.player1 != username:
            del global_var.opengamedict[gameidnum]
            game1.player2 = username
            global_var.currentgamedict[gameidnum] = game1
            global_var.usergamesdict[username] += [game1.idnum]
            global_var.usergamesdict[game1.player1] += [game1.idnum]
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/cancel_game/<gameid>', methods = ['POST'])
def cancel(gameid):
    username = session['user']
    gameidnum = int(gameid)
    if gameidnum in global_var.opengamedict:
        if global_var.opengamedict[gameidnum].player1 == username:
            del global_var.opengamedict[gameidnum]
            return(redirect('/'))
        else:
            return(redirect('/'))
    else:
        return(redirect('/'))

@app.route('/Battle_Lines/<gameid>', methods = ['GET'])
def Battle_Lines(gameid):
    if 'user' in session:
        username = session['user']
        idnum = int(gameid)
        if idnum in global_var.currentgamedict:
            game1 = global_var.currentgamedict[idnum]
            if (username == game1.player1):
                return(render_template('BattleLines.html', user = session['user'], gameid = gameid, player = "player1"))
            elif (username == game1.player2):
                return(render_template('BattleLines.html', user = session['user'], gameid = gameid, player = "player2"))
            else:
                return(redirect('/'))
        else:
            return(redirect('/'))
    else:
        return(redirect('/login'))

@app.route('/get_game_status/<gameid>')
def get_game_status(gameid):
    idnum = int(gameid)
    if idnum in global_var.currentgamedict:
        status1 = global_var.currentgamedict[idnum].getstatus()
        return(json.dumps(status1))

@app.route('/send_game_move', methods = ['POST'])
def send_game_move():
    if 'user' in session:
        username = session['user']
        request.get_json
        global_var.currentgamedict[gameid].makemove(player,cardnum,handnum)
        return(True)

@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('css', path)

'''
@app.route('/number/<number>')
def main(number):
    return(int(number)*2)
'''

if __name__ == "__main__":
    with open('usernamepassword.csv') as csvfile:
        r = csv.DictReader(csvfile,['username','password'])
        for row in r:
            name = row['username']
            global_var.usergamesdict[name] = []
    app.run()