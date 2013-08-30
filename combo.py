
def getcombo(array):
    if ( len(array) == 0):
        return [] 
    else:
        for element in array:
            array.remove(element)
            comb_without_elem = getcombo(array)
            comb_with_elem = list(comb_without_elem)
            comb_with_elem.append([element])
            return comb_without_elem + comb_with_elem 


                    
