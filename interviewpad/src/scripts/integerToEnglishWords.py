"""
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"


Constraints:

0 <= num <= 2^31 - 1

"""


class Solution:
	def __init__(self):
		self.numberToString = {
			'1': 'one',
			'2': 'two',
			'3': 'three',
			'4': 'four',
			'5': 'five',
			'6': 'six',
			'7': 'seven',
			'8': 'eight',
			'9': 'nine',
			'10': 'ten',
			'11': 'eleven',
			'12': 'twelve',
			'13': 'thirteen',
			'14': 'fourteen',
			'15': 'fifteen',
			'16': 'sixteen',
			'17': 'seventeen',
			'18': 'eighteen',
			'19': 'nineteen',
			'20': 'twenty',
			'30': 'thirty',
			'40': 'forty',
			'50': 'fifty',
			'60': 'sixty',
			'70': 'seventy',
			'80': 'eighty',
			'90': 'ninty',
			'100': 'hundred',
			'1000': 'thousand',
			'1000000': 'million',
			'1000000000': 'billion'
		}
	
	def lessThanThousand(self, num):
		if num < 1000:
			strNum = str(num)
			if strNum in self.numberToString.keys():
				return self.numberToString[strNum]
			first = ''
			second = ''
			third = ''
			if len(strNum) == 3 and strNum[0] and strNum[0] != '0':
				first = f'{self.numberToString[strNum[0]]} {self.numberToString["100"]}'
				second = f'{self.numberToString[str(int(strNum[1]) * 10)]}'
				third = f'{self.numberToString[str(strNum[2])]}'
			if len(strNum) == 2:
				if strNum in self.numberToString.keys():
					second = f'{self.numberToString[str(int(strNum))]}'
				else:
					second = f'{self.numberToString[str(int(strNum[0]) * 10)]}'
					third = f'{self.numberToString[str(strNum[1])]}'
			if len(strNum) == 1 and strNum[2] and strNum[2] != '0':
				third = f'{self.numberToString[str(strNum[2])]}'
			print('first ', first)
			print('second ', second)
			print('third ', third)
			return f'{first} {second} {third}'
	
	def numberToWords(self, num: int) -> str:
		return self.lessThanThousand(num)


if __name__ == "__main__":
	# for i in range(1, 1000):
	# 	print(f'{i} ===> {Solution().numberToWords(i)}')
	print(f'{100} ===> {Solution().numberToWords(60)}')
