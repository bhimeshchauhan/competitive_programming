"""

enQueue(q, x):

While stack1 is not empty, push everything from stack1 to stack2.
Push x to stack1 (assuming size of stacks is unlimited).
Push everything back to stack1.
Here time complexity will be O(n)

deQueue(q): 

If stack1 is empty then error
Pop an item from stack1 and return it
Here time complexity will be O(1)

"""

# Python3 program to implement Queue using
# two stacks with costly enQueue()

class Queue:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enQueue(self, x):
		
		# Move all elements from s1 to s2
		while len(self.s1) != 0:
			self.s2.append(self.s1[-1])
			self.s1.pop()

		# Push item into self.s1
		self.s1.append(x)

		# Push everything back to s1
		while len(self.s2) != 0:
			self.s1.append(self.s2[-1])
			self.s2.pop()

	# Dequeue an item from the queue
	def deQueue(self):
		
			# if first stack is empty
		if len(self.s1) == 0:
			print("Q is Empty")
	
		# Return top of self.s1
		x = self.s1[-1]
		self.s1.pop()
		return x

# Driver code
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())

# This code is contributed by PranchalK

"""

Complexity Analysis: 

Time Complexity: 
Push operation: O(N). 
In the worst case we have empty whole of stack 1 into stack 2.
Pop operation: O(1). 
Same as pop operation in stack.
Auxiliary Space: O(N). 
Use of stack for storing values.

"""

# Method 2 (By making deQueue operation costly)

"""

enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).
Here time complexity will be O(1)

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from stack1 to stack2.
  3) Pop the element from stack2 and return it.
Here time complexity will be O(n)

"""

# Python3 program to implement Queue using
# two stacks with costly deQueue()

class Queue:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	# EnQueue item to the queue
	def enQueue(self, x):
		self.s1.append(x)

	# DeQueue item from the queue
	def deQueue(self):

		# if both the stacks are empty
		if len(self.s1) == 0 and len(self.s2) == 0:
			print("Q is Empty")
			return

		# if s2 is empty and s1 has elements
		elif len(self.s2) == 0 and len(self.s1) > 0:
			while len(self.s1):
				temp = self.s1.pop()
				self.s2.append(temp)
			return self.s2.pop()

		else:
			return self.s2.pop()

	# Driver code
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())

# This code is contributed by Pratyush Kumar


"""

Complexity Analysis: 

Time Complexity: 
Push operation: O(1). 
Same as pop operation in stack.
Pop operation: O(N). 
In the worst case we have empty whole of stack 1 into stack 2
Auxiliary Space: O(N). 
Use of stack for storing values. 

"""

# Queue can also be implemented using one user stack and one Function Call Stack.

"""

enQueue(x)
  1) Push x to stack1.

deQueue:
  1) If stack1 is empty then error.
  2) If stack1 has only one element then return it.
  3) Recursively pop everything from the stack1, store the popped item 
    in a variable res,  push the res back to stack1 and return res

"""

# Python3 program to implement Queue using
# one stack and recursive call stack.
class Queue:
	def __init__(self):
		self.s = []
		
	# Enqueue an item to the queue
	def enQueue(self, data):
		self.s.append(data)
		
	# Dequeue an item from the queue
	def deQueue(self):
		# Return if queue is empty
		if len(self.s) <= 0:
			print('Queue is empty')
			return
		
		# pop an item from the stack
		x = self.s[len(self.s) - 1]
		self.s.pop()
		
		# if stack become empty
		# return the popped item
		if len(self.s) <= 0:
			return x
			
		# recursive call
		item = self.deQueue()
		
		# push popped item back to
		# the stack
		self.s.append(x)
		
		# return the result of
		# deQueue() call
		return item
	
# Driver code
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)
	
	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())
	
# This code is contributed by iArman


"""

Time Complexity: 
Push operation : O(1). 
Same as pop operation in stack.
Pop operation : O(N). 
The difference from above method is that in this method element is returned 
and all elements are restored back in a single call.
Auxiliary Space: O(N). 
Use of stack for storing values.

"""