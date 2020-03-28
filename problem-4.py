def reverse(a):
    b=0
    while a>0:
        c=a%10
        b=b*10+c
        a=a/10
    return b

def is_palendrome(a):
    return reverse(a) == a

print(is_palendrome(38183))