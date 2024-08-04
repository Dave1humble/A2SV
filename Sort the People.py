class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = list(zip(heights, names))
        combined.sort(reverse=True, key=lambda x: x[0])
        res = []
        for height, name in combined:
            res.append(name)
        return res
