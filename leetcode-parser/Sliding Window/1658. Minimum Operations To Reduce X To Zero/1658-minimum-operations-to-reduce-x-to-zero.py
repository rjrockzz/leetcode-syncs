class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        Given an integer array nums and integer x. In one operation we can only either     
        remove an element from the leftmost or the rightmost element from the array nums           and subtract its value from k
        '''
        '''
        We can reformulate this problem: we need to choose several values from the beginning and several values from end, such that sum of this numbers is equal to x. It is equivalent to finding some contiguous subarray, such that it has sum of elements equal to sum(nums) - x, which has the biggest length. In this way problem becomes quite classical and I prefer to solve it using cumulative sums.

Imagine, that we have nums = [1,1,4,2,3], x = 5. Then we need to find contiguous subarray, such that its sum is equal to sum(nums) - x = 6. It means, that we need to find two cumulative sums, one of them equal to goal plus another one. Note also, that all nums are positive, so all cumulative sums will be different.

We keep in dic indexes for each cumulative sum, so, when we iterate num in dic and check if num + goal in dic, then we can get length of window: dic[num + goal] - dic[num] and update ans.

Complexity: time complexity is O(n), space complexity as well.

Remark: this idea will work also if we can have negative numbers in our nums. We need to keep in dic smallest and biggest indexes for each value of cumulative sum and then find maximum between ends of two segments. If we asked to find window of minimum length, and we have negative numbers, it is also possible, but we need to keep defaultdict of all indexes and then use idea of merge sort to find closest pair. Complexities will be also O(n).
        '''
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0: return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1