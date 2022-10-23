class Solution:
    def findErrorNums(self, nums):
        set_dup = set()
        for index,i in enumerate(nums):
            set_dup.add(i)
            if len(set_dup)!=index+1:
                dup = i
                nums.remove(i)
                break
        sum_range = (len(nums)+1)*((len(nums)+1) + 1)//2
        return [dup, sum_range-sum(nums)]
            
        
        