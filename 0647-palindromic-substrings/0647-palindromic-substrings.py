class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            count += self.checkPalindrome(s, i, i) #even length
            count += self.checkPalindrome(s, i, i+1) #odd length

        return count

    def checkPalindrome(self , s:str , left:int, right:int) ->int:
        count =0
        
        while(left >= 0 and right < len(s) and s[left] == s[right]):

            count += 1
            right += 1
            left -= 1

        return count