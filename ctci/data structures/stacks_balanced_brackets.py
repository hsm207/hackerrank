def is_matched(expression):
    stack = []
    pair_lookup = {'{': '}', '(': ')', '[': ']'}
    # loop through each character in the expression and push its closing counterpart
    for ch in expression:
        if ch in pair_lookup:
            stack.append(pair_lookup[ch])

        # when encounter a closing counterpart, check that the stack is not empty and that the top of the stack
        # matches the closing counterpart
        # otherwise, we know that the expression does not match
        else:
            if not stack or stack[-1] != ch:
                return False
            else:
                stack.pop()
    # stack should be empty after going through all the characters in expression
    return len(stack) == 0


# expr = '{[(])}'
# is_matched(expr)
# expr = '{[(])}'
# stack = []
# pair_lookup = {'{': '}', '(': ')', '[': ']'}

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")

import bisect