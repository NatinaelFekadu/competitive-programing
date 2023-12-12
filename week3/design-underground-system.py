class UndergroundSystem:

    def __init__(self):
        self.time = {}
        self.checked_in_customers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in_customers[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.checked_in_customers.pop(id)
        travel = (start_station, stationName)
        time = t - check_in_time

        if travel in self.time:
            travel_time, count = self.time[travel]
            self.time[travel] = (time+travel_time,count+1)
        else:
            self.time[(travel)] = (time,1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation,endStation)
        total_time, count = self.time[travel]
        return total_time/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checked_in_customers(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)