import sys
import argparse
import Signature_Function

#Two prime factor are choosen for key generation
p = 5
q = 11

#Task 1 RSA Digital Signature (Functionas are called from signature_function.py file )
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-g", "--genkeypair",type=str, help="Key pair generate")

    parser.add_argument("-m", "--message", type=str, help="Message to be hashed")

    parser.add_argument("-s", "--sign", type=str, help="Message to be signed",)
    parser.add_argument("-v", "--verifySign", type=str, help="Verify Sign")

    parser.add_argument("-d", "--privatekey_d", type=str, help="Signer key")
    parser.add_argument("-e", "--publickey_e", type=str, help="Verifier key")
    parser.add_argument("-N", "--publickey_N", type=str, help="Verifier key")

    parser.add_argument("-ss", "--signersign", type=str, help="Sign to verify")

    args = parser.parse_args()

    if args.genkeypair:   # Public and private key pair generation      e.g.  python RSADigitalSign.py -g key
        N, e, d = Signature_Function.rsa_KeyGen(p, q)
        print(f"Private key 'd' is : {d}")
        print(f"Public key N : {N}, and e : {e}")
    if args.message and not args.sign and not args.verifySign:  #hashing plain text message   e.g. python RSADigitalSign.py -m "This is message to Bob from Alice"
        if args.message:
            hashed_message = Signature_Function.rsa_hashMessage(args.message)
            print(f"Hashed message is:", hashed_message)
        else:
            print("Please provide message -m")
    if args.sign:  # Signing the message   e.g. python RSADigitalSign.py -s sign -m <message> -d <private/secret key> -N <public key>
        if args.message and args.privatekey_d and args.publickey_N:
            Signature = Signature_Function.rsa_sign(int(args.privatekey_d), int(args.publickey_N), args.message)
            print(f"Signature is:", Signature)
        else:
            print("Please provide message -m and private/secret key -d and public key -N")
    if args.verifySign:   # Verifying the signed message   e.g. python RSADigitalSign.py -v verify -m <message> -e <public key e> -N <public key N> -ss <signature>
        if args.signersign and args.message and args.publickey_e and args.publickey_N:
            isVeified = Signature_Function.rsa_verify(int(args.publickey_e), int(args.publickey_N), args.message, args.signersign)
            print(f"verification function returns: ", isVeified)
        else:
            print("Please provide message -m and public key -e and -N and signer sign --ss")

if __name__ == "__main__":
    main()

