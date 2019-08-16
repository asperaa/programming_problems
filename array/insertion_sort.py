"""Insertion Sort algorithm"""
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        element = arr[i]
        j = i - 1 
        while j>=0:
            if element < arr[j]:
                arr[j+1] = arr[j]
            else:
                break
            j -= 1
        arr[j+1] = element
    return arr

if __name__ == "__main__":
    arr = [10, 4, 6, 7, 12, 2, 9]
    print(insertion_sort(arr))
        