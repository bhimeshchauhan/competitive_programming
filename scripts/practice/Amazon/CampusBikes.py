"""

Campus Bikes

On a campus represented on the X-Y plane, there are 
n workers and m bikes, with n <= m.

You are given an array workers of length n where 
workers[i] = [xi, yi] is the position of the ith worker. 
You are also given an array bikes of length m where 
bikes[j] = [xj, yj] is the position of the jth bike. 
All the given positions are unique.

Assign a bike to each worker. Among the available bikes 
and workers, we choose the (workeri, bikej) pair with the 
shortest Manhattan distance between each other and assign 
the bike to that worker.

If there are multiple (workeri, bikej) pairs with the same 
shortest Manhattan distance, we choose the pair with the 
smallest worker index. If there are multiple ways to do that, 
we choose the pair with the smallest bike index. Repeat this 
process until there are no available workers.

Return an array answer of length n, where answer[i] is the 
index (0-indexed) of the bike that the ith worker is assigned to.

The Manhattan distance between two points p1 and p2 is 
Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Example 1:

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: Worker 1 grabs Bike 0 as they are closest (without ties), 
and Worker 0 is assigned Bike 1. So the output is [1, 0].

Example 2:

Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation: Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 
share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, 
and Worker 2 will take Bike 1. So the output is [0,2,1].

Constraints:

n == workers.length
m == bikes.length
1 <= n <= m <= 1000
workers[i].length == bikes[j].length == 2
0 <= xi, yi < 1000
0 <= xj, yj < 1000
All worker and bike locations are unique.

"""


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def dist(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])

        # the distance would never be over 2000 due to the problem criteria
        buckets = [[] for _ in range(2000)]

        # default answer array
        res = [-1] * len(workers)

        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = dist(worker, bike)
                # put the <worker, bike> pair into corresponding bucket
                # note here when we push the pair, the order is guranteed already
                buckets[distance].append([i, j])

        taken = set()
        for bucket in buckets:
            for w, b in bucket:
                # check worker does not have a bike and the bike is not taken
                if res[w] == -1 and b not in taken:
                    res[w] = b
                    taken.add(b)

        return res


"""

First step: claculate distances of all (worker, bike) pairs and make a dictionary using them. 
Distances are the keys in this dictionay. The dictionary will look like this:
distances = {dist_val1: [[w1,b1],[w2,b3]], dist_val2: [[w0,b1],[w1,b2]], ...}

Second, start from the minimum value in the dictionary and loop through the (worker, bike) pairs
for that distance, if the bike has not been assigned yet and the worker doesn't have a bike yet, 
assign the bike to that worker. Since we created this dictionary, going through workers and bikes 
in ascending order, we don't need to sort the list of each distance[k].

If n is the total number of pairs between workers and bikes, 
making the dictionary if of O(n). Also, worst case scenario, 
each entry in the dictionary belongs to one pair of worker 
and bike which makes filling ans to be of O(n) and the overall 
solution is of O(n).

"""


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        ans = [-1]*len(workers)
        distances = collections.defaultdict(list)
        set_bikes = set()

        for i in range(len(workers)):
            for j in range(len(bikes)):
                distances[abs(workers[i][0]-bikes[j][0]) +
                          abs(workers[i][1]-bikes[j][1])].append([i, j])

        for k in sorted(distances.keys()):
            for i in range(len(distances[k])):
                if ans[distances[k][i][0]] == -1 and distances[k][i][1] not in set_bikes:
                    ans[distances[k][i][0]] = distances[k][i][1]
                    set_bikes.add(distances[k][i][1])

        return ans
