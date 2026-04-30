class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st=[]
        for num in num:
            while st and st[-1]>num and k>0:
                st.pop()
                k-=1
            st.append(num)
        while k>0:
            st.pop()
            k-=1
        res="".join(st).lstrip('0')
        if res:
            return res
        else:
            return '0'
