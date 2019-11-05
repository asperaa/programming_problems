"""Word break problem. Naive aprroach"""

def word_break(s, word_list) :
    word_dict = dict()
    for word in word_list:
        word_dict[word] = True
    return word_break_util(s, word_dict, 0)

def word_break_util(s, word_dict, start):
    length = len(s)
    if start == length:
        return True

    for end in range(start+1, length):
        if s[start: end+1] in word_dict and word_break_util(s, word_dict, end+1):
            return True
    return False

if __name__ == "__main__":
    word_list = ["cats", "dog", "sand", "and", "cat"]

    print(word_break("catsandog", word_list))
