"""
Maybe optimal, which is O(n^2), but too complex and redundant.
Just choose target, and shrink boundaries one by one, starting from both edges.
"""
class Solution:
    def sortedTwoSum(self, nums: List[int], target: int) -> List[int]:
        waitings = {}
        result = []

        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in waitings and waitings[nums[i]]:
                result.append([complement, nums[i]])
                waitings[nums[i]] = False
            elif nums[i] not in waitings:
                waitings[complement] = True

        return result


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)

        prev = None
        for i in range(len(sorted_nums)):
            if sorted_nums[i] >= 0:
                break

            if sorted_nums[i] == prev:
                continue

            target = sorted_nums[i]
            twosum_result = self.sortedTwoSum(sorted_nums[i+1:], target*-1)
            result += [[target] + l for l in twosum_result]
            prev = sorted_nums[i]

        if sorted_nums.count(0) >= 3:
            result.append([0, 0, 0])

        return result
