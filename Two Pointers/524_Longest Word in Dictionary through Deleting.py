class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        if not s or not dictionary: return ''
        S = ''
        for _s in dictionary:
            p2 = 0
            for p1 in range (len(s)):
                if p2 <len(_s) and _s[p2] == s[p1]:
                    p2+=1
                    continue
            if p2 == len(_s) and not S:
                S = _s
            elif p2 == len(_s):
                if len(S) > len(_s):
                    continue
                elif len(S) < len(_s):
                    S = _s
                elif S < _s:
                    continue
                else: S =_s        

        return S        

if '__name__' == '__main__':
    a = Solution()
    input = 'abpcplea'
    d = ["ale","apple","monkey","plea"]
    print(a.findLongestWord(input,d))
                     





            






        