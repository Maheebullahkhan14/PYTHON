#Sum of all odd Numbers
num = (int(input("Enter The Number : ")))
total = 0

for i in range(1 , num+1):
    if i%2 != 0:
        total = total + i

print(f"Sum of All odd Numbers : {total} ")