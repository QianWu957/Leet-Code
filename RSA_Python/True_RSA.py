import sys

def gcd(x, y):
    if y == 0:
        return x
        
    elif y!=0:
        return gcd(y, x % y)

def get_e(phi):
    phi_list = list(range(2,phi))
    e_list = []
    for e in range(2, len(phi_list)):
        if gcd(e, phi) == 1:
            e_list.append(e)
    return e_list[2]


def get_d(e, phi):
    d = 0
    flag = True
    while flag:
        if (e * d) % phi == 1:
            return d
        d = d + 1

def slow_expmod(i, j, k):
    return pow(i,j) % k


def key_gen(p,q):
    n = p * q
    phi = (p - 1)*(q - 1)
    e = get_e(phi)
    d = get_d(e, phi)
    return (n, e, d, phi)


def execution():
    input_file = sys.argv[1]
    # input_file = "input.txt"
    inputs = []
    # inputs = 0
    with open(input_file, 'r') as filereader:
        for every_line in filereader:
            inputs.append(every_line.strip())
            # print(inputs)
            # print(len(inputs[0]))
            # print(len(inputs[1]))

   

    for i in range(len(inputs)):
        if len(inputs[i]) != 2:
            p, q = inputs[i].split()
            p, q = int(p), int(q)
            # print(p,q)
        else:
            # plain_text = []
            plain_text = int(inputs[i])
            # print(plain_text)

            n, e, d, phi = key_gen(p, q)

            encryption, decryption = [], []

            # for digit in plain_text:
            encryption = slow_expmod(plain_text, e, n)

            # print(encryption)

            # for cipher in encryption:
            decryption = slow_expmod(encryption, d, n)
            # print(decryption)
            
            print("p: " + str(p) + ", q: " + str(q) + ", n: " + str(n) +  ", phi: " + str(phi) + ", e: " + str(e) + ", d: " + str(d) + ", message: " + str(plain_text) + ", encrypted: " + str(encryption) + ", decrypted: " + str(decryption))


execution()






