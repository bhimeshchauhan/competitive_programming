import math
import string
MAX_NUM = math.inf

def validate_hex(hex):
  return all(c in string.hexdigits for c in hex)

def is_square(i):
    return i == math.isqrt(i) ** 2

def min_breaks(hex, index = 0):
    hex_length = len(hex)
    if index == hex_length:
        return 0
    numeric = 0
    result = MAX_NUM
    for i in range(index, hex_length):
        num = int(hex[i], 16)
        numeric = numeric * 16 + num
        if is_square(numeric):
            result = min(result, 1+min_breaks(hex, i+1))
    return result

def get_min(hex):
    if not validate_hex(hex):
        return "Invalid hex"
    pieces = min_breaks(hex)
    if pieces == MAX_NUM:
        return -1
    return pieces

hex = "1a919"
print(get_min(hex))
