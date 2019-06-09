def mergeTwo(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    
    i = 0
    j = 0

    arr3 = []
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    
    while i < n1:
        arr3.append(arr1[i])
        i+=1
    
    while j < n2:
        arr3.append(arr2[j])
        j+=1
    
    return arr3

def merge(arr1, arr2, arr3):
    arr4 = mergeTwo(arr1, arr2)
    arr5 = mergeTwo(arr3, arr4)

    return arr5


if __name__ == "__main__":
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    arr3 = [7, 8, 9]

    print(merge(arr1, arr2, arr3))
