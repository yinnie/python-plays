from flask import Flask, request
import json

app = Flask ( __name__)

waiting_game = None      #current game
games = [] 

class Game(object):
     id_generator = 0
     def __init__(self):
       self.player1 = self.id_generator
       self.player2 = self.id_generator + 1
       self.board = [0 for x in range(9)]
       self.id_generator += 2
     @property
     def turn(self):
       #assuming player 1 will update the board starting with 1"
       return [self.player1, self.player2][sum(self.board)]
     def json(self):
       return json.dumps({'board': self.board})

@app.route('/home')
def start_play():
    global waiting_game
    if waiting_game == None :
       waiting_game = Game()
       games.append(waiting_game)
       get_board(waiting_game.player1) 
    else:
       game = waiting_game
       waiting_game = None
       #there is already a game but you have to wait till the other one places his move
       if game.turn == game.player2:
          get_board(game.player2)

@app.route('/get_board/<int:player_id>')
#by default this is a GET
def get_board(player_id):
    #get the current game board so he can make a move
    #first pull out the game that this player is in 
    (game,) = [g for g in games if player_id in [g.player1, g.player2] ]
    #check if player id matches what turn() returns
    if game.turn == player_id:
       return 'player %s' % player_id + game.json() 
    else:
       #it is not this player's turn yet but he requested..so he needs to wait
       print "waiting for the other player to finish move"

@app.route('/submit_board/<int:player_id>', methods = ['POST'])
def summit_board(player_id):
    #alter the board state. need to check if submission is valid.
    #TODO: this function also needs to check if it is your turn. 
    # otherwise accessing this url repeatedly will mean you can alter state when not turn
    #get the game that this player is in
    (game,) = [g for g in games if player_id in [g.player1, g.player2] ]
    game.board = json.loads(request.form)
    return json.dumps({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
