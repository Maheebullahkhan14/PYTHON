#check if a given key is present or not in a dictionary 
mydict = {"Gulam" : "Mysql" , "kaif" :"Sql" ,"deepak" : "python"}
user_ip = input("enter the key to check")

if user_ip in mydict.keys():
    print("key is present in the dictionary ")
    print("value is " , user_ip)
else:
    print("not present ")