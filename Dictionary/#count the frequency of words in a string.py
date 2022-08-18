#count the frequency of words in a string 
string = (" hello i am saying hello can yo say back hello")
li = string.split()

dict1 = {}
for i in li:
    if i not in dict1.keys():
        dict1[i] = 0
    dict1[i] += 1

print(dict1)