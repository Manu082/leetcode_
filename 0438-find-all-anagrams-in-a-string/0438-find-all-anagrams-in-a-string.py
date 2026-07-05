class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p) 
        res = []

        if n < k:
            return res

        pMap = {}
        sMap = {}

        for c in p:
            pMap[c] = pMap.get(c , 0) + 1 

        left = 0
        count = k

        for right in range(n):
            ch = s[right] 

            sMap[ch] = sMap.get(ch , 0) + 1 

            if ch in pMap and sMap[ch] <= pMap[ch]:
                count -= 1

            if right - left + 1 > k:
                leftch = s[left]

                if leftch in pMap and sMap[leftch] <= pMap[leftch]:
                    count += 1

                sMap[leftch] -= 1
                left += 1

            if count == 0:
                res.append(left)

        return res  