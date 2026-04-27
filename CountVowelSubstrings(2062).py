class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        c=0
        v={'a','e','i','o','u'}
        n=len(word)
        for i in range(n):
            if word[i] in v:
                u=set()
                for j in range(i,n):
                    if word[j] in v:
                        u.add(word[j])
                        if len(u)==5:
                            c+=1
                    else:
                        break
        return c
        
