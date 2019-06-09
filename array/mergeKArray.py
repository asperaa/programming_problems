def merge2Array(arr1, arr2, n1, n2):
    arr3 = [None]*(n1+n2)
    i = 0
    j = 0
    k = 0

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i = i + 1
            k = k + 1
        else:
            arr3[k] = arr2[j]
            j = j + 1
            k = k + 1
        
    
    while i < n1:
       arr3[k] = arr1[i]
       i = i + 1
       k = k + 1
    while j < n2:
        arr3[k] = arr2[j]
        j = j + 1
        k = k + 1

    return arr3



arr1 = [1, 2, 3, 8]
arr2 = [4, 5, 6, 9, 78]

n1 = len(arr1)
n2 = len(arr2)

print(merge2Array(arr1, arr2, n1, n2))




