import time
from typing import List
import math


def binary_search(n, nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (right + left) // 2
        print(f"inner {left=}, {right=},{mid=},{nums[mid]=}")
        if nums[mid] < n:
            left = mid + 1
        else:
            right = mid
    return left


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) + len(nums2) < 4:
            res = sorted(nums1 + nums2)
            if len(res) % 2 == 1:
                return res[len(res) // 2]
            else:
                return (res[len(res) // 2 - 1] + res[len(res) // 2]) / 2
        if len(nums1) == 0:
            nums1 = nums2[-2:]
            nums2.pop()
            nums2.pop()
        if len(nums2) == 0:
            nums2 = nums1[-2:]
            nums1.pop()
            nums1.pop()
        print(f"{nums1=}, {nums2=}")

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        left, right = 0, len(nums1) - 1
        while left < right:
            mid = (right + left) // 2
            print(f"outer {left=}, {right=},{mid=},{nums1[mid]=}")
            idx = binary_search(nums1[mid], nums2)
            print(f"returned {idx=}, {nums2[idx]=}")
            if nums2[idx] > nums1[mid]:
                idx -= 1
                print(f"new {idx=}, {nums2[idx]=}")

            to_the_left = mid + idx + 1 + 1
            to_the_right = len(nums1) + len(nums2) - mid - idx - 1 - 1
            print(f"{to_the_left=}, {to_the_right=}")
            if (len(nums1) + len(nums2)) % 2 == 0:

                if to_the_left == to_the_right:
                    if len(nums2) > 1:
                        print(sorted(nums1[mid : mid + 2] + nums2[idx : idx + 2]))
                        a, b = sorted(nums1[mid : mid + 2] + nums2[idx : idx + 2])[1:3]

                        result = (a + b) / 2
                        print(result)
                        return result
                    else:
                        a, b = sorted(nums1[mid : mid + 2] + nums2[idx : idx + 2])[0:2]

                        result = (a + b) / 2
                        print(result)
                        return result

                if to_the_left == to_the_right + 2:
                    # print(nums1, nums2, f"{mid=} {idx=}")
                    # print(nums1[max(mid - 1, 0) : mid + 1])
                    # print(nums2[max(idx - 1, 0) : idx + 1])
                    # print(
                    #     sorted(
                    #         nums1[max(mid - 1, 0) : mid + 1]
                    #         + nums2[max(idx - 1, 0) : idx + 1]
                    #     )[-2:]
                    # )
                    a, b = sorted(
                        nums1[max(mid - 1, 0) : mid + 1]
                        + nums2[max(idx - 1, 0) : idx + 1]
                    )[-2:]
                    result = (a + b) / 2
                    print(result, f"aaa {a=}{b=}")
                    return result

                if to_the_left + 2 == to_the_right:
                    a, b = sorted(nums1[mid + 1 : mid + 3] + nums2[idx + 1 : idx + 3])[
                        :2
                    ]
                    result = (a + b) / 2
                    print(result, f"bbb {a=}{b=}")
                    return result

                elif to_the_left > to_the_right:
                    right = mid
                else:
                    left = mid + 1
            else:
                if to_the_left == to_the_right + 1:
                    result = max(nums1[mid], nums2[idx])
                    print(result)
                    return result
                if to_the_left + 1 == to_the_right:
                    result = min(nums1[mid + 1], nums2[idx + 1])
                    print(result)
                    return result
                elif to_the_left > to_the_right + 1:
                    right = mid
                else:
                    left = mid + 1
            print(f"{left=}, {right=}")
        return left


s = Solution()
assert (
    s.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 8
)
assert (
    s.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 7.5
)
assert s.findMedianSortedArrays([], [1, 2, 3, 4]) == 2.5
assert s.findMedianSortedArrays([1, 3], [2]) == 2
assert s.findMedianSortedArrays([], [2, 3]) == 2.5
assert s.findMedianSortedArrays([1, 2, 3, 4, 5], []) == 3

assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert s.findMedianSortedArrays([0, 0], [0, 0]) == 0
assert s.findMedianSortedArrays([], [0]) == 0
assert s.findMedianSortedArrays([2], []) == 2
assert s.findMedianSortedArrays([3], [1, 2, 4]) == 2.5
