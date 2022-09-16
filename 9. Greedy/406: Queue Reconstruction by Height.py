class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        if not people:
            return 0
        res = []
        people.sort(key = lambda x:(-x[0],x[1]))
        print(people)

        for i in people:
            res.insert(i[1],i)
        
        return res