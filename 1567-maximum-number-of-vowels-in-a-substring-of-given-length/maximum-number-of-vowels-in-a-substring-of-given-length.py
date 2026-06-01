class Solution:

    def is_vowel(self, ch):
        return ch.lower() in "aeiou"

    def maxVowels(self, s: str, k: int) -> int:

        n = len(s)

        count = 0

        # First window
        for i in range(k):
            if self.is_vowel(s[i]):
                count += 1

        maxCount = count

        i = 0
        j = k

        while j < n:

            # Remove left character
            if self.is_vowel(s[i]):
                count -= 1

            # Add right character
            if self.is_vowel(s[j]):
                count += 1

            maxCount = max(maxCount, count)

            i += 1
            j += 1

        return maxCount