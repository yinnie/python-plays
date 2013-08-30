import itertools
    
def largest_palindrom():
    #get the combinations of three digits
    all_three_digits = itertools.combinations(range(100,1000), 2) 
    #take the products and turn into strings
    products_strings = map(lambda x:x
