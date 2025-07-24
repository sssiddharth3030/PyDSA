# quick sort is Divide & Conquer based Algorithm

def partition(arr, low, high):
    pivot = arr[high]

    i = low-1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i+1, high)
    return i+1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr,low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr = [10,7,8,11,1,5,9]
    n = len(arr)

    quickSort(arr, 0, n-1)

    for val in arr:
        print(val, end=" ")
