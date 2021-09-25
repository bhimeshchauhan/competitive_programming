"""

Validate IP Address

Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid 
IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 
and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" 
are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" 
are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, 
lower-case English letter ('a' to 'f') and 
upper-case English letters ('A' to 'F').

Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 
and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, 
while "2001:0db8:85a3::8A2E:037j:7334" and 
"02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

Example 1:

Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:

Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.

Example 4:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
Output: "Neither"

Example 5:

Input: IP = "1e1.4.5.6"
Output: "Neither"

Constraints:

IP consists only of English letters, digits and the characters '.' and ':'.

"""
class Solution:
    def validIPAddress(self, IP: str) -> str:
            if self.isIPv4(IP):
                return "IPv4"
            elif self.isIPv6(IP):
                return "IPv6"
            else:
                return "Neither"

    def isIPv4(self, IP) -> bool:
        arr = IP.split('.')
        # Must contain 4 groups
        if len(arr) != 4:
            return False
        for val in arr:
            # 01 is not valid
            if len(val) > 1 and val[0] == '0':
                return False
            # Range 0 to 255
            if val.isdigit() and int(val) <= 255:
                continue
            else:
                return False
        return True

    def isIPv6(self, IP) -> bool:
        arr = IP.split(':')
        # Must contain 8 groups
        if len(arr) != 8:
            return False
        for val in arr:
            # 0(a8::07) or greater than 4 letters (2001c) are not valid.
            if len(val) > 4 or len(val) == 0:
                return False
            elif self.isValidHexa(val):
                continue
            else:
                return False
        return True

    def isValidHexa(self, val) -> bool:
        # All numbers are valid (9999, 0008, 1 are all valid)
        if val.isdigit():
            return True
        for char in val:
            # 0-9 valid
            if char.isdigit():
                continue
            # a-f valid
            elif ord(char) >= ord('a') and ord(char) <= ord('f'):
                continue
            # A-F valid
            elif ord(char) >= ord('A') and ord(char) <= ord('F'):
                continue
            else:
                return False
        return True