from typing import List


def is_valid_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    return True


# def triangleNumber(nums: List[int]) -> int:
#     # N^3 solution
#     sum = 0
#     for i in range(len(nums)-2):
#         for j in range(i+1, len(nums) - 1):
#             for k in range(j+1, len(nums)):
#                 # print(f"{nums[i]}-{nums[j]}-{nums[k]}")
#                 if is_valid_triangle(nums[i], nums[j], nums[k]):
#                     sum += 1
#     return sum

def triangleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums = sorted(nums)

    for i in range(len(n), )


print(triangleNumber([4, 2, 3, 4]))
