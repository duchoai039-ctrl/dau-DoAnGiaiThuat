class Solution:
    def countEven(self, num: int) -> int:
        dem = 0
        for i in range(2, num + 1):
            d = 0
            for k in str(i):
                d += int(k)
            if d % 2 == 0:
                dem+=1
        return dem
            
        



        