🧠 Functionality Overview
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

🔧 Argument List
Argument	Alias	Description
--genkeypair	-g	Generate key pair
--message	-m	Message to hash or sign
--sign	-s	Trigger signing operation
--secretkey	-sk	Private key used for signing
--verifySign	-v	Trigger signature verification
--publickey	-pk	Public key used for verification
--signersign	-ss	Signature to verify
🚀 Example Workflows
Generate Key Pair
python DigitalSign.py -g key

Hash a Message
python DigitalSign.py -m "Hello, Alice!"

Sign a Message
python DigitalSign.py -s sign -m "Hello" -sk my_private_key

Verify a Signature
python DigitalSign.py -v verify -m "Hello" -pk my_public_key -ss my_signature

📌 Notes

Make sure the Signature_Function.py module is available and correctly implements:

KeyGen_Dig()

hash_message(message)

sign_message(secret_key, message)

sign_verifier(public_key, message, signature)

Ensure correct format for keys and signature (likely base64 or hex).

Python version: ≥ 3.6 recommended.
