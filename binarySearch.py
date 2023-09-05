from random import randint

def binarySearch(arr, high, low, num):
    mid = (high + low) // 2
    
    if num == arr[mid]:
        return mid
    #Num is in right zone
    elif num > arr[mid]:
        return binarySearch(arr, high, mid+1, num)
    #Num is in left zones
    elif num < arr[mid]:
        return binarySearch(arr, mid-1, low, num)
    else: return -1

arr = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Introduce a number: "))
print(arr)
print(binarySearch(arr, len(arr), 0, num))

