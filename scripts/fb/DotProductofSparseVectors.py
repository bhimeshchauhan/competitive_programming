"""

Dot product of sparse vectors


Suppose we have very large sparse vectors (most of the elements in vector are zeros)

Find a data structure to store them
Compute the Dot Product.
Follow-up:
What if one of the vectors is very small?


"""
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