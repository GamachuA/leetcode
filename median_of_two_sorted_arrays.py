# Given two sorted arrays nums1 and nums2 of sizes m and n respectively,
# return the median of the two sorted arrays.
# The overall time complexity must be O(log (m+n)).
# The arrays are individually sorted in non-decreasing order.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for efficient binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while left <= right:
            mid1 = (left + right) // 2        # partition for nums1
            mid2 = half - mid1                # partition for nums2

            left1  = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            right1 = nums1[mid1]     if mid1 < m else float('inf')

            left2  = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            right2 = nums2[mid2]     if mid2 < n else float('inf')

            # Correct partition found
            if left1 <= right2 and left2 <= right1:
                # Odd total length → median is the middle element
                if total % 2:
                    return min(right1, right2)
                # Even → average of two middle values
                return (max(left1, left2) + min(right1, right2)) / 2

            # Move binary search window
            elif left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1

