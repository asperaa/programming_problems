"Backspace string compare"
def backspaceCompare(s1, s2):
    length_s1 = len(s1)
    length_s2 = len(s2)

    i = length_s1, j = length_s2
    count_1 = count_2 = 0

    while i >= 0 and j >= 0:
        if s1[i].isalpha() and s2[j].isalpha():
            if count_1 == 0 and count_2 == 0:
                i -= 1
                j -= 1