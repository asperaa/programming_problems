"""Min cost climbing stairs. Time - O(n). Space - O(1)"""
def min_cost(costs):
    
    prev_min = costs[0]
    curr_min = costs[1]

    for cost in costs[2:]:
        temp = curr_min
        curr_min = min(curr_min + cost, prev_min + cost)
        prev_min = temp
    
    final_cost = min(curr_min, prev_min)
    return final_cost

if __name__ == "__main__":
    costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(min_cost(costs))