"""

Erect the Fence

You are given an array trees where trees[i] = [xi, yi] 
represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum 
length of rope as it is expensive. The garden is well fenced 
only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

Example 1:

Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:

Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]

Constraints:

1 <= points.length <= 3000
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.
"""


"""
So the crux of the problem is to somehow find the boundary of all these points.
The main idea behind how to do that is to first identify a single point which 
is obviously going to be in the result set and then start finding points from 
that starting point. I have taken the approach to always find the most anticlockwise 
list of points from a particular point. Therefore we use the cross product to identify 
these set of points (because angle between those two vectors would be positive if the 
new vector is more anticlockwise than the last one).

Time complexity O(N*H), H means the number of nodes on the fence
Space complexity O(N), the worst case is all nodes are on the fence
"""


class Solution:
    @staticmethod
    def check_cross_product(a, b, o):
        ax = a[0] - o[0]
        ay = a[1] - o[1]
        bx = b[0] - o[0]
        by = b[1] - o[1]
        return ax*by - ay*bx
    
    @staticmethod
    def find_farthest_pt(pts, pt):
        far = None
        for val in pts:
            if not far:
                far = tuple(val)
            else:
                dist_new = (val[0] - pt[0]) ** 2 + (val[1] - pt[1]) ** 2
                dist_old = (far[0] - pt[0]) ** 2 + (far[1] - pt[1]) ** 2
                if dist_new > dist_old:
                    far = tuple(val)
        return far
    
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        
        ltm_pt = None
        for val in points:
            if not ltm_pt:
                ltm_pt = tuple(val)
            elif val[0] < ltm_pt[0]:
                ltm_pt = tuple(val)

        tree_dict = set()
        vis = {}
        curr_pt = ltm_pt
        while(curr_pt and curr_pt not in vis):
            tree_dict.add(curr_pt)
            found_pt = []
            for val in points:
                if tuple(val) != curr_pt:
                    if not found_pt:
                        found_pt.append(val)
                    else:
                        crp_prd = Solution.check_cross_product(found_pt[0], val, curr_pt)
                        if crp_prd > 0:
                            found_pt = []
                            found_pt.append(val)
                        elif not crp_prd:
                            found_pt.append(val)
            vis[curr_pt] = True
            farthest_pt = Solution.find_farthest_pt(found_pt, curr_pt)
            for val in found_pt:
                tup = tuple(val)
                tree_dict.add(tup)
            curr_pt = farthest_pt
        return tree_dict