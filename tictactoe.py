#stab at tic tac toe 
import random

class Board:
#	BOARD = {(0,0): ' ', (0, 1): ' ',(0,2): ' ', (1,0): ' ', (1,1): ' ',(1,2): ' ',

        def __init__(self, board):
            self.BOARD = [[' ', ' ',' '],
                          [' ', ' ',' '],
                          [' ', ' ',' ']]
#       def get_possible_moves( current_board ):      # get whatever valid moves are available at the moment
#          pass
        def cell_taken(self, row_num, col_num):
            if self.BOARD[row_num][col_num] == ' ':
               return False
            else:
               return True 
               
        def show(self):
            for element in self.BOARD:
                print '|'.join(element)     #for each element, join the individual pieces inside of it with '|' inside
                                        #notice '|' is in front of join(element)               
        def move(self, a_human, a_computer ):
            if self.counter % 2 == 0:
               a_human.move( self )                          
            else:
               a_computer.move( self )        
        counter = 0        
        WINNING_BOARDS = [[[0,0], [0,1], [1,2]],      #a list of triplets. each triplet is a winning triplet combination
						  [[1,0], [1,1], (1,2)],
						  [[2,0], [2,1], [2,2]],
						  [[0,0], [1,0], [2,0]],
						  [[0,1], [1,1], [2,1]],
						  [[0,2], [1,2], [2,2]],
						  [[0,0], [1,1], [2,2]],
						  [[0,2], [1,1], [0,2]],
						  ]
						  
class Human:

      def __init__(self):
          pass    
          
      moves = []          
      
      def move( self, board ):
		  print "place your move. enter row number of move"
		  row = int(raw_input())         #player has to first put in row number
		  print "enter column number of move"
		  col = int(raw_input())         #remember to convert to int
		  if  board.cell_taken ( row, col ) == False: #check if that square is taken
		      board.BOARD[row][col] = 'x'          #update the board. mark that cell with 'x'
		      self.moves.append([row, col])
		      board.counter += 1
		      print " human "
		  else: 
		      print "that cell is taken. please try again"
		      self.move(board)      
		      
      def win( self, board ):
          for element in board.WINNING_BOARDS:     #loop through all the winning triplets. see if x_values contain their elements
              if element[0] in self.moves and\
                 element[1] in self.moves and\
                 element[2] in self.moves:
                 print "human WON!! "
                 return True
                 break
          return False
          
class Computer:

       def __init__(self):
           pass
       moves = []
           
       def move(self, board ):
           row = random.randint(0,2)
           col = random.randint(0,2)       
           if board.cell_taken ( row, col ) == False: #check if that square is taken
              board.BOARD[row][col] = 'o'          
              self.moves.append([row, col])
              board.counter += 1
              print " computer "
           else: 
              self.move(board)
              
       def win( self, board ):
           for element in board.WINNING_BOARDS:     #loop through all the winning triplets. see if x_values contain their elements
               if element[0] in self.moves and\
                  element[1] in self.moves and\
                  element[2] in self.moves:
                  print "computer WON!! "
                  return True
                  break
           return False           


board = Board( [[' ', ' ',' '],
			    [' ', ' ',' '],
			    [' ', ' ',' ']] )
human = Human()
computer = Computer()

#def minimax(current_board, player):
 #   possible_boards = get_possible_boards(current_board)
  #  for board in possible_boards:
   #     if winning(board, player) == 1:
    #        return board
     #   else:
      #      return minimax(board,1 if player==2 else 1) 
            
#def winning(board, player):
    	                      
def main():
    while True:
          board.show()
          board.move( human, computer)
          if human.win( board ) or computer.win ( board ):
             break
    board.show()
  
   
if __name__ == '__main__':
    main()








    
    