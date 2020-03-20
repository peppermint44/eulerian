def divisible_by_2(a):
    if a%2 == 0:
        return True
    else:
        return False

def fibonacci():
    a=0
    b=1
    sum=0
    while a+b<4000000:
        f=a+b
        if divisible_by_2(f):
            sum=sum+f
        c=a
        a=b
        b=c+b
    print(sum)

fibonacci()