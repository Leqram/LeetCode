from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

sol = Solution()

nums = [3,2,2,3]
val = 3
print(sol.removeElement(nums=nums, val=val))