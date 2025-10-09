import sys
import argparse
from datetime import datetime
import random

def seed(seedvalue):
    return random.seed(seedvalue)

def reseed(reseedvalue):
    return random.seed(reseedvalue)

def generate():
    random.randint(1, 269269811)
    return random.random()

#Task 4 PRNG for randomness generation SEED, RESEED, GENERATE
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--seedvalue",type=str, help="seed value for PRNG", default= "2692698")
    parser.add_argument("-r", "--reseedvalue",type=str, help="re seed value for PRNG", default= "2692698")
    parser.add_argument("-n", "--count",type=int, help="number of sequence", default= "10")
    
    args = parser.parse_args()
    seed(args.seedvalue)
    if(args.reseedvalue):
        reseed(args.reseedvalue)
    for m in range(0,args.count):
        randomValue = generate()         # random number generation      e.g.  python task4_PRNG.py -s <seed value> -r <reseed value>
        print(f"{randomValue}")

if __name__ == "__main__":
    main()
