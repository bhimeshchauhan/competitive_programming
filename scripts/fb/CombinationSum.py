
from collections import deque
from copy import deepcopy
class Solution:
    def isPresent(self, q, temp):
        lA = sorted(temp)
        for i in q:
            if sorted(i) == lA:
                return True
        return False
        
    def combinationSum(self, candidates, target):
        q = deque()
        for item in candidates:
            q.append([item])
        res = []
        while q:
            pop = q.popleft()
            temp = deepcopy(pop)
            if sum(temp) == target and not self.isPresent(res, temp):
                res.append(temp)
            for idx in range(len(candidates)):
                curr = candidates[idx]
                if sum(pop)+curr <= target:
                    temp = deepcopy(pop)
                    temp.append(curr)
                    q.append(temp)
        return res
        
        
        


if __name__ == "__main__":
    candidates = [1]
    target = 2
    print(Solution().combinationSum(candidates, target))