class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged = None
        result = []

        for i in range(len(sorted_intervals)):
            interval = sorted_intervals[i]
            if merged is None:
                merged = interval
            else:
                if merged[1] >= interval[0]:
                    merged[1] = max(merged[1], interval[1])
                else:
                    result.append(merged)
                    merged = interval

        if merged is not None:
            result.append(merged)

        return result
