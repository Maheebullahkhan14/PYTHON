import random 

attempts = 0

number = random.randint(1,10)
print("i am thinking a number between 1 to 10")

while attempts < 6:
    guess_number = int(input("enter the Number : "))
    attempts+=1

    if guess_number<number:
        print("higher")

    elif guess_number > number :
        print("Lower")

    elif guess_number == number :
        break 


if guess_number == number:
    print(str(attempts))
    print(f"good job you had guessed the Number in {attempts} attempts")

print("out of attempts")

