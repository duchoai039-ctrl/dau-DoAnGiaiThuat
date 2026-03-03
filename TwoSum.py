class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in pos:
                return (pos[need], i)
            pos[nums[i]] = i
        