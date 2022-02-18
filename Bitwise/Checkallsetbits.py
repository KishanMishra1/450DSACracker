'''Given a number N. You have to check whether every bit in the binary representation of the given number is set or not.'''

# User function Template for python3
class Solution:
    def isBitSet(self, N):
        # code here
        return 1 if ((N != 0) and ((N & (N + 1)) == 0)) else 0


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isBitSet(N))
# } Driver Code Ends
