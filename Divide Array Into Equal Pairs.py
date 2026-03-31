class Solution(object):
    def divideArray(self, nums):
        from collections import Counter
        dem = Counter(nums)
        for i in dem.values():
            if i % 2: #kiem tra xem số đó lẻ hay chẳn
                return False
        return True
       
        