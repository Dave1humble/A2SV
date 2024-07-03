class Solution:
  def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    for num in range(left, right + 1):
        is_covered = False
        for start, end in ranges:
            if start <= num <= end:
                is_covered = True
                break  

        if not is_covered:
            return False

    return True
