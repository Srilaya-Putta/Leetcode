class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=-1
        mx=0
        h=[-1]*(256)
        for right in range(len(s)):
            if h[ord(s[right])]>left:
                left=h[ord(s[right])]
            mx=max(mx,right-left)
            h[ord(s[right])]=right
        return mx
