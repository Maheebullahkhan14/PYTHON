'''# function to check string is
 palindrome or not'''

def ispalindrome(s):                    # my first step is to convert my string in reverse
    rev = ''.join(reversed(s))          #after that check my reversed variable is same or not with my variable word 
                                        # if equal then True else false 
                                        #after that taking the input from the user if the input is true then print Yes  else false
                                
    if s == rev :
        return True
    return False

s = input("Enter the word : ")

ans = ispalindrome(s)

if ans==True:
    print("Yes")
else :
    print("No")

   


    