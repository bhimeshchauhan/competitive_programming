class Solution(object):
    def myAtoi(self, s):
        state = "at_beginning"
        sign = 1
        total = 0
        for c in s:
            if state == "at_beginning":
                if c.isspace():
                    None
                elif c == '-':
                    sign = -1
                    state = "reading_digits"
                elif c == '+':
                    sign = 1
                    state = "reading_digits"
                elif c.isdigit():
                    total = int(c)
                    state = "reading_digits"
                else:
                    break
            elif state == "reading_digits":
                if c.isdigit():
                    total = total*10 + int(c)
                else:
                    break
        return min(
            int(2**31)-1,
            max(
                total * sign,
                int(-2**31)
            )
        )
