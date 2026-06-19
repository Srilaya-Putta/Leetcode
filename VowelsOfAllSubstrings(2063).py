class Solution:
    def countVowels(self, word: str) -> int:
        v=set("aeiou")
        n=len(word)
        t=0
        for i in range(n):
            if word[i] in v:
                t+=(i+1)*(n-i)
        return t
        
