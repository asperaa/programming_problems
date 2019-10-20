"""Climb stairs using only 1 or 2 steps. Find the num of ways.Space and time - O(n) and O(1)"""
def climb_stairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    first = 1
    second = 2
    for i in range(3, n+1):
        ans = first + second
        first = second
        second = ans
    return ans

if __name__ == "__main__":
    print(climb_stairs(5))