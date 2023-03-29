class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        satisfaction = deque(satisfaction)
        likeTime = lambda x: sum((i+1) * v for i, v in enumerate(x))
        output = likeTime(satisfaction)
        while satisfaction:
            satisfaction.popleft()
            output = max(output, likeTime(satisfaction))
        return output