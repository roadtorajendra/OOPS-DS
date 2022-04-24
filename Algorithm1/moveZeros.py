class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        nums[j:] = [0]*(len(nums)-j)
        return nums

print(Solution().moveZeroes([0,0,1]))

#Fails the [0,0,1] test case
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeros = 0
        i = 0
        for num in nums:
            if num == 0:
                nums.pop(i)
                count_zeros += 1
            i += 1
        nums.extend([0]*count_zeros)'''