class Solution:
    def findDisappearedNumbers(self, nums):
        my_arr = []
        max_val = max(max(nums), len(nums))
        for i in range(1,max_val+1):
            my_arr.append(i)
        return list(set(my_arr) - set(nums))