'''Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res=0
        n=len(A)
        
        for i in range(0,32):
            
            sm=0
            x=1<<i
            for j in range(0,n):
                if A[j]&x:
                    sm+=1
            if sm%3:
                res=(res|x)
        return res
