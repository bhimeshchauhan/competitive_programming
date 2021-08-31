"""

Given list of transactions, return a list of users who were involved in transaction more then equal to the threshold number of times. Return list of user names in sorted order of thier names.
Transactions -> (User1, User2, Amount)
Eg. Transactions - [[88, 90, 100], [90, 88, 200], [90, 1, 60]], Threshold = 2
Return = [88, 90] Since number of transactions involving 88 -2, involving 90-3 involving 1 -1.

"""

class Solution():
    def userTransactions(self, transactions: List[List[int]], threshold: int) -> List[int]:
        u = {}
        o = set()
        for t in transactions:
            t1, t2 = t[0], t[1]
            u[t1], u[t2] = (1 if t1 not in u else u[t1] + 1), (1 if t2 not in u else u[t2] + 1)

            if u[t1] >= threshold:
                o.add(t1)
            if u[t2] >= threshold:
                o.add(t2)
        
        return list(o)
    


def solution(transactions, threshold):
    d = {}
    for u1, u2, amount in transactions:
        d[u1] = d.get(u1, 0) + 1
        d[u2] = d.get(u2, 0) + 1
    return sorted([key for key in d.keys() if d[key] >= threshold])