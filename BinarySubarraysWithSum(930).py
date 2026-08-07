class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        f={0:1}
        s=0
        c=0
        for i in nums:
            s+=i
            if s-goal in f:
                c+=f[s-goal]
            if s in f:
                f[s]+=1
            else :
                f[s]=1
        return c
        
