class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        freq = {}
        for i in hand:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1

        sorted_hand = sorted(hand)

        for i in sorted_hand:
            count = freq[i]
            if count == 0: 
                continue
            else:
                for j in range(groupSize):
                    card = i+j
                    if card not in freq or freq[card] < count:
                        return False
                        
                    freq[card] -= count

        return True