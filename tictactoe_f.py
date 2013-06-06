#stab at tic tac toe 
import random

class Board:                                         #acts only as a data storage. all methods are made into functions
#	BOARD = {(0,0): ' ', (0, 1): ' ',(0,2): ' ', (1,0): ' ', (1,1): ' ',(1,2): ' ',
        def __init__(self, board):
            self.BOARD = [[' ', ' ',' '],
                          [' ', ' ',' '],
                          [' ', ' ',' ']]              
     
        WINNING_BOARDS = [[[0,0], [0,1], [0,2]],      #a list of triplets. each triplet is a winning triplet combination
						  [[1,0], [1,1], (1,2)],
						  [[2,0], [2,1], [2,2]],
						  [[0,0], [1,0], [2,0]],
						  [[0,1], [1,1], [2,1]],
						  [[0,2], [1,2], [2,2]],
						  [[0,0], [1,1], [2,2]],
						  [[0,2], [1,1], [0,2]],
						  ]
        human_moves = []                             
        computer_moves = []
        human = True
        winner = None

def show( list_of ):
    for element in list_of:
        print "|".join(element)

def move( a_board ):  
    if a_board.human == True:
       a_board.human = False
       if human_move ( a_board ) == True:               #run human_move function and check winning
          return True
       else:
          return False
    else:
       a_board.human = True
       if computer_move (a_board) == True:            #run computer move function and check winning
          return True
       else:
          return False
              
def human_move( a_board ):
    print "place your move. enter row number of move"
    row = int(raw_input())               
    print "enter column number of move"
    col = int(raw_input())                            #remember to convert to int
    if check_valid_move(a_board, row, col) == True:
	   print " human "
	   if update_board(a_board, 0, row, col) == True:    # 0 is human
	      a_board.winner = "human"
	      print " human won!! "
	      return True
	   else:
	      return False
    else:
	   human_move(a_board) 
        
def computer_move( a_board ):                
    row = random.randint(0,2)
    col = random.randint(0,2)
    if check_valid_move(a_board, row, col) == True:
	   print " computer "
	   if update_board(a_board, 1, row, col) == True:    # 1 is computer
	      a_board.winner = "computer"
	      print " computer won!! "
	      return True
	   else:
	      return False
    else:
	   computer_move(a_board) 
    
def check_valid_move(a_board, row, col):
    if a_board.BOARD[row][col] == ' ':
       return True
    else:
       return False
    
def update_board(a_board, player, row, col):   
    if player == 0:                                   #0 is human
       a_board.human_moves.append([row, col])
       a_board.BOARD[row][col] = 'x'
       return check_winning(a_board.human_moves, a_board.WINNING_BOARDS)
    else:
       a_board.computer_moves.append([row, col])
       a_board.BOARD[row][col] = 'o'
       return check_winning(a_board.computer_moves, a_board.WINNING_BOARDS)
    
def check_winning(list_of_moves, list_of_winning_boards):
    print list_of_moves
    for element in list_of_winning_boards:     
        if element[0] in list_of_moves and\
           element[1] in list_of_moves and\
           element[2] in list_of_moves:
           return True
    return False

def get_possible_moves ( a_board ):
    #given a certain state of the board. what are the possible empty places player can go
    # return a list of possible cells
    possible_moves = []
    for element in a_board.BOARD:
        for pair in element:
            if check_valid_move(board, element, pair) == True
                possible_moves.append([element, pair])
    return possible_moves

def value ( a_board ):                                  #utility value of terminal leaf node
    if a_board.winner == "human":   
       return -1
    elif a_board.winner == "computer":
       return 1
    else:
       return 0

              						              
board = Board( [[' ', ' ',' '],                      #board is the only globally exposed item.
			    [' ', ' ',' '],
			    [' ', ' ',' ']] )
board_imaginary = Board( [[' ', ' ',' '],            #theoretical board for AI to do calculations
			    [' ', ' ',' '],
			    [' ', ' ',' ']] )

#def get_possible_moves( current_board ):      # get whatever valid moves are available at the moment     
    	                      
def main():
    while True:
          show( board.BOARD )
          if move( board ) == True:
             break
    show( board.BOARD )
     
if __name__ == '__main__':
    main()







    
    