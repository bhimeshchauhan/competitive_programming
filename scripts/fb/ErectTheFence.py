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
Time complexity O(N*H), H means the number of nodes on the fence
Space complexity O(N), the worst case is all nodes are on the fence
"""
class Solution(object):
    def outerTrees(self, points):
        #start with the leftmost point on the map
        leftmost = [float('inf'), float('inf')]
        for x,y in points:
            if x < leftmost[0]:
                leftmost = [x,y]
        #set this leftmost point as a starter
        current = leftmost
        
        res = set()
        res.add((leftmost[0],leftmost[1]))
        while True:
            target = points[0]
            linenodes = []
            for node in points:
                if node != current:
                    val = self.crossproduct(current,target,node)
                    if val > 0: #node is on the left of target
                        target = node 
                        linenodes = []
                    elif val == 0: #node is inline with the target
                        if ((node[0]-current[0])**2+((node[1]-current[1])**2)) < ((target[0]-current[0])**2+((target[1]-current[1])**2)):
                            linenodes.append(node) 
                        else:
                            linenodes.append(target)
                            target = node
                    else: #node is on the right of target, we don't care
                        continue 
            for linenode in linenodes:
                res.add((linenode[0],linenode[1]))
            if target == leftmost: #we encounter the start point, let's break 
                break
            res.add((target[0],target[1]))

            current = target
        return [[x,y] for x,y in res]
    
    def crossproduct(self,origin, target, node):
        x1 = origin[0] - target[0]
        y1 = origin[1] - target[1]
        x2 = origin[0] - node[0]
        y2 = origin[1] - node[1]
        return y2*x1 - y1*x2
    
    
    