import collections
class Solution:
    def isAnagram(self, s, t):
        if len(s) == len(t):
            s_dict = collections.Counter(s)
            t_dict = collections.Counter(t)
            if s_dict.keys() == t_dict.keys():
                for key in s_dict:
                    if s_dict[key] != t_dict[key]:
                        return False
                return True
        else:
            return False

assert Solution().isAnagram("anagram", "nagaram")
assert not Solution().isAnagram("rat", "car")