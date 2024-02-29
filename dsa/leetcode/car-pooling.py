class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        minHeap = []
        currPass = 0
        for passengers, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                currPass -= minHeap[0][1]
                heapq.heappop(minHeap)
            currPass += passengers
            if currPass > capacity:
                return False
            heapq.heappush(minHeap, [end, passengers])
        return True