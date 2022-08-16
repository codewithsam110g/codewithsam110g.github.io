import random

# Two byte hash
def myHash(string):
    random.seed("H4shS33d" + string)
    num = random.getrandbits(16)
    return hex(num)[2:].zfill(4)

def encryptFlag(flag):
    enc = ""
    for char in flag:
        enc += myHash(char)
    return enc

flag = input("Enter flag : ")
enc = encryptFlag(flag)
print("Encrypted flag is : ", enc)

