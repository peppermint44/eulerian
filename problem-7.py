import datetime
from datetime import timedelta

def divisible_by_any(a,list):
     for b in list:
         if divisible_by(a,b):
             return True
     return False

def divisible_by(a,b):
    if a%b == 0:
        return True
    else:
        return False

def is_prime(a):
    for x in range(2,a/2+1):
        if divisible_by(a,x):
            return False
    return True

def is_coprime(a,divisors):
    return not divisible_by_any(a,divisors)

def prime_number(a):
    start = datetime.datetime.now()

    candidate=1
    primes=[]
    while len(primes) < a:
        candidate=candidate+1
        # if is_prime(candidate):
        if is_coprime(candidate, primes):
            primes.append(candidate)
    
    diff = datetime.datetime.now() - start

    print("time:",  diff.seconds)
    return candidate
        

print(prime_number(10001))
# print(is_prime(4))
