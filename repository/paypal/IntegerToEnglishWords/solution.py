"""

1.

"""
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def one(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num)

        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)

        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num)

        # numbers will be in three segments for thousands
        def two(num):
            # if there is no num return empty string
            if not num:
                return ''
            # if num is less than 10
            elif num < 10:
                return one(num)
            # If number is less than 20
            elif num < 20:
                return two_less_20(num)
            # If the number is anything other than 10s and 20s
            else:
                # D
                tenner = num // 10
                rest = num - tenner * 10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

        # numbers will be in three segments for thousands
        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'

        # billion division
        billion = num // 1000000000
        # million division after billion division
        million = (num - billion * 1000000000) // 1000000
        # thousand division after billion and million division
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        # hundred division after billion and million and thousand division
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        # If the num is not there just return Zero
        if not num:
            return 'Zero'

        # Initialize result
        result = ''
        # If billion is found
        if billion:
            # result = because it will be three digits
            result = three(billion) + ' Billion'
        # If million is found
        if million:
            # add space
            result += ' ' if result else ''
            # result = because it will be three digits
            result += three(million) + ' Million'
        # If thousand is found
        if thousand:
            # add space
            result += ' ' if result else ''
            # result = because it will be three digits
            result += three(thousand) + ' Thousand'
        # For rest of it
        if rest:
            # add space
            result += ' ' if result else ''
            # result = because it will be three digits
            result += three(rest)
        return result
