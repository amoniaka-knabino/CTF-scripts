
from Crypto.PublicKey import RSA
from math import sqrt
from sys import argv

def factorize(n):
    '''
    https://www.quaxio.com/exploring_three_weaknesses_in_rsa/
    '''
    if n%2==0:
        return 2
    if n%3==0:
        return 3
    if n%5==0:
        return 5
    m = sqrt(n)
    i=7
    while i<=m:
        if (n%i==0):
            return i
        if (n%(i+4)==0):
            return i+4
        if (n%(i+6)==0):
            return i+6
        if (n%(i+10)==0):
            return i+10
        if (n%(i+12)==0):
            return i+12
        if (n%(i+16)==0):
            return i+16
        if (n%(i+22)==0):
            return i+22
        if (n%(i+24)==0):
            return i+24
        i+=30


key_file = open(argv[1], 'r')
key = key_file.read()
key_file.close()
print(key)
pubkey = RSA.importKey(key)
p = factorize(pubkey.n)
print(p)




