"""

Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, 
so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), 
and "rats" and "arts" are similar, but "star" 
is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  
Notice that "tars" and "arts" are in the same group even though they are not similar.  
Formally, each group is such that a word is in the group if 
and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is 
an anagram of every other string in strs. How many groups are there?

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:

Input: strs = ["omv","ovm"]
Output: 1

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other

"""
class Solution:
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        group = 0 
        visited = set()
        for string_ in A:
            if(string_ in visited): continue
            visited.add(string_)
            self.dfs(string_,A,visited)
            group += 1
        return group

    def dfs(self,string_,A,visited):
        for i in range(len(A)):
            if(A[i] in visited): continue
            if(self.similar(A[i],string_)):
                visited.add(A[i])
                self.dfs(A[i],A,visited)

    def similar(self,A,B):
        diff = 0 
        for i in range(len(B)):
            if(A[i] != B[i]):
                diff+= 1
            if (diff > 2): return False
        return True
        