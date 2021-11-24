"""

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, 
with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]

"""

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words, k):
        table = {}
        for word in words:
            if word in table:
                table[word] += 1
            else:
                table[word] = 1
        # set up a max heap
        heap = []
        heapq.heapify(heap)
        for key in table:
            heapq.heappush(heap, (-table[key], key))
        # pop top k
        res = []
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append(popped)
        # sort res alphabetically
        res.sort()
        newres = []
        for word in res:
            newres.append(word[1])
        return newres
