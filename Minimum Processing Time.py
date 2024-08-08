class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(processorTime)
        processorTime.sort()
        tasks.sort(reverse=True)
        maxx = 0
        for i in range(n):
            maxx = max(maxx, processorTime[i] + max(tasks[i*4:i*4 + 4]))
        return maxx
