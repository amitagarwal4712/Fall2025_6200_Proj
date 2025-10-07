Functionality Overview
1. Generate Key Pair

Generate a public-private key pair.

Command:

python DigitalSign.py -g key


Returns:

Private Key

Public Key

2. Hash Message

Hash a plaintext message (no signing, no verification).

Command:

python DigitalSign.py -m "This is message to Bob from Alice"


Returns:

Hashed message in hexadecimal

3. Sign Message

Digitally sign a message using the secret (private) key.

Command:

python DigitalSign.py -s sign -m "Your message here" -sk <private_key>


Returns:

Signature in hexadecimal

Note: Both message -m and secret key -sk are required.

4. Verify Signature

Verify the digital signature for a message using the public key.

Command:

python DigitalSign.py -v verify -m "Your message here" -pk <public_key> -ss <signature>


Returns:

1 if the signature is valid

0 if the signature is invalid

Note: Requires message -m, public key -pk, and signature --ss.
