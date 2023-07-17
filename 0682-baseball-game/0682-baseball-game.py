"""
X : Append to stack
+ : Append to stack -> Sum of previous two elements
D : Append to stack -> Double of Previous Element
C : Pop Stack element
"""
class Solution:
    def calPoints(self, operations) -> int:
        stack = []
        sum_so_far = 0
        for i in operations:
            if i == "C":
                remove = stack.pop()
                sum_so_far-= int(remove)
            elif i == "D":
                double = 2*int(stack[-1])
                stack.append(double)
                sum_so_far+= int(double)
            elif i == "+":
                add = int(stack[-1]) + int(stack[-2])
                stack.append(add)
                sum_so_far+= int(add)
            else:
                stack.append(i)
                sum_so_far+= int(i)
        return sum_so_far
            
print(Solution().calPoints(["5","2","C","D","+"]))