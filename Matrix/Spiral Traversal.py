#spiral traversal of a matrix
'''def display(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()'''


'''def spiralOrder(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])'''
def spiralmat(matrix):
    top,bottom=0,len(matrix)
    left,right=0,len(matrix[0])

    while left<right and top<bottom: 
        for i in range(left,right):
            print(matrix[top][i],end=" ")  # go straight
        top+=1
        for i in range(top,bottom):
            print(matrix[i][right-1],end=" ") # go down
        right-=1

        if not (left<right and top<bottom):
            break
            
        for i in range(right-1,left-1,-1):
            print(matrix[bottom-1][i],end=" ") #print from 2nd last row element to the first
        bottom-=1
        for i in range(bottom-1,top-1,-1):
            print(matrix[i][left],end=" ") #print from 1st of middle row to the 2nd middle --> completing the spiral
        left+=1




matrix=[[1,2,3],[5,6,7],[9,10,11],[13,14,15]]
spiralmat(matrix)
