"""

Search string with Trie using Wildcard

Search a string in TRIE DS where search string can have "." and "". For example: "aB.cZ"

"""

WILDCARD = '.'


class Trie:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

    def write(self):
        print(self.children)

    def insert(self, key):
        node = self
        for char in key:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.isLeaf = True

    def find(self, key):
        # stack of node, count of char, current word
        stack = [(self, 0, '')]
        result = []

        while stack:
            curr, count, currWord = stack.pop()

            if count == len(key):
                if curr.isLeaf:
                    result.append(currWord)
                continue

            currChar = key[count]
            if currChar == WILDCARD:
                for childChar, node in curr.children.items():
                    stack.append((node, count + 1, currWord + childChar))
                continue

            if currChar in curr.children:
                node = curr.children[currChar]
                stack.append((node, count + 1, currWord + currChar))

        return result


def main():
    trie = Trie()
    trie.insert('word')
    trie.insert('ward')
    trie.insert('oi')
    trie.insert('boi')
    
    assert(trie.find('..') == ['oi'])
    assert(trie.find('') == [])
    assert(trie.find('w.rd') == ['word', 'ward'])
    assert(trie.find('...') == ['boi'])
    assert(trie.find('.oi') == ['boi'])


if __name__ == '__main__':
    main()
