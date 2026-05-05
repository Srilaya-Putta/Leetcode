class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        lm=0
        rm=0
        w=0
        r=len(height)-1
        while l<r:
            if height[l]<height[r]:
                w+=max(0,lm-height[l])
                lm=max(lm,height[l])
                l+=1
            else:
                w+=max(0,rm-height[r])
                rm=max(rm,height[r])
                r-=1
        return w


        
