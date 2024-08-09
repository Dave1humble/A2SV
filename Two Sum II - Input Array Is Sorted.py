class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers) 
        i = 0
        j = N - 1
        res = []
        while i < j:
            if numbers[i] + numbers[j] == target:
                res.append(i + 1)
                res.append(j + 1)
                break
                
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i +=1
        return res


         
        
