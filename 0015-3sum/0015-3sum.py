class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Result Set
        result = set()
        #1. Split the nums into three lists: Negative Number, Positive Numbers, And Zeroes
        negative, positive, zeroes = [], [] ,[]
        for num in nums:
            if num>0:
                positive.append(num)
            elif num<0:
                negative.append(num)
            else:
                zeroes.append(num)
            
        #2. Creating a Separate set for negatives and positives for O(1) lookup times
        negative_sets , positive_sets = set(negative), set(positive)
        #3. If there is at least 1 zero in the list, add all cases where -num exists in negative_sets and num exists in positive_sets
        # ie. (-3,0,3) = 0
        if zeroes:
            for num in positive_sets:
                if -num in negative_sets: # O(1) lookup
                    result.add((-num,0,num))
        # 4. If there are atleast 3 zeroes in the list then we can also include (0,0,0) = 0
        if len(zeroes)>=3:
            result.add((0,0,0))
        # 5. For all pairs of negative numbers (-3,-1), check to see if their complement (4) exists in the positive number set
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                target = -1 * (negative[i] + negative[j])
                if target in positive_sets:
                    result.add(tuple(sorted([negative[i], negative[j], target])))
        # 5. For all pairs of positive numbers (1,1), check to see if their complement (-2) exists in the negative number set
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                target = -1 * (positive[i] + positive[j])
                if target in negative_sets:
                    result.add(tuple(sorted([positive[i], positive[j], target])))
        return result