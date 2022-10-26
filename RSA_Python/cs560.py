
import sys
import math

def fastExpMod(a, e, m):  
    result = 1
    e = int(e)
    while e != 0:
        if e % 2 != 0: 
            e -= 1
            result = (result * a) % m
            continue
        e >>= 1
        a = (a * a) % m
    return result




def computeE(fn):
    collection_ = list(range(2,fn))
    for i in range(2, len(collection_)):
        if math.gcd(i, fn) == 1:
            collection_.append(i)
            print(collection_)
    return collection_[2]

def compute_d(e, fn):
    d = 0
    exist = True
    while exist:
        if (e * d) % fn == 1:
            return d
        d += 1

def create_keys(p,q):
    n = p * q
    fn = (p - 1)*(q - 1)
    e = computeE(fn)
    d = compute_d(e, fn)
    return (n, e, d, fn)


def encrypt_file():
    # read_file = sys.argv[1]
    read_file = input.txt
    content = []
    with open (read_file, 'r') as filereader:
        for row in filereader:
            content.append(row.strip())

    for i in range(len(content)):
        if len(content[i]) > 2:
            p,q = content[i].split()
            p, q = int(p), int(q)
            print(p,q)
        else:
      
            message = int(content[i])

            n, e, d, fn = create_keys(p, q)

            cipher, decipher = [], []

            cipher, decipher = fastExpMod(message, e, n), fastExpMod(cipher, d, n)

            print("p:" , p , ", q:" , q , ", n:" , n , ", phi:" , fn , ", e:" , e , ", d:" , d , ", message:" , message , ", encrypted:" , cipher , ", decrypted:" , decipher)



encrypt_file()



    