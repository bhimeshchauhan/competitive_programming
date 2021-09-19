"""

Minnimum number of strings to make a string plindrome

Given a string of size ‘n’. The task is to remove or delete the minimum number of 
characters from the string so that the resultant string is a palindrome. 

Note: The order of characters should be maintained. 

Examples : 

Input : aebcbda
Output : 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string

Input : geeksforgeeks
Output : 8


"""

# Python3 program for above approach

"""

- Take two indexes first as ‘i’ and last as a ‘j’
- now compare the character at the index ‘i’ and ‘j’
- if characters are equal, then 
    - recursively call the function by incrementing ‘i’ by ‘1’ and decrementing ‘j’ by ‘1’
- else 
    - recursively call the two functions, the first increment ‘i’ by ‘1’ keeping ‘j’ constant, 
    second decrement ‘j’ by ‘1’ keeping ‘i’ constant.
    - take a minimum of both and return by adding ‘1’

"""

# Utility function for calculating
# Minimum element to delete
def utility_fun_for_del(Str, i, j):
	
	if (i >= j):
		return 0

	# Condition to compare characters
	if (Str[i] == Str[j]):
		
		# Recursive function call
		return utility_fun_for_del(Str, i + 1,
										j - 1)

	# Return value, increamenting by 1
	# return minimum Element between two values
	return (1 + min(utility_fun_for_del(Str, i + 1, j),
					utility_fun_for_del(Str, i, j - 1)))

# Function to calculate the minimum
# Element required to delete for
# Making string pelindrom
def min_ele_del(Str):

	# Utility function call
	return utility_fun_for_del(Str, 0,
						len(Str) - 1)

# Driver code
Str = "abefbac"

print("Minimum element of deletions =",
	min_ele_del(Str))


# DP

"""

We will first define the DP table and initialize it with -1 throughout the table. Follow the below approach now,

- Define the function transformation to calculate the Minimum number of deletions and 
insertions to transform one string into another
- We write the condition for  base cases
- Checking the wanted condition
- If the condition is satisfied we increment the value and store the value in the table
- If the recursive call is being solved earlier than we directly utilize the value from the table
- Else store the max transformation from the subsequence
- We will continue the process till we reach the base condition
- Return the DP [-1][-1]

"""

# function definition
def transformation(s1,s2,i,j,dp):
	
	# base cases
	if i>=len(s1) or j>=len(s2):
		return 0
	
	# checking the ndesired condition
	if s1[i]==s2[j]:
		
		# if yes increment the cunt
		dp[i][j]=1+transformation(s1,s2,i+1,j+1,dp)
		
	# if no
	if dp[i][j]!=-1:
		
		#return the value form the table
		return dp[i][j]
	
	# else store the max tranforamtion
	# from the subsequence
	else:
		dp[i][j]=max(transformation(s1,s2,i,j+i,dp),
					transformation(s1,s2,i+1,j,dp))
		
	# return the dp [-1][-1]
	return dp[-1][-1]

					

s1 = "geeksforgeeks"
s2 = "geeks"
i=0
j=0

#initialize the array with -1
dp=[[-1 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
print("MINIMUM NUMBER OF DELETIONS: ",
	len(s1)-transformation(s1,s2,0,0,dp),
	end=" ")
print("MINIMUM NUMBER OF INSERTIONS: ",
	len(s2)-transformation(s1,s2,0,0,dp),
	end=" " )
print("LCS LENGTH: ",transformation(s1,s2,0,0,dp))

#code contributed by saikumar kudikala
