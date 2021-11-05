"""

Path For user Browsing

Input: log of events 2d array on a webpage (no guarantee of any sorting) 
format [id, timestamp, action]
e.g. ['100', '50', 'login'] is a row in list

Build/print a graph that represents the paths all users took in their browsing
As well as the times each "node" was visited
Example

(not an exact example just an idea) 

Login (2)
-- Logout (1)
----- Closed Browser (2)
-- Visit A Page (1)
Refesh (4)
-- action (num_visitors_who_did_this)
---- sub action (x)
-- action2(x)

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
