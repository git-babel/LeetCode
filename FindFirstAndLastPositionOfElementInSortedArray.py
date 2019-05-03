class Solution:
    def getFirstIndexOf(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        pivot = (end - start) // 2
        candidate = -1

        while end > start:
            if nums[pivot] == target:
                candidate = pivot

            if nums[pivot] >= target:
                end = pivot - 1
            else:
                start = pivot + 1

            pivot = start + (end - start) // 2

        if nums[start] == target:
            candidate = start

        return candidate


    def getLastIndexOf(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        pivot = (end - start) // 2
        candidate = -1

        while end > start:
            if nums[pivot] == target:
                candidate = pivot

            if nums[pivot] <= target:
                start = pivot + 1
            else:
                end = pivot - 1

            pivot = start + (end - start) // 2

        if nums[start] == target:
            candidate = start

        return candidate


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1, -1]

        firstIdx = self.getFirstIndexOf(nums, target)
        lastIdx = self.getLastIndexOf(nums, target)

        return [firstIdx, lastIdx]
