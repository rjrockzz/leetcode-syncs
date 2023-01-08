from decimal import Decimal
class Solution:
    
    def gcd(self,a,b):
        while b:
            a,b=b,a%b            
        return a
           
    def Slope(self,point1,point2): 
        dx=point1[0]-point2[0]
        dy=point1[1]-point2[1]
        gcd_=self.gcd(dx,dy)
        
        return (dx/gcd_,dy/gcd_)
       
    
    def maxPoints(self, points: List[List[int]]) -> int:
        if points==None:
            return 0
        
        n=len(points)
        
        if n<=2:
            return n    
        maxPoints=0
        
        for i in range(n):
            slopes={}
            dups=1
            for j in range(i+1,n):
                if points[i]==points[j]:
                    dups+=1
                else:
                    slope=self.Slope(points[i],points[j])
                    
                    if slope in slopes:
                        slopes[slope]+=1
                    else:
                        slopes[slope]=1
                        
            maxPoints=max(maxPoints,dups)
            
            for slope in slopes:
                maxPoints=max(maxPoints,slopes[slope]+dups)
                
        return maxPoints