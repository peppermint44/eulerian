def fibonacci():
    a=1
    b=2
    count=2
    while a+b<4000000:
        count=count+1
        c=a
        a=b
        b=c+b
    print(a+b)



fibonacci()