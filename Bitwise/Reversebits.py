'''Given a 32 bit number X, reverse its binary form and print the answer in decimal.'''

#User function Template for python3

class Solution:
    def reversedBits(self, X):
        b = bin(X)[2:]
        if len(b) < 32:
        	x = 32 - len(b)
            b = ("0"*x)+b
            b = b[::-1]
            return int(b,2)
        else:
             b = b[::-1]
             return int(b,2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends
