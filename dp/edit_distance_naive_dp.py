"""Edit distance. DP Recur"""
def edit_distance_util(source, dest, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    
    if source[m-1] == dest[n-1]:
        return edit_distance_util(source, dest, m-1, n-1)
    
    insert_opt = 1 + edit_distance_util(source, dest, m, n - 1)
    remove_opt = 1 + edit_distance_util(source, dest, m - 1, n)
    replace_opt = 1 + edit_distance_util(source, dest, m-1, n-1)

    return min(insert_opt, remove_opt, replace_opt)

def edit_distance(source, dest):
    return edit_distance_util(source, dest, len(source), len(dest))

if __name__ == "__main__":
    print(edit_distance("nirav", "nitin"))
