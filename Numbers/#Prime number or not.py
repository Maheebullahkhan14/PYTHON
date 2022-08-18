#Prime number or not 
num = int(input("Enter the number : "))

if num < 2 :                            # first we have to see that number should not be less then 2 if it is less then not a prime
    print("Not a prime Number")

else :                                  # i is any number in range 
    for i in range(2,num):              # suppose if number is divided by i (any number ) then not a prime number
        if num%i==0 :                   
            print("Not a prime number")
            break                       # break statment because only check one time is its not a prime then break 
    
    else :
        print("Number is prime ")

        
