sentence = "my Name is Khan Maheebullah"

# converting the string into list using split 
splitting = sentence.split()
#print(splitting)
# now i am reversing the list doing slicing
reverse = splitting[::-1]
print(reverse)

#now join function is used to convert the list into str
rev = ' '.join(reverse)

#print(rev)