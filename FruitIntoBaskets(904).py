class Solution(object):
    def subarraySum(self, nums, k):
        notebook={}
        notebook[0]=1
        current_sum=0
        count=0
        for i in range(0,len(nums)):
            current_sum+=nums[i]
           
            diff=current_sum-k
            if(diff in notebook):
                count+=notebook[diff]
                
            if(current_sum in notebook):
                notebook[current_sum]+=1
            else:
                notebook[current_sum]=1

            
            
            
            
        return count
        
