class Solution:
    def interchangeableRectangles(self, rectangles) -> int:
        result = 0
        count = Counter([w/h for w,h in rectangles])
        for c in count.values():
            if c>1: # we do this since we can't take a pair out of 1 option:P
                result+= (c * (c-1))//2 # remember this from the drawing of the permuations that we took 
        return result