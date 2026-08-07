class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        d = {}

        for right in range(len(s)):
            if s[right] not in d:
                d[s[right]] = 1
            else:
                d[s[right]] += 1

            while len(d) == 3:
                count += len(s) - right

                d[s[left]] -= 1

                if d[s[left]] == 0:
                    del d[s[left]]

                left += 1
        return count
