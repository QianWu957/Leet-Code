class Solution:
    def minWindow(self, s: str, t: str) -> str:


        if len(s) < len(t):
            return ''

        
        left, right = 0 ,0 
        start, end = 0, -1
        min_len = len(s)+1
        need = len(t)

        cnt = collections.Counter(t)

        print(cnt)

        for right in range(len(s)):
            ch = s[right]
            if ch in cnt:
                if cnt[ch] > 0:
                    need -=1
                cnt[ch]-=1

            while need == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start, end = left, right

                ch = s[left]
                if ch in cnt:
                    if cnt[ch] >=0:
                        need +=1
                    cnt[ch] +=1
                left +=1
        
        return s[start: end+1]