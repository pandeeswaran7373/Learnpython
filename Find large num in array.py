#find largest number in array

def findLargeNum(arr):
    max_element=arr[0]
    for num in arr:
        if num > max_element:
            max_element=num
    return max_element
#find

user_input=input("Enter Values With Space: ")

arr=[int(x) for x in user_input.split()]

print("The largest element in the array is", findLargeNum(arr));
