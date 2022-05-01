'''def permute(data, i, length): 
    if i==length: 
        yield (''.join(data))
    else: 
        for j in range(i,length): 
            #swap
            data[i], data[j] = data[j], data[i] 
            yield from permute(data, i+1, length) 
            data[i], data[j] = data[j], data[i]  
  

string = "ABC"
n = len(string) 
data = list(string) 
print(list(permute(data, 0, n)))

str1 = "ABCDefg"
for i in range(len(str1)-1): ##- 1 is (len(s1) - 1) 
    print(str1[i:i+2])       ## +2 is len(s1)'''
class Solution:
    
    def permute(self, data, i, length):
        if i==length:
            yield (''.join(data))
        else:
            for j in range(i, length):
                data[i], data[j] = data[j], data[i]
                yield from self.permute(data, i+1, length)
                data[i], data[j] = data[j], data[i]
                
    def checkInclusion(self, s1, s2):
        s2_combs = []
        for k  in range(len(s2)-(len(s1)-1)):
            s2_combs.append(s2[k:k+len(s1)])
            
        s1_combs = list(self.permute(list(s1),0,len(s1)))
        if len(list(set(s1_combs) & set(s2_combs))) > 0:
            return True
        else:
            return False

print(Solution().checkInclusion("prosperity","properties"))