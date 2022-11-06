def maxSubArray(nums: list[int]):
    maxSum = 0
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
        maxSum = max(maxSum, sum)
        if sum < 0:
            sum = 0
    return maxSum


