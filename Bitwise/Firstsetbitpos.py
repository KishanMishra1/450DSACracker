'''Given a number N having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit. 
If there are 0 or more than 1 set bit the answer should be -1.
Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.'''




# User function Template for python3
import math
class Solution:
    def findPosition(self, N):
        # code here
        if N==0:
            return -1
        elif N&(N-1)==0:
            return int(math.log2(N)+1)
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends
