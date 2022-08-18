def add(x,y):
    return x + y 

def sub(x,y):
    return x - y

def Multiply(x ,y):
    return x*y

def division(x,y):
    return x/y


print("select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.multiplication")
print("4.Divison")


while True :
    choice = input("Enter choice 1/2/3/4 : ")
     
    # check if choice is one of the four option
    if choice in ('1','2','3','4'):
        num1= float(input("Enter The num1"))
        num2 = float(input("Enter the num2"))


        if choice == '1':
            print(num1, '+' ,num2 , '=', add(num1,num2) )

        elif choice == '2':
            print(num1, '-',num2, '=', sub(num1,num2))

        elif choice == '3':
            print(num1, '*', num2 ,'=',Multiply(num1,num2) )

        elif choice == '4':
            print(num1 ,'/',num2,'=',division(num1,num2) )

        # check if user wants another calculation
        # break the while loop if answer is no  
        next_calculation = input("Lets do  next Calculation? : yes/no")

        if next_calculation == 'no':
            break 
        


        else :
            print("Invalid Input")