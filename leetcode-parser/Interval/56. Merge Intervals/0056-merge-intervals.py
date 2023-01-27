class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0], x[1]))
        i = 0
        j = 1
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[j][0]:
                if intervals[i][1] >= intervals[j][1]:
                    intervals[i] = [intervals[i][0], intervals[i][1]]
                else:
                    intervals[i] = [intervals[i][0], intervals[j][1]]
                intervals.pop(j)
            else:
                i+=1
                j+=1
        return intervals
                