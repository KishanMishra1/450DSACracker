[https://practice.geeksforgeeks.org/explore?page=1&category[]=Bit%20Magic&sortBy=submissions]


Missing Number of Elements

Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

class Solution:
    def MissingNumber(self,res,n):
        res1=0
        xor=0
        for i in res:
            res1=res1^i
        for i in range(1,n+1):
            xor=xor^i
        return xor^res1

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
