"""selection sort in an array"""
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def selection_sort(arr):
    if len(arr) == 0:
        return arr

    length = len(arr)
    for i in range(0, length):
        min_index = i
        for j in range(i+1, length):
            if arr[j] <= arr[min_index]:
                min_index = j
        arr = swap(arr, i, min_index)
    return arr

if __name__ == "__main__":
    arr = [1, 2, 100, 10, 80]
    print(selection_sort(arr))