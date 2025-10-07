##🚀 Usage
##✅ 1. Generate Key Pair

Generates RSA public and private keys using small primes p = 5 and q = 11.

python RSADigitalSign.py -g key


Returns:

Private Key d

Public Key: N and e

##🔒 2. Hash a Message

Hashes a plain text message using SHA-256 (in rsa_hashMessage function).

python RSADigitalSign.py -m "Hello from Alice"

##✍️ 3. Sign a Message

Signs a message using private key d and public modulus N.

python RSADigitalSign.py -s sign -m "Hello from Alice" -d <private_key_d> -N <public_key_N>

##🕵️ 4. Verify a Signature

Verifies the signed message using public exponent e, modulus N, and the signature.

python RSADigitalSign.py -v verify -m "Hello from Alice" -e <public_key_e> -N <public_key_N> -ss <signature>

##🧾 CLI Arguments
Short	Long	Description	Required With
-g	--genkeypair	Generate RSA key pair	
-m	--message	Message to hash/sign/verify	All operations
-s	--sign	Sign the message	-m, -d, -N
-v	--verifySign	Verify a signature	-m, -e, -N, -ss
-d	--privatekey_d	Private key for signing	Signing
-e	--publickey_e	Public key exponent for verifying	Verifying
-N	--publickey_N	RSA modulus for signing/verifying	Signing / Verifying
-ss	--signersign	Signature to verify	Verifying
