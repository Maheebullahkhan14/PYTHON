#python program to print duplicates from a list 
list1 = [ 2 , 5 , 6 , 2 , 7 , 5 , 7 , 8]
x =[]
y =[]

for i in list1:
    if i not in x:
        x.append(i)

for i in x :
    if list1.count(i) > 1:
        y.append(i)

print(y)