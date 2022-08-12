
n=int(input("enter a number"))



def reverse(n):
    r = 0
    rem = 0
    sign = 1
    if n < 0:
        sign = -1
    n = n*sign
    while n > 0:
        rem = n % 10
    r = r*10+rem
    n = n//10
    if n < (pow(-2, 31)) or n > (pow(2, 31)-1):
        return 0
    else:
        return r*sign


print(reverse(123))
