"""Two sum sorted. O(nlogn)"""
def two_sum(arr, target):
    for i in range(len(arr)):
        l, r = i + 1, len(arr) - 1
        item = target - arr[i]

        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == item:
                return [i+1, mid+1]
            elif item < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1

if __name__ == "__main__":
    arr = [1, 3, 4, 5]
    print(two_sum(arr, 9))