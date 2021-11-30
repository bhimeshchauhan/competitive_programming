class TrieNode:
    def __init__(self):
        self.children = dict()
        self.three = []                                    # three sentences


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, sentence, time):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            for i, (t, s) in enumerate(node.three):        # update three sentences
                if s == sentence:
                    tmp = node.three[:]
                    tmp[i][0] = time
                    break
            else:
                tmp = node.three + [[time, sentence]]
            node.three = sorted(tmp, key=lambda x: (-x[0], x[1]))[:3]


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # keep tracking {sentence: time}
        self.d = collections.Counter()
        self.trie = Trie()                                  # trie
        # pointer to root and move along with input characters
        self.node = self.trie.root
        for sentence, time in zip(sentences, times):        # add initial info
            self.d[sentence] += time
            self.trie.add(sentence, time)
        self.cur = ''                                       # prefix
        # True if prefix cannot be found
        self.prefix_none = False

    def input(self, c: str) -> List[str]:
        if c == '#':                                        # input ends
            self.node = self.trie.root                      # reset self.node to root
            # increment counter by 1
            self.d[self.cur] += 1
            # update sentence and time
            self.trie.add(self.cur, self.d[self.cur])
            self.cur = ''                                   # reset prefix string
            self.prefix_none = False                        # reset this flag
            return []                                       # return
        self.cur += c                                       # making prefix
        # when prefix is not found the first time and time after 1st time
        if c not in self.node.children or self.prefix_none:
            self.prefix_none = True                         # set flag
            return []
        self.prefix_none = False                            # reset prefix_none flag
        self.node = self.node.children[c]                   # move to next node
        return [word for _, word in self.node.three]        # return 3 words
