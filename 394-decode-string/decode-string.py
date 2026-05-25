class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ""
        currNum = 0

        for ch in s:

            # Build number
            if ch.isdigit():
                currNum = currNum * 10 + int(ch)

            # Push current state
            elif ch == '[':
                stack.append((currStr, currNum))
                currStr = ""
                currNum = 0

            # Decode current bracket
            elif ch == ']':
                prevStr, num = stack.pop()
                currStr = prevStr + currStr * num

            # Normal character
            else:
                currStr += ch

        return currStr