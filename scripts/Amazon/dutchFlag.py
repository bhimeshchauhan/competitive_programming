"""
Given an array A[] consisting 0s, 1s and 2s. The task is to write a 
function that sorts the given array. The functions should put all 0s first, 
then all 1s and all 2s in last.

Examples: 
 

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

[0, 1, 2, 0, 1, 2]
 s              e
 m

[0, 1, 2, 0, 1, 2]
    s           e
    m

[0, 1, 2, 0, 1, 2]
    s           e
       m

[0, 1, 2, 0, 1, 2]
    s        e
       m
       
[0, 1, 1, 0, 2, 2]
    s     e
       m

[0, 1, 1, 0, 2, 2]
    s     e
          m

[0, 0, 1, 1, 2, 2]
       s  e
             m

"""

class Solution:
    def main(self, a):
        arr_size = len(a)
        lo = 0
        hi = arr_size - 1
        mid = 0
        while mid <= hi:
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo = lo + 1
                mid = mid + 1
            elif a[mid] == 1:
                mid = mid + 1
            else:
                a[mid], a[hi] = a[hi], a[mid]
                hi = hi - 1
        return a
        
        
if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2]
    print(Solution().main(arr))