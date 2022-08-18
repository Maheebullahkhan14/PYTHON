#Remove Duplicates from a Strings

def Remove_Dup(s):
    string =set(s)
    string = ''.join(string)
    duplicate =''

    for i in s:
        if (i in duplicate ):
            pass
        else:
            duplicate = duplicate +i

    print("After the removing ",duplicate)

s = ("Gulluulkhaan")
Remove_Dup(s)