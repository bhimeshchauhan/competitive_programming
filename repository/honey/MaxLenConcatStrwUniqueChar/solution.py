from collections import defaultdict


class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # Create list of set(List)
        arr = [set(_) for _ in arr if len(set(_)) == len(_)]
        # Default Dict
        contra = defaultdict(list)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # If the set is not disjoint, we know the set has char in common
                if not arr[i].isdisjoint(arr[j]):
                    contra[i].append(j)
                    contra[j].append(i)
        used = {}

        def helper(val):
            if val in used:
                return used[val]
            ss = sum(val)
            if ss == 0:
                return 0
            fist_one = val.index(1)
            if ss == 1:
                return len(arr[fist_one])
            tmp = list(val)
            tmp[fist_one] = 0
            rm_max = helper(tuple(tmp))
            kp_max = len(arr[fist_one])
            for i in contra[fist_one]:
                tmp[i] = 0
            kp_max += helper(tuple(tmp))
            mm = max(kp_max, rm_max)
            used[val] = mm
            return mm

        return helper(tuple([1] * len(arr)))


assert Solution().maxLength(["un","iq","ue"]) is 4
assert Solution().maxLength(["cha","r","act","ers"]) is 6
assert Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]) is 26