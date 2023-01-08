'''
Greedy:
Approach: Greedy
Intuition
We can see that the total damage that can be caused in the game is the sum of all the elements of the damage array. Intuitively, we can also realize that among all the damages caused at every level, the armor should be used to block the largest damage, let's say this largest damage is d. The armor could either completely block the damage if armor >= d or partially block it if armor < d. This means we can block min(armor, d) damage with the armor. We get the net damage suffered in the game by subtracting the amount of damage blocked by the armor from the total damage.

Following this discussion, we iterate over all the elements of the damage array and compute the sum of its elements, let's call it totalDamage. While iterating over the elements, we also find the largest element of the damage array, let's call it maxDamage. The amount of damage blocked after using the armor (at the level with damage equal to maxDamage) would be min(armor, maxDamage). As a result, the total damage dealt throughout the game is totalDamage - min(armor, MaxDamage).

In the end, we return totalDamage - min(armor, maxDamage) + 1 as the answer.
'''
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        '''
        The last health remaining should be 1.
        We can take protect once, and use the armour.
        '''
        max_damage = max(damage)
        for index, i in enumerate(damage):
            if i == max_damage:
                if armor>=damage[index]:
                    damage[index]=0
                else:
                    damage[index]-=armor
                break
        return sum(damage)+1
            