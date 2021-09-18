"""

Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k 
adjacent and equal letters from s and removing them, causing the left and the right side 
of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.

"""


"""

In-place stack example: S = "aabbbcdddcc", K = 3

         i,j                             // i, j start at 1
S  = [ a, A, b, b, b, c, d, d, d, c, c ] // S[j] overwrites S[i]
st = [ 0 ]                               // S[i] == S[i-1], no change


          ->i,j                          // i, j move up 1
S  = [ a, a, B, b, b, c, d, d, d, c, c ] // S[j] overwrites S[i]
st = [ 0, 2 ]                            // S[i] != S[i-1], st.push(i)


             ->i,j                       // i, j move up 1
S  = [ a, a, b, B, b, c, d, d, d, c, c ] // S[j] overwrites S[i]
st = [ 0, 2 ]                            // S[i] == S[i-1], no change


                ->i,j                    // i, j move up 1
S  = [ a, a, b, b, B, c, d, d, d, c, c ] // S[j] overwrites S[i]
st = [ 0, 2 ]                            // S[i] == S[i-1], no change


          i<-------j                     // i moves back because...
S  = [ a, a, B--B--B, c, d, d, d, c, c ] // ...3 b's found, so...
st = [ 0 ]                               // ...i = st.pop() - 1


           ->i      ->j                  // i, j move up 1
S  = [ a, a, C<-------C, d, d, d, c, c ] // S[j] overwrites S[i]
st = [ 0, 2 ]                            // new letter, st.push(i)


              ->i      ->j               // i, j move up 1
S  = [ a, a, c, D<-------D, d, d, c, c ] // S[j] overwrites S[i]
st = [ 0, 2, 3 ]                         // new letter, st.push(i)


                 ->i      ->j            // i, j move up 1
S  = [ a, a, c, d, D<-------D, d, c, c ] // S[j] overwrites S[i]
st = [ 0, 2, 3 ]                         // S[i] == S[i-1], no change


                    ->i      ->j         // i, j move up 1
S  = [ a, a, c, d, d, D<-------D, c, c ] // S[j] overwrites S[i]
st = [ 0, 2, 3 ]                         // S[i] == S[i-1], no change


             i<--------        j         // i moves back because...
S  = [ a, a, c, D--D--D,  ,  ,  , c, c ] // ...3 d's found, so...
st = [ 0, 2 ]                            // ...i = st.pop() - 1


              ->i               ->j      // i, j move up 1
S  = [ a, a, c, C<----------------C, c ] // S[j] overwrites S[i]
st = [ 0, 2 ]                            // S[i] == S[i-1], no change


                 ->i               ->j   // i, j move up 1
S  = [ a, a, c, c, C<----------------C ] // S[j] overwrites S[i]
st = [ 0, 2 ]                            // S[i] == S[i-1], no change


          i<--------                 j   // i moves back because...
S  = [ a, a, C--C--C,  ,  ,  ,  ,  ,   ] // ...3 c's found, so...
st = [ 0 ]                               // ...i = st.pop() - 1


S  = [ a, a ]                            // only keep S up to i
   = "aa"                                // then join to a string


"""

# Recursion

class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        count, i = 1, 1
        while i < len(S):
            if S[i] == S[i-1]: count += 1
            else: count = 1
            if count == K: S = self.removeDuplicates(S[:i-K+1] + S[i+1:], K)
            i += 1
        return S

# In-Place Stack

class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        SC, st, i, j = list(S), [0], 1, 1
        while j < len(S):
            SC[i] = SC[j]
            if i == 0 or SC[i] != SC[i-1]: st.append(i)
            elif i - st[-1] + 1 == K: i = st.pop() - 1
            i += 1
            j += 1
        return "".join(SC[:i])
