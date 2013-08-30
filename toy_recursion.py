#little recursion problems

def sum( list_numbers ):
    if len(list_numbers)==0:
        return 0
    elif len(list_numbers)==1:
        return list_numbers[0]
    else:
        x = list_numbers[0]
        rest_of_list = list_numbers[1::]
        return x + sum(rest_of_list)


def reduce_func( function, list_things, acc=None):
    if len(list_things)==0:
        return acc 
    elif len(list_things) > 0:
        if acc is None:
           acc = list_things[0]
        else:
           acc = function(acc, list_things[0])
        new_list = list_things[1::]
        return reduce_func( function, new_list, acc ) 
        
def map_func( function, list_things ):
    if len(list_things) ==0:
       return [] 
    else:
       def reduce_map( x, y):
           x.append ( function(y) )
           return x
       return reduce_func( reduce_map, list_things, [] )       
   
