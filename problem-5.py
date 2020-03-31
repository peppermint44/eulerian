# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def lcm(low,high):
    found=False
    a=1
    list=range(low,high)
    while not found:
        divisible_by_all(a,list)
        a=a+1   

def divisible_by(a,b):
    if a%b == 0:
        return True
    else:
        return False

def divisible_by_any(a,list):
    for b in list:
        if divisible_by(a,b):
            return True
    return False

def divisible_by_all(a,list):
    for b in list:
        if not divisible_by(a,b):
            return False
    return True

print(range(5,15))