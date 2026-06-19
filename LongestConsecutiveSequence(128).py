class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        numSet = set(nums)
        res = 1

        for num in numSet:
            if num+1 in  numSet:
                continue

            count = 1

            while (num-count) in numSet:
                count+=1
            res = max(count,res)
        
        return res
