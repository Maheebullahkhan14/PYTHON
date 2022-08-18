# Python code to clone or copy a list
# import copy
# list1 = [ 45 , 2 , 6 , 7]

# list2 = copy.copy(list1)

# list2[2] =5

# print(list2)


#Method 2 Using a assignment operator
def cloning(list1):
    li_copy = list1
    return li_copy


list1 = [8 , 9 ,12 , 56 , 4 ]
b = cloning(list1)
print(b)


