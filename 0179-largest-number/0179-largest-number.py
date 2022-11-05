class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        So this is what we're essentially doing : 
        "9", "34"
        "934" > "349" 
        we're comparing every element possible from the current element, until we get a sorted         item, please check in the All Concepts Learnt, cmp_to_key()
        '''
        # Converting every integer to a string
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        # Creating a comparitor function
        def compare(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key = cmp_to_key(compare))
        # Now to deal with the edge case of "00000", we're gonna convert it first to int then           string again 
        return str(int("".join(nums)))
        
        