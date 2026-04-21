class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        ans=start^goal
        c=0
        while(ans!=0):
            rem = ans%2
            if rem==1:
                c+=1
            ans=ans//2
        return c
        
