class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        max_index = {s[i]:i for i in range(len(s))}
        end = start = 0
        res = []
        for i in range(len(s)):
            end = max(end,max_index[s[i]])
            if end == i:
                res.append(end-start+1)
                start = end+1
        
        return res
       