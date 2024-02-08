# write an algorithm to determine if a number is "happy".

def number_is_happy(n):
    if n == 1:
        return True
    elif n == 4:
        return False
    else:
        return number_is_happy(sum([int(i) ** 2 for i in str(n)]))
    
print(number_is_happy(19))



# longest valid parentheses with comments

def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

print(longest_valid_parentheses(")()()(()))(((()(((((((())))))))))"))


