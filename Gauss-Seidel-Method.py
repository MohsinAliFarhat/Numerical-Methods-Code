def Gauss_Seidel(A,X, B, iterations):
        n = len(A)
        for new in range(0,iterations): 
            for i in range(0,n):
                element = B[i] #32
                
                for j in range(0,n):
                    if(i!=j):
                        element = element-A[i][j]*X[j]
                X[i] = element/A[i][i]
            print("\nGAUSS-SEIDEL METHOD Iteration:"+str(new+1)+"\n"+str(X)+"\n")
            
        return X
                


x = Gauss_Seidel(A, X, B,iterations) 
