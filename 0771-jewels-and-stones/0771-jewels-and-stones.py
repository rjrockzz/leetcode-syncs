class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_hashmap = Counter(stones)
        sum_jewel = 0
        for i in jewels:
            sum_jewel += stone_hashmap[i]
        return sum_jewel