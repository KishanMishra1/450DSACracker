'''Given a number N and a bit number K, check if Kth bit of N is set or not. A bit is called set if it is 1.
Position of set bit '1' should be indexed starting with 0 from LSB side in binary representation of the number.'''


#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends
#User function Template for python3


class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        return n&(1<<k)

#{ 
#Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        obj = Solution()
        if obj.checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        
        T-=1

if __name__=="__main__":
    main()
#} Driver Code Ends
