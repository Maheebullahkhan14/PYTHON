'''if the input number divisible by 3 then fizz
if the number divisible by 5 then buzz
and if divided by both 3 and 5 then fizzbuzz
and if not divisible by any number then given that input number itself'''

def fizzbuzz(input):
    
    if input%3 == 0 and input%5 == 0 :
        return "fizzbuzz"
    if input%3 == 0 :
        return "buzz"
    if input%5 == 0 :
        return "Fizz"

    else :
        return input

fizzbuzz(15)
print(fizzbuzz(10))
