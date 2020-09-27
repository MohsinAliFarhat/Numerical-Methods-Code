def convertToReducedEchelon(matrix,n):
    i=0
    j=0
    k=0
    flag=0
    
    for i in range(0,n):
        if(matrix[i][i]==0):#Check if diagonal element is zero
            
            c=1             #We try to search beneath the 0 diagonal element for non-zero element
            while((i+c)<n and matrix[i+c][i]==0): #keep searching untilwe find it
                c=c+1
            if((i+c)==n):
                flag = 1    #This means all elements in column are zero, so we check if solution exists or not
                break
            for k in range(0,n+1):  #This loop is used to exchange two rows such that diagonal element is now non-zero
                temp = matrix[j][k]
                matrix[j][k] = matrix[j+c][k]
                matrix[j+c][k] = temp
        
        for j in range(0,n):#Perform operations to make all non-diagonal elements zero
             if(i!=j):
                 
                 p = matrix[j][i]/matrix[i][i]
                 for k in range(0,n+1):
                     matrix[j][k] = matrix[j][k] - (matrix[i][k])*p
    return flag                
     
def showResult(matrix, n, flag):
    
    print("Solution:")
    
    if(flag==2):
        print("Infinite Solution possible")
    elif(flag==3):
        print("No Solution Exists")
    else:
        print("Final Matrix\n",matrix,"\n")
        for i in range(0,n):
            print("x"+str(i+1)+" = "+str(matrix[i][n]/matrix[i][i])+" ")
            
            
def checkForSolution(matrix,n, flag):
    flag=3
    for i in range(0,n):
        sum = 0
        for j in range(0,n):
            sum = sum+matrix[i][j]  
        if(sum==matrix[i][j]):      #Infinite solution when number of variables is more than non-zero rows
            flag=2
    return flag

print("\nSYSTEM:1")
matrix = [[0,2,3,8],[4,6,7,-3],[2,1, 6,5]]
n=len(matrix)
flag=0
flag = convertToReducedEchelon(matrix,n)
if(flag==1):
    flag = checkForSolution(matrix,n,flag)
    
print(showResult(matrix,n,flag))

print("------------------------------------")

print("\nSYSTEM:2")
matrix = [[0,-3,7,2],
        [1,2,-1,3],
        [5,-2,0,2]]
n=len(matrix)
flag=0
flag = convertToReducedEchelon(matrix,n)
if(flag==1):
    flag = checkForSolution(matrix,n,flag)
    
print(showResult(matrix,n,flag))