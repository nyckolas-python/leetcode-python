class Solution(object):
    """
        https://leetcode.com/problems/plus-one/description/
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        remainder = 1
        for i, digit in enumerate(digits[::-1]):
            new_digit = (digit + remainder) % 10
            remainder = (digit + remainder) // 10
            result.insert(0, new_digit)

        if remainder:
            result.insert(0, remainder)

        return result


s = Solution()
print(s.plusOne([1,2,3])) # [1,2,4]
print(s.plusOne([4,3,2,1])) # [4,3,2,2]
print(s.plusOne([9])) # [1,0]
