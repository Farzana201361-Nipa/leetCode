from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts =Counter(nums)
        for num, count in counts.items():
            if count == 1:
                return num

sol= Solution()
print(sol.singleNumber([2,2,1]))
print(sol.singleNumber([4,1,2,1,2]))
print(sol.singleNumber([1]))