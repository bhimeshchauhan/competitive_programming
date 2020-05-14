class Solution:
    # @return a boolean
    def isValid(self, s):
        # Initialize stack and the dict
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            # Add to stack if the char is an opening bracket
            if char in dict.values():
                stack.append(char)
            # If it's a closing bracket check if there was a closing bracket on stack
            elif char in dict.keys():
                # If the stack isd empty or the
                if stack == [] or dict[char] != stack.pop():
                    return False
            # else
            else:
                return False
        # in the end if the stack is empty then return boolean
        return stack == []


assert Solution().isValid('()(){}[]')
assert not Solution().isValid('()(){(][]')
