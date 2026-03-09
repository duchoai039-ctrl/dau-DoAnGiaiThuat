class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        b = numBottles
        n = numExchange

        return b + (b - 1) // (n - 1)