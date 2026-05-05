class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st=[]
        ma=0
        i=0
        n=len(heights)
        while i<n:
            h=heights[i]
            start=i
            while st and st[-1][1]>h:
                idx,height=st.pop()
                ma=max(ma,height*(i-idx))
                start=idx
            st.append((start,h))
            i+=1
        for idx,height in st:
                ma=max(ma,height*(n-idx))
        return ma
