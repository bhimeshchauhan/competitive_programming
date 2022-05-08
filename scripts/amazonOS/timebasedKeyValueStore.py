"""

Time Based Key-Value Store

https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

"""


from collections import defaultdict


class TimeMap:

    def __init__(self):
        # Declare Default Dictionary because we want to append [values,timestamp] to the key
        self.d = defaultdict(list)
        """
        Initialize your data structure here.
        """

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the value to the key with the timestamp
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Store the value of key in a variable
        temp = self.d[key]

        # Edgecase 1
        if not temp:
            return ""

        # Edgecase2
        if timestamp > temp[-1][1]:
            return temp[-1][0]

        # Egdecase3
        if timestamp < temp[0][1]:
            return ""

        # We will have an array with timestamp values and we have to find a particular timestamp value or smaller than it
        # We will use binary search O(logN) time
        l = 0
        r = len(temp)-1
        while l <= r:
            mid = (l+r)//2
            if temp[mid][1] > timestamp:
                r = mid-1
            else:
                l = mid + 1

        # Return the matching value
        if l < len(temp)-1:
            return temp[l][0]
        else:
            return temp[r][0]
