def LUdecomp(matrix, n): 
	L = [[0 for x in range(n)] 
				for y in range(n)]; 
	U = [[0 for x in range(n)] 
				for y in range(n)]; 
	for i in range(n): 
		for k in range(i, n): 
			sum = 0; 
			for j in range(i): 
				sum += (L[i][j] * U[j][k]); 
			
			U[i][k] = matrix[i][k] - sum; 
		for k in range(i, n): 
			if (i == k): 
				L[i][i] = 1; 
			else: 
				sum = 0; 
				for j in range(i): 
					sum += (L[k][j] * U[j][i]); 
				 
				L[k][i] = int((matrix[k][i] - sum) /
									U[i][i]); 
	return L,U
    
def back_subsitution(matrix,b):
   x=[0 for x in range(0,len(matrix))]
   for row in reversed(range(len(matrix))):
      sum_=0
      for column in range(0,len(matrix[0])):
        if(column==row):
            continue
        sum_ =sum_+ matrix[row][column] *x[column]
      x[row] = (b[row]-sum_)/matrix[row][row]
   return x 

def forward_subsitution(matrix,b):
   x=[0 for x in range(0,len(matrix))]
   for row in range(0,len(matrix)):
      sum_=0
      for column in range(0,len(matrix[0])):
        if(column==row):
            continue
        sum_ =sum_+ matrix[row][column] *x[column]
      x[row] = (b[row]-sum_)/matrix[row][row]
   return x        

matrix= [[4,-2,-3,6],
        [-6,7,6.5,-6],
        [1,7.5,6.25,5.5],
        [-12,22,15.5,-1]]
b = [12,-6.5,16,17]
L,U  =LUdecomp(matrix,len(matrix))
n = len(matrix)
for i in range(n): 
		# Lower Traingular
		for j in range(n): 
			print(L[i][j], end = "\t"); 
		print("", end = "\t"); 
		# Upper Traingular
		for j in range(n): 
			print(U[i][j], end = "\t"); 
		print("");

y =forward_subsitution(L,b)
x = back_subsitution(U,y)
print("")
for i in range(0,len(x)):
    print("x"+str(i+1)+" ",x[i])