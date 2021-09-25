"""

Search Suggestions System

Given an array of strings products and a string searchWord. We want to 
design a system that suggests at most three product names from products 
after each character of searchWord is typed. Suggested products should 
have common prefix with the searchWord. If there are more than three products 
with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.

"""

"""

Instead of traversing through all the possible characters, 
I made products list inside each node ( got my idea from https://leetcode.com/problems/map-sum-pairs/). 
For each character, you can return first three of the corresponding trie node. if traversing fail, rest 
of the highlights should be empty. so add empty list while length of ans list and searchWord are same 
to the answer

"""


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        self.root = {}

        node = self.root
        products.sort()
        ans = []
        # creating trie
        for product in products:
            for char in product:
                if char not in node:
                    node[char] = {'products': []}
                node = node[char]
                node['products'].append(product)

            node = self.root

        # traverse the trie
        for char_index in range(len(searchWord)):
            char = searchWord[char_index]
            if char in node:
                node = node[char]
                result = []
                # add top three or less product that needs to be in the highlight
                for product in node['products']:
                    result.append(product)
                    if len(result) == 3:
                        break
                ans.append(result)
            else:
                # if character was not in the current Trie node, break because there is match.
                break

        # rest of the highlights should be empty, because no matching characters are in the node.
        while len(ans) < len(searchWord):
            ans.append([])
        return ans

