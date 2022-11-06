def sort01s(nums: list[int]) -> None:
    c0 = c1 = c2 = 0
    for i in nums:
        if i == 0:
            c0 = c0 + 1
        elif i == 1:
            c1 = c1 + 1
        else:
            c2 = c2 + 1
    ans = []
    for i in range(c0):
        ans.append(0)
    for i in range(c1):
        ans.append(1)
    for i in range(c2):
        ans.append(2)
    nums.clear()
    for i in ans:
        nums.append(i)

sort01s([2, 0, 2, 1, 1, 0])
