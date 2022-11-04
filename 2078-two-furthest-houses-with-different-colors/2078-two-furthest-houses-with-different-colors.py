class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist=0
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                if colors[i]!=colors[j]:
                    max_dist = max(max_dist, abs(i-j))
        return max_dist
            