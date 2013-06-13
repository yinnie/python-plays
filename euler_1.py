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
        
def euler003(number):
    prime_numbers = [2]
    
    def find_prime( a_number ):
      own_primes = []
      print own_primes
      for x in prime_numbers:
          if a_number%x == 0:
             own_primes.append(x)
             find_prime( a_number/x )
      if own_primes.count == 0:
         prime_numbers.append( a_number )
    n = 3
    while n < number:
      find_prime(n)
      n+=1
    print prime_numbers
    return prime_numbers[-1]  

print euler003(25)
