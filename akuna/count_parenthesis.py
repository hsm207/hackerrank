def balanced(a_str):
    stack = []
    pair_lookup = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

    for char in a_str:
        if char in pair_lookup:
            stack.append(pair_lookup[char])
        else:
            if not stack or char != stack[-1]:
                return False
            else:
                stack.pop()

    return len(stack) == 0
