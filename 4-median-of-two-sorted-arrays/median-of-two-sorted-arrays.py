class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        sLength = n + m
        i = 0
        j = 0

        med_ind = sLength // 2
        even = (sLength % 2 == 0)

        element = 0
        prev = 0

        while i + j <= med_ind:

            prev = element

            if i < n and (j >= m or nums1[i] <= nums2[j]):
                element = nums1[i]
                i += 1
            else:
                element = nums2[j]
                j += 1

        if even:
            return (prev + element) / 2
        else:
            return element