
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = 0
        for num in nums:
            counts = counts ^ num
        return counts

sol= Solution()
print(sol.singleNumber([2,2,1]))
print(sol.singleNumber([4,1,2,1,2]))
print(sol.singleNumber([1]))