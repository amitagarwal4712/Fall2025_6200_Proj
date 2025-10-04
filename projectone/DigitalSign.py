import sys
import argparse
import Signature_Function

#Task 1 Digital Signature (Functionas are called from signature_function.py file )
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-g", "--genkeypair",type=str, help="Key pair generate")

    parser.add_argument("-m", "--message", type=str, help="Message to be hashed")

    parser.add_argument("-s", "--sign", type=str, help="Message to be signed",)
    parser.add_argument("-sk", "--secretkey", type=str, help="Signer key")

    parser.add_argument("-v", "--verifySign", type=str, help="Verify Sign")
    parser.add_argument("-pk", "--publickey", type=str, help="Verifier key")
    parser.add_argument("-ss", "--signersign", type=str, help="Sign to verify")

    args = parser.parse_args()

    if args.genkeypair:   # Public and private key pair generation      e.g.  python DigitalSign.py -g key
        private_key, public_key = Signature_Function.KeyGen_Dig()
        print(f"Private key is : {private_key}")
        print(f"Public key is : {public_key}")
    if args.message and not args.sign and not args.verifySign:  #hashing plain text message   e.g. python DigitalSign.py -m "This is message to Bob from Alice"
        if args.message:
            hashed_message = Signature_Function.hash_message(args.message)
            print(f"Hashed message is:", hashed_message.hexdigest())
        else:
            print("Please provide message -m")
    if args.sign:  # Signing the message, return in hex format sign   e.g. python DigitalSign.py -s sign -m <message> -sk <private/secret key>
        if args.message and args.secretkey:
            Signature = Signature_Function.sign_message(args.secretkey, args.message)
            print(f"Signature is:", Signature)
        else:
            print("Please provide message -m and private/secret key -sk")
    if args.verifySign:   # Verifying the sign for the message, returns 1 if successylly verified else returns 0 if verification failed e.g. python DigitalSign.py -v verify -m <message> -pk <public key> -ss <signature>
        if args.signersign and args.message and args.publickey :
            isVeified = Signature_Function.sign_verifier(args.publickey, args.message, args.signersign)
            print(f"verification function retunrs: ", isVeified)
        else:
            print("Please provide message -m and public key -pk and signer sign --ss")

if __name__ == "__main__":
    main()

