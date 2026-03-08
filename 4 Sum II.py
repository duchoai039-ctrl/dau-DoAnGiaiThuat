class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = {}

        for a in nums1:
            for b in nums2:
                s = a + b
                count[s] = count.get(s, 0) + 1

        result = 0

        for c in nums3:
            for d in nums4:
                result += count.get(-(c + d), 0)

        return result