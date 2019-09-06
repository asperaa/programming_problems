"""Calculate the score of parentheses following a various rules"""
def score_of_parentheses(brackets):
        stack = []
        for bracket in brackets:
            collector = 0
            if bracket == "(":
                stack.append(bracket)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    collector = stack.pop()
                    while stack[-1] != "(":
                        collector += stack.pop()
                    stack.pop()
                    stack.append(collector*2)
        final_score = 0
        while stack:
            final_score += stack.pop()
            
        return final_score

if __name__ == "__main__":
    b1 = "()"
    b2 = "(())"
    b3 = "()()"
    b4 = "(()(()))"
    bs = [b1, b2, b3, b4]
    for b in bs:
        print(score_of_parentheses(b))