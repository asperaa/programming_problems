"""Word break .1D DP. Time - O(n2). Space - O(n)"""
def word_break(s, word_list):
    length = len(s)
    dp = [False] * (length+1)
    dp[0] = True
    word_dict = set(word_list)

    for i in range(1, length+1):
        for j in range(0, i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[length]

if __name__ == "__main__":
    word_list = ["cats", "dog", "sand", "and", "cat"]
    word_list1 = ["a"]
    print(word_break("catsandog", word_list))

    