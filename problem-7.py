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
    return not divisible_by_any(a,range(2,a/2+1))

def is_coprime(a,divisors):
    return not divisible_by_any(a,divisors)

def prime_number(prime_number_count):
    start = datetime.datetime.now()
    candidate=1
    primes=[]
    while len(primes) < prime_number_count:
        candidate=candidate+1
        if is_coprime(candidate, primes):
            primes.append(candidate)
    coprime_time = datetime.datetime.now() - start

    start = datetime.datetime.now()
    candidate=1
    primes=[]
    while len(primes) < prime_number_count:
        candidate=candidate+1
        if is_prime(candidate):
            primes.append(candidate)
    prime_time = datetime.datetime.now() - start

    return (candidate, coprime_time.microseconds, prime_time.microseconds)
        
def first_prime_numbers(n):
    data=[]
    for i in range(1,n+1):
        data.append(prime_number(i))
    return data

print(first_prime_numbers(1000))