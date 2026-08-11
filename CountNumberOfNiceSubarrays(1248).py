class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        tot=0
        odds=0
        prefix_counts={0:1}
        for num in nums:
            if num%2==1:
                odds+=1
            if odds-k in prefix_counts:
                tot+=prefix_counts[odds-k]
            prefix_counts[odds]=prefix_counts.get(odds,0)+1
        return tot
