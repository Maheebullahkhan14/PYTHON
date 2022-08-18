#write a program to sum of n digit 
number = int(input("enter the number : "))
total = 0

while number > 0 :
    digit = number%10
    total = total + digit
    number = number//10

print(f"the sum of digit is  {total} ")
