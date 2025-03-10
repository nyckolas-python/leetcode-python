class Solution(object):
    """
        https://leetcode.com/problems/valid-palindrome/
    """
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ''.join([char.lower() for char in s if char.isalnum()])

        return s1[::-1] == s1


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama")) # True
    print(s.isPalindrome("race a car")) # False
    print(s.isPalindrome(" ")) # True
