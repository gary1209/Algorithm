"""
Description:
Given an integer array, sort it in ascending order in place.
Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

Example1:
Input: [3, 2, 1, 4, 5]
Output: [1, 2, 3, 4, 5]

Example2:
Input: [2, 3, 1]
Output: [1, 2, 3]
"""

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        if not A:
            return

        self.quick_sort(A, 0, len(A) - 1)
        return
    
    def quick_sort(self, A, start, end):
        # you can choose pivot randomly
        if start >= end:
            return

        pivot = A[start]
        left = start
        right = end
        while left <= end:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)