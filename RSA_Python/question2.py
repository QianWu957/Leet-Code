res = [0] * 3
# print(res)

# for i in range(len(alpha)):
#     if alpha[i] 

names = ["ab","cd","abcdefg"]
snames = []
for i in range(len(names)):
    snames.append(list(names[i]))

# print(snames)
friends = ["adfdab", "cdfaeb","dkjlifg"]
sfriends = []
for i in range(len(friends)):
    sfriends.append(list(friends[i]))
print(sfriends)

readout = [[0]*2 for _ in range(3)]
# print(readout) 

for i in range(len(readout)):
    readout[i] = [snames[i], sfriends[i]]

print(readout)


res = [0] * 3

hashmap = {}
print(readout[0][0])
for i in range(len(readout)):
    hashmap[readout[i][1]] = 1
    print(hashmap)
    if readout[i][0] in hashmap:
        # res[i] = 1
        print("TRUE")
    else:
        res[i] = 0
print(res)

    

    

