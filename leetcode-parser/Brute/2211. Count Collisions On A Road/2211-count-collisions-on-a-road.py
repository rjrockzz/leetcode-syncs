class Solution:
    def countCollisions(self, directions: str) -> int:
        '''
        R - L -> 2 = S - S
        R - S -> 1 = S - S
        S - L -> 1 = S - S
        S - L -> 1 = S - S
        == 5
        '''
        '''
        All possible permutations:
        R - S = 1 -> left_state = "S"
        R - R = 0 -> left_state = "R"
        R - L = 2 -> left_state = "S"
        L - R = 0 -> left_state = "R"
        L - L = 0 -> left_state = "L"
        L - S = 0 -> left_state = "S"
        S - R = 0 -> left_state = "R"
        S - L = 1 -> left_state = "S"
        S - S = 0 -> left_state = "S"
        '''
        left_state = directions[0]
        counter = 0
        trailing_r = 0
        for i in range(1,len(directions)):
            if left_state=="R" and directions[i]=="L":
                counter +=2
                if trailing_r!=0:
                    counter+=trailing_r
                    trailing_r = 0
                left_state = "S"
            elif left_state=="S" and directions[i]=="L":
                counter+=1
                left_state="S"
            elif left_state=="R" and directions[i]=="S":
                counter+=1
                if trailing_r!=0:
                    counter+=trailing_r
                    trailing_r = 0
                left_state="S"
            elif left_state=="R" and directions[i]=="R":
                trailing_r+=1            
            else:
                left_state = directions[i]
                continue
        return counter
                
                
            
            
            