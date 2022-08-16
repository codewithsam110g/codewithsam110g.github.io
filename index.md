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

1. A image called leak.png 

![Image](/docs/assets/leak.png)

2. A Python file called Chall.py [Link](https://github.com/codewithsam110g/codewithsam110g.github.io/blob/main/docs/assets/chall.py)

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
As we can in the image the flag is Encrypted using the encrypt function in the given python file

as we can see the code is not randomized, it means if we pass a letter "a" as input not matter what happens, it will return the same answer

this is because the random function asks for a seed value to generate something, as the seed is already given, if we use the same seed it will
generate same psuedo-random character which defies its purpose

and from above code every letter is composed of 4 values in encrypted value

To crack this, we can make a lookup table with given alphanumeric(Numbers & Alphabets) characters and symbols

Now, we will take the given encrypted value and break it into smaller sections which will represent their character

we do this by dividing the length of given function by 4 as we know that each character is 4 letters from this line in code

```python
    return hex(num)[2:].zfill(4) #filling 4 values
```

now that will give us number of characters in encrypted value, now we use this to divide the length of the encrypted value again to give the section length

Finally we will construct a list from the encrypted value with sections by using

```python

    [given[i:i+section_size] for i in range(0, len(given), section_size)]

```

now we just compare the value from broken_encypted_val in list and add it to the answer

If we put all of that together we get this final code

```python

import random

def myHash(string):
    random.seed("H4shS33d" + string)
    num = random.getrandbits(16)
    return hex(num)[2:].zfill(4)

def encrypt(value):
    enc = ""
    for char in value:
        enc += myHash(char)
    return enc
    
possible_values=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","_","{","}","!"]
listval = []

for s in possible_values:
    listval.append(encrypt(s))

lut = {listval[i]:possible_values[i] for i in range(len(possible_values))}

given="08ef07973844262cd256a8635295ad53ece7518ae30f1fb9bdbfbfa95295262c1fb917ac757352956685500ebfa9cf347573d2566685bdbfbfa9cf34bdbff2a30797b15a66856217cf34668507287573262c908276b5"

section_size = len(given)//(int(len(given)/4))

broken_enc = [given[i:i+section_size] for i in range(0, len(given), section_size)]
val = []
for s in broken_enc:
    if(s in lut):
        val += lut[s]

res = ""
for s in val:
    res+=s

print(res)

```

