class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            max_index = arr.index(max(arr[:size]))
            if max_index != size - 1:
                if max_index != 0:
                    arr[:max_index + 1] = reversed(arr[:max_index + 1])
                    result.append(max_index + 1)
            
                arr[:size] = reversed(arr[:size])
                result.append(size)
        
        return result
