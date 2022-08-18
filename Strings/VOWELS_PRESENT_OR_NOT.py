#Python program to accept the strings which contains all vowels
def check_Vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    for char in vowels:
        if char in string:
            print("String is accepted")
            break

        else :
            print("Not accepted ")
            break

if __name__== '__main__':

    string1 = ("Abcd")
    check_Vowels(string1)