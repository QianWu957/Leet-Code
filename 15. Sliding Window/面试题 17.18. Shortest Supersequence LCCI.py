class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:

        if len(small) > len(big):
            return []
        
        cnt = collections.Counter(small)
        print(cnt)

        left, right = 0, 0 
        start, end = 0, -1
        need = len(small)
        min_len = len(big)+1
        # res = []

        for right in range(len(big)):
            ch = big[right]
            if ch in cnt:
                if cnt[ch] > 0:
                    need -=1
                cnt[ch] -=1
            
            while need == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start, end = left, right
                    # res = [left, right]

                ch = big[left]
                if ch in cnt:
                    if cnt[ch] >=0:
                        need +=1
                    cnt[ch] +=1
                
                left +=1

        return [] if (start == 0 and end == -1) else [start, end]




