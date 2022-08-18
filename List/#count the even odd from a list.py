#count the even odd from a list 
list1 = [12 , 56 , 11 , 5 , 78 , 3]
counteven = 0
countodd = 0

for i in list1:
    if i % 2 == 0:
        
        counteven += 1
    else :
        countodd +=1

print('count of even is : ',counteven)
print('count of odd is : ',countodd)