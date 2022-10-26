i = 0
    # # while i != len(inputs):
    # for i in range(len(inputs)):
    #     if len(inputs[i]) == 2:
    #         p, q = inputs[i].split()
    #         p, q = int(p), int(q)
    #         i += 1
    #         plain_text = []
    #         k = 0
    #         while k < 5:
    #             plain_text.append(int(inputs[i]))
    #             k +=1
    #             i += 1

    #         n, e, d, phi = key_gen(p, q)

    #         encryption, decryption = [], []

    #         for digit in plain_text:
    #             encryption.append(slow_expmod(digit, e, n))

    #         for cipher in encryption:
    #             decryption.append(slow_expmod(cipher, d, n))
            
            
    #         for j in range(5):
    #             print("p: " + str(p) + ", q: " + str(q) + ", n: " + str(n) +  ", phi: " + str(phi) + ", e: " + str(e) + ", d: " + str(d) + ", message: " + str(plain_text[j]) + ", encrypted: " + str(encryption[j]) + ", decrypted: ", decryption[j])

