class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for n in asteroids:
            st.append(n)
            while len(st)>1 and ((st[-2]>0) and (st[-1]<0)):
                m,n = st.pop(),st.pop()
                if abs(m)!=abs(n):
                    if abs(m)>abs(n):
                        st.append(m)
                    else:
                        st.append(n)
        
        return st