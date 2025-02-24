class Solution(object):
    """
        https://leetcode.com/problems/add-binary/description/
    """
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), 'b')
        # return bin(int(a, 2) + int(b, 2))[2:]