"""Merge sort in an array"""

def merge(arr, l, mid, r):
    size_l = mid - l + 1
    size_r = r - mid
    L = [0]*size_l
    R = [0]*size_r
    for i in range(0, size_l):
        L[i] = arr[l+i]
    for j in range(0, size_r):
        R[j] = arr[mid+1+j]
    
    i, j, k = 0, 0, l

    while i < size_l and j < size_r:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < size_l:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < size_r:
        arr[k] = R[j]
        j += 1
        k += 1
    

def merge_sort(arr, l, r):
    if l < r:
        mid = (l + (r-1))//2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, mid, r)
    return arr

if __name__ == "__main__":
    arr = [5, 2, 10, 4, 5]
    print(merge_sort(arr, 0, len(arr)-1))