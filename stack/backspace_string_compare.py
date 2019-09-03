"""Backspace compare string"""
def backspaceCompare(str_1: str, str_2: str) -> bool:
    length_1 = len(str_1)
    length_2 = len(str_2)
    i = length_1 - 1
    j = length_2 - 1
    count_1 = 0
    count_2 = 0
    while i >= 0 or j >= 0:
        while i >= 0:
            if str_1[i] == "#":
                count_1 += 1
                i -= 1
            elif count_1 > 0:
                count_1 -= 1
                i -= 1
            else:
                break
        while j >= 0:
            if str_2[j] == "#":
                count_2 += 1
                j -= 1
            elif count_2 > 0:
                count_2 -= 1
                j -= 1
            else:
                break
                
        
        if i < 0:
            return j < 0
        if j < 0:
            return i < 0
        
        if str_1[i] != str_2[j]: 
            return False
        
        i -= 1
        j -= 1
    return True

if __name__ == "__main__":
    s1 = "ab##"
    s2 = "c#d#"
    print(compare_string(s1, s2))

