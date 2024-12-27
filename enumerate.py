matrix1 = [3, 7, 3]
matrix2 = [8, 1, 2]

# lets add them
matrix3 = []
for ind in range(len(matrix1)):
    matrix3.append(matrix1[ind] + matrix2[ind])
    
print(matrix3)