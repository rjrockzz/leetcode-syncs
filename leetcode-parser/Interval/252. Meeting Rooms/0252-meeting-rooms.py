class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Step 1 : For all the interval questions, sort the First Key Elements.
        intervals.sort(key=lambda x:(x[0], x[1]))
        prev = 0
        for i in intervals:
            if i[0]>=prev:
                prev = i[1]
                continue
            else:
                return False
        return True