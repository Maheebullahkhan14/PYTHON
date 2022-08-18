#Find Samllest  list element on inputs provided by user.
#creating empty list to store Values
list1 = []

#how many values to be inserted in empty list taken by user
num = int(input("Enter the how many values of list : "))

for i in range(1,num+1):
    l_values = int(input("enter the value "))
    list1.append(l_values)                      #

print("The minimum value is " ,min(list1))