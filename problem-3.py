def is_prime(a):
    for x in range(2,a/2):
        if divisible_by(a,x):
            return False
    return True

def divisible_by(a,b):
    if a%b == 0:
        return True
    else:
        return False

def prime_factors(a):
    for b in range(2,a/2):
        if divisible_by(a,b) and is_prime(b):
            print(b)

is_prime(600851475143)