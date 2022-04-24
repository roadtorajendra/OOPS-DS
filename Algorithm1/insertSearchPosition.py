class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        middle = (start+end)//2
        #print(start, end, middle)

        while not(nums[middle] == target) and start <= end and middle >= 0:
            if nums[middle] < target:
                start = middle+1
            else:
                end = middle-1
            middle = (start+end)//2
            #print(start, end, middle)
        if nums[middle] >= target and middle >= 0:
            return middle
        else:
            return middle+1

custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(Solution().searchInsert(custArray, 16))

custArray = [1, 3, 5, 6]
print(Solution().searchInsert(custArray, 0))

custArray = [1, 3]
print(Solution().searchInsert(custArray, 4))