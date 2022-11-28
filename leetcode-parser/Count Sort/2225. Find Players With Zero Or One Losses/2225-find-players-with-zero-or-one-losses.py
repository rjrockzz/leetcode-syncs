class Solution:
    def findWinners(self, matches):
        winner_hashmap = {}
        loser_hashmap = {}
        answer = []
        for i in matches:
            winner_hashmap[i[0]] = 1 + winner_hashmap.get(i[0], 0)
            loser_hashmap[i[1]] = 1 + loser_hashmap.get(i[1], 0)
        # for no losses, we'll take a set difference between the winner and the loser hashmap
        answer.append(sorted(list(set([*winner_hashmap]) - set([*loser_hashmap]))))
        answer.append(sorted([k for k, v in loser_hashmap.items() if v == 1]))
        return answer