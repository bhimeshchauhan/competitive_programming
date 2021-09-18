"""

Count All Valid Pickup and Delivery Options

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:

Input: n = 3
Output: 90

Constraints:

1 <= n <= 500

"""
"""
Given n orders, each order consist in pickup and delivery services, so we have altogether 2n 
slots to fit in all the pickups and deliverys. Since delivery(i) is always after of pickup(i) 
for all i, we can deduce that:

- The first slot must be a pickup, and there are 2n-1 possible slots for its delivery.
- If the first delivery is at the second slot, then the third slot must be a pickup; if the first 
delivery is after the second slot, then the second slot must be a pickup. Either way, the second 
delivery can be put in any of the remaining 2n-3 empty slot.
- By induction, we can find that there are Sn = (2n-1) * (2n-3) * ... * 3 * 1 different arrangements 
of pickup and delivery pairs.
- And for every arrangement, there are n! permutations, so the final result is (n! * Sn) % 1000000007.
"""

def countOrders(self, n: int) -> int:
    a = 1
    for i in range(2, n+1):
        a *= i*(2*i-1)
    return a % (10**9 + 7)