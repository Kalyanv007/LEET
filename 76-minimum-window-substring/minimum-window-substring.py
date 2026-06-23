class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hash_map = [0] * 256

        for ch in t:
            hash_map[ord(ch)] += 1

        l = 0
        r = 0

        cnt = 0
        minLen = float('inf')
        startIndex = -1

        n = len(s)
        m = len(t)

        while r < n:

            if hash_map[ord(s[r])] > 0:
                cnt += 1

            hash_map[ord(s[r])] -= 1

            while cnt == m:

                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    startIndex = l

                hash_map[ord(s[l])] += 1

                if hash_map[ord(s[l])] > 0:
                    cnt -= 1

                l += 1

            r += 1

        if startIndex == -1:
            return ""

        return s[startIndex:startIndex + minLen]