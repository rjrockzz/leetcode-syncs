class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n= len(nums)
        nums.sort()
        ans= nums[0]+ nums[1]+nums[2];
        if (ans> target):
            return ans;
        #diff= abs(target-ans);
        for i in range (0,n-2):
            left= i+1
            right= n-1
            while (left< right):
                sumi= nums[i]+nums[left]+nums[right]
                if (sumi<target):
                    left+=1
                elif (sumi > target):
                    right-=1
                else:
                    return target
                if (abs(target-sumi) < abs(target-ans)):
                    #diff= abs(target-sumi)
                    ans= sumi
        return ans