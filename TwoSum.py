class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        sortedNums = sorted(nums)
        sortedIdx = sorted(range(len(nums)), key=lambda k: nums[k])
        
        while(True):
            sum = sortedNums[start] + sortedNums[end]
            if (sum < target):
                start += 1
            elif (sum > target):
                end -= 1
            elif (sum == target):
                return [sortedIdx[start], sortedIdx[end]]
