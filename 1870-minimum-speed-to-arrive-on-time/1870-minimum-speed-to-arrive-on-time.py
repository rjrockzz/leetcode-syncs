class Solution:
    def minSpeedOnTime(self, dist: List[int], t: float) -> int:
        left, right, min_speed = 1, 10_000_000 + 1, -1
        while left < right:
            speed = left + (right - left) // 2
            if (sum((dist[i] + speed - 1) // speed for i in range(len(dist) - 1)) +
                dist[-1] / speed) > t:
                left = speed + 1
            else:
                right = speed
                min_speed = speed
        return min_speed