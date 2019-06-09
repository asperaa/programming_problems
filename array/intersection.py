def intersection(lst1, lst2):

    lst3 = [num for num in lst1 if num in lst2]

    return lst3


if __name__ == "__main__":
    lst1 = [1, 3, 5]
    lst2 = [1, 3, 6]

    print(intersection(lst1, lst2)) 
    