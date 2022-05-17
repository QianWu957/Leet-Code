class Solution:
    def twoSum(self, numbers, target: int):
        if not numbers: return []
        head, tail = 0, len (numbers)-1

        while head < tail:
            sum = numbers[head] + numbers[tail]

            if sum < target:
                head += 1

            elif sum > target:
                tail -= 1
        
            else:
                return [head+1, tail+1]
        return []


if __name__ == '__main__':
    a = Solution()
    nulist = [1,2,7,45]
    t = 9
    print(a.twoSum(nulist, t))
