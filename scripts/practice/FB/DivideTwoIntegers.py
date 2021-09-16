"""

Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 
32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that 
your function returns 231 − 1 when the division result overflows.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:

Input: dividend = 0, divisor = 1
Output: 0

Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0

"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        # Once the divisor is bigger than the current dividend,
        # we can't fit any more copies of the divisor into it anymore */
        while divisor >= dividend:
            # We know it'll fit at least once as divivend >= divisor.
            # Note: We use a negative powerOfTwo as it's possible we might have
            # the case divide(INT_MIN, -1). */
            powerOfTwo = -1
            value = divisor
            # Check if double the current value is too big. If not, continue doubling.
            # If it is too big, stop doubling and continue with the next step */
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value;
                powerOfTwo += powerOfTwo
            # We have been able to subtract divisor another powerOfTwo times.
            quotient += powerOfTwo
            # Remove value so far so that we can continue the process with remainder.
            dividend -= value

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != 1 else quotient