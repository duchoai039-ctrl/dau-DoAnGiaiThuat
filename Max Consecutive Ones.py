class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        kq = 0
        dem = 0

        for i in nums:
            if i == 0:
                dem = 0
            else:
                dem +=1
            if kq < dem:
                kq = dem
        return kq