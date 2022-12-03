
def has_valid_parantheses(str1):
    str1 = str1.strip()
    if len(str1) <=0:
        return False
    stack = []
    matchmap = {')':'(', '}':'{', ']':'['}
    charsset = (')','(', '}','{', ']','[')
    atleastonceoccurance = False
    for char1 in str1:
        if char1 in charsset:
            atleastonceoccurance = True
            if char1 in matchmap:
                if stack and stack[-1] == matchmap[char1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(char1)
    if len(stack) > 0:
        return False
    return atleastonceoccurance


if __name__ == "__main__":
    str1 = input()
    result = has_valid_parantheses(str1)
    print('true' if result else 'false')