"""

Count the number of words with given prefix using Trie

"""


class TreeNode:
    def __init__(self):
        #  Indicates end of string
        self.last = False
        self.children = [None] * (26)


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, text):
        #  First get the length of text
        length = len(text)
        #  This variable are used to task find the index location of character
        index = 0
        #  Get the root node
        head = self.root
        level = 0
        while (level < length):
            #  Get the index
            index = ord(text[level]) - ord('a')
            if (head.children[index] == None):
                #  When need to add new Node
                head.children[index] = TreeNode()

            #  Visit to child node
            head = head.children[index]
            level += 1

        if (head != None):
            #  Indicates end of string
            head.last = True

    def words(self, head):
        counter = 0
        if (head != None):
            if (head.last == True):
                counter += 1

            i = 0
            while (i < 26):
                if (head.children[i] != None):
                    #  Count word
                    counter += self.words(head.children[i])

                i += 1

        return counter

    def wordsByPrefix(self, prefix):
        head = self.root
        if (head != None):
            #  Display given prefix
            print(" Prefix : ", prefix)
            #  Get the length of prefix
            n = len(prefix)
            level = 0
            index = 0
            print(" Result :  ", end="")
            #  Check that prefix exists in a trie tree
            while (level < n):
                index = ord(prefix[level]) - ord('a')
                if (head.children[index] != None):
                    #  Visit to child node
                    head = head.children[index]
                else:
                    #  When prefix not exist
                    print(0)
                    return

                level += 1

            if (level == n):
                if (head == None):
                    print(1)
                else:
                    print(self.words(head))


def main():
    #  Make tree
    task = Trie()
    #  Tree Words
    task.insert("pincode")
    task.insert("ipcode")
    task.insert("pineapple")
    task.insert("pink")
    task.insert("pinch")
    task.insert("pinball")
    #  Test A
    #  Prefix : "pin"
    #  pin->["pincode","pineapple","pink","pinch","pinball"]
    #  Result : 5
    task.wordsByPrefix("pin")
    #  Test B
    #  Prefix : "pinc"
    #  pin->["pincode","pinch"]
    #  Result : 2
    task.wordsByPrefix("pinc")
    task.wordsByPrefix("app")


if __name__ == "__main__":
    main()
