#write a program to count a digit 
number = int(input("Enter the number : "))
count = 0
while number > 0 :
    
    count+=1
    number=number//10

print(count)




