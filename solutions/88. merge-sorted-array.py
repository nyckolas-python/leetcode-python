class Solution(object):
    """
        https://leetcode.com/problems/merge-sorted-array/
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


if __name__ == "__main__":
    s = Solution()
    print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)) # [1,2,2,3,5,6]
    print(s.merge([1], 1, [], 0)) # [1]
    print(s.merge([0], 0, [1], 1)) # [1]
    print(s.merge([2,0], 1, [1], 1)) # [1,2]
