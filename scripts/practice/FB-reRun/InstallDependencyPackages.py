from collections import *
class Node:
    def init(self):
        self.ind = 0
        self.children = []
class Solution:
    def findOrder(self, numCourses, prerequisites):

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []


print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))






def topological_sort(graph):
    output = []
    visited = {}
    for node, adjacencyList in graph.items():
        if node in visited:
            continue
        stack = [node]
        while len(stack) > 0:
            cur = stack[-1]
            neighbors = graph[cur]
            count = 0
            for neighbor in neighbors:
                if not neighbor in visited:
                    if neighbor in stack:
                        raise Exception("Found cycle")
                    stack.append(neighbor)
                    count += 1
            if count == 0:
                # Cannot move
                output.append(stack.pop(-1))
                visited[cur] = None

    return output
