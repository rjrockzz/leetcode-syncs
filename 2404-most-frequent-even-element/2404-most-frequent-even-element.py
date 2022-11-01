class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter(nums)
        hashmap_sorted = dict(sorted(counter.items(), key = lambda x : (-x[1], x[0])))
        for k,v in hashmap_sorted.items():
            if k%2==0:
                return k
        return -1