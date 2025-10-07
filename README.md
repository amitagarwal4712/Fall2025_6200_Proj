# Project 1 Fall 2025 Cryptography- ITIS6200
## 🛠️ Requirements

- Python 3.x
## 🧰 Installation

Install dependencies:
```bash
pip install pycryptodome
```

## 🚀 Task # 1 - Digital Signature

### Function 1- Key Generation
```bash
python DigitalSign.py -g key
```
### Function 2- Hash message

```bash
python DigitalSign.py -m "This is message to Bob from Alice"
```
### Function 3- Sign a message

```bash
python DigitalSign.py -s sign -m "this is from alice to bob" -sk <"private key from Function 1 output">
```
### Function 4- Verify signtaure message

```bash
python DigitalSign.py -v verify -m "message used while signed in function 3" -pk "public key from function 1 output" -ss "signature from function 3 output"
```
Output: 1 if verified, 0 if verification failed

## 🚀 Task # 1 - Digital Signature - RSA style based on 2 prime factor p and q 
### Function 1- Key Generation
```bash
python RSADigitalSign.py -g key
```
### Function 2- Hash message

```bash
python RSADigitalSign.py -m "This is message to Bob from Alice"
```
### Function 3- Sign a message

```bash
python RSADigitalSign.py -s sign -m "this is the message from alice to Bob" -d "private key 'd' from Function 1" -N "public key 'N' from function 1"
```
### Function 4- Verify signtaure message

```bash
python RSADigitalSign.py -v verify -m "message used while signed in function 3" -e "public key exponent 'e' from function 1" -N "public key 'N' from function 1" -ss "signature genetaed in function 3"
```
Output: 1 if verified, 0 if verification failed
