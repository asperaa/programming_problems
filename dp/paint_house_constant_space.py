"""Paint house.Time - O(n). Space - O(n)"""
def paint_house(costs):
    if not costs:
        return 0
    
    length = len(costs)

    first, second, third = costs[0]

    for i in range(1, length):
        temp_first, temp_second, temp_third = first, second, third
        first = (min(temp_second, temp_third) + costs[i][0])
        second = (min(temp_first, temp_third) + costs[i][1])
        third = (min(temp_first, temp_second) + costs[i][2])

    return min(first, second, third)

if __name__ == "__main__":
    costs = [[5,8,6], [19,14,13], [7,5,12], [14,15,17], [3,20,10]]
    print(paint_house(costs))