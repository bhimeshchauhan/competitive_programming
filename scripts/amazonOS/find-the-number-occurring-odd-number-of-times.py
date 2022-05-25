"""

Find the Number Occurring Odd Number of Times

https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/


"""
# function to find the element occurring odd
# number of times


from collections import Counter


def getOddOccurrence(arr, arr_size):

    for i in range(0, arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count += 1

        if (count % 2 != 0):
            return arr[i]

    return -1


# driver code
arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
n = len(arr)
print(getOddOccurrence(arr, n))


# function to find the element
# occurring odd number of times
def getOddOccurrence(arr, size):

    # Defining HashMap in C++
    Hash = dict()

    # Putting all elements into the HashMap
    for i in range(size):
        Hash[arr[i]] = Hash.get(arr[i], 0) + 1

    # Iterate through HashMap to check an element
    # occurring odd number of times and return it
    for i in Hash:

        if(Hash[i] % 2 != 0):
            return i
    return -1


# Driver code
arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
n = len(arr)

# Function calling
print(getOddOccurrence(arr, n))

# Python program to find the element occurring odd number of times


def getOddOccurrence(arr):

    # Initialize result
    res = 0

    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element

    return res


# Test array
arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

print("%d" % getOddOccurrence(arr))


# importing counter from collections

# Python3 implementation to find
# odd frequency element

def oddElement(arr, n):

    # Calculating frequencies using Counter
    count_map = Counter(arr)

    for i in range(0, n):

        # If count of element is odd we return
        if (count_map[arr[i]] % 2 != 0):
            return arr[i]


# Driver Code
if __name__ == "__main__":

    arr = [1, 1, 3, 3, 5, 6, 6]
    n = len(arr)
    print(oddElement(arr, n))

# This code is contributed by vikkycirus
