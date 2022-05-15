class Solution:
    def rob(self, nums, currentIndex=0, tempDict={}) -> int:
        if currentIndex >= len(nums):
            return 0
        else:
            if currentIndex not in tempDict:
                stealFirstHouse = nums[currentIndex] + self.rob(nums, currentIndex+2, tempDict)
                skipFirstHouse = self.rob(nums, currentIndex+1, tempDict)
                tempDict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return tempDict[currentIndex]

print(Solution().rob([2,7,9,3,1]))