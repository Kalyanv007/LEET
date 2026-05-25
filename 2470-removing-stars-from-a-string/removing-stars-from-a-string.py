class Solution:
    def removeStars(self, s: str) -> str:
        n=len(s)
        st=[]
        for i in range(n):
            if s[i].isalpha():
                st.append(s[i])
            elif s[i]=='*':
                st.pop()
        str1=""
        for i in st:
            str1+=i
        return str1