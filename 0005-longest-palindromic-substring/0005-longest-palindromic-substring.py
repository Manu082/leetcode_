class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        end = 0

        for i in range(n):
            odd =  self.checkPalindrome(s, i, i)
            even = self.checkPalindrome(s, i, i+1)
            odd_even = max(odd , even)

            if (odd_even  >(end - start)):
                start = i - (odd_even -1) // 2
                end = i + odd_even // 2

        return s[start:end + 1]

    def checkPalindrome (self, s:str, left:int , right:int)-> int:
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1

        return right - left - 1