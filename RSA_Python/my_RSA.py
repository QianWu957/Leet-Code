import sys
import math



def select_e(fn):
    list = []
    for e in range(2, fn):
        if math.gcd(e, fn) == 1:
            list.append(e)
    #list.sort()

    return list[2]  # Choose the third smallest coprime


def match_d(e, fn):
    d = 0
    while True:
        if (e * d) % fn == 1:
            return d
        d += 1


# 模N大数的幂乘的快速算法
def fastExpMod(b, e, m):  # 底数，幂，大数N
    result = 1
    e = int(e)
    while e != 0:
        if e % 2 != 0:  # 按位与
            e -= 1
            result = (result * b) % m
            continue
        e >>= 1
        b = (b * b) % m
    return result


def create_keys(p, q):
    n = p * q
    fn = (p - 1)*(q - 1)
    e = select_e(fn)
    d = match_d(e, fn)
    return (n, e, d, fn)


def encrypt_file():
    #input_file = sys.argv[1]
    input_file = "input.txt"
    input_list = []
    with open(input_file, 'r') as filereader:
        for line in filereader:
            input_list.append(line.strip())
    
    i = 0
    while i < len(input_list):
        first_line = input_list[i].split()
        p = int(first_line[0])
        q = int(first_line[1])
        i += 1
        mess = []
        for j in range(5):
            mess.append(int(input_list[i]))
            i += 1

        n, e, d, fn = create_keys(p, q)
        encrypted_list = []
        decrypted_list = []

        for M in mess:
            encrypted_list.append(fastExpMod(M, e, n))

        for C in encrypted_list:
            decrypted_list.append(fastExpMod(C, d, n))
        #print(encrypted_list)
        
        for j in range(5):
            print("p:" , p , ", q:" , q , ", n:" , n , ", phi:" , fn , ", e:" , e , ", d:" , d , ", message:" , mess[j] , ", encrypted:" , encrypted_list[j] , ", decrypted:" , decrypted_list[j])


if __name__ =='__main__':
    encrypt_file()