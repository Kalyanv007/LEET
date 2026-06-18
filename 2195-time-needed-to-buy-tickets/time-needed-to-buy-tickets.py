class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        for i in range(len(tickets)):
            if i<=k:
                time+=min(tickets[i],tickets[k]) #for before k
            else:
                time+=min(tickets[i],tickets[k]-1)#for after k
        return time