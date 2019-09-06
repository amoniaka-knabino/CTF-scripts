#python3 extract_n_e.py kye.pem

from Crypto.PublicKey import RSA
from sys import argv

def extract_n_e(filename):
    key_file = open(filename, 'r')
    key = key_file.read()
    pubkey = RSA.importKey(key)
    return pubkey.n, pubkey.e

print(extract_n_e(argv[1]))