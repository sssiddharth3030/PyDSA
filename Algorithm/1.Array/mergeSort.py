# Merge Sort is a Divide and Conquer Algorithm

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        mergeSort(left_arr)
        mergeSort(right_arr)
        
        # left arr index, right array index & merrgered array index
        i, j, k = 0, 0, 0

        while (i< len(left_arr) and j < len(right_arr) ):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j +=1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

if "__main__":
    arr = [10,7,8,11,1,5,9]
    n = len(arr)

    mergeSort(arr)

    # for val in arr:
    #     print(val, end=" ")