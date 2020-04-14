def binary_to_decimal(binary):
    repeat=True
    multiplier=1
    decimal=0
    while repeat:
        remainder=binary%10
        place_value=remainder*multiplier
        decimal=decimal+place_value 
        binary=binary/10
        multiplier=multiplier*2
        repeat=binary>0
    return decimal

def decimal_to_binary(decimal):
    binary=0    
    while decimal > 0:
        remainder=decimal%2
        decimal=decimal/2
        binary=binary*10+remainder
    return binary

print(decimal_to_binary(69))