n=int(input("Enter a number:"))
res=0
def checkPalindrome(x,res):
    
    
    while(x>0):
        rem=x%10
        res= res*10+rem
        x=x//10
    
    if n==res:
        return True
    else:
        return False
       


print(checkPalindrome(n,res))
