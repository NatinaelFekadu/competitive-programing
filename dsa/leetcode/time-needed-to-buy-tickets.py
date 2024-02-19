class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        ticket = tickets[k]
        count = 0
        for i, val in enumerate(tickets):
            if i > k and val >= ticket:
                count += 1
            if val >= ticket:
                time_taken += ticket
            else:
                time_taken += val
        return time_taken - count