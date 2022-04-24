#Use list as stack to store the second half of the digits, pop to compare with the first half of the digits.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = 0
        while x >= 10**digits:
            digits += 1
        
        store = []
        for i in range(digits//2):
            store.append(x % 10)
            x = x//10
        
        if digits%2 == 1:
            x = x // 10
        for i in range(digits//2):
            pop = store[-1]
            store = store[:-1]
            if pop != x % 10:
                return False
            x = x//10
        return True
    
    def isPalindromeStr(self, x):
        return str(x) == str(x)[::-1]
        #the slice statement [::-1] means start at the end of the string 
        #and end at position 0, move with the step -1, negative one, which means one step backwards.

    def IsPalindrome(self, x):
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        else:
            revertedNumber = 0
            while x > revertedNumber:
                #print(x, revertedNumber)
                revertedNumber = revertedNumber * 10 + x%10
                x = x//10
                #print(x, revertedNumber)
            return x == revertedNumber or x == revertedNumber//10


sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindromeStr(121))
print(sol.IsPalindrome(1221))

'''First of all we should take care of some edge cases. All negative numbers are not palindrome, for example: -123 is not a 
palindrome since the '-' does not equal to '3'. So we can return false for all negative numbers.
Now let's think about how to revert the last half of the number. For number 1221, if we do 1221 % 10, we get the last digit 1, 
to get the second to the last digit, we need to remove the last digit from 1221, we could do so by dividing it by 10, 1221 / 10 = 122. Then we can get the last digit again by doing a modulus by 10, 122 % 10 = 2, and if we multiply the last digit by 10 and add the second last digit, 1 * 10 + 2 = 12, it gives us the reverted number we want. Continuing this process would give us the reverted number with more digits.
Now the question is, how do we know that we've reached the half of the number?
Since we divided the number by 10, and multiplied the reversed number by 10, when the original number is less than the reversed 
number, it means we've processed half of the number digits.
'''
