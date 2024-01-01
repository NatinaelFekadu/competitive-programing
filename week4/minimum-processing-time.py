class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        i = 3
        max_times = []
        for time in processorTime:
            max_times.append(time + tasks[i])
            i += 4
        return max(max_times)