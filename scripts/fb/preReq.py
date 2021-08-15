# DFS detect cyclic graph

def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


# BFS detect cyclic graph

"""
N =6
p = [[2,1],[4,1],[3,2],[5,4]]

0
     1
   /   \
  2     4 
 /       \
3         5

todo = {0: set(), 1: set(), 2: {1}, 3: {2}, 4: {1}, 5: {4}}
graph =  {1: {2, 4}, 2: {3}, 4: {5}})
todo = {0: set(), 1: set(), 2: {1}, 3: {2}, 4: {1}, 5: {4}}
node 0
todo = {1: set(), 2: {1}, 3: {2}, 4: {1}, 5: {4}}
node 1
todo = {2: set(), 3: {2}, 4: set(), 5: {4}}
node 2
todo = {3: set(), 4: set(), 5: {4}}
node 4
todo = {3: set(), 5: set()}
node 3
todo = {5: set()}
node 5
todo= {}
N =6
p = [[2,1],[4,1],[3,2],[5,4],[2,3]]

0
     1
   /   \
  2     4 
 //       \
3         5

# initial 
todo = {0: set(), 1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
graph =  {1: {2, 4}, 2: {3}, 4: {5}, 3: {2}})

# processing
todo = {0: set(), 1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
node 0
todo = {1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
node 1
todo = {2: {3}, 3: {2}, 4: set(), 5: {4}}
node 4
todo ={2: {3}, 3: {2}, 5: set()}
node 5
todo ={2: {3}, 3: {2}}

# No nodes' indegree equals 0, so nothing will be append to the queue.
# Queue becomes empty, the while loop stop. If the indegree_item has items,it means it has cycle.
"""
from collections import deque
from collections import defaultdict
class Solution:
    """
    
N =6
p = [[2,1],[4,1],[3,2],[5,4]]

     1     0
   /   \
  2     4 
 /       \
3         5
   
 
    
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        todo = {i: set() for i in range(numCourses)} 
        graph = defaultdict(set)
        for i,j in prerequisites:
            todo[i].add(j)
            graph[j].add(i)
        q = deque([])
        for k,v in todo.items():
            if len(v) == 0:
                q.append(k)
        while q:
            n = q.popleft()
            for i in graph[n]:
                todo[i].remove(n)
                if len(todo[i]) == 0:
                    q.append(i)
            todo.pop(n)
        return not todo