class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        freq = {}
        for num in hand:
           freq[num]=freq.get(num,0)+1

        # Form groups
        for card in hand:

            if freq[card] == 0:
                continue

            for x in range(card, card + groupSize):

                if x not in freq or freq[x] == 0:   #after building a hashmap of how many elements are there check if a group of the groupsize can be formed from the smallest still remaining element in the map to check for consecutiveness 
                    return False 

                freq[x] -= 1

        return True