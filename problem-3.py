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

# def divisible_by_any(a,list):
#     for b in list:
#         if divisible_by(a,b):
#             return True
#     return False

def get_prime_factors(a):
    prime_factors = {}
    b = 2
    while a > 1:
        print("checking: ", b)
        if is_prime(b) and divisible_by(a,b):
            # we found a prime factor of a!!
            prime_factors[b] = 1

            a = a/b
            while divisible_by(a,b):
                prime_factors[b] = prime_factors[b] + 1
                a = a/b

            print(b, "divides the original 'a'", prime_factors[b], "times")

        b = b + 1

    prime_factors = {int(k) : v for k, v in prime_factors.items()}
    return prime_factors

print(get_prime_factors(999992))