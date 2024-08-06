class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            sorted_= sorted(str(num))
            for i in range(len(sorted_)):
                if sorted_[i] != '0':
                    sorted_[0], sorted_[i] = sorted_[i], sorted_[0]
                    break
            return int(''.join(sorted_))
        if num < 0:
            sorted_ = sorted(str(num)[1:], reverse=True)
            return -int(''.join(sorted_))
