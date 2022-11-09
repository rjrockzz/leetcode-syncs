class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 # tracks the max area so far
        stack = [] # pair: (index, height)
        # stack will help us access the least recently added elements.
        
        for i,h in enumerate(heights):
            start = i # starting index while we calculate for the further heights.
            while stack and stack[-1][1] > h:
                '''
                
                             ___
                            |   |
                         ___|   |  <----- this condition where stack's top element is greater than the height after it          
                        |   |   |___
                     ___|   |   |   |
                    |   |   |   |   |
                ____|___|___|___|___|___
                '''
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start,h))
        
        # The still remaining elements, where start to calculate theirs heights as well
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
            