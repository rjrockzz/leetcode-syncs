class Solution:
    def diagonalSum(self, mat) -> int:
        if len(mat)==1:
            return mat[0][0]
        sum_left_diagonal = 0
        sum_right_diagonal = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    sum_left_diagonal+=mat[i][j]
                if i+j==(len(mat)-1) and i!=j:
                    sum_right_diagonal+=mat[i][j]
        return sum_left_diagonal + sum_right_diagonal