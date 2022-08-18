#find the words which are greater then length k 
def larger_word(k , str):

    string = []
    
    text = str.split(" ")
    for i in text:
        if len(i)>k:
            string.append(i)
    return string

k = 4
str = ("Encyclopedia is very Helpful")
print(larger_word(k,str))