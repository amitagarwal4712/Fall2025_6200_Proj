import sys
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib
import math
from hashlib import sha512

# TASK#1(Digital Signature) : Functions for Task #1
##########################################################################Digital Signature FUNCTION#####################################################################################
# This function returns the generated Public and Private key for Digital Signature
def KeyGen_Dig():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# This function returns the hashed message
# input parameter
#      message           -> plain string message
def hash_message(message):
    h = SHA256.new(message.encode('utf-8'))
    return h

# This function returns the signer's sign in Hex format
# input parameter
#      sec_key  -> secret/private key of signer
#      message  -> plain text message
def sign_message(sec_key, message):
    hashed_message = hash_message(message)
    signer = pkcs1_15.new(RSA.import_key(sec_key.replace('\\n', '\n').encode('utf-8')))
    signature = signer.sign(hashed_message)
    return signature.hex()

# This function returns 1 If signature are verified successfully else return 0 if signature are not verified
# input parameter
#      p_key      -> Public key of signer
#      message    -> plain text Message
#      signature  -> Signature in hex format
def sign_verifier(p_key, message, signature):
    hashedmessage = hash_message(message)
    verifier = pkcs1_15.new(RSA.import_key(p_key.replace('\\n', '\n').encode('utf-8')))
    try:
        verifier.verify(hashedmessage, bytes.fromhex(signature))
        return 1
    except ValueError:
        return 0

# TASK#1(RSA Digital Signature) : Functions for Task #1
##########################################################################RSA Style FUNCTION#####################################################################################
# This RSA KeyGen function returns generated key private key 'd', publick key 'N'  publick key exponent 'e'
# input parameter
#      p  -> large prime number
#      q  -> large prime number <> p
def rsa_KeyGen(p, q): #   Generates the RSA public and private key pair from two prime numbers. public key=(e, n) , private key=(d, n).
    N = p * q  # calculate n = p * q
    p_n = (p - 1) * (q - 1)  # Compute the totient, phi_n = (p-1) * (q-1)
    e = 5  # Choosing e i.e. 2 < e <  (p-1)(q-1) and not factor of (p-1)*(q-1) and gcd(e, p_n) = 1
    while extended_gcd(e, p_n)[0] != 1:
        e += 1
    d = mod_inverse(e, p_n)  # Calculate d, modular multiplicative inverse of e mod p_n
    return (N, e, d)  # Public key = N, e, private key = d

# This RSA hash function returns the hashed message
# input parameter
#      message           -> plain string message
def rsa_hashMessage(message):
    h = int.from_bytes(hashlib.sha512(message.encode('utf-8')).digest(), byteorder='big')
    return h

# This RSA function returns the signer's sign
# input parameter
#      privatekey_d  -> private key of signer i.e. 'd'
#      publickey_N   -> public key of signer i.e. 'N'
#      message  -> plain text message
def rsa_sign(privatekey_d, publickey_N, message):#  Signs a message by first hashing it and then calculating sign by the hash with the private key.
    hash_value = rsa_hashMessage(message)
    signature = pow(hash_value, privatekey_d, publickey_N)      # The signature is hash^d mod N
    return signature

# This RSA function returns 1 If signature are verified successfully else return 0 if signature are not verified
# input parameter
#      publickey_e      -> Public key of signer 'e' exponent
#      publickey_N      -> Public key of signer 'N'
#      message    -> plain text Message
#      signature  -> Signature in
def rsa_verify(publickey_e, publickey_N, message, signature):# Verifies a signature by cacluclating it with the public key and  comparing the result to the message's hash.
    hash_from_signature = pow(int(signature), publickey_e, publickey_N)     # calculate sig^e mod N 
    original_hash = (rsa_hashMessage(message) % publickey_N)               # calculate H(M) mod N    for H(M) Congurent sig^e mod N
    if hash_from_signature == original_hash: 
        return 1 
    else: 
        return 0

def is_prime(n):  # verifiying if nyumber is prime
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def extended_gcd(a, b):  #Extended Euclidean algorithm to find gcd(a, b) and coefficients x and y
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(a, m): #Finds the modular multiplicative inverse of a mod m
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
