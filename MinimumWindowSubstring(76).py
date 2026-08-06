class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = [0] * 128

        for c in t: 
            need[ord(c)] += 1
        left = start = end = 0 
        missing = len(t)
        for right, c in enumerate(s,1):
            i = ord(c)
            missing -= need[i] > 0 
            need[i] -= 1
            while missing == 0 : 
                if not end or right - left < end - start: 
                    start,end = left,right
                i = ord(s[left])
                need[i] += 1
                missing += need[i] > 0 
                left += 1
        return s[start:end]
