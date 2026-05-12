class Solution(object):
    def findClosestNumber(self, nums: List[int]) -> int:
        kq = nums[0]
        for i in nums:
            if abs(i) < abs(kq):
                kq = i
            elif abs(i) == abs(kq):
                kq = max(kq, i)  # cùng khoảng cách → lấy số lớn hơn
        return kq
        