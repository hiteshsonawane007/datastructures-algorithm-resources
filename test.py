def is_balanced_parentheses(s):
    if not s:
        return "The string is empty."
    
    stack = []
    parentheses = {"(": ")", "[": "]", "{": "}"}
    missing_characters = []

    for char in s:
        if char in parentheses:
            stack.append(char)
        elif char in parentheses.values():
            if not stack or parentheses[stack.pop()] != char:
                missing_characters.append(char)
                return False, len(missing_characters), missing_characters

    while stack:
        missing_characters.append(parentheses[stack.pop()])

    if missing_characters:
        return False, len(missing_characters), missing_characters
    else:
        return True, 0, []

# Test cases
print(is_balanced_parentheses(""))  # "The string is empty."
print(is_balanced_parentheses("()"))  # (True, 0, [])
print(is_balanced_parentheses("()[]{}"))  # (True, 0, [])
print(is_balanced_parentheses("(]"))  # (False, 1, [']'])
print(is_balanced_parentheses("([)]"))  # (False, 2, [']', ')'])
print(is_balanced_parentheses("{[]}"))  # (True, 0, [])
