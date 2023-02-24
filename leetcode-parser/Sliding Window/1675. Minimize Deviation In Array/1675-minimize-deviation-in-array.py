class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        # pretreatment
        possible = []
        for i, num in enumerate(nums):
            if num % 2 == 0:
                temp = num
                possible.append((temp, i))
                while temp % 2 == 0:
                    temp //= 2
                    possible.append((temp, i))
            else:
                possible.append((num, i))
                possible.append((num*2, i))

        heapq.heapify(possible)
        min_deviation = inf
        need_include = {i: 1 for i in range(n)}
        not_included = n
        current_start = 0
        seen = []
        # get minimum from heap
        while possible:
            current_value, current_item = heapq.heappop(possible)
            seen.append([current_value, current_item])
            need_include[current_item] -= 1
            if need_include[current_item] == 0:
                not_included -= 1
            if not_included == 0:
                while need_include[seen[current_start][1]] < 0:
                    need_include[seen[current_start][1]] += 1
                    current_start += 1
                if min_deviation > current_value - seen[current_start][0]:
                    min_deviation = current_value - seen[current_start][0]

                need_include[seen[current_start][1]] += 1
                current_start += 1
                not_included += 1

        return min_deviation