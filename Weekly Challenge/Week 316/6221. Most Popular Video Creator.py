class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        # t = [max_view, view, id]
        hashmap = {}
        max_view = 0

        for name, id, view in zip(creators, ids, views):
            t = hashmap[name]
            t[0] +=view
            if t[0] < t[1] or t[0] == t[1] and id < t[2]:
                t[1] , t[2] = view, id
            else:
                hashmap[name] = [view, view, id]
            
            max_view = max(max_view, hashmap[name][0])

        res = []
        for name, (max_view1, view, id) in hashmap:
            if max_view1 == max_view:
                res.append([name, id])
        
        return res

