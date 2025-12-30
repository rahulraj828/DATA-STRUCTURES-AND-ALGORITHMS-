class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged_list = []
        inserted = False

        for interval in intervals:
            if not inserted and newInterval[0] < interval[0]:
                merged_list.append(newInterval)
                inserted = True
            merged_list.append(interval)

        if not inserted:
            merged_list.append(newInterval)

        # Phase 2: Merge intervals
        res = []
        start, end = merged_list[0]

        for i in range(1, len(merged_list)):
            curr_start, curr_end = merged_list[i]

            if curr_start <= end:
                end = max(end, curr_end)
            else:
                res.append([start, end])
                start, end = curr_start, curr_end

        res.append([start, end])
        return res