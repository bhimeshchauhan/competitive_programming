- Number of Islands
- Level Order (and Zigzag) Tree Traversal
- Word Series (Word Ladder 1 & 2, Word Break 1 & 2, Word Search 1 & 2).
- "parking lot" OOD question
- Bloomberg | Software Engineering Intern | London | January 2020 [Offer] - LeetCode Discuss
- Amazon Dublin Ireland | Onsite - SDE New Grad 2021 | Income Calculator - LeetCode Discuss
- What are Design patterns? example and explanation? https://leetcode.com/discuss/interview-experience/1060893/amazon-sde-new-grad-2021-dublin-experience-offer
- Round2 Onsite: This was a class design. In the beginning, there were 2 LP questions then he asked how a hash table is implemented as a starter and then asked to design a file system and implement search on the filesystem based on certain parameters (like file size creation date etc) https://leetcode.com/discuss/interview-question/609070/Amazon-OOD-Design-Unix-File-Search-API Round 3: Bar raiser Basically asked LP questions and asked to Design a task scheduler (in memory) and then implement a function that finds the time a certain task takes to complete (given that there exist tasks that have to be executed before it ) Round 4: Simple Number of islands question along with LP questions
- 1 OOP questions variant of UNIX command, Game of Life Question and Iterator Question.
- Remove all duplicate numbers from a list.
- Amazon Dublin Ireland | Onsite - SDE New Grad 2021 | Income Calculator We want to implement an income calculator that,given a compensation package and start date,returns the income per year until the present. The input is:

Start date (SimpleDate)
Base salary per year(int)
RSU per year (int)
Sign on bonus, only once (int)

SimpleDate is my own implementation of Date. It has these fields:

SimpleDate:
  month: int
  year: int

You can also use SimpleDate.now() to get the current date. Example: Given these values Base salary: 120,000 RSU: 60,000 Sign on: 25,000 Start date: 02/2018 Current date 02/2020 The calculator should return: 2018: 190,000 (11 months income, including February plus sign on) 2019: 180,000 (12 months income) 2020: 15,000 (only January, excluding February) My Proposed Solution -


def income_calculator(start_date, base_salary, rsu, sign_on):

    current_date = SimpleDate.now()

    start = start_date.year

    mp = {}

    salary_p_month  = base_salary//12
    rsu_p_month = rsu//12

    if start == current_date.year:
        n_month = current_date.month - start_date.month
        fisrt_income = salary_p_month*n_month + rsu_p_month*n_month + sign_on
        mp[start] = first_income
        return mp
    else:
        n_month = 12 - start_date.month + 1
    fisrt_income = salary_p_month*n_month + rsu_p_month*n_month + sign_on
    mp[start] = first_income

    start += 1

    while current_date.year != start:
        income = 12*(salary_p_month + rsu_p_month)
        mp[start] = income
        start += 1

    income = (current_date.month - 1)*(salary_p_month + rsu_p_month)
    mp[start] = income

    return mp

https://leetcode.com/problems/min-stack/ However, it came with the constraint that we would be needing extra O(n) space. I was also asked to implement exception handling to deal with situations when you call pop() or getMin() on an empty stack.

First round: 2-3 behavioral questions followed by a coding question. The question was given a binary tree find a subtree within the binary tree that adds up to a certain target sum.

Second round: 2-3 behavoral questions followed by an OOD question. The question was a bit vague and I had a hard time understanding their english but essentially it was to design a wharehouse class that had certain constraints such that the particular wharehouse could only store certain products.

Fourth round: 2-3 behavioral questions. This was another coding round, which involved taking a string that say said "This sweater cost $40 dollars." The objective was to take that number and apply a 20% discount and return the string back with the updated price, i.e., "This sweater cost $32 dollars.".

This round was interesting since it was not any of the Leetcode questions. I was given certain conditions for a valid transaction and I had to write a function that will determine if the transaction is valid or not. The goal of this round was to see how I can write a maintainable and scalable code. For example, how can we add more conditions for a valid transaction and still not alter the main function very much. I had LP questions as part of this round also.

