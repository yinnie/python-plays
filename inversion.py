def rest (index, array):
    """returns a subarray starting at index+1"""
    index = index + 1
    return array[index:]
                
def inversion ( element, compared_ele):
    return element > compared_ele
                    
def num_invert (elem, sub_array):
    """number of inversion of a single element with regard to a sub_array"""
    count = 0
    for e in sub_array:
        if inversion(elem, e):
            count +=1
    return count
                                                             
def count_inversion ( array ): 
    """returns number of inversions in a given array"""
    count = 0
    for index, elem in enumerate(array):
        count += num_invert (elem, rest(index, array) )
    return count

def total_paths (n, acc_r, acc_l):
    """total number of paths for robot to go down R or D nxn grid from corner"""
    if acc_r==n or acc_l ==n:
        return 1
    else:
        return total_paths(n, acc_r+1, acc_l) + total_paths(n, acc_r, acc_l+1)
       
def cdr(a_set):
    return a_set[1:]

def subsets( a_set ):
    """all subsets of a set"""
    if a_set == []:
        return [[]]
    else:
        rest = subsets(cdr(a_set))
        return rest +  map(lambda e: e+ [a_set[0]] , rest)

#make change problem
def change_combo ( value, coins ):
    if value<0:
        print " sth is wrong"
    if value == 0:
        return [[]]
    else: 
        usable_coins = filter(lambda x:x<=value, coins)
        all_combos = []
        for coin in usable_coins:
            all_combos += map(lambda x:x+[coin], change_combo((value - coin), usable_coins))

def unique (string):
    l = list(string)
    dic = {}
    for i, ele in enumerate(l):
       if ele in dic:
           l[i] = ' '
       else: 
           dic[ele] = 1
    string_list = ''.join(l).split()
    return ''.join(string_list)

