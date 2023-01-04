'''
**Intuition**
If the frequence freq of a level is 1,
then it is not possible to complete all the tasks.

Otherwise, we need to decompose freq = 3 tasks + 3 tasks + .... + 2 tasks,
with the minimum number of 3 and 2.

We need a lot a 3-tasks, and plus one or two 2-tasks.


**Explanation**
Tasks with same difficulty level can be done together,
in group of 2-tasks or 3-tasks.

So we count the frequnce freq for each level.

If freq = 1, not possible, return -1
If freq = 2, needs one 2-tasks
If freq = 3, needs one 3-tasks
If freq = 3k, freq = 3 * k, needs k batchs.
If freq = 3k + 1, freq = 3 * (k - 1) + 2 + 2, needs k + 1 batchs.
If freq = 3k + 2, freq = 3 * k + 2, needs k + 1 batchs.

To summarize, needs (freq + 2) / 3 batch,
return the sum of (freq + 2) / 3 if possible.


Complexity
Time O(n)
Space O(n)
'''
class Solution:
    def minimumRounds(self, tasks):
        freq = Counter(tasks).values()
        return -1 if 1 in freq else sum((a + 2) // 3 for a in freq)