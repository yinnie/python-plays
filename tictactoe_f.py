# -*- coding: utf-8 -*-
#stab at tic tac toe 
import random
import copy
import logging
from os.path import realpath, join, dirname

log_file = realpath(join(dirname(__file__), "tictactoe.log"))
logging.basicConfig(filename=log_file, filemode="w+", level=logging.DEBUG)
log = logging.getLogger(__name__)

class Board(object):                                   
    winning_boards  = [[[0,0], [0,1], [0,2]],     
						  [[1,0], [1,1], (1,2)],
						  [[2,0], [2,1], [2,2]],
                          [[0,0], [1,0], [2,0]],
                          [[0,1], [1,1], [2,1]],
						  [[0,2], [1,2], [2,2]],
						  [[0,0], [1,1], [2,2]],
						  [[0,2], [1,1], [2,0]],
						  ]
    
    def __init__(self, board=None):
        if board is None:
            self.human_moves = []                             
            self.computer_moves = []
            self.human = True
            self.winner = None
            self.draw = False
        else:
            self.human_moves = copy.deepcopy(board.human_moves) 
            self.computer_moves = copy.deepcopy(board.computer_moves)
            self.human = board.human 
            self.winner = board.winner 
            self.draw = board.draw 

    @staticmethod
    def generate_fresh_board():
        return [[' ']*3 for x in range(0,3)]

    @property
    def computer(self):
        return not self.human
    @property
    def BOARD(self):
        BOARD = [[' ']*3 for x in range(0,3)]
        for (row, col) in self.human_moves: #(row col is a tuple)
            BOARD[row][col] = 'x'
        for row, col in self.computer_moves:
            BOARD[row][col] = 'o'
        return BOARD
    def show(self):
        for element in self.BOARD:
            print "|".join(element)


def play( a_board ):  
        if a_board.human:
            next_turn = move_result( a_board, human_move( a_board ),  "human")
            next_turn.human = False
        elif a_board.computer:
            next_turn = computer_move ( a_board)
            # a_board.computer = True
            next_turn.human = True
        return next_turn

def human_move( a_board ):
    print "place your move. enter row number of move"
    row = int(raw_input())               
    print "enter column number of move"
    col = int(raw_input())                            #remember to convert to int
    return [row, col]

def computer_move ( a_board ):
   return Minimax (a_board)

def dumb_computer_move( a_board ):                
    row = random.randint(0,2)
    col = random.randint(0,2)
    return [row, col]

def move_result( a_board, the_move, player ):
    if check_valid_move(a_board, the_move[0], the_move[1]) :
       print player
       new_board = update_board(a_board, player, the_move[0], the_move[1])
    else:
       new_board =  move_result( a_board, human_move(a_board), player)

    return new_board

def update_board( a_board, player, row, col ):   
    a_board = Board(a_board)
    if player == "human" :
       a_board.human_moves.append([row, col])
       a_board.BOARD[row][col] = 'x'
       if check_winning(a_board.human_moves, a_board.winning_boards):
          a_board.winner = "human"
    elif player == "computer":
        a_board.computer_moves.append([row, col])
        a_board.BOARD[row][col] = 'o'
        if check_winning(a_board.computer_moves, a_board.winning_boards):
          a_board.winner = "computer"
    else:
        raise Exception("Bad paramater in update_board: player")

    return a_board   
    
def check_winning( list_of_moves, list_of_winning_boards ):
    for element in list_of_winning_boards:     
        if element[0] in list_of_moves and\
           element[1] in list_of_moves and\
           element[2] in list_of_moves:
           return True
    return False

def check_valid_move( a_board, row, col ):
   if row > 2 or row < 0 or col > 2 or col < 0:
        print "invalid move. enter a number between 0 and 2"
        return False
   elif a_board.BOARD[row][col] == ' ':
        return True
   else:
        print "that cell is taken. "    
        return False

def Minimax ( a_board ):
    return Max ( a_board, 0)

def Max(a_board, depth):
    board_temp = Board(a_board)
    if check_ending ( board_temp ):
       return leaf_value ( board_temp )
    value = -2
    for element in get_possible_boards (board_temp): 
        value_temp = Min ( element, depth + 1 )       
        if value_temp > value:
           value = value_temp
           the_right_move = element 
    log.info("max value is {value}".format(value=value))
    if depth == 0:
       print "max value ", value
       return the_right_move
    return value 

def Min ( a_board, depth ):
    # min value of current state of board
    board_temp = Board(a_board)
    if check_ending ( board_temp ):
       return leaf_value ( board_temp )
    value = 2
    the_right_move = board_temp 
    for element in get_possible_boards ( board_temp ):
        value_temp = Max (element, depth + 1) 
        if value_temp < value:
           value = value_temp
           the_right_move = element 
    log.info("min value is {value}".format(value=value))
    return value

def get_possible_boards ( a_board ):
    possible_boards = []
    for cell in get_empty_cells( a_board ):
        if a_board.human == True:
           #updating the newly created board with a mark in one of the empty cells
           new_board = update_board(a_board , "human", cell[0], cell[1])
           new_board.human = False
        elif a_board.human == False:
           new_board = update_board(a_board, "computer", cell[0], cell[1])
           new_board.human = True
        possible_boards.append(new_board)

    log.info("=========================================")
    for each_board in possible_boards:
        log.info( "possible board: {board}".format(board=each_board.BOARD))
    log.info("=========================================")
    return possible_boards
    
def get_empty_cells( a_board ):
    empty_cells = []
    for row in range(0, 3): 
        for col  in range(0, 3):
            if  a_board.BOARD[row][col]== ' ':
               empty_cells.append([row, col])
    return empty_cells

def leaf_value ( a_board ):                                 
    #the value of a certain board that we already know is ended
    if a_board.winner == "human":   
       return -1
    elif a_board.winner == "computer":
       return 1
    elif a_board.draw == True:
       return 0
    else:
       print "this is not a terminal board"

def check_ending( a_board  ):   
    if check_winning (a_board.human_moves, a_board.winning_boards):
       a_board.winner = "human"
       return True
    elif check_winning (a_board.computer_moves, a_board.winning_boards):
       a_board.winner = "computer"
       return True
    else:
       for element in a_board.BOARD:
           for cell in element:
               if cell == ' ':
                  return False
       a_board.draw = True
       return True

def main():
    board = Board()                      #board is the only globally exposed item.
#    board.human_moves=[[0,0],[1,1],[1,2]]
#    board.computer_moves=[[0,2],[0,1],[1,0]]
    board_imaginary = Board()             #theoretical board for AI to do calculations
    while True:
          board.show( )
          if check_ending( board ) == False:
              board = play( board )
          elif board.winner == "human":
                 print "human won"
                 break
          elif board.winner == "computer":
                 print "computer won"
                 break
          elif board.draw == True:
                 print "it's a draw! game over"
                 break
    board.show( board.BOARD )
     
if __name__ == '__main__':
   main()
   
