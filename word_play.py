import string 
#what words contain 'UU' what contain Q without U
txt = open("sowpods.txt")
words = []

def contain_0( double, txt):
    return filter( lambda x : double in x,  txt )

def contain_1( letter0, letter1, txt):
    return filter( lambda x : letter0 in x and letter1 not in x, txt)
   
def stripped( words ):
    return map( lambda x: x.strip(), words)

def has_double(double, txt):
    for word in txt:
        if double in word: 
            return True 
    return False 

def not_doubled( all_doubles, txt ):
    return filter( lambda double: not has_double(double, txt), all_doubles)

alphabet = list( string.ascii_uppercase )

doubles = [ a+a  for a in alphabet]

def longest_pan ( txt ):
    all_pan = filter( lambda x: x==x[::-1], stripped(txt) )
    return max(all_pan) 
         
vowels = ['A', 'E', 'I', 'O', 'U', 'Y']    

def contain_all( letters, word):
    for letter in letters:
        if letter not in word:
            return False 
    return True 

def has_repeats( word ):
    counts = map( lambda x: word.count(x), word)
    if 2 in counts:
        return (True, max(counts))
    return (False, 0)

def max_repeats ( eval_func, txt):
    words = filter( lambda x: eval_func(x)[0], txt)
    return reduce( lambda x, y: y if eval_func(x)[1] < eval_func(y)[1] else x, words)

def anagram( a, b):
    return list(a).sort() == list(b).sort()  

def anag_in_list ( col ) :
    l = []
    dic = {}
    for word in col:
        word_sorted = ''.join(sorted(word))
        if word_sorted in dic:
            return word
        dic[word_sorted] = word

def all_anag ( txt ):
    by_lengths = { k:[] for k in range(1, 16) }
    for x in txt:
        by_lengths[x.strip().__len__()].append(x)
    keys = sorted(by_lengths, reverse= True)
    for key in keys:
        anas = anag_in_list( by_lengths[key])
        if anas:
            return anas
    
#problem 1
#words0 = contain_0 ( 'UU', txt )
#print( stripped(words0) ) 
#words1 = contain_1 ('Q', 'U', txt)
#print( stripped(words1) )

#problem 2
#print ( not_doubled ( doubles, txt) )

#problem 3
#print ( longest_pan (txt) )

#problem 4
#print ( filter( lambda x: contain_all(vowels, x), txt) )
#in any order? 

#problem 5
#print ( max_repeats (has_repeats, txt) )

#problem 6
print( all_anag (txt) ) 
