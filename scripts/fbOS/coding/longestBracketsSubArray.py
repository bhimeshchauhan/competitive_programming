"""

Say we have a list of Strings contains an starting process Ai and an edning one Bi where i is an integer showing the id of the process. We can have muliple Start/End pairs which are shown by adding numbers after each one of these letters.

an Starting process should always end with the equivalent End (evey Ai should come before Bi)
a valid path cannot have duplicate processes, like A1, B1, A1, B1
both Ai and Bi should exist in the valid path
This is very similar to matching ( with )
For example:
[A1, B1, A2, B2] is a valid process array since every Ai has ended with the same Bi.
[A1, A2, B2, B1] or [A1, A2, B1, B2] are also valid
[A1, A2, B1, B2] valid
[A1, B1, A2, B2] valid
[A1, B2, B1, A2] invalid
[A1, B2] invalid
[A1, A2] invalid
[A1, B1, B1] invalid
[] valid
[A1, A1, B1] invalid
[A1, A1, B1, B1] invalid
[A1, B1, A1] invalid
[A1, B1, A1, B1] invalid

Given a list of processes, find the longest valid process subarray you can find:

[A1, B1, A2, B2] : return 4
[A1, A2, B2] : return 2 (A2, B2)
[A1, B1, A2, A1, B1, B2] : return 4 (A2, A1, B1, B2)
I tried to solve is via stack and similar to Longest Valid Parenthesis but it failed for cases where you have full match (A1, B1, A2, A1, B1, B2 vs A1, B1, A2, B2)


"""

# Python program to find length of the longest valid
# substring

def findMaxLen(string):
    n = len(string)

    # Create a stack and push -1
    # as initial index to it.
    stk = []
    stk.append(-1)

    # Initialize result
    result = 0

    # Traverse all characters of given string
    for i in range(n):

        # If opening bracket, push index of it
        if string[i] == '(':
            stk.append(i)

        # If closing bracket, i.e., str[i] = ')'
        else:

            # Pop the previous opening bracket's index
            if len(stk) != 0:
                stk.pop()

            # Check if this length formed with base of
            # current valid substring is more than max
            # so far
            if len(stk) != 0:
                result = max(result,
                             i - stk[len(stk)-1])

            # If stack is empty. push current index as
            # base for next valid substring (if any)
            else:
                stk.append(i)

    return result


# Driver code
string = "((()()"

# Function call
print(findMaxLen(string))

string = "()(()))))"

# Function call
print(findMaxLen(string))
