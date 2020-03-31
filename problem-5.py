# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def lcm(low,high):
    a=1
    list=range(low,high)
    while True:
        if divisible_by_all(a,list):
            return(a)
        a=a+1   

def divisible_by(a,b):
    if a%b == 0:
        return True
    else:
        return False

def divisible_by_all(a,list):
    for b in list:
        if not divisible_by(a,b):
            return False
    return True

print(lcm(1,21))