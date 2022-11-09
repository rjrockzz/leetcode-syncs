class Solution:
    def kLengthApart(self, nums, k) -> bool:
        flag = 0
        for i,n in enumerate(nums):
            if n == 1:
                if flag == 1:
                    if i - left_ptr > k:
                        left_ptr = i
                    else:
                        return False
                else:
                    flag = 1
                    left_ptr = i
        return True