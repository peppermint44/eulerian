    # A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.
    # Find the largest palindrome made from the product of two 3-digit numbers.
def reverse(a):
    b=0
    while a>0:
        c=a%10
        b=b*10+c
        a=a/10
    return b

def is_palindrome(a):
    return reverse(a) == a

def largest_palindrome_as_product(low,high):
    largest_palindrome=0
    for x in range (low,high):
        for y in range (low,high):
            z=x*y
            if is_palindrome(z):
                if z>largest_palindrome:
                    largest_palindrome=z
    return largest_palindrome
   
print(largest_palindrome_as_product(100,1000))