class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = {}
        for i, x in enumerate(arr2):
            hash_map[x] = i
       
        def custom_sort_key(x):
            position = hash_map.get(x, len(arr2))
           
            return (position, x)
        
        arr1.sort(key=custom_sort_key)
        return arr1
