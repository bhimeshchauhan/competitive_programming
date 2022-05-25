# Python3 program to convert
# integer value to roman values

# Function to convert integer to Roman values
import math


def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1


# Driver code
if __name__ == "__main__":
    number = 3549
    print("Roman value is:", end=" ")
    printRoman(number)


"""
"""

# Python3 program for above approach

# Function to calculate Roman values


def intToRoman(num):

    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    # Converting to roman
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]

    ans = (thousands + hundreds +
           tens + ones)

    return ans


# Driver code
if __name__ == "__main__":
    number = 3549
    print(intToRoman(number))


"""
"""

# Python 3 program to convert integer
# number to Roman values


def integerToRoman(A):
    romansDict = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }

    div = 1
    while A >= div:
        div *= 10

    div /= 10

    res = ""

    while A:

        # main significant digit extracted
        # into lastNum
        lastNum = int(A / div)

        if lastNum <= 3:
            res += (romansDict[div] * lastNum)
        elif lastNum == 4:
            res += (romansDict[div] +
                    romansDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[div * 5] +
                    (romansDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[div] +
                    romansDict[div * 10])

        A = math.floor(A % div)
        div /= 10

    return res


# Driver code
print("Roman value for the integer is:"
      + str(integerToRoman(3549)))
