def modifyMatrix(mat, m, n):  

    row = [0] * m 
    col = [0] * n       

    for i in range(0, m): # Initialize all values of row[] as 1 
        row[i] = 1                

    for i in range(0, n) : # Initialize all values of col[] as 1 
        col[i] = 1     

    for i in range(0, m) :        # Store the rows and columns to be marked
        for j in range(0, n) :    # as 0 in row[] and col[] arrays respectively 

            if (mat[i][j] == 0) :  
                row[i] = 0 
                col[j] = 0 

    for i in range(0, m) :       # Modify the input matrix mat[] using the  
        for j in range(0, n):    # above constructed row[] and col[] arrays
            if ( row[i] == 0 or col[j] == 0 ) :  
                mat[i][j] = 0 
                   

def printMatrix(mat) : # A utility function to print out the motified atrix 

    for i in range(0, m):            

        for j in range(0, n) :  

            print(mat[i][j], end = " ")  

        print() 

mat=[ [1, 0, 0, 1], 
    [0, 0, 1, 0], 
    [0, 0, 0, 0] ]
m=3
n=4

modifyMatrix(mat, m, n)
printMatrix(mat)
