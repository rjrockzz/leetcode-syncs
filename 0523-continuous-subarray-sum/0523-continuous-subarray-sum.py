'''
The optimal solutions for this kind of problems are always Hashmap + Prefix Sum!

Note that if we first generate the whole prefix sum list of the input array, then we could get all subarray sum in O(n^2), which is good but not optimal.
The idea comes: Also take Hashmap into use with Prefix Sum, reduce time to O(n).

We should initiate a Hashmap
key is prefix sum % k,
value is index of the current prefix sum.

When we reach some position, for example i, whose prefix sum % k is already in the Hashmap, and Hashmap[prefix sum % k] = j, then it means that nums[j+1:i+1] % k == 0, which is what we want! (We need to check i - j >= 2, as given)

Time: O(n)
Space: O(min(n, k))
There could be at most k keys in the Hashmap.
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        mapping = {0: -1}
        running_sum = 0
        
        for i, num in enumerate(nums):
            
            running_sum = (running_sum + num) % k
            
            if running_sum not in mapping:
                mapping[running_sum] = i
            else:
                if i - mapping[running_sum] >= 2:
                    return True
        
        return False