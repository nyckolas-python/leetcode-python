import math


class Solution(object):
    """
        https://leetcode.com/problems/sqrtx/
    """
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.floor(math.sqrt(x)))

    def mySqrtBabylonianMethod(self, x: int) -> int:
        if x == 0:
            return 0

        r = x
        while r * r > x:
            r = (r + x // r) // 2

        return r

    def mySqrtBinarySearch(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right, ans = 0, x, 0
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
