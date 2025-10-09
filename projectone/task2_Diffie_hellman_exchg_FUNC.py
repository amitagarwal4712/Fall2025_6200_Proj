import sys
import getopt
import datetime
import io
import random

P=71    # large primary number
G=5119  # Random generator Number public key

def generate_secret_key():   #Generates a random private key like 'a' for Alice, 'b' for Bob.
    return random.randint(1, P - 1)

def calculate_public_key():   #Calculates the public key from the private key.  like gaModP or gbModP
    private_key = generate_secret_key()
    return P, G, private_key, pow(G, private_key, P)

def calculate_shared_secret(public_key, private_key):    #Calculates the shared secret using the other party's public key and own private key.  (gaModP)bModP or (gbModP)aModP
    return pow(int(public_key), int(private_key), P)
