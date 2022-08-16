# Solving and Capturing Flags in CTF

Hi iam SaiKris2 a RGUKT Student from Nuzvid Campus from PUC1

Today we are looking good to crack some flags from these Challanges

Its Right we are doing some CTF (Caputure The Flag) Challanges from the Event Hosted by InvadersCTF

## About the Event

This event is hosted by Invaders CTF Group from 10th of August 2:00 pm until 14 of August 2:00 pm, in this Website https://ctf.pwn.af/challenges

It might be taken down by the time this website is published

So basically, There are a lot of Sections / Categories in Which we can solve problems

The list of Categories:

- Web
- PWN
- Misc
- Rev
- Crypto

Each have there own set of challenges starting from easy to hard

I did a Couple of Problems from each Section of Apart from Crypto

Now enough of the boring part and lets break our keyboards!!! Ahem! I mean lets start Cracking the Challanges

## Misc Category

1. Encrypted

### Description of Challange

Recover the flag by reversing the encryption.

They gave us 2 files

1. A image called leak.png [Image](/codewithsam110g.github.io/leak.png)
2. A Python file called Chall.py [Link](https://github.com/codewithsam110g/codewithsam110g.github.io/blob/main/chall.py)

### Code given chall.py

```python

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

```
