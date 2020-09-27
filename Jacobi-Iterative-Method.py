

iterations = 3							 				 
X = [0, 0, 0, 0, 0]	
X_previous = [0, 0, 0, 0, 0]					 
A = [[4,0,1,0,1], [2,5,-1,1,0], [1,0,3,-1,0],[0,1,0,4,-2], [1,0,-1,0,5]] 
B = [32,19,14,-2,41] 

def Jacobi_iterative_method(A,X, B, iterations):
    n = len(A)
    for new in range(0,iterations):       
        X=list(X_previous)
        
        for i in range(0,n):
            element = B[i] #
            
            for j in range(0,n):
                if(i!=j):
                    element = element-A[i][j]*X[j]
            X_previous[i] = element/A[i][i]
        print("\nJACOBI'S METHOD\nIteration:"+str(new+1)+"\n"+str(X_previous)+"\n")
            
    return X
x = Jacobi_iterative_method(A, X, B,iterations)                 

