import mergeSort
import math

def binarySearch(arr, target):
    left , right = 0, len(arr) - 1

    while(left < right):
        mid = math.ceil( left + ((right - left)/2 ) )

        # print(arr[left], arr[mid], arr[right])

        if arr[mid] == target:
            return mid
        elif arr[right] == target:
            return right
        elif arr[left] == target:
            return left
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1

    return -1

def callBinarySearch(arr, target):
    position = binarySearch(arr, target)

    if position == -1:
        print(target, 'not found.')
    else:
        print(arr[position], "found at arr[", position + 1 , "].")
    
    return position


if __name__ == "__main__":
    arr = [10,7,8,11,1,5,9,13]

    mergeSort.mergeSort(arr)

    print(arr)

    callBinarySearch(arr, 3)
    callBinarySearch(arr, 5)
    callBinarySearch(arr, 10)
    callBinarySearch(arr, 13)
    callBinarySearch(arr, 30)

