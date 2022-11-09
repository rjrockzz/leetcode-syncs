class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Not a constant space, but yeah, we can implement a Bucket Sorting Algorithm.
        bucket_sort = {}
        
        for i in nums:
            bucket_sort[i] = 1 + bucket_sort.get(i,0)
        nums[:] = []    
        bucket_sort = dict(sorted(bucket_sort.items(), key = lambda x: x[0]))
        for k,v in bucket_sort.items():
            nums.extend([k]*v)
        