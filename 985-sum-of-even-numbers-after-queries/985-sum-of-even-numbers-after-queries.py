class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        '''
        Runtime complexity is O(len(nums)+len(queries)), because we do a single pass over         nums and a single pass over queries, The space complexity is O(1), because we only         use one integer variable (the result list doesn't count, as it's not necessary for         the algorithm to function).
        '''
        
        result = []
        even_sum = sum([v for v in nums if v % 2 == 0])
        
        for i in queries:
            if nums[i[1]]%2==0:
                even_sum-=nums[i[1]]
            
            nums[i[1]] = nums[i[1]]+i[0]
            
            if nums[i[1]]%2==0:
                even_sum+=nums[i[1]]
            result.append(even_sum)            
        return result
    