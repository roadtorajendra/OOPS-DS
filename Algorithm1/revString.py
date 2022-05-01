class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        rev_list = []
        for word in s_list:
            word = list(word)
            for i in range(len(word)//2):
                word[i], word[-i-1] = word[-i-1], word[i]
            word = ''.join(word)
            rev_list.append(word)
        s = ' '.join(rev_list)
        return s

    def reverseOneLiner(self, s):
        return " ".join(word[::-1] for word in s.split())

    def reverseWordFastest(self, one_word):
        l = 0
        r = len(one_word)-1
        while l < r:
            one_word[l], one_word[r] = one_word[r], one_word[l]
            l,r = l+1,r-1

s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))