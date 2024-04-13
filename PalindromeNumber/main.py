class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)[::-1]
        return reverse == str(x)



sol = Solution()

print(sol.isPalindrome(10))