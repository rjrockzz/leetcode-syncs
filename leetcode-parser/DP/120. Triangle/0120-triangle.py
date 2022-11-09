class Solution:
    # O(n*n/2) space, top-down 
    # We also construct a result array which increases our space complexity
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        res = [[0 for i in range(len(row))] for row in triangle]
        # We construct a Space Graph for computing the triangle's minimums
        # It looks like this >>
        
        '''
                    [0]
                   [0,0]
                  [0,0,0] 
                 [0,0,0,0]
        '''

        res[0][0] = triangle[0][0]

        '''
                    [2]
                   [0,0]    <--- start the traversals from here.
                  [0,0,0] 
                 [0,0,0,0]
        '''

        for i in range(1, len(triangle)):  # traversing the rows
            for j in range(len(triangle[i])): # traversing the each element inside the row
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        '''
        * The final result array!
                    [2]
                   [5,6]
                 [11,10,13] 
                [15,11,18,16]
        '''
        return min(res[-1])