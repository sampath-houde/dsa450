import math


def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    for i in range(m):
        nums1.pop()
    for i in range(n):
        nums1.append(nums2[i])
    gap1Times = 0
    gap = math.ceil(len(nums1) / 2)

    while gap > 0:
        p1 = 0
        p2 = gap + p1
        while p2 < len(nums1):
            if nums1[p1] >= nums1[p2]:
                temp = nums1[p1]
                nums1[p1] = nums1[p2]
                nums1[p2] = temp
            p1 = p1 + 1
            p2 = p2 + 1
        if gap == 1:
            gap1Times = gap1Times + 1
        if gap1Times > 2:
            gap = 0
        gap = math.ceil(gap/2)


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

"""
[1,2,3,2,5,6]
"""
