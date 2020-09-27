n = 3   #Iterations to be performed
A = [[4,0,1,0,1], [2,5,-1,1,0], [1,0,3,-1,0],[0,1,0,4,-2], [1,0,-1,0,5]]
A_temp = [[0 for x in range(len(A)-1)]for y in range(len(A[0]))]
x = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
x_temp = [0,0,0,0,0]
B = [32,19,14,-2,41]
count=0
row=0
col=0

for i in range(0,len(A)):
    col=0
    for j in range(0,len(A)):
        if(j==i):
            continue
        else:
            A_temp[row][col] = A[i][j]
            col=col+1            
    row=row+1

for i in range(0, n):
    for j in range(0,len(A[0])):
        x_temp[j] = ((1/A[j][j])*(B[j] - A_temp[j][0]*x[j][0] - A_temp[j][1]*x[j][1] - A_temp[j][2]*x[j][2] - A_temp[j][3]*x[j][3]))

    for k in range(0,5):
            count=0
            
            for z in range(0,5):
                if(k==z):
                    continue                
                x[k][count] = x_temp[z]
                count=count+1

    print("Iteration: "+str(i+1)+"\n"+str(x_temp)+"\n")
