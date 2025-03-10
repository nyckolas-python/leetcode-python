class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        for el in t:
            if el == s[count]:
                count += 1
        return count == len(s)


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc")) # True
    print(s.isSubsequence("axc", "ahbgdc")) # False
