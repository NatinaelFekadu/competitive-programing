from collections import Counter, defaultdict


class FrequencyTracker(object):
    def __init__(self) -> None:
        self.frequency = Counter()
        self.frequency_counter = Counter()
        
    def add(self, number):
        self.frequency[number] += 1
        self.frequency_counter[self.frequency[number]] += 1
        self.frequency_counter[self.frequency[number] - 1] -= 1
        
    def deleteOne(self, number):
        if self.frequency[number]:
            self.frequency[number] -= 1
            if self.frequency[number] == 0: 
                del self.frequency[number]
            self.frequency_counter[self.frequency[number]] += 1
            self.frequency_counter[self.frequency[number] + 1] -= 1 

    
    def hasFrequency(self, frequency):
        return self.frequency_counter[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)