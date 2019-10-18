"""Power of x. Binary Search Recursive"""
def power_util(x, n):
    if n == 0:
        return 1
    half = power_util(x, n//2)

    if n%2 == 0:
        return half*half
    else:
        return half*half*x

def power(x, n):
    N = n
    if N < 0:
        x = 1/x
        N = -N
    
    return power_util(x, N)

if __name__ == "__main__":
    print(power(2.0, 4.0))
