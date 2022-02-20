class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,cols=len(matrix),len(matrix[0])
        low,high=0,row*cols-1
        
        while(low<=high):
            mid=(low+high)//2
            
            num=matrix[mid//cols][mid%cols]
            
            if num==target:
                return True
            elif num>target:
                high=mid-1
            else:
                low=mid+1
        return False