Find the count of a given sequence that appears in an array. There can be any amount of characters between the numbers of the sequence. ex 4,5,6,2 would have a count of 1. sequence 4,6,2 array [ 3, 4, 4, 6, 7, 8 , 2, 6, 9, 2] count of sequences: 6 https://leetcode.com/discuss/interview-question/437362/amazon-sde-count-of-sequences-within-an-array

2 LP´s and Medium exercise on Trie Structure (make sure you know how to use a Trie, the Explore section here has a really good card on it). Really similar to an Amazon tagged exercise.

2 LP´s, then started with an extremely simple exercise, and afterwards, the interviewer started adding complexity, to see how I adapted my solution so that it scaled. The interviewer was testing my knowledge on Object Oriented Design, which I use in my everyday work, but had not prepared for the interview. This was almost a disaster, my solution was far from good.

Course Schedule II -

Given huge database of sentences, write a class to find most frequently used words

Questions on data structures like array list, linked list, hash table, binary search tree. Differences between these data structures and when would you use which one. Inheritance and Composition.

Coding: Design a Tic Tac Toe Game

Given a graph and destination D, find shortest path between all nodes. Not given any graph implementation, and input is a list of edges ([1,2,3] = Node 1 to Node 2, distance 3). Had to implement my own adjacency list and "nodes" (Dijkstra's Algorithm)

Similar to this question, but exclude the combined word (ex. instead of [['car','super', 'supercar'], the answer is [['car','super'],)https://leetcode.com/discuss/interview-question/314550/amazon-onsite-interview-concatenated-words

https://leetcode.com/problems/copy-list-with-random-pointer/

https://leetcode.com/problems/longest-happy-prefix/

https://leetcode.com/problems/insert-interval/

Design a system to generate and apply coupons for e-commerce site based on product and its category.

https://leetcode.com/problems/lfu-cache/

Find the next value from the target node using BST

https://leetcode.com/problems/string-to-integer-atoi/

Longest common prefix among an array of strings - but the longest between any two (instead of the longest in all)

https://leetcode.com/problems/boundary-of-binary-tree/

https://leetcode.com/problems/integer-to-roman/

K most frequent items(item_id) in a stream. Input is a stream of (item_id,timestamp). This I was able to easily solve using hashmap and min-heap Then, Interviewer asked me to find frequent items in last hour given a timestamp. For example, Given time 6:07 PM, Return k most frequent items from 5:07 PM to 6:07 PM. Gave an answer using queue, hashmap and min-heap, Not an optimal answer, But it worked.

Three sum

Round 1 - 2 interviewers https://leetcode.com/discuss/interview-experience/1060893/Amazon-SDE-new-grad-2021-Dublin-Experience-or-Offer/854173

Implement queue using stack

Find loop in single linkedlist

find missing element in an array

Explain any sorting algorithm

Time and space complexity for the above problems

Difference similarity between list, linkedlist and array

Implementation of Hashmap

Difference between set, hashmap, list

Round 2 - 1 inerviewer

2 LP questions

What are Design patterns? example and explanation?

Best coding practices

https://leetcode.com/problems/integer-to-english-words/

Time complexity for the above problem

Round 3 - 1 interviewer

Print matrix spirally. Time and space complexity for the above problem

Given a prefect binary tree, print middle nodes of it without knowing the height of the tree. Sample Input:

			1
		  /    \
	    2       3
	  /   \    /  \
	 4     5  6    7

Sample Ouput2 3 Sample Input

		   1
		  /  \
		 2    3

Sample Output2 3

Given an array of large numbers and a number K, give an algorithm to search for a triplet whose sum is K. You can modify the array. You can print any triplet whose sum is K.

After basic introduction, the interviewer asked me questions about Hashmaps. such as time complexity and how to handle collisions. And he asked me how would I implement a structure to store contact informations(phones numbers, names and area codes). I think I did ok in this part, and the interviewer agreed with me on how I would use a hashmap to do so.

https://leetcode.com/problems/valid-parentheses/

Merge List + find Top K Elements , I solved this using a Heap to merge the Lists, and a later variation involved using BFS, basically the question was , Recommend a user features that are used by friends and friends of friends N - level deep. Given an api which can give you user's friends and friends most used features.

https://leetcode.com/problems/number-of-islands/

https://leetcode.com/problems/knight-probability-in-chessboard/

Given a positive integer N, and a starting point 1 one can perform any of the following 2 operations in one step: https://leetcode.com/discuss/interview-experience/906535/amazon-sde-i-bangalore-october-2020-offer

Add 1 to the number

Double the number The task is to find the minimum number of steps to reach N (desired complexity O(log n)).

Given a set of N numbers (both positive and negative) sorted in increasing order with A[i] < A[j] for all i<j, find whether there exists an index i (i = 1 .. N) such that A[i] = i. If multiple answers are present return any one of them. (desired complexity O(log n)).

Give the design of an automated valet parking system with the following specifications:

There are 3 parking areas (each of different sizes) for 3 different vehicle sizes - small, medium and large.

Small one can accommodate only small vehicles, medium can accommodate small and medium vehicles and similarly for the large one.

Design a system which issues a parking ticket to a vehicle entering the lot with the optimal parking space allotted to it. For eg., if a medium vehicle arrives and both medium and large parking areas have vacant spaces, the vehicle should be allotted the medium slot.

Also design a syntax for the token ID which is generated when each vehicle enters the lot. The ID should be uniquely able to determine the details of the slot where the vehicle is parked for smooth parking and un-parking.

Provide the class design of the same.

Virtual Onsite Round 3 (Bar Raiser, Coding + CS Fundamentals)

Given a set of N integers find the kth largest contiguous subarray sum.

Questions on OS like describe the boot up process of OS.

Difference between caching, paging and buffering.

Difference between stack and heap memory, calloc and malloc, etc.

Things to keep in mind while designing a software product (scalability, memory leaks, deadlocks).

Design a restaurant table booking system with the following specifications:

The restaurant has X tables of size 2, Y tables of size 3 and Z tables of size 4.

There are 3 slots from 6:30 pm to 11 pm, each of 1.5 hrs.

Restaurant can take bookings upto 7 days in advance.

No two parties will share a table.

A pack of size N should always be assigned the largest table available.

Wastage of seats should be minimised.

Provide the database structure to support the above constraints (space should be optimised).

Provide an algorithm to allot table to an incoming reservation with the following specs:

Allot table(s) to a group of N people for the ith day and the jth slot.

Provide pseudo code for the algorithm stated above.

Search for smallest element in sorted rotated list

Tell me about a situation when you had a tight deadline and what are the sacrifices you made to achieve the deadline.

TTL LRU Cache. https://leetcode.com/discuss/interview-question/284925/ttl-lru-cache

Tell me about a time you couldn't finish your task within the given deadline.

flatten a hierarchical linked list.

A variant of topological sort in a graph.

Find smallest +ve missing integer from given array without extra space. (follow up : Array can contain both positive and negative numbers). Ex : ar [1,9,8] output :2

You have locking suitcase system (the one in which there will be number codes). Find the minimum number of steps to reach from given number to target number. You can move any place digit at a time. (for n-digit codes, discuss complexity). Ex : start : 0-0-1Target : 1-0-0 min steps = 2 …..changing an xth place digit by b will be counted as b steps. follow -up...what if you are not allowed to use certain numbers(not digits but whole number )(given as array)Ex: [100,234,115]

Implement a custom collection class with add, remove and getRandomOperations in O(1) time

Amazon Store operates dark stores which can be thought of as strategically located warehouses which service a geographical area around them. Each warehouse has a racking facility which is designed in a layout like this

  17  16  15  14  13
  18   5   4    3    12
  19   6   1    2    11
  20   7   8    9    10
  21  22  23 24…....

Where the numbers indicate the rack number. The facility can be theoretically very large and hence the representation might not fit in computer memory. The entry and the pick up desk of the facility is located near rack 1, so the start and the end of the order packing needs to start from near rack 1. In order to pick up an item from its rack the pickup partner needs to navigate the facility in four possible directions - top, left, bottom and right along the racks. No other form of navigation is allowed. It takes 1 unit duration to travel between neighbouring racks and it takes 1 unit duration to select and pick up an item. Given an order which looks like Order #123Item #1 - Rack 13Item #2 - Rack 10Item #3 - Rack 23 The total duration for preparing this order for delivery is the sum of the navigation and pick up duration of all items. Write a program which outputs a navigation plan to the pickup partner such that the preparation time of the given order is minimized Output: 1->8->23->24->25->10->11->12->13 https://leetcode.com/discuss/interview-question/1586723/amazon-sde-3-interview-question

https://leetcode.com/discuss/interview-question/system-design/685338/microsoft-onsite-design-the-t9-predictive-text-algorithm-and-system (not sure)

https://kobejean.github.io/algorithms/2020/03/08/the-award-budget-cuts-problem/

Poker Cards Game As we all know that poker cards have four suites: Spades, Hearts, Clubs and Diamonds with figures from 1 to 13. Now you are given a set of poker cards, you can pick any one card as the first card. And except for the first card, you can only pick the card that has the same suit or figure with the previous one. Return the max number of cards you can. For example: [(H, 3), (H, 4), (S, 4), (D, 5), (D, 1)], it returns 3 as follows: (H,3)-->(H,4)-->(S,4) https://leetcode.com/discuss/interview-question/1030942/Amazon-Onsite-Inteview-Poker-Cards-Game

Given a game board| B ||A | C | D||E | F | G ||H | I | J|Rules of movinga. you can not move to same row.b. you can not move in same column.Given a starting point and number of moves tell the number of possible options https://leetcode.com/discuss/interview-question/1170079/amazon-onsite-imdb-team

Given an array of integers(pos/neg) in sorted order, return an array of elements square in sorted order.

Given an array of wine prices, any given year you can sell a bottle of wine only from either of the ends. Bottle of wine increases every year. Find max profit after selling all.

Given a uni-directed graph with numbers find maximum root to leaf sum with using only internal data structure.

https://leetcode.com/problems/binary-tree-maximum-path-sum/

https://leetcode.com/problems/word-break/ Given a dictionary of words and a string, state if the string if broken into multiple words consists of dictionary words. I explained him the standard solution using BFS which is O(n) time ans O(n) space.However, the interviewer was deeply interested with me solving the question via making a Graph and then solving it. https://leetcode.com/discuss/interview-question/600412/Amazon-onsite

A very similar question to this , same concept of BFS will applyGiven a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?https://leetcode.com/discuss/interview-question/411357/ Amazon | OA 2019 | 🧟‍♀️ Zombie in Matrix - LeetCode Discuss

given a list of unique strings, if the last char at string A match first char at string B then you can append them together: good+dog -> goodog . Now return the longest possible string (length of concatenated String, not the string number). https://leetcode.com/discuss/interview-question/250623/Onsite-question-for-Amazon-String-concatenation(Updated)/246655

Convert BST to Doubly Linked List without deforming tree and without using extra space except used for creating List. So this shouldn’t be done inplace.Time and Space Complexity of my solutions -: O(n) & O(1) respectively

You are given a subarray which has only 0’s and 1’s , Maximise the subarray containing 1’s and in this you can only flip one 0 , tell the index of that 0Similar to thisfind-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximizedon GFGTime and Space Complexity of my solutions -: O(n) & O(1) respectively

Given 2 large files say file1, file2 consisting of strings of customerid - find the unique customers present in those files. Basically unique words (ex. customer1, customer 3, customer5 and so on)! My approach - Solved using HashSet but interviewer told it won't work as input is very large and Set would exceed Memory limit. I told maybe something like divide and conquer but wasn't able to come up with the actual solution.

For SDE I found Amazon mostly ask Graph Medium questions for example: 323. Number of Connected Components in an Undirected Graph 547. Number of Provinces

https://leetcode.com/problems/word-ladder/

implement business logic for amazon products with friends. Writing a function like you would in a work style

for the given binary tree find the distance or number of hop required to move from one node to another.

https://leetcode.com/problems/frog-jump SDE 2

https://leetcode.com/problems/sliding-puzzle/ SDE 2

Write a program to print the sum of two roman numbers

https://leetcode.com/problems/best-time-to-buy-and-sell-stock If there is a tie, then return the minimum days to finish the transaction. Example: [1 2 3 1 3], we can buy at index 0 and sell at 2, the profit is 2. but we can also buy at index 3 and sell at 4 which only takes 2 days. So return [3, 4]

describe the differences between Set, Map, Array, List and which data structure should be used with different scenarios

https://leetcode.com/problems/k-similar-strings/

Given a file consisting of lines like this:
2017-02-01T20:00 OperationA Start
2017-02-01T20:01 OperationA End
2017-02-01T20:08 OperationB Start
2017-02-01T20:09 OperationC Start
2017-02-01T20:10 OperationB End
2017-02-01T20:12 OperationC End
Produce an average runtime of all operations.
Example output:
Average: 0 days 0 hours 2 minutes (0 days 0 hours 6 minutes total for 3 operations)
. Write a class that subscribes to a log of Alexa utterances, where each message contains line with the following fields (time,sessionId, location, questionText) - represents a question asked by customer to Alexa at time T, write algorithm to find the top-N question pairs. For example, given the following log file containing::2 - 13 - 3 10-Mar-2020 10:34:00, S1, CA, what is expiry of avocado10-Mar-2020 10:30:00, S1, CA, how many calories in avocado10-Mar-2020 10:32:00, S1, CA, can i eat avacado after one week 10-Mar-2020 10:31:00, S2, WY, is mango safe for dogs 10-Mar-2020 10:33:00, S2, WY, is mango safe for cats 10-Mar-2020 12:47:00, S3, MT, find best watch 10-Mar-2020 12:49:00, S3, MT, find best sports watch 11-Mar-2020 11:11:00, S5, TX, is mango safe for dogs 11-Mar-2020 11:12:00, S5, TX, is apple safe for dogs 11-Mar-2020 16:24:00, S4, CA, how many calories in guacamole 11-Mar-2020 16:23:00, S4, CA, how many calories in avocado11-Mar-2020 16:23:00, S4, CA, what is expiry of avocado It should return (what is expiry of avocado, how many calories in avocado)

We are given a list of cars, and the direction of the road they are in. We need to find the order in which cars leave the intersection. The list of cars have the cars at the intersection in order. However, if two cars are in opposite direction, for example East/West or North/South, they can leave the intersection even though other cars arrived before it.

Given a list of inputs in the form of a string array, for example [["Item: Bread", "Id:1"], ["Item: Meat", "Id:3"], ["Item: Sauce", Id:2], ["Item: Bread", "Id:4"]], we need to arrange the input string in order and output the result. The interviewer said do not worry about parsing the string. I gave the solution of sorting based on Id and then getting the result. It was very unclear what the interviewer was expecting. Also, I made the mistake of having only screen, and the interviewer said he was nodding to my questions, and I was writing code in another window. This was a very uncomfortable interview.

Write an API for Linux find command. It was this exact question: https://leetcode.com/discuss/interview-question/369272/Amazon-or-Onsite-or-Linux-Find-Command

Medium OOD question. Very similar to linux find command question (https://leetcode.com/discuss/interview-question/369272/Amazon-or-Onsite-or-Linux-Find-Command) but for validation of purchases. If you are good at applying SOLID principles, this should be solvable. The question was in Java, I spent a couple of minutes to convert it to Python.

https://leetcode.com/problems/russian-doll-envelopes/

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

A variation of meeting rooms: https://leetcode.com/problems/meeting-rooms/Given a list of meeting rooms and a meeting reservation request. Find if the reservation request can be fulfilled or not.Follow up: What if the list of meeting rooms is sorted?Edit: I found a similar one here: https://leetcode.com/problems/my-calendar-i/

Coding: create stack with O(1) push, pop and min.

K most frequent items(item_id) in a stream. Input is a stream of (item_id,timestamp). Then, Interviewer asked me to find frequent items in last hour given a timestamp. For example, Given time 6:07 PM, Return k most frequent items from 5:07 PM to 6:07 PM. Gave an answer using queue, hashmap and min-heap, Not an optimal answer, But it worked.

https://leetcode.com/problems/integer-to-roman/

https://leetcode.com/problems/reorder-data-in-log-files/

Design and implement a playlist of a user’s most recently played songs on Amazon music. It should support the following operations: getSong and addSong. getSong – user should be able to search and get the song from the playlist if the song exists. addSong – add the song into the playlist if the song is not already present.

Design a Parking Lot , Which takes assigns a ticket number a when car arrives and a vacant parking slot is available and rejects if not, Empty the parking slot when car departs. There were different types of cars and parking spots(small,medium and large).

https://leetcode.com/problems/longest-common-subsequence/

https://leetcode.com/problems/longest-consecutive-sequence/

https://leetcode.com/problems/trapping-rain-water/

Merge k sorted linked list & array. (Highly scalable solution was expected)

Implementaion of coin change variation of dynamic programming. -

https://leetcode.com/problems/design-in-memory-file-system/

https://leetcode.com/problems/copy-list-with-random-pointer/

https://leetcode.com/problems/product-of-array-except-self/

https://leetcode.com/problems/median-of-two-sorted-arrays/

https://leetcode.com/problems/rectangle-overlap/

https://leetcode.com/problems/design-tic-tac-toe/

https://leetcode.com/problems/longest-consecutive-sequence/solution/

https://leetcode.com/problems/concatenated-words/

https://leetcode.com/problems/word-search-ii/

https://leetcode.com/problems/making-file-names-unique/

Given a Binary tree mentioned below. Remove redundant connection from Binary Tree. Eg: Node 0 is connected to 2 and 4 both

				3
			 /     \
		  2          4
	  /    \      /    \
    1	      0         5

Follow up question - Assume the tree as a Binary Search Tree & was asked to solve it.

https://leetcode.com/problems/find-all-anagrams-in-a-string/

Largest pair sum that is less than or equal to k in an array

https://leetcode.com/discuss/interview-question/369272/Amazon-or-Onsite-or-Linux-FindCommand

Make Amazon.com's top 20 items sold in last hour. The only interface given to you is a function telling you which item is sold, at the time it is sold. // Invoked as items are being soldvoid (Item item); // Can be called whenevervector GetTop20SoldInLastHour();

SDE 2 question 1) implement prefix search with dictionary of priorities dictionary: [] {amazing, 10}{amazon, 5}{amazonian, 3} create classcreate your own search structureand also method with parameterof prefix like "A", "AM", "AMAZONI", etc.

Given multiple school children and the paths they took from their school to their homes, find the longest most common path (paths are given in order of steps a child takes). Example: child1 : a -> g -> c -> b -> echild2 : f -> g -> c -> b -> uchild3 : h -> g -> c -> b -> x result = g -> c -> b Note: There could be multiple children. Input was not given as a string format, I did so in the examples to clarify the paths taken. The input was in the form of steps and childID and it was not ordered so you also had to put it in a map. For example input looked like this: (child1, a)(child2, f)(child1, g)(child3, h)(child1, c)... As you can see, for child1 path is a -> g -> c, but the children themselves are not ordered, their steps are. Damn guys, I never thought Amazon would ask such a difficult question, I suggested using a trie but afterwards I realized that I did not ask for another case where say a fourth child has the path g -> c -> b -> h -> x, in this case g -> c -> b is still the most common path but a trie will miss it (but I'm not sure though, maybe it would not be). https://leetcode.com/discuss/interview-question/1215680/amazon-onsite-question https://leetcode.com/problems/longest-common-subpath/

https://leetcode.com/problems/rotting-oranges/

https://leetcode.com/problems/all-paths-from-source-to-target/

https://leetcode.com/discuss/interview-question/algorithms/124715/amazon-is-cheese-reachable-in-the-maze

Implement operations for an AutoComplete feature. New Grad 2021

InsertWords(words) - Given a stream of words, store the words

CheckPrefix(prefix) - Returns if the prefix exists

SearchPrefix(prefix) Given a prefix string, return words starting with the prefix string.Eg: Insert Words {car, cart, carpool, bus, apple, cargo}SearchPrefix (car) -> car, cart, carpool, cargoFollow up questions – SearchPrefix() return in sorted order/ top k results

Isomorphic Strings New Grad 2021

Design Unix Find command - https://leetcode.com/discuss/interview-question/609070/Amazon-OOD-Design-Unix-File-Search-API New Grad 2021 Loading... (leetcode.com)

Design and implement a playlist of a user’s most recently played songs on Amazon music. It should support the following operations: getSong and addSong. getSong – user should be able to search and get the song from the playlist if the song exists. addSong – add the song into the playlist if the song is not already present.

In the logistic floor robots entered and exited, how many robot exist at any specific time. interviewer was not very specific about the question and I had to question a lot to understand and construct the problem statement.

https://leetcode.com/problems/jump-game-ii/

SDE 2 question 1) implement prefix search with dictionary of priorities dictionary: [] {amazing, 10}{amazon, 5}{amazonian, 3} create classcreate your own search structureand also method with parameterof prefix like "A", "AM", "AMAZONI", etc.

https://leetcode.com/discuss/interview-question/1215680/Amazon-Onsite-Question. https://leetcode.com/problems/longest-common-subpath/ Given multiple school children and the paths they took from their school to their homes, find the longest most common path (paths are given in order of steps a child takes). Example: child1 : a -> g -> c -> b -> echild2 : f -> g -> c -> b -> uchild3 : h -> g -> c -> b -> x result = g -> c -> b Note: There could be multiple children. Input was not given as a string format, I did so in the examples to clarify the paths taken. The input was in the form of steps and childID and it was not ordered so you also had to put it in a map. For example input looked like this: (child1, a)(child2, f)(child1, g)(child3, h)(child1, c)... As you can see, for child1 path is a -> g -> c, but the children themselves are not ordered, their steps are. Damn guys, I never thought Amazon would ask such a difficult question, I suggested using a trie but afterwards I realized that I did not ask for another case where say a fourth child has the path g -> c -> b -> h -> x, in this case g -> c -> b is still the most common path but a trie will miss it (but I'm not sure though, maybe it would not be).

Given two number in the form of sting, we have to perform two operations: Remove all the zeroes from the number and then add the two numbers.

Given two numbers in the form of LinkedList we have to add the numbers. But there was a condition that we cannot reverse the linkedlist.

https://leetcode.com/problems/asteroid-collision/

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

https://leetcode.com/problems/minimum-knight-moves/

Group Product Id pairs into Categories ****https://leetcode.com/discuss/interview-question/690707/Amazon-or-Phone-Interview-or-Group-Product-Id-pairs-into-Categories

https://leetcode.com/problems/word-break-ii/

Search for smallest element in sorted rotated list

https://leetcode.com/problems/binary-tree-right-side-view/