#Palindrome or not 
def ispalindrome(word):
    rev = ''.join(reversed(word))

    if word == rev:
        return True 
    return False

word = input("Enter The word To Check : ")

ans = ispalindrome(word)

if ans == True :
    print("Palindrome")
else : 
    print("Not a Palindrome")
    