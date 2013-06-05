#an initial tic tac toe program that checks if somebody is winning
#trying to do it without classes. more like function style
#dont interrupt the program if there is no user input

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
                  
X_VALUES = []    # create an empty list to store the 'marks'/'moves' coordinates

def show():
    for element in BOARD:
        #for each element, join the individual pieces inside of it with '|' inside
        #notice '|' is in front of join(element)
       print '|'.join(element)

def move():     #player makes marks / moves.   
    row = int(raw_input()) #player has to first put in row number
    col = int(raw_input())      #remember to convert to int
    BOARD[row][col] = 'x'       #update the board. mark that cell with 'x'
    X_VALUES.append([row, col])

def won():       #loop through all the winning triplets. see if x_values contain their elements
    for element in WINNING_BOARDS:
        if element[0] in X_VALUES and\
           element[1] in X_VALUES and\
           element[2] in X_VALUES:
           return True
           break
    return False
           

def main():
    while True:
          show()
          move()
          if won():
             break
    print "YOU WON!! "
   
if __name__ == '__main__':
    main()








    
    