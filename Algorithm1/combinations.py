class Solution:

    def combine(self, n, k, subarrays=[], out=[], i=0):
        A = []
        for a in range(n):
            A.append(a+1)

        if len(A) == 0 or k > len(A):
            return

        if k==0:
            subarrays.append(out)
            return
        
        for j in range(i, len(A)):
            self.combine(n, k-1, subarrays, out+[A[j],],j+1)
        return subarrays

print(Solution().combine(2,1))

'''LC needed subarrays and out as empty list
class Solution:

    def combinehelper(self, n, k, subarrays=[], out=[], i=0):
        A = []
        for a in range(n):
            A.append(a+1)

        if len(A) == 0 or k > len(A):
            return

        if k==0:
            subarrays.append(out)
            return 
        
        for j in range(i, len(A)):
            self.combinehelper(n, k-1, subarrays, out+[A[j],],j+1)
        return subarrays
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combinehelper(n,k,list(),list())
        '''
