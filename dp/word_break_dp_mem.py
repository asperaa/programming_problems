"""Word Break. DP with Memoisation"""
def word_break_util(s, word_dict, start, dp):
    length = len(s)
    if start == length:
        return True
    
    if dp.get(start):
        return dp[start]

    for end in range(start, length):

        if s[start: end+1] in word_dict and word_break_util(s, word_dict, end+1, dp):
            dp[start] = True
            return dp[start]
    dp[start] = False
    return dp[start]

def word_break(s, word_list):
    word_dict = set(word_list)
    dp = dict()
    return word_break_util(s, word_dict, 0, dp)


if __name__ == "__main__":
    word_list = ["cats", "dog", "sand", "and", "cat"]
    word_list1 = ["a"]
    print(word_break("catsanddog", word_list))

