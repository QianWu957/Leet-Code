def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 拓展的欧几里得算法
def ext_gcd(a, b):

    if b == 0:
        x1 = 1
        y1 = 0
        x = x1
        y = y1
        r = a
        return r, x, y
    else:
        r, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - a // b * y1
        return r, x, y


# 生成公钥私钥
def get_key(p, q):
    n = p * q
    fyn = (p - 1) * (q - 1)

    # 此处抱着e与fyn互素，并且得到的x要大于0
    e = fyn      # 初始化e
    while e > 1 :
        e -= 1
        r, x, y, = ext_gcd(e, fyn)  # 传入fn和e到ext_gcd()中，得到d
        if (gcd(e, fyn) == 1) & (x > 0):
            break
    # d*e%
    d = x              # 扩展的欧几里得算法中得到的x就是e的逆元
    print(n)
    print(fyn)
    return (n, e), (n, d)


# 加密
def encryption(x, pubkey):
    n = pubkey[0]
    e = pubkey[1]
    y = x ** e % n   # 加密
    return y


# 解密
def decryption(y, prikey):
    n = prikey[0]
    d = prikey[1]
    x = y ** d % n      # 解密
    return x



if __name__ == '__main__':
    p = int(input("请给定第一个质数p的值："))
    q = int(input("请给定第二个质数q的值："))
    x = int(input("请给定要加密的消息x的值："))
   
    # 生成公钥私钥
    pubkey, prikey = get_key(p, q)
    print("加密前的消息是：", x)
    y = encryption(x, pubkey)
    print("加密后的消息是：", y)
    after_x = decryption(y, prikey)
    print("解密后的消息是：", after_x)
