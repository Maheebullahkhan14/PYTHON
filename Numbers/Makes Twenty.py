'''Makes Twenty : if the sum of two number is 20 or one number is 20 then return True'''
def MakesTwenty(num1,num2):
    if num1+num2 == 20  or num1 == 20 or num2==20:
        return True

    else:
        return False


print(MakesTwenty(10,16))