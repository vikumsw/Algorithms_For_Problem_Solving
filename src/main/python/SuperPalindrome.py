import math

def countSuperPalindromes(l,r):
    leftMargin  = int(math.ceil(math.sqrt(l)))
    rightMargin = int(math.floor(math.sqrt(r)))
    
    #define a lambda fn to check for palindrome
    isPalindrome = lambda i : str(i) == str(i)[::-1]
    
    superPalindromes = list()
    count = 0
    
    for i in range(leftMargin,rightMargin+1):
        if isPalindrome(i) and isPalindrome(i*i):
            superPalindromes.append(i*i)
            count+=1
            
    print(superPalindromes)
    return count
    
    
print(countSuperPalindromes(4,1000))
