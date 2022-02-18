 '''You are given an array arr[], you have to re-construct an array arr[].
The values in arr[] are obtained by doing Xor of consecutive elements in the array.'''


# User function Template for python3

def game_with_number(arr, n):
    # Complete the function
    res = []
    for i in range(len(arr)-1):
        res.append(arr[i]^arr[i+1])
    res.append(arr[-1])
    return res


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)

# } Driver Code Ends
