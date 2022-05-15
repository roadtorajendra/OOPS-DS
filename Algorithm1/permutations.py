##https://medium.com/@guguru/permutation-algorithm-via-backtracking-39fc1bf07a33
class Solution:
    def permute(self, nums):
        return list(self.permutehelper(nums, 0, len(nums)))
        
        
    def permutehelper(self, data, i, length):
        if i == length:
            yield list(data)
        else:
            for j in range(i, length):
                data[i], data[j] = data[j], data[i]
                yield from self.permutehelper(data, i+1, length)
                data[i], data[j] = data[j], data[i]

print(Solution().permute([1,2,3]))