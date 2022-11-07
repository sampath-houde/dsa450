def merge(intervals: list[list[int]]) -> list[list[int]]:
    ans = []
    if len(intervals) == 1:
        return intervals
    intervals.sort()
    tempInterval = intervals[0]
    start = tempInterval[0]
    end = tempInterval[1]

    temp = []
    for interval in intervals:
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            ans.append([start, end])
            start = interval[0]
            end = interval[1]
    ans.append([start, end])
    return ans


merge([[1, 3], [2, 6], [8, 10], [15, 18]])
