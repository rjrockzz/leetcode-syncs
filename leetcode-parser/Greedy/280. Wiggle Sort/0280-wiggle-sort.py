class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Nothing special here, if we have three elements a0⩽a1⩽a2 , then just change elements and get a0⩽a2⩾a3. The similar trick if we have a0⩾a1⩾a2 . It is a bit similar to bubble sort, but we need only one pass through data.
        '''
        # Time: O(nlogn), Space: O(1)
        nums.sort()
        for i in range(1,len(nums)-1,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]