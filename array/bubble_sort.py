"""Bubble sort in an array"""

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    return arr

def bubble_sort(arr):
    length = len(arr)

    for i in range(0, length):
        for j in range(0, length-1):
            if arr[j] >= arr[j+1]:
                arr = swap(arr, j, j+1)
    return arr

if __name__ == "__main__":
    arr = [6, 10, 5, 1, 10]
    print(bubble_sort(arr))