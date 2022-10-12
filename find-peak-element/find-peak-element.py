class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # wherever we factor in the complexity being O(logn), we know it's gonna be
        # a Binary Search
        # SEE HOW HERE WE TALK ABOUT THE NEIGHBOUR THAT MEANS WE HAVE TO UTILIZE THE BS II
        new_nums = [float("-inf")] + nums + [float("-inf")]
        for i in range(1,len(new_nums)-1):
            if new_nums[i-1]<new_nums[i]>new_nums[i+1]:
                return i-1

            