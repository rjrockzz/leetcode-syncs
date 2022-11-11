'''
Since the problem is asking us to remove duplicates in place, it seems like the only choice we have is to use a two-pointers approach. Also since the array is sorted, duplicates are grouped together in the array.
(1) Using a pointer i to point to the index where the element will be replaced.
(2) Using another pointer, j, to go through the array and check if the jth element is the same as the j-1 element or not.
(3) If nums[j]!=nums[j-1], we should replace nums[i] with nums[j] and move i forward by 1. This is because nums[j] is the first element without duplicates before it, and we should keep it in the results.

In the end, nums[:i] will be the array without any duplicates, so we just return i. Note that i should start at 1 since nums[0] will always be there no matter what.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j-1]
                i += 1
        nums[i] = nums[-1]
        return i+1