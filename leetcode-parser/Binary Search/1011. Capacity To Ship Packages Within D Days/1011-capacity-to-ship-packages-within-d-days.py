class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        '''
        Explanation
            Given the number of bags,
            return the minimum capacity of each bag,
            so that we can put items one by one into all bags.

            We binary search the final result.
            The left bound is max(A),
            The right bound is sum(A).
        '''
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    days += 1
                    if days > D:  # cannot ship within D days
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left