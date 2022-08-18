#reverse a list in python 
list1 = [100, 200, 300, 400, 500]
a = list1[::-1]
#print(a)


#Swapping of first and last index value from as list
def swaplist(newlist):
    length = len(newlist)

    temp = newlist[0]
    newlist[0]= newlist[length - 1]
    newlist[length - 1] = temp

    return newlist

newlist =[12 , 23 , 45 , 65]
b = swaplist(newlist)
print(b)
