def mergeTwo(arr1, arr2):
    n1, n2 = (len(arr1), len(arr2))
    i = j = 0
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

def mergeList(long_list):
    arr1, arr2, arr3 = long_list

    arr4 = mergeTwo(arr1, arr2)
    arr5 = mergeTwo(arr4, arr3)

    return arr5

if __name__ == '__main__':
    example_list = [[1, 2, 4], [5, 6, 7], [10]]
    print(mergeList(example_list))