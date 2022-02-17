#{ 
#Driver Code Starts
#Initial Template for Python 3

import math



 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        position = 1
        m = 1
    
        while (not(n & m)) :
    
            # left shift
            m = m << 1
            position += 1
        
        return position
        

#{ 
#Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
