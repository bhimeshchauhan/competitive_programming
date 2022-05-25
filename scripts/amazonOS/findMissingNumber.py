# getMissingNo takes list as argument
def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return total - sum_of_A


# Driver program to test the above function
A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)
# This code is contributed by Pratik Chhajer

"""
"""

# a represents the array
# n : Number of elements in array a


def getMissingNo(a, n):
    i, total = 0, 1

    for i in range(2, n + 2):
        total += i
        total -= a[i - 2]
    return total


# Driver Code
arr = [1, 2, 3, 5]
print(getMissingNo(arr, len(arr)))

# This code is contributed by Mohit kumar


"""
"""

# Python3 program to find
# the missing Number
# getMissingNo takes list as argument


def getMissingNo(a, n):
    x1 = a[0]
    x2 = 1

    for i in range(1, n):
        x1 = x1 ^ a[i]

    for i in range(2, n + 2):
        x2 = x2 ^ i

    return x1 ^ x2


# Driver program to test above function
if __name__ == '__main__':

    a = [1, 2, 4, 5, 6]
    n = len(a)
    miss = getMissingNo(a, n)
    print(miss)

# This code is contributed by Yatin Gupta


"""

"""

# Python3 program to find
# the missing Number
# getMissingNo takes list as argument


def getMissingNo(a, n):
    n_elements_sum = n*(n+1)//2
    return n_elements_sum-sum(a)


# Driver program to test above function
if __name__ == '__main__':

    a = [1, 2, 4, 5, 6]
    n = len(a)+1
    miss = getMissingNo(a, n)
    print(miss)
