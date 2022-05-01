"""

Search Suggestions System

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

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

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 10^4
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.

"""


from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()

        def search(words, word):
            res = []
            for w in words:
                if w.startswith(word):
                    res.append(w)
            return res[:3]
        for i in range(1, len(searchWord)+1):
            result.append(search(products, searchWord[:i]))
        return result


if __name__ == "__main__":
    products = ["bags", "baggage", "banner", "box", "cloths"]
    searchWord = "bags"
    print(Solution().suggestedProducts(products, searchWord))


# TRIE

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.suggestions = list()


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()

        # sort the input lexicographically
        # before inserting them into the trie
        products.sort()

        # now, the usual trie insertion
        # pattern but for every word given to us
        for product in products:
            cur = root
            for letter in product:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]

                # once we've moved to the first letter
                # of the current word, add the current
                # word to it's suggestion list (at most 3)
                # and this list will be sorted since we've
                # done the sorting beforehand
                # now, for every letter for every word in the trie
                # it'll have an additional list with the 3 most
                # close suggestions
                if len(cur.suggestions) < 3:
                    cur.suggestions.append(product)

            cur.end = True

        # init the result object, the judge
        # needs this pattern if there are
        # no valid answers
        res = [[]] * len(searchWord)

        cur = root

        # iterate over all the letters
        # in the given searchWord and
        # gather the suggestions
        for i in range(len(searchWord)):
            if searchWord[i] not in cur.children:
                break

            # we're moving to the node before
            # getting the suggestions because
            # in the first iteration, this will
            # be the root node (we followed a similar
            # pattern while populating the trie too)
            cur = cur.children[searchWord[i]]
            res[i] = cur.suggestions

        return res
