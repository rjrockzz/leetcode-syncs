class Solution:
    def leastBricks(self, wall) -> int:
        # we take a count of all the gaps which might be existing in the wall
        countGap = {0 : 0} # At position 0 we have 0 gaps
        
        # Now we traverse until and except the last element of the list.
        for i in wall:
            total = 0
            for j in i[:-1]:
                total+=j
                countGap[total] = 1 + countGap.get(total,0)
        return len(wall) - max(countGap.values())