class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(v for v in nums if v % 2 == 0)
        
        for i in queries:
            if nums[i[1]]%2==0:
                even_sum-=nums[i[1]]
            
            nums[i[1]] = nums[i[1]]+i[0]
            
            if nums[i[1]]%2==0:
                even_sum+=nums[i[1]]
            result.append(even_sum)            
        return result
            