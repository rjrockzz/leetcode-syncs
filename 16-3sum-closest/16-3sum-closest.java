class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;
        
        if (n == 3)
            return nums[0] + nums[1] + nums[2];
        
        Arrays.sort(nums);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int left = i + 1;
            int right = n - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                int diff = target - sum;
                if (Math.abs(diff) < Math.abs(minDiff))
                    minDiff = diff;
                
                if (minDiff == 0)
                    break;
                
                if (sum < target)
                    left++;
                else
                    right--;
            }
        }
        
        return target - minDiff;
    }
}