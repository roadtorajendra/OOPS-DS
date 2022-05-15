class Solution:
    def letterCasePermutation(self, s):
        #a = [s.lower(), s.upper(),s]
        #a = []
        #for i in range(len(s)):
        #    kk = list(self.permute(list(s.lower()),i))
        #    ll = list(self.permute(list(s.upper()),i))
            #print(s[i])
        #    a = a+kk+ll
        #    print(a)
            #print(i)
        #return list(set(a))
        #return list(set(list(self.permute(list(s)))+[s.upper()]+[s.lower()]+[s])
        results = []
        self.helper(results, s, "", 0)
        return results
        
    def helper(self, results, s, permutation, start):
        if len(permutation) == len(s):
            results.append(permutation)
            return

        if s[start].isalpha():
            self.helper(results, s, permutation+s[start].upper(), start+1)
            self.helper(results, s, permutation+s[start].lower(), start+1)
        else:
            self.helper(results, s, permutation+s[start], start+1)

    def permute(self, s, i):
        if type(s[i]) is not int and s[i].lower():
            s[i] = s[i].upper()
            yield (''.join(s))
        if type(s[i]) is not int and s[i].upper():
            s[i] = s[i].lower()
            yield (''.join(s))     

print(Solution().letterCasePermutation("dnTJ"))