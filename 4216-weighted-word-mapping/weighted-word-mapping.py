class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result=""
        for word in words:
            sum_word=0
            for char in word:
                sum_word+=weights[ord(char) - ord('a')]
            rem = sum_word % 26
            result += chr(ord('z') - rem)
        return result