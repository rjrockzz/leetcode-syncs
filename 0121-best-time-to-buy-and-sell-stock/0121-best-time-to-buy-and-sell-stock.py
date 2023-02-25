class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        left_pointer_buy = 0
        for right_pointer_sell in range(1, len(prices)):
            if prices[right_pointer_sell] < prices[left_pointer_buy]:
                left_pointer_buy = right_pointer_sell
            res = max(res, prices[right_pointer_sell] - prices[left_pointer_buy])
        return res