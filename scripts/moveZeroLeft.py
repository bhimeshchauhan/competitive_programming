"""

Given an integer array, move all elements that are 0 to the left while maintaining the order of other elements in the array. 
The array has to be modified in-place.

"""

class Solution():
    def main(arr):
        ptr_one = len(arr) - 2
        ptr_two = len(arr) - 1
        while ptr_one >= 0:
            if arr[ptr_one] != 0:
                arr[ptr_two], arr[ptr_one] = arr[ptr_one], arr[ptr_two]
                ptr_two -= 1
            ptr_one -= 1
    
    
if __name__ == "__main__":
    arr = [0, 10, 20, 0, 59, 63, 0, 88, 0]
    Solution.main(arr)
    print(arr)