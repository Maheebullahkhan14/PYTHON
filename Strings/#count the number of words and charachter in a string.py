#Program to Calculate the Number of Words and the Number of Characters Present in a String
String = "Lets go to the goa for the vacation"
charcount = 0
wordcount = 1

for i in String :
    if i == ' ':
        wordcount += 1
    charcount +=1

print(f"this sentence contains {wordcount}")
print(f"this sentence contains {charcount}")


'''Give the string as static input and store it in a variable.
Take a variable to say stringwords that stores the total words in the given string.
Initialize the stringwords to 1.
Take a variable to say stringchars that store the total characters in the given string.
Initialize the stringchars to 0.
To Traverse, the characters in the string, use a for loop and increment the stringchars variable each time by 1.
If a space character is encountered then increment the stringwords by 1.
Print the total number of characters and words in the string i.e stringchars and stringwords.
The Exit of the program.'''