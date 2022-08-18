'''Old MacDonald :- Write a python Function to capitalise the First and Fourth letter of macdonald'''

def Capitalise(word):
    return word[0].upper() + word[1:3] + word[3].upper() +word[4:]

print(Capitalise('macdonald'))