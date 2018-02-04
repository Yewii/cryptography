#!/usr/bin/env python3

import random


# 质数判断
def is_prime(num):
    Flag = 0
    a = 2
    a1 = pow(a, num, num)
    a2 = pow(a, 1, num)
    if a1 == a2:
        return 1
    else:
        return 0


# 获取随机质数
def get_random_prime():
    Flag = 0
    while not Flag:
        p = random.randrange(2 ** 5, 2 ** 6)

        if p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0 or p % 13 == 0:
            continue

        Flag = is_prime(p)
    return p


# 获取随机数a,bimport struct

IV = "7380166f 4914b2b6 1adc42d7 da634630 a96f35bc 163438aa e38d4e4d b0f8364e"

IV = int(IV.replace(" ", ""), 16)

a = []
for i in range(0, 8):
        a.append(0)
        a[i] = (IV >> ((7 - i) * 32)) & 0xFFFFFFFF
IV = a

# 打印加密密文
def out_hex(list1):
        for i in list1:
                print("%08x" % i)
        print("\n")

def rotate_left(a, k):
        k = k % 32
        return ((a << k) & 0xFFFFFFFF) | ((a & 0xFFFFFFFF) >> (32 - k))

T_j = []


for i in range(0, 16):
        T_j.append(0)
        T_j[i] = 0x79cc4519
for i in range(16, 64):
        T_j.append(0)
        T_j[i] = 0x7a879d8a

# 布尔函数
def FF_j(X, Y, Z, j):
        if 0 <= j < 16:
                ret = X ^ Y ^ Z
        elif 16 <= j < 64:
                ret = (X & Y) | (X & Z) | (Y & Z)
        return ret


# 布尔函数
def GG_j(X, Y, Z, j):
        if 0 <= j < 16:
                ret = X ^ Y ^ Z
        elif 16 <= j < 64:
                ret = (X & Y) | ((~ X) & Z)
        return ret

# 置换函数
def P_0(X):
        return X ^ (rotate_left(X, 9)) ^ (rotate_left(X, 17))


# 置换函数
def P_1(X):
        return X ^ (rotate_left(X, 15)) ^ (rotate_left(X, 23))

# 压缩函数
def CF(V_i, B_i):
        W = []
        for j in range(0, 16):
                W.append(0)
                unpack_list = struct.unpack(">I", B_i[j * 4:(j + 1) * 4])
                W[j] = unpack_list[0]
        for j in range(16, 68):
                W.append(0)
                W[j] = P_1(W[j - 16] ^ W[j - 9] ^ (rotate_left(W[j - 3], 15))) ^ (rotate_left(W[j - 13], 7)) ^ W[j - 6]
                str1 = "%08x" % W[j]
        W_1 = []
        for j in range(0, 64):
                W_1.append(0)
                W_1[j] = W[j] ^ W[j + 4]
                str1 = "%08x" % W_1[j]

        A, B, C, D, E, F, G, H = V_i
        """
        print "00",
        out_hex([A, B, C, D, E, F, G, H])
        """
        for j in range(0, 64):
                SS1 = rotate_left(((rotate_left(A, 12)) + E + (rotate_left(T_j[j], j))) & 0xFFFFFFFF, 7)
                SS2 = SS1 ^ (rotate_left(A, 12))
                TT1 = (FF_j(A, B, C, j) + D + SS2 + W_1[j]) & 0xFFFFFFFF
                TT2 = (GG_j(E, F, G, j) + H + SS1 + W[j]) & 0xFFFFFFFF
                D = C
                C = rotate_left(B, 9)
                B = A
                A = TT1
                H = G
                G = rotate_left(F, 19)
                F = E
                E = P_0(TT2)

                A = A & 0xFFFFFFFF
                B = B & 0xFFFFFFFF
                C = C & 0xFFFFFFFF
                D = D & 0xFFFFFFFF
                E = E & 0xFFFFFFFF
                F = F & 0xFFFFFFFF
                G = G & 0xFFFFFFFF
                H = H & 0xFFFFFFFF
                """
                str1 = "%02d" % j
                if str1[0] == "0":
                        str1 = ' ' + str1[1:]
                print str1,
                out_hex([A, B, C, D, E, F, G, H])
                """

        V_i_1 = []
        V_i_1.append(A ^ V_i[0])
        V_i_1.append(B ^ V_i[1])
        V_i_1.append(C ^ V_i[2])
        V_i_1.append(D ^ V_i[3])
        V_i_1.append(E ^ V_i[4])
        V_i_1.append(F ^ V_i[5])
        V_i_1.append(G ^ V_i[6])
        V_i_1.append(H ^ V_i[7])
        return V_i_1

# 哈希函数
def hash_msg(msg):
        len1 = len(msg)
        reserve1 = len1 % 64
        msg1 = msg.encode() + struct.pack("B",128)
        reserve1 = reserve1 + 1
        for i in range(reserve1, 56):
                msg1 = msg1 + struct.pack("B",0)

        bit_length = (len1) * 8
        bit_length_string = struct.pack(">Q", bit_length)
        msg1 = msg1 + bit_length_string

        print(len(msg1))
        group_count = int(len(msg1) / 64)
        print(group_count)

        m_1 = B = []
        for i in range(0, group_count):
                B.append(0)
                B[i] = msg1[i*64:(i+1)*64]

        V = []
        V.append(0)
        V[0] = IV
        for i in range(0, group_count):
                V.append(0)
                V[i+1] = CF(V[i], B[i])

        return V[i+1]

print("abc")
y = hash_msg("abc")
print("result: ")
out_hex(y)

def get_random_num():
    a = random.randrange(2 ** 5, 2 ** 6)
    return a

# 判定p,g是否互质
def is_coprime(p, g):
    if p < g:
        p, g = g, p
    while g != 0:
        Flag = p % g
        p = g
        g = Flag
    if (p, g) == (1, 0):
        return 1
    else:
        return 0

# 确定p,g
def compare_pg():
    Flag = 1
    while Flag:
        p = get_random_prime()
        g = get_random_prime()
        if p < g and is_coprime(p, g):
            continue

        Flag = 0

    return p, g

# 计算公钥A,B
def public_key(g, a):
    A = g ** a
    return A

# 计算公共秘钥K
def KEY(A, b):
    K = A ** b
    return K


# 三方Diffie–Hellman
def Diffie_Hellman():
    p, g = compare_pg()
    print("大质数p:", p)
    print("本源根g:", g)
    print()

    a = get_random_num()
    print("Alice的私钥a:", a)
    b = get_random_num()
    print("Bob的私钥b:", b)
    c = get_random_num()
    print("Charlie的私钥c:", c)
    print()


    A = public_key(g, a)
    B = public_key(g, b)
    C = public_key(g, c)
    Ya = KEY(A, b)
    Yb = KEY(B, c)
    Yc = KEY(C, a)
    Ka = KEY(Yb, a)
    Kb = KEY(Yc, b)
    Kc = KEY(Ya, c)
    if Ka == Kb and Kb == Kc:
        print("公共秘钥K：", Ka)
    else:
        print("error")

if __name__ == "__main__":
    Diffie_Hellman()