"""

Design AutoComplete System

Design a search autocomplete system for a search engine. Users may input a sentence 
(at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n 
where sentences[i] is a previously typed sentence and times[i] is the corresponding 
number of times the sentence was typed. For each input character except '#', return 
the top 3 historical hot sentences that have the same prefix as the part of the 
sentence already typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the 
exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). 
If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, 
you need to return an empty list.

Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object 
with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c.
Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
Returns the top 3 historical hot sentences that have the same prefix as the part of 
the sentence already typed. If there are fewer than 3 matches, return them all.

Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search. 

Constraints:

n == sentences.length
n == times.length
1 <= n <= 100
1 <= sentences[i].length <= 100
1 <= times[i] <= 50
c is a lowercase English letter, a hash '#', or space ' '.
Each tested sentence will be a sequence of characters c that end with the character '#'.
Each tested sentence will have a length in the range [1, 200].
The words in each input sentence are separated by single spaces.
At most 5000 calls will be made to input.

"""


"""

Explanation

- We first build a trie for the given sentences and times. 
Note that we negate hot so that we can easily return the Top 3 
hot sentences after sorting them in ascending order.
- We initialize the following three variables to keep track of search state. 
They will be reset when the user types #:
    - search_term is used to track the current input.
    - last_node stores the previous node when we search in trie. 
    It ensures that we do not always start searching from trie 
    root when there are sentences that match the current input.
    - no_match is a flag. It ensures that we skip searching once 
    there are no sentences that match the current input. The user 
    can still type and we will record the input in search_term.
- We only perform searching if the latest input character is in last_node's children.

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_sentence = False
        self.hot = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence, hot):
        node = self.root
        for char in sentence:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_sentence = True
        node.hot -= hot


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.build_trie(sentences, times)
        self.reset_search()

    def build_trie(self, sentences, times):
        self.trie = Trie()
        for i, sentence in enumerate(sentences):
            self.trie.insert(sentence, times[i])

    def reset_search(self):
        self.search_term = ""
        self.last_node = self.trie.root
        self.no_match = False

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.search_term, 1)
            self.reset_search()
        else:
            self.search_term += c

            if not c in self.last_node.children or self.no_match:
                self.no_match = True
                return []

            self.last_node = self.last_node.children[c]
            result = []
            self.dfs(self.last_node, self.search_term, result)

            return [sentences[1] for sentences in sorted(result)[:3]]

    def dfs(self, node, path, result):
        if node.is_sentence:
            result.append((node.hot, path))

        for char in node.children:
            self.dfs(node.children[char], path+char, result)
