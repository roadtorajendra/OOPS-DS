#1 2 3 4 5 6 7 8 9
# G G G G G G B B B 

class Solution:

    def isBadVersion(self, index_list):
        num = 'GGGGGGBBB'
        return num[index_list] == 'B'

    def firstBadVersion(self, n):
        left, right = 0, n

        while left < right:
            mid = (left+right)//2

            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid+1

        if self.isBadVersion(right):
            return right

        return -1

print(Solution().firstBadVersion(9))

