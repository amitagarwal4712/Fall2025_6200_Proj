import sys
import argparse
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib
import math
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hmac
import base64

globSecretKey=""
globIV = ""

#HMAC function to mac for providided cipher text, in our case we have encrypted with AES CBC
def hmac_sha256(secretkey: bytes, message: bytes)-> bytes:

    print(f"")
    print(f"Input to HMAC functions:")
    print(f"HMAC Key         : {secretkey}")
    print(f"CipherText       : {message}")
    print(f"")

    block_size = 64  # SHA256's block size in bytes

    # If the secretkey is longer than the block size, hashing
    if len(secretkey) > block_size:
        secretkey = hashlib.sha256(secretkey).digest()

    # Pad the key with zeros to match the block size
    keyPrime = secretkey.ljust(block_size, b'\x00')  # calculate K'

    # Inner padding (ipad) and outer padding (opad)
    opad = b'\x5c' * block_size
    ipad = b'\x36' * block_size

    # names = ["A", "B"]     cnt = [1, 2]    zip(names, cnt)= [('A', 1), ('B', 2)]
    kXORipad = bytes(a ^ b for a, b in zip(keyPrime, ipad))   #  ^ provides the XOR operation on bits
    kXORopad = bytes(a ^ b for a, b in zip(keyPrime, opad))

    # Inner hash calculation
    inner_hash = hashlib.sha256(kXORipad + message).digest()

    # Outer hash calculation
    hmac_result = hashlib.sha256(kXORopad + inner_hash).digest()
    print(f"Output of HMAC functions:")
    print(f"HMAC Tag         : {hmac_result.hex()}")
    return hmac_result

#Encrypt with AES CBC
def sym_enc(message):
    print(f"Input to sym_enc functions:")
    print(f"Message          : {message}")
    print(f"")
    print(f"Global value used into sym_enc functions:")
    print(f"globSecretKey Key: {globSecretKey}")
    print(f"globIV           : {globIV}")
    # Encryption
    cipher = AES.new(globSecretKey, AES.MODE_CBC, globIV)
    # Pad the plaintext to a multiple of the block size
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext)

def encrypt_then_mac_message(secretkey,hmacsecretkey, IV, message):
    #Encrypting the message
    ciphertext = sym_enc(message)
    print(f"")
    print(f"Output of sym_enc functions:")
    print(f"Ciphertext       : {ciphertext}")
    #Doing MAC on encrypted cipher text
    mac_tag = hmac_sha256(hmacsecretkey, ciphertext)
    #encrypt_mac_tag = IV + ciphertext + mac_tag

    return ciphertext.decode('utf-8') + mac_tag.hex()

#Decrypt with AES CBC
def sym_dec(ciphertext):
    print(f"")
    print(f"Input to sym_dec functions:")
    print(f"Ciphertext       : {ciphertext}")
    print(f"")
    print(f"Global value used into sym_dec functions:")
    print(f"globSecretKey Key: {globSecretKey}")
    decoded_encrypted_data = base64.b64decode(ciphertext)

    IV= decoded_encrypted_data[:AES.block_size]  #fetching IV from encrypted message
    ctext = decoded_encrypted_data[AES.block_size:]   
    cipher = AES.new(globSecretKey, AES.MODE_CBC, iv = IV)
    decryp_padded_data = cipher.decrypt(ctext)
    plaintext = unpad(decryp_padded_data,AES.block_size).decode('utf-8')
    return plaintext

def verify_then_decrypt_mesage(hmackey, ciphertext):
    # Verify the MAC tag first
    print(f"")
    print(f"ciphertext is    : {ciphertext}")
    print(f"hmacsecretkey is : {hmackey}")
    print(f"")
    plaintext=""

    mac_tag = ciphertext.decode('utf-8')[-64:]   #fetching MAC tag from combined cipher text
    encText = ciphertext.decode('utf-8')[:-64]   #fetching encrypted text from combined cipher text

    calculated_mac_tag_hex = hmac_sha256(hmackey, encText.encode('utf-8'))
    print(f"")
    if hmac.compare_digest(mac_tag.encode('utf-8'), calculated_mac_tag_hex.hex().encode('utf-8')):
        print("MAC tag verified successfully. Message is authentic and untampered.")
        plaintext = sym_dec(encText.encode('utf-8'))
    else:
        print("MAC tag verification is failed. Either Message or tag may be compromised.")
    return plaintext

#Task 5 Secure Message Exchange
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-sk", "--secretkey",type=str, help="symmetric secret key")
    parser.add_argument("-hk", "--hmackey",type=str, help="hmac symmetric secret key")
    parser.add_argument("-i", "--iv",type=str, help="IV value")
    parser.add_argument("-m", "--message",type=str, help="message to be encrypt then MAC")

    parser.add_argument("-c", "--ciphertextmessage",type=str, help="message to be decrypted")
    args = parser.parse_args()

    global globSecretKey
    globSecretKey = args.secretkey.encode('utf-8')
    

    #encrypt then HMAC
    if args.secretkey and args.hmackey and args.message and args.iv:   # HMAC creation      e.g.  python task5_SecureMessageExchange.py -sk <secretkey> -hk <hmackey> -i <IV> -m <message>
       global globIV
       globIV = args.iv.encode('utf-8')
       encrype_then_HMAC_message = encrypt_then_mac_message(args.secretkey.encode('utf-8'),args.hmackey.encode('utf-8'), args.iv.encode('utf-8'), args.message.encode('utf-8'))
       print(f"")
       print(f"Output of Encrypt then MAC functions:")
       print(f"Ciphertext + HMAC Tag       : {encrype_then_HMAC_message}")
    #verify the encrypt then HMAC and get plain text
    if args.secretkey and args.hmackey and args.ciphertextmessage:   # ciphertext + HMAC creation      e.g.  python task5_SecureMessageExchange.py -sk <secretkey> -hk <hmackey>  -c <ciphertext>
       plainMessage = verify_then_decrypt_mesage(args.hmackey.encode('utf-8'), args.ciphertextmessage.encode('utf-8'))
       if plainMessage != "":
        print(f"")
        print(f"Decrypted Plaintext message : {plainMessage}")

if __name__ == "__main__":
    main()
