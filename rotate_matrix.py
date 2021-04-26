def rotate_matrix(square_matrix):
    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j],
             square_matrix[j][~i]) = (square_matrix[~j][i],
                                      square_matrix[~i][~j],
                                      square_matrix[j][~i],
                                      square_matrix[i][j])
            
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rotate_matrix(A)
assert A == [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]]