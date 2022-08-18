'''Fibonacci series is like the addition of previous two number  like 0 , 1 , 1 , 2 , 3, 5,  8 and so on
if we add 0 + 1 we will get 1 as our 2nd fibonacci series number 
so to do this first we have to assign 2 Values 0 and 1  after adding we will get the fibonacci series '''

def fibonacci(n):                 
    prevnum = 0
    currentnum = 1
    for i in range(1,n):
        prevprevnum = prevnum
        prevnum = currentnum
        currentnum =  prevprevnum + prevnum
    return currentnum
        

n = int(input("Enter the number To find Fibonacci num "))
print(fibonacci(n))


