# #find the index of the maximum value using function 

def maximum(list):
    max = list[0]
    index = 0

    for i in range(1 , len(list)):
        if list[i] > max:
            max = list[i]
            index = i
    print(index) 

list = [ 45 , 78 , 12 , 79 , 89]
maximum(list)
'''
Here, we have taken a list named ‘my_list’, which contains a list of integers. 
We initially take the first element of the list as the maximum element and store the element into ‘max’. 
Then we take a variable as ‘index’ and store it with the value 0.

After that, we shall iterate a loop from index 1 to the last element of the list. 
Inside the loop using an if statement, we shall compare the ith element, i.e.,
 the current element of ‘my_list’ with the ‘max’ variable. 
If the value of the current element happens to be greater than the value of ‘max’,
 then we shall assign the value of the current element to ‘max’ and the current index to ‘i’. 
After completion of the for loop, we shall print the value of ‘index’, 
which will denote the index of the maximum value from the list.'''


