#stab at tic tac toe 

#our board is a list of triplet strings
BOARD = [[' ', ' ',' '],
          [' ', ' ',' '],
          [' ', ' ',' ']]
          
#a list of triplets. each triplet is a winning triplet combination
WINNING_BOARDS = [[[0,0], [0,1], [0,2]],
                  [[1,0], [1,1], [1,2]],
                  [[2,0], [2,1], [2,2]],
                  [[0,0], [1,0], [2,0]],
                  [[0,1], [1,1], [2,1]],
                  [[0,2], [1,2], [2,2]],
                  [[0,0], [1,1], [2,2]],
                  [[0,2], [1,1], [0,2]],
                  ]
                  
X_VALUES = []                      # create an empty list to store the moves of the first player
O_VALUES = []                      # create a list to store the marks that the second player
counter = 0                        # counter to keep track of who is placing the mark

def show():
    for element in BOARD:
       print '|'.join(element)     #for each element, join the individual pieces inside of it with '|' inside
                                   #notice '|' is in front of join(element)

def move( counter_num ):           #player makes marks / moves.   
    global counter                 #put global in front of counter so python know to look for it instead of creating one
    row = int(raw_input())         #player has to first put in row number
    col = int(raw_input())         #remember to convert to int
    if cell_taken ( row, col ) == False: #check if that square is taken
       counter += 1    
       if counter_num % 2 == 0:   
          BOARD[row][col] = 'x'       #update the board. mark that cell with 'x'
          X_VALUES.append([row, col])
       else:
          BOARD[row][col] = 'o'       #update the board. mark that cell with 'x'
          O_VALUES.append([row, col])
    else:
        print "that cell is taken. place somewhere else"

#def socre_move ( player, move_coordinate ): # score of a certain player's certain move
 #   score = 0
  #  winning_score = 
    #total score is score of current stage of move and total of all potential moves
   # score += winning_score ( player1 )
    #score += -losing_score ( player2 )                                 
                                         #for every move in the rest of the possible moves. calculate score and all potential moves
    #return score  
    
        
def won( player ):                     # player's list of moves
    for element in WINNING_BOARDS:     #loop through all the winning triplets. see if x_values contain their elements
        if element[0] in player and\
           element[1] in player and\
           element[2] in player:
           return True
           break
    return False

def cell_taken( row_num, col_num):
    if BOARD[row_num][col_num] == ' ':
       return False
    else:
       return True           

def main():
    while True:
          show()
          move(counter)
          if won( X_VALUES) or won ( O_VALUES):
             break
    show()
    print "YOU WON!! "
   
if __name__ == '__main__':
    main()








    
    