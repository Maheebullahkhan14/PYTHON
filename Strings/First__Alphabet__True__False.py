'''Animal cracker - Take two word string if both the string letter 
 startswith same alphabet then return true '''




def word_checker(name):
    first ,second= name.split()                #First we have to split both the string with spaces
    
    return first[0] == second[0]               #assinging the value of first word equal to value of second 

                                               #so if my first character of both string is same then True else false


print(word_checker('bar darfoo'))


