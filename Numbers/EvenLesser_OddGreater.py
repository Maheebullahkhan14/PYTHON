# if both numbers are Even then give the lesser number 
#if one or another number is odd give the greatest number

def complex(num1 , num2):                        #assigning two numbers  
    if (num1 % 2 == 0 ) and (num2 % 2 == 0):     #condition if my both number is even then give the lesser number
        if num1 > num2 :
            return num2

    elif (num1 %2!= 0 ) or (num2 % 2!= 0):       # if my num1 or num2 is odd then give the greatest number 
        if num2 > num1 :
            return num2

        else :
            return num1


  
print(complex(105,5)) 

