class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        def backtracking(s, flag, ip):
            
            if flag == 4 and s == '':
                self.res.append(ip[:-1])
                return

            for i in range(1,4):
                if i > len(s): 
                    continue
                if int(s[:i])< 256:
                    backtracking(s[i:], flag+1 , ip+s[:i]+'.')
                if s[0] == '0':
                    break
        backtracking(s, 0 , '')
        return self.res
