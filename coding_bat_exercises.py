# www.codingbat.com/home/peter@norvig.com import copy
import copy
from collections import deque

def unique(items):
    return sorted(set(items)) 

def sum_squares(nums):
    return sum( map( lambda x:x**2, nums) )

def sum_square_1(nums):
    return sum(x**2 for x in nums)

def sum_squares_while(nums):
    sum = 0
    n = 0
    while n < len(nums):
        sum+=nums[n]**2
        n+=1
    return sum

def blackjack(player, dealer):
    def total(cards):
        if 1 in cards:
           sum0= sum(cards)
           cards1 = copy.deepcopy(cards)
           for x in range(len(cards1)):
               if cards1[x]==1:
                  cards1[x]+=10 
                  if sum(cards1) > 21:
                     cards1[x] = 1
           return sum(cards1)
        else:
          return sum(cards)
    if total(player) <=21 and total(dealer) >= 21:
       return True
    elif total(player) <= 21 and total(player) > total(dealer):
       return True
    else:
       return False

def rock_paper_scissors(a,b):
    defeaters = {'rock':'paper', 'paper':'scissors', 'scissors':'paper'}
    if a == b:
       return 0
    elif a == defeaters[b]:
       return 1
    elif b == defeaters[a]:
       return -1

def piglatin(word):
    vowels = ['a','e','i','o','u']
    letters = list(word)
    if letters[0] in vowels:
       letters.append('way')
       return''.join(letters)
    else:
       consonants = []
       letters_queue = deque(letters)
       while letters_queue[0] not in vowels:
             consonants.append(letters_queue[0])
             letters_queue.popleft()
       letters_queue.extend(consonants)       
       letters_queue.append('ay')
       return ''.join(letters_queue) 
    
def piglatin2(word):
    vowels = ['a','e','i','o','u','A','E',"I",'O','U']
    letters = list(word)
    new_word = 'apple'
    if letters[0] in vowels:
       letters.append('way')
       new_word= ''.join(letters)
    else:
       consonants = []
       vowels.extend(['y','Y'])
       letters_queue = deque(letters)
       print letters_queue
       if letters_queue[0]=='q' and letters_queue[1] =='u':
          consonants.append('qu')
          letters_queue.popleft()
          letters_queue.popleft()
       else:
          while letters_queue[0] not in vowels:
               consonants.append(letters_queue[0])
               print consonants
               letters_queue.popleft()
       letters_queue.extend(consonants)       
       letters_queue.append('ay')
       new_word =''.join(letters_queue) 
    if word.istitle():
       return  new_word.capitalize()
    elif word.isupper():
       return new_word.upper()
    
   
print piglatin2('pig') 






















