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
						  [[0,1], [1,1], [2,1]],
						  [[0,2], [1,2], [2,2]],
						  [[0,0], [1,1], [2,2]],
						  [[0,2], [1,1], [2,0]],
						  ]
        human_moves = []                             
        computer_moves = []
        human = True
        winner = None

def show( list_of ):
    for element in list_of:
        print "|".join(element)

def play( a_board ):  
        if a_board.human:
            move_result( a_board, human_move( a_board ),  "human")
            a_board.human = False
        else:
            move_result( a_board , computer_move( a_board ), "computer")
            a_board.human = True

def move_result( a_board, the_move, player ):
    if check_valid_move(a_board, the_move[0], the_move[1]) :
       print player
       update_board(a_board, player, the_move[0], the_move[1])
    else:
       move_result( a_board, human_move(a_board), player)

def human_move( a_board ):
    print "place your move. enter row number of move"
    row = int(raw_input())               
    print "enter column number of move"
    col = int(raw_input())                            #remember to convert to int
    return [row, col]
    
def computer_move( a_board ):                
    row = random.randint(0,2)
    col = random.randint(0,2)
    return [row, col]

def check_valid_move( a_board, row, col ):
   if row > 2 or row < 0 or col > 2 or col < 0:
        print "invalid move. enter a number between 0 and 2"
        return False
   elif a_board.BOARD[row][col] == ' ':
        return True
   else:
        print "that cell is taken. "    
        return False

def update_board( a_board, player, row, col ):   
    if player == "human" :
       a_board.human_moves.append([row, col])
       a_board.BOARD[row][col] = 'x'
       if check_winning(a_board.human_moves, a_board.WINNING_BOARDS):
          a_board.winner = "human"
    else:
       a_board.computer_moves.append([row, col])
       a_board.BOARD[row][col] = 'o'
       if check_winning(a_board.computer_moves, a_board.WINNING_BOARDS):
          a_board.winner = "computer"
       
    
def check_winning( list_of_moves, list_of_winning_boards ):
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
            if check_valid_move(a_board, element, pair) == True:
                possible_moves.append([element, pair])
    return possible_moves

def value ( a_board ):                                  #utility value of terminal leaf node
    if a_board.winner == "human":   
       return -1
    elif a_board.winner == "computer":
       return 1
    else:
       return 0

def ending( a_board):
    if a_board.BOARD.count == 0:
       print "game over! it's a draw"
       return True
    else:
       return False
              						              
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
          if ending( board ) == False:
              if board.winner == "human":
                 print "human won"
                 break
              elif board.winner == "computer":
                 print "computer won"
                 break
              else:
                 play(board )
          else:
              print "it's a draw! game over"
    show( board.BOARD )
     
if __name__ == '__main__':
    main()
   
