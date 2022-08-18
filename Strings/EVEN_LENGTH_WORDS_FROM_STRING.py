#Python program to print even length words in a string
# Step 1- Define a function that will print even words in the string

# Step 2- Use split to extract the words

# Step 3- Run a loop to iterate over the words

# Step 4- Check if the length is even

# Step 5- Print word if the length is even

def evenlength(str):
    a = str.split()

    for i in a:
        if len(i)%2 ==0:
            print(i ,end = ' ')
            

str = "khan Maheebullah is preparing very bad"
evenlength(str)