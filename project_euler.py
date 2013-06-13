def euler001(n):
    value = 0
    for x in range(n):
        if x%3 == 0 or x%5==0:
           value+=x
    return value

def euler002(limit):
    value = 0
    index = 0
    a, b = 0,1
    while index < 3000:
        a,b = b, a+b
        if a < limit:
           if a%2 == 0:
              value += a
           index+=1
        else:
           return value           
        
def euler003 ( number ):
    prime_factors = []
    n = 2
    while number > 1:
        if number % n ==0:
           number = number/n
           prime_factors.append(n)
        else:
           n += 1 
    return max(prime_factors)

def euler004 (number_of_digits):
    #get all the two digit numbers
    all_two_digits = [str(x)+str(y) for x in range(10) for y in range(10)]
    all_three_digits = [str(x)+str(y)+str(z) for x in range(10) for y in range(10) for z in range(10)]
    palindroms_2 = []
    palindroms_3 = []

    def check_pandindroms_string (list_of_string, number_of_elements):
        first_half, second_half = list_of_string[:number_of_elements/2], list_of_string[number_of_elements/2:]
        first_half = ''.join(first_half)
        second_half = ''.join(second_half)
        return  first_half == second_half[::-1]

    def check_palindroms_number (number):
        digits = list(str(product))       #turn integer to list of strings 
        if len(digits)%2==0:
           number_of_eles = len(digits)
           return check_pandindroms_string(digits, number_of_eles)
        else: 
           number_of_eles = len(digits)-1
           return check_pandindroms_string(digits, number_of_eles)

    if number_of_digits == 2:
        for number0 in all_two_digits:
             for number1 in all_two_digits:
                 product = int(number0) * int(number1)
                 if check_palindroms_number (product):
                    palindroms_2.append(product)
        return max(palindroms_2)
    else:
        for number0 in all_three_digits:
             for number1 in all_three_digits:
                 for number2 in all_three_digits:
                     product = int(number0) * int(number1) * int(number2)
                     if check_palindroms_number (product):
                        palindroms_3.append(product)
        return max(palindroms_3)

print euler004(3)
