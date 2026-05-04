class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st=[]
        for ast in asteroids:
            while st and ast<0 and st[-1]>0:
                if st[-1]<-ast:
                    st.pop()
                    continue
                elif st[-1]==-ast:
                    st.pop()
                break
            else:
                st.append(ast)
        return st

    
        
