"""

Given an array of characters where each character represents a fruit tree, you 
are given two baskets, and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. 
You will pick one fruit from each tree until you cannot, i.e., you will stop when 
you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the 
subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

"""

def fruits_into_baskets(fruits):
    window_start = 0
    refer_dict = {}
    max_count = 0
    
    for window_end in range(len(fruits)):
        if fruits[window_end] not in refer_dict:
            refer_dict[fruits[window_end]] = 0
        refer_dict[fruits[window_end]] += 1
        
        while len(refer_dict) > 2:
            refer_dict[fruits[window_start]] -= 1
            if refer_dict[fruits[window_start]] == 0:
                del refer_dict[fruits[window_start]]
            window_start += 1
        max_count = max(max_count, window_end - window_start + 1)
    return max_count


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
