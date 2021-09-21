"""

Stickers to Spell Word

We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters 
from your collection of stickers and rearranging them. You can use each sticker 
more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. 
If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common 
US English words, and target was chosen as a concatenation of two random words.

 

Example 1:

Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

Example 2:

Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.

Constraints:

n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target <= 15
stickers[i] and target consist of lowercase English letters.

"""

# DFS

class Solution:
    def minStickers(self, stickers, target):
        cnt, res, n = collections.Counter(target), [float("inf")], len(target)  
        def dfs(dic, used, i):
            if i == n: res[0] = min(res[0], used)
            elif dic[target[i]] >= cnt[target[i]]: dfs(dic, used, i + 1)
            elif used < res[0] - 1:
                for sticker in stickers:
                    if target[i] in sticker:
                        for s in sticker: dic[s] += 1
                        dfs(dic, used + 1, i + 1)
                        for s in sticker: dic[s] -= 1
        dfs(collections.defaultdict(int), 0, 0)
        return res[0] < float("inf") and res[0] or -1
    

# BFS

class Solution(object):
    def minStickers(self, stickers, target):
        d = collections.Counter()
        cc = collections.Counter(target)
        res = [+float('inf')]
        stickers = [s for s in stickers if set(target).intersection(set(s))]
        
        target = list(target)
        self.dfs(d, 0, 0, stickers, res, target,cc)
        return res[0] if res[0] < float('inf') else -1
    
    
    """
    D = {hashmap of what I have knocked off, a subsequence in target}
    i = where I am in target
    n = number of used stickers
    stickers = ptr to stickers list
    res = [result] mutable collection to store the min
    target = list(target) to pass the reference/ptr to this list as opposed to copying a str over 
    cc = what is needed within target
    """
    def dfs(self,d,i,n, stickers,res, target, cc):
        
        if i == len(target):
            res[0] = min(res[0], n) 
            return
        
        if d[target[i]] >= cc[target[i]]:
            #all](https://leetcode.com/problems/substring-with-concatenation-of-all-words) good I have enough of target[i]
            self.dfs(d, i+1, n , stickers, res, target, cc)
            return
        if n + 1 < res[0]:
            for s in stickers:
                if target[i] in s:
                    for l in s: d[l] +=1
                    self.dfs(d, i+1, n + 1, stickers, res, target, cc)
                    for l in s: d[l] -=1