#count the even Numbers in a list 

list= [ 12 , 45 , 22 , 36]

counter = 0

for i in list:
    if i % 2 == 0:
        counter += 1

print(str(counter))