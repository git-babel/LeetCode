"""
If you divide list in half, one of two is strictly increasing, by description.
If target is in increasing range, recursively search in that one.
Else, search in the other one.
"""

class Solution:
    def _search(self, nums: List[int], target: int, start: int, end: int):
        if end - start < 0:
            return -1

        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1

        pivot = start + (end - start) // 2
        l = nums[start]
        r = nums[end]

        if nums[pivot] == target:
            return pivot
        elif l <= nums[pivot]:
            if nums[pivot] > target and l <= target:
                return self._search(nums, target, start, pivot-1)
            else:
                return self._search(nums, target, pivot+1, end)
            elif nums[pivot] <= r:
                if nums[pivot] < target and r >= target:
                    return self._search(nums, target, pivot+1, end)
            else:
                return self._search(nums, target, start, pivot-1)

    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums,  target, 0, len(nums) - 1)
