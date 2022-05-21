"""


"""


from functools import lru_cache


@lru_cache(None)
def helper(coinTuple, need, i=0):
    if need <= 0 or i == len(coinTuple):
        return need == 0

    return helper(coinTuple, need - coinTuple[i], i + 1) or \
        helper(coinTuple, need, i + 1)


def newCoinChange(coins, target):
    return helper(tuple(coins), target)


print(newCoinChange([1, 5, 10], 0))
print(newCoinChange([1, 5, 10], 1))
print(newCoinChange([1, 5, 10], 2))
print(newCoinChange([1, 5, 10], 6))
print(newCoinChange([1, 5, 10], 11))
print(newCoinChange([1, 5, 10], 16))
print(newCoinChange([1, 5, 10], 17))
print(newCoinChange([3, 10, 2], 5))
print(newCoinChange([1, 3, 7, 12, 8], 18))
