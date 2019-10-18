"""Binary Search Recursion"""
def bs(arr, l, r, item):
    if r >= l:        
        mid = l + (r-l)//2

        if arr[mid] == item:
            return mid
        elif item < arr[mid]:
            return bs(arr, l, mid-1, item)
        else:
            return bs(arr, mid+1, r, item)
    else:
        return False
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(bs(arr, 0, len(arr)-1, 5))