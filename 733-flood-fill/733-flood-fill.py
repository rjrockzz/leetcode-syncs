class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)): # R-1, R+1, C-1, C+1
                '''
                4-D Pixel Traversal :O
                '''
                if 0 <= x < m and 0 <= y < n and image[x][y] == old: # Consists of the 2 dimensions
                    '''
                    We're checking whether the coordinates actually lie within the image
                    and then we compare IF THE COLOR is actually the same as the one we had previously
                    AND As soon as we have the condition satisfied, we move forward!
                    '''
                    dfs(x, y)
        '''
        To keep our limits in check about the pixel dimensions, we also assign m, n.
        '''
        old, m, n = image[sr][sc], len(image), len(image[0]) 
        '''
        old is the color of original pixel, length of the row (m), length of the column (n)
        '''
        if old != newColor: 
            dfs(sr, sc)
        '''
        If the old color is actually equal to the new color, flood fill will NOT proceed,
        because there are no changes initially only.
        '''
        return image