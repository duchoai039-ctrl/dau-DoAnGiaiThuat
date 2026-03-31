class Solution(object):
    def findDifference(self, nums1, nums2):
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
        #ép thành kiểu set để trừ ra kí tự khác nhau rồi ép lại thành kiểu list đẻ in ra

        