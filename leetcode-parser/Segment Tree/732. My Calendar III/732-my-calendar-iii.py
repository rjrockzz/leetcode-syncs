class MyCalendarThree(object):

    def __init__(self):
        self.sts, self.ends = [], []
        self.mxv = 0


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        from bisect import bisect_left as bl, bisect_right as br, insort_left as il
        from heapq import heappop, heappush
        i, j = bl(self.ends, start), br(self.sts, end)
        il(self.sts, start, i, j)
        il(self.ends, end, i, j)
        heap = []
        for pp in range(i, j + 1):
            while heap and heap[0] <= self.sts[pp]:
                heappop(heap)
            heappush(heap, self.ends[pp])
            self.mxv = max(self.mxv, len(heap))
        return self.mxv