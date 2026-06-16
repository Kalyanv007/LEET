class Solution:
    def processStr(self, s: str) -> str:
        result=""
        for char in s:
            if char.islower():
                result+=char
            elif char=='*':
                result=result[:len(result)-1]
            elif char=='#':
                result+=result
            else:
                result=result[::-1]
        return result