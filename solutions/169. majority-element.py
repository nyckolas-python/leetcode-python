from collections import Counter


class Solution(object):
    """
        https://leetcode.com/problems/majority-element/
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data_count = Counter(nums)
        return max(data_count, key=data_count.get)


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2])) # 2
    print(s.majorityElement([3,2,3])) # 3
