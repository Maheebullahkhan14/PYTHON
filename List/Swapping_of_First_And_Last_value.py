def swaplist(newlist):

    length = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[length - 1]

    return newlist

newlist = [12 , 5 , 8 , 50]
b = swaplist(newlist)

print(b)