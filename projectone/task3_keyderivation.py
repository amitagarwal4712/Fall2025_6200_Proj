import sys
import argparse
from Crypto.Hash import SHA256

def keyderivation_hash_message(message):
    h = SHA256.new(message).digest()[:16]
    return h

#Task # 3- Encryption Key Derivation
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-k", "--secretkey",type=str, help="secret key need to hash")
    
    parser.add_argument("-n", "--number",type=int, help="How many time want to hash the secret key")
    args = parser.parse_args()

    if args.secretkey and args.number:   # hashed the secret key number of times as much number user inputs      e.g.  python task3_keyderivation.py -k <secretkey> -n <times to be hashed>
        hashedMessage = args.secretkey.encode('utf-8')
        for m in range(1, args.number):
            hashedMessage= keyderivation_hash_message(hashedMessage)

        print(f"After {args.number} time hashing, hashed value (HEX) is: {hashedMessage.hex()}")

if __name__ == "__main__":
    main()
