

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Solving this by using a 2d list of form [x,y]
        Here index of this list is the ith person
        x is the number of people this person trusts
        y is the number of people who trust this guy

        Once we create this list, then we will loop through it to find the judge
        The judge will be then person having [0, n-1] as it trusts no one and n-1 people trusts it
        """
        # special case
        if n == 1 and len(trust) == 0:
            return 1

        link = [[0, 0] for x in range(n+1)]  # create a emppty link array

        for x, y in trust:
            link[x][0] = link[x][0] + 1  # as this guy trusts one more person
            # as this guy is trusted by one more person
            link[y][1] = link[y][1] + 1

        judge = -1
        for x in range(n+1):
            if link[x][0] == 0 and link[x][1] == n-1:  # condition for a judge
                judge = x
                break
        return judge


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # if trust list is empty and there is only 1 person, return 1 (since that must be the judge)
        if len(trust) == 0 and n == 1:
            return 1

        # if trust list is empty and there is more than 1 person, return -1 (no way to tell which one is the judge)
        if len(trust) == 0 and n > 1:
            return -1

        # if len(trust) is less than n-1, means not everybody trust some else, return -1
        if len(trust) < n - 1:
            return -1

        # if len(trust) = 1 and n = 2, return trust[0][1]
        if len(trust) == 1 and n == 2:
            return trust[0][1]

        # sort trust with lambda function, first by x[1] then by x[0]
        sortt = sorted(trust, key=lambda x: (x[1], x[0]))

        # set countn = 1, maxcount = 1, and jn = 0 (jn is the index of the judge, initially set at 0)
        countn = 1
        maxcount = 1
        jn = 0
        # iterate through trust, if sortt[i][1] = sortt[i+1][1], increase countn by 1, if maxcount < countn, set maxcount = countn and jn = sortt[i][1]
        for i in range(len(trust)-1):
            if sortt[i][1] == sortt[i+1][1]:
                countn += 1
                if maxcount < countn:
                    maxcount = countn
                    jn = sortt[i][1]
            else:       # else, set countn back to 1
                countn = 1

        if jn == 0:  # if jn = 0, return -1
            return -1

        # iterate through trust, if maxcount = n-1 and jn = trust[i][0], means even though every body trust someone, that someone trust somebody else, so there is no judge (return -1)
        for i in range(len(trust)):
            if maxcount == n-1 and jn == trust[i][0]:
                return -1

        if maxcount == n-1:     # if maxcount == n-1, return judgenumber jn, else, return -1
            return jn
        else:
            return -1
