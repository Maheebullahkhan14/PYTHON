# Python Program to Calculate Sum of Even Numbers from 1 to N# 
#first we have to take the input from the user 
# after that assigning the variable with value 0
# i  which is nothing but my numbers in num variable from 0 to input num
# if my my i is even then add the i with my total variable 
# num = 5  so 1 not even , 2 even add 2 in total variable now my totat = 2
# 3 not even , 4 even so add 4 with total like 4 + 2= 6

num = int(input("Enter the num : "))
total = 0 
for i in range(1 ,num+1):         
    if i % 2 == 0:
        total = total + i

print(f"Sum of Even Number is : {total}")