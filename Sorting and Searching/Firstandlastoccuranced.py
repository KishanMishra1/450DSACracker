
def find(arr,n,x):
    first = 0
    last = 0
    
    if x not in arr:
        first  = -1
        last = -1
        return [first, last]
    else:
        first = arr.index(x)
        
        for i in range(len(arr)):
            if arr[first] == arr[i]:
                last = i
        
        return [first, last]
    
    
    # code here

#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends
