def divisible_by_3(a):
    if a%3 == 0:
        return True
    else:
        return False
    # boolean(yes or no) or true/false

def divisible_by_5(b):
    if b%5 == 0:
        return True
    else:
        return False

n=0
for x in range(1,1000):
    if divisible_by_3(x) or divisible_by_5(x):
        n=n+x

print(n)

# n=5
# n=n*n
# print(n)
