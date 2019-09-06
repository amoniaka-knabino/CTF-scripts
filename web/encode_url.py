from sys import argv

def encode(s):
     ans = ''
     for x in s:
         ans += '%' + hex(ord(x))[2:]
     return ans

def main():
    print(encode(argv[1]))

if __name__ == '__main__':
    main()
