import bisect


"""
https://leetcode.com/problems/search-insert-position/description/
"""

class Solution(object):
    def searchInsert(self, nums, target):
        # Initialize two pointers for the search boundaries.
        left, right = 0, len(nums) - 1

        # Use binary search to find the insert position.
        while left <= right:
            # Calculate the middle index to compare with the target.
            mid = (left + right) // 2  # Using // for integer division in Python 3.
            # If the middle element is greater than or equal to the target,
            # search the left half including the current middle.
            if nums[mid] >= target:
                right = mid - 1
            # If the middle element is less than the target,
            # search the right half excluding the current middle.
            else:
                left = mid + 1
        # The left pointer will end up at the insert position, so return it.
        return left

    def searchRecursiveInsert(self, nums, target):
        """
        Recursive function for binary search.
        The arguments are:
            left - the left boundary of the current search range.
            right - the right boundary of the current search range.
        """
        def recursive_search(left, right):
            # Base case: if the left index exceeds the right index,
            # target is not found, and the position of insertion will be left.
            if left > right:
                return left

            # Calculate the middle index of the current range.
            mid = (left + right) // 2

            # If the value in the middle equals target, return the index mid.
            if nums[mid] == target:
                return mid
            # If target is less than nums[mid],
            # search the left half by decreasing the right boundary.
            elif target < nums[mid]:
                return recursive_search(left, mid - 1)
            # Otherwise, target is greater than nums[mid],
            # search the right half by increasing the left boundary.
            else:
                return recursive_search(mid + 1, right)

        # Start the recursive binary search on the whole array.
        return recursive_search(0, len(nums) - 1)

    def searchBisectInsert(self, nums, target):
        return bisect.bisect_left(nums, target)

if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5)) # 2
    print(s.searchBisectInsert([1,3,5,6], 5)) # 2
    print(s.searchRecursiveInsert([1,3,5,6], 5)) # 2
    print(s.searchInsert([1,3,5,6], 2)) # 1
    print(s.searchBisectInsert([1,3,5,6], 2)) # 1
    print(s.searchRecursiveInsert([1,3,5,6], 2)) # 1
