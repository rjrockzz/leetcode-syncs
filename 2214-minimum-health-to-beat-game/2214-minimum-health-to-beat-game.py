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
            