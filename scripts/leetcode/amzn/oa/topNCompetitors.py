"""

Input

The input to the function/method consists of five arguments - numCompetitors, an integer representing the number of 
competitors for the Echo device;
topNCompetitors, is an integer representing the maximum number of 
competitors that Amazon wants to identify;
competitors, a list of strings representing the competitors;
numReviews, an integer representing the number of reviews from 
different websites that are identified by the automated webcrawler;
reviews, a list of string where each element is a string that consists 
of space-separated words representing user reviews.

Output
Return a list of strings representing Amazon's top N competitors in order of most frequently mentioned to least frequent.

Note
The comparison of strings is case-insensitive. If the value of topNCompetitors is more than the number of competitors discussed in the reviews then output the names of only the competitors mention.
If competitors have the same count (e.g. newsh'op=2, shopnow=2, mymarket=4), sort alphabetically. topNCompetitors=2, Output=[mymarket, newsh'op]

Example
Input:
numCompetitors=6
topNCompetitors = 2
competitors = [newsh'op, shopnow, afashion, fashionbeats, mymarket, tcellular]
numReviews = 6
reviews = [
"newsh'op is providing good services in the city; everyone should use newsh'op",
"best services by newsh'op",
"fashionbeats has great services in the city",
"I am proud to have fashionbeats",
"mymarket has awesome services",
"Thanks newsh'op for the quick delivery"]

Output
["newsh'op", "fashionbeats"]

Explanation
"newsh'op" is occurring in 3 different reviews. "fashionbeats" is occuring in 2 different user reviews and "mymarket" is occurring in only 1 review.


"""

# N: top N competitors
# C: # of competitors 
# R: # of reviews
# W: avg # of words in a review
# Time complexity: O(C + R * (W + N))
# Space complexity: O(C + N)

# import heapq


# class HeapNode:

#     def __init__(self, competitor):
#         self.competitor = competitor
#         self.count = 0

#     def __gt__(self, other):
#         if self.count != other.count:
#             return self.count > other.count
#         else:
#             return self.competitor > other.competitor

# def topNumCompetitors(numCompetittors, topNCompetitors, competitors, numReveiws, reviews):
#     hashTable = {} # Space O(C)
#     for competitor in competitors: # Time O(C)
#         hashTable[competitor] = HeapNode(competitor)
#     # Min heap and will always kick out the competitor who has the most less freq count
#     heap, heapHash = [], {} # Space O(N)
#     for review in reviews: # Time O(R)
#         words = review.split()
#         for word in words: # Time O(W)
#             if word.lower() in hashTable:
#                 # Found competitor
#                 break
#         competitor = word.lower()
#         if competitor in heapHash:
#             heapNode = heapHash[competitor]
#             heapNode.count += 1
#             heapq.heapify(heap) # Time O(N)
#         else:
#             heapNode = hashTable[competitor]
#             heapNode.count += 1
#             heapq.heappush(heap, heapNode) # Time O(logN)
#         heapHash[competitor] = heapNode
#         if len(heap) > topNCompetitors:
#             victim = heapq.heappop(heap)
#             del heapHash[victim.competitor]
#     return [heapNode.competitor for heapNode in heapHash.values()]

# if __name__ == '__main__':
#     print(topNumCompetitors(6, 2, ['newsh'op', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular'], 6,  [
# "newsh'op is providing good services in the city; everyone should use newsh'op",
# "best services by newsh'op",
# "fashionbeats has great services in the city",
# "I am proud to have fashionbeats",
# "mymarket has awesome services",
# "Thanks newsh'op for the quick delivery"])) # Output ['newsh'op', 'fashionbeats']
    
    
def topcompetitors(numComp, topComp, comps, numReviews, reviews):
    comps.sort()
    d = {}
    output = []
    for i in comps:
        d[i] = 0

    for review in reviews:
        review = review.split()
        for word in review:
            if word in d:
                d[word] += 1
                break

    for _ in range(topComp):
        maxval = 0
        maxkey = ''
        for key, val in d.items():
            if val > maxval:
                maxval = val
                maxkey = key
        output.append(maxkey)
        del d[maxkey]
    return output


numComp = 6
topComp = 2
comps = ['newsh\'op', 'shopnow', 'afashion', 'fashionbeats', 'mymarket', 'tcellular']
numReviews = 6
reviews = [
    "newsh'op is providing good services in the city; everyone should use newsh'op",
    "best services by newsh'op",
    "fashionbeats has great services in the city",
    "I am proud to have fashionbeats",
    "newsh'op has awesome services",
    "Thanks newsh'op for the quick delivery"]

print(topcompetitors(numComp, topComp, comps, numReviews, reviews))



    
    