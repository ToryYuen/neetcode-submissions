class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l, r = m - 1, n - 1

        for i in range(len(nums1) - 1, -1, -1):
            if l == -1:
                nums1[i] = nums2[r]
                r -= 1
            elif r == -1:
                nums1[i] = nums1[l]
                l -= 1
            elif nums1[l] >= nums2[r]:
                nums1[i] = nums1[l]
                l -= 1
            else:
                nums1[i] = nums2[r]
                r -= 1
        