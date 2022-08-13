# This problem was recently asked by Amazon:

# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

def matrix_spiral_print(M):
    # Fill this in.

    ''' k - starting row index
        l - starting column index
        i - iterator '''

    k = 0
    l = 0
    m = 4 # number of columns
    n = 5 # number of rows

    while k < m and l < n:
        # First row
        for i in range(l, n): 
            print(M[k][i], end = " ") 
        k += 1

        # Last column
        for i in range(k, m): 
            print(M[i][n - 1], end = " ") 
        n -= 1

        # Last row
        if (k < m): 
            for i in range(n - 1, (l - 1), -1) : 
                print(M[m - 1][i], end = " ") 
            m -= 1

        # First column
        if (l < n): 
            for i in range(m - 1, k - 1, -1) : 
                print(M[i][l], end = " ") 
            l += 1
              

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
