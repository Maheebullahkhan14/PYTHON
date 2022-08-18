#Remove i th character from the string 
'''In this method, one just has to run a loop and append the characters as they come and 
build a new string from the existing one except when the index is i.'''

teststr = "geeksforgeeks"

newstr = ''

for i in range(len(teststr)):
    if i!= 3 :
        newstr = newstr + teststr[i]
print(newstr)