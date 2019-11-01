"""Check whether a given string is the sub string subsequence of not"""
def is_subsequence(s, t):
    source_index = 0

    for character in t:
        print(source_index)
        if s[source_index] == character:
            source_index += 1
        if source_index >= len(s):
            break
    return source_index == len(s)

if __name__ == "__main__":
    print(is_subsequence("leetcode", "yyyyyylyyyyyyyyyyyyyyyyeyyyyyyyyyyyyeyyyyyyyyyytyyyyyyyyycyyyyyoyyyyyyyyydyyyyyyyyeyyyyy"))