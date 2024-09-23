#Solution using dictionary
class Solution:
    def twoSum(self, nums:list[int],target: int)-> list[int]:
        visited={}
        for index in range(0, len(nums)):
            number = nums[index]
            if target- number in visited:
                return[visited[target-number],index]
            visited[number] = index
sol= Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([3,2,4],6))
print(sol.twoSum([3,3],6))
    
    
