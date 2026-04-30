class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        map1={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in map1:
                if st:
                    top=st.pop()
                else:
                    top='#'
                if map1[ch]!=top:
                    return False
            else:
                st.append(ch)
        return not st

        
