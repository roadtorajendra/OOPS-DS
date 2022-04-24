class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = nums[:-k]
        nums2 = nums[-k:]
        nums3 = []
        for i in range(k):
            nums3.insert(0,nums2.pop())
        nums = nums3+nums1
        return nums

    def rotateO1Space(self, nums, k):
        k = k%len(nums) #Mostly returns k

        v = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = v

nums = [1,2,3,4,5,6,7]
k = 3

nums = [-1,-100,3,99]
k = 2
print(Solution().rotate(nums, k))