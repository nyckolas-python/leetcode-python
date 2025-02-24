class Solution(object):
    """
    https://leetcode.com/problems/plus-one/description/
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])


s = Solution()
print(s.lengthOfLastWord("Hello World")) # 5
print(s.lengthOfLastWord("   fly me   to   the moon  ")) # 4
print(s.lengthOfLastWord("luffy is still joyboy")) # 6
