'''
We can further optimize the previous approach by using counting sort.
A comparison-based sorting method (like heapsort, mergesort, etc.) takes (nlogn) time. However, using counting sort, we can access the elements in sorted order in linear time.

The idea behind counting sort is that in an additional array arrayFreq we store the frequency of each element of the input array where arrayFreq's index denotes the element of the input array. Thus, in an indirect way when the indices of arrayFreq are accessed in increasing order, we also access the element of the input array in sorted order. You can get a brief idea from the following image.
'''
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n, icecreams = len(costs), 0
        m = max(costs)

        costsFrequency = [0] * (m + 1)
        for cost in costs:
            costsFrequency[cost] += 1

        for cost in range(1, m + 1):
            # No ice cream is present costing 'cost'.
            if not costsFrequency[cost]:
                continue
            # We don't have enough 'coins' to even pick one ice cream.
            if coins < cost:
                break
            
            # Count how many icecreams of 'cost' we can pick with our 'coins'.
            # Either we can pick all ice creams of 'cost' or we will be limited by remaining 'coins'.
            count = min(costsFrequency[cost], coins // cost)
            # We reduce price of picked ice creams from our coins.
            coins -= cost * count
            icecreams += count
            
        return icecreams