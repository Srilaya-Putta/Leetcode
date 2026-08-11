import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # a  a  b  b  a  c
        #  aa    bb      
        #       abba   
        # 0 | 1  2  3  4  5
        # 01     23  
        #       1234
        
        # enumerate all palindrome
        ls = len(s)
        is_palin = [[False] * ls for _ in range(ls)]

        # loop over s and update is_palin
        def expand(left, right):
        # Expand while s[left:right + 1] remains a palindrome
            while left >= 0 and right < ls and s[left] == s[right]:
                is_palin[left][right] = True
                left -= 1
                right += 1

        for center in range(ls):
            expand(center, center)       # Odd length: "aba"
            expand(center, center + 1)   # Even length: "abba"

        # use dp
        path = []
        ret = []
        #print(is_palin)
        def dfs(srt):
            #nonlocal path
            if srt >= ls:
                ret.append(
                    path.copy())
                #path = []

            for i in range(srt, ls):
                if is_palin[srt][i]:
                    path.append(s[srt:i+1])

                    dfs(i+1)
                    path.pop()
        
        dfs(0)
        return ret

                    
