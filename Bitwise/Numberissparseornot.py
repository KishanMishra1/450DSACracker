'''Given a number N. 
The task is to check whether it is sparse or not.
A number is said to be a sparse number if no two or more consecutive bits are set in the binary representation.'''



#User function Template for python3

class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):
        #Your code here 
        count=0
        while n>0:
            if n&1==1:
                count+=1
            else:
                count=0
            if count==2:
                return False
            n>>=1
        return True


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        if ob.isSparse(n):
            print("1")
        else:
            print("0")
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
