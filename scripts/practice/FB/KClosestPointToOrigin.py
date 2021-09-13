"""

K Closest Point to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104

"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Minheap solution 2, useful when k is much smaller than N, which could reduce time complexity to ~O(N)
            The idea is to maintain a heap of size k.
        
        Steps:
            1. For each point (x, y) in the array, we insert them into a binary heap
                along with the distance (we reverse the sign) since we need to keep points with smallest distance
            2. To keep the heap of size k, we use `heappushpop` function to immediately
                remove the smallest element as we push a new one.

        Complexity:
            time: O(N*logK)
            space: O(K) for the heap
        '''
        heap = []
        for x, y in points:  # O(N)
            dist = -(x ** 2 + y ** 2)
            if k == len(heap):
                heapq.heappushpop(heap, (dist, x, y))  # O(logK) as time complexity depend on the size of the heap
            else:
                heapq.heappush(heap, (dist, x, y))  # O(logK)
        return [(x, y) for dist, x, y in heap]
        
      
    def kClosest_minHeap1(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Minheap solution 1, useful when N is small and k is almost up to N,
            so MinHeap would have a constant factor of 2N.

        Steps:
            1. Create a list of tuples containing (dist, x, y) points
            2. Heapify such that we have a tree-based data structure where the parent node
                is always smaller than child node. ie. the tree root is the smallest element in the tree
            3. For k times, we use `heappop` (a function that removes the smallest element in this minHeap)
                to get k closest distance (x, y) pointss
        
        Complexity:
            time: O(N + k*logN)
            space: O(N) since we keep two arrays of size N and k, where max of k would be N
        '''
        min_heap = []
        for x, y in points:  # O(N)
            min_heap.append((x ** 2 + y ** 2, x, y))  # (distance, x, y)
        
        heapq.heapify(min_heap)  # O(N)
        
        output = []
        for _ in range(k):  # O(k)
            dist, x, y = heapq.heappop(min_heap)  # O(logN)
            output.append((x, y))
            
        return output


    def kClosest_naive(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Naive solution using hashmap.
        
        Complexity:
            time: O(N logN)  -- sorting a list
            space: O(N)  -- hashmap
        '''
        d = {}
        for x, y in points:  # O(N)
            dist = x ** 2 + y ** 2
            d[(x, y)] = dist
        
        sorted_d = sorted([(k, v) for k, v in d.items()], key=lambda x: x[1])  # O(N logN)
        # print(sorted_d)
        return [i[0] for i in sorted_d][:k]  # O(N)