"""

PROBLEM : Given data about users, action and time of action, convert the given data in a table like format into a structure that can help identify customer dropoff.
You can use any data structure for input and output.

INPUT DATA
ID. TIME ACTION
100 1000 A
200 1000 A
100 1100 B
200 1150 B
200 1200 C
100 1200 A
300 1500 B
300 1600 B
400 1700 B

EXPECTED OUTPUT
A (2)
-> B (2)
-> C (1)
-> A (1)
B (2)
-> B (1)

"""


# assumed form of the elements of events
# (user: str, timestamp: int, behavior: str)
from random import shuffle


def createBehaviorGraph(events):
    # return value is a trie
    # structure of each node
    # trie[behavior: str] = [timesVisited: int, nextBehaviors: another map]
    ret = {}

    # sort events by timestamp
    events.sort(key=lambda event: event[1])

    # structure of current map
    # current[userId: str] = trie node
    # this represents where the current user is in our behavior trie
    current = {}

    for user, timestamp, behavior in events:
        if user not in current:
            current[user] = ret
        node = current[user]

        if behavior not in node:
            node[behavior] = [0, {}]
        node[behavior][0] += 1
        current[user] = node[behavior][1]

    return ret


# just for fun, this prints out a trie like it appears in the OP's post
# "node" is a trie node, "before" is an integer indicating how many dashes
# to put before we print out the behaviors at this node. this is essentially
# just a preorder traversal of our trie graph
def printGraph(node, before=0):
    beforeString = ('-' * before) + (' ' if before > 0 else '')
    for behavior in node:
        timesVisited, nextBehaviors = node[behavior]
        print("%s%s (%d)" % (beforeString, behavior, timesVisited))
        printGraph(nextBehaviors, before + 2)


sampleOpInput = [('1', 1, "Login"), ('2', 3, "Login"), ('3', 1, "Refresh"), ('4', 2, "Refresh"), ('1', 5, "Logout"),
                 ('2', 4, "Visit a page"), ('1', 10, "Close browser"), ('5', 696969, "Refresh"), ('9', 100, "Refresh")]
# put the input list in random order
shuffle(sampleOpInput)

printGraph(createBehaviorGraph(sampleOpInput))
