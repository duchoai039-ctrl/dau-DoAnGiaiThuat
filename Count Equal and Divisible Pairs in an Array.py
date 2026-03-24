class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dem = 0
        n = len(nums)

        for i in range(n - 1): #duyet mang nguoc
            for j in range(i + 1, n): #duyet mang tu i cho den het
                if (i * j) % k == 0 and nums[i] == nums[j]: #neu thoa dieu kien thi + 1 vao dem
                    dem+=1
        return dem
        

      

  