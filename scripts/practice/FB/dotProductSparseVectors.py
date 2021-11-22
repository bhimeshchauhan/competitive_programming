"""

Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse 
vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100


"""

# With class definition
class SparseVector:
    def __init__(self, nums: List[int]):
        self.sv = []
        for idx, item in enumerate(nums):
            if item != 0:
                self.sv.append((idx, item))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        print(self.sv, vec.sv)
        ans = 0
        for idx, val1 in self.sv:
            for jdx, val2 in vec.sv:
                if idx == jdx:
                    ans += val1 * val2
        return ans
                    

# With List
def sparseVDotProduct(a,b):
    listA=[]
    listB=[]

    for i in range(len(a)):
        if a[i]!=0:
            listA.append((i,a[i]))

    for i in range(len(b)):
        if b[i]!=0:
            listB.append((i,b[i]))

    p1=0
    p2=0
    result=0

    while (p1<len(listA) and p2<len(listB)):
        if listA[p1][0]==listB[p2][0]:
            result+= listA[p1][1]*listB[p2][1]
            p1+=1
            p2+=1
        elif listA[p1][0] < listB[p2][0]:
            p1+=1
        else:
            p2+=1

    return result

a=[0,2,3,4,0,0,0,0,0,0,5]
b=[5,1,0,0,0,0,0,0,0,0,9,3]
print(sparseVDotProduct(a, b))
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)