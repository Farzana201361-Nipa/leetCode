# Example 1:

# Input: x = 121
# Output: true
# Example 2:

# Input: x = -121
# Output: false
# Example 3:

# Input: x = 10
# Output: false
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_list=list(str(x)) #Coverting the number into a string then type casting it into list
        copy_list=num_list.copy() 
        copy_list.reverse()
        if(copy_list ==num_list):
            return True
        else:
            return False
        
sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))