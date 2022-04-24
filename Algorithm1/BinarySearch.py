import math


class Solution:
    def BinarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        middle = math.floor((start+end)/2)
        while not(nums[middle] == target) and start <= end:
            if nums[middle] < target:
                start = middle+1
            else:
                end = middle - 1
            middle = math.floor((start+end)/2)
        if nums[middle] == target:
            return middle
        else:
            return -1 

custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(Solution().BinarySearch(custArray, 15))

