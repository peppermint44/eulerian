def is_prime(a):
    for x in range(2,a):
        if divisible_by(a,x):
            return False
    return True


def divisible_by(a,b):
    if a%b == 0:
        return True
    else:
        return False

print(is_prime(15))