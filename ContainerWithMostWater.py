class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:
            curr_area = (end - start) * min(height[start], height[end])
            max_area = max(max_area, curr_area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area
