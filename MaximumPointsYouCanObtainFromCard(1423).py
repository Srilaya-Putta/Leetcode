class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxsum=0
        lsum=0
        rsum=0
        for i in range(0,k):
            lsum+=cardPoints[i]
        maxsum=lsum
        r=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[r]
            r-=1
            maxsum=max(maxsum,lsum+rsum)
        return maxsum
