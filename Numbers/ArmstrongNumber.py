num = int(input("Enter The Number")) #taking the number from the input
sum=0                                
order = len(str(num))
temp = num

while (num > 0):
    digit = num%10                     #552 after doing mod this will give 2
    sum += digit ** order              # order is len of the digit so 2**4
    num = num//10                      #after the sum of order we have to update the num like 552 into 55
                                       # so it goes on changing 
if sum == temp :
    print("armstrong")

else:
    print("not ")

