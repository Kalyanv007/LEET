class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to count frequency of characters in current window
        freq = {}

        # Left pointer of sliding window
        left = 0

        # Stores max frequency of any char in current window
        max_freq = 0

        # Stores result
        max_len = 0

        # Traverse through each character with right pointer
        for right in range(len(s)):

            # Increase frequency of current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update the max frequency in current window
            max_freq = max(max_freq, freq[s[right]])

            # If window is invalid (more than k replacements)
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update max_len with current valid window size
            max_len = max(max_len, right - left + 1)

        return max_len