class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

RUNNER = Solution()
print(RUNNER.isPalindrome(121))
print(RUNNER.isPalindrome(123))
