#Second largest number in list which contain duplicate value
# given list
given_list = [5, 6, 7, 7, 8, 1, 9, 9]
# converting the given list into set using set() function

given_list = set(given_list)
# converting the given_list set to list using list() function

given_list = list(given_list)
# sorting the given list in ascending order

given_list.sort(reverse=True)
# Calculating the second largest element after sorting

seclarg = given_list[1]
# printing the second largest element in the given list
print("printing the second largest element in the given list : ", seclarg)       
        
        
        