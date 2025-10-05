# Fall2025_6200_Proj
NOTE: install pycryptodome with command before execute any function as prequiste :      pip install pycryptodome

#Task # 1
  1) Signature_Function.py - This file contains the functions for Digital Signature and RSA Ditgital Signature for Key Generation, Hashing, Sign and verify
      Digital Signature: Following are functions created and called from DigitalSign.py file 
         KeyGen_Dig()  - Returns generated Public/Private key pair
         hash_message(message)- Returns the hash of message, input parameter is message
         sign_message(sec_key, message)- Returns the signature on message with private key of sender, input parameter is secret key and message
         sign_verifier(p_key, message, signature)- Verify the signature with public key of sender by receiver and return 1 if signature verified successfuly else returns 0 if signature verification is failed
                                                  input parameter p_key is public key, message message which need to be verified and signature
     RSA Digital Signature: Following are functions created  and called from RSADigitalSign.py file 
         rsa_KeyGen(p,q)      - Returns generated 1 private key 'd' and 2 Public key 'N' and 'e' exponent. Input parameter are p and q, both are large prime number
         rsa_hashMessage(message) - Returns the hash of message, input parameter is message
         rsa_sign(privatekey_d, publickey_N, message)        - Returns the signature on message with RSA formula hash(m)^d mod N  where d is private key and N is public key.
                                                              input parameter is private key d, publiv key N and mssage need to be signed
         rsa_verify(ublickey_e, publickey_N, message, signature)      - Verify the signature with public key of sender by receiver and return 1 if signature verified successfuly else returns 0 if signature verification is failed. for H(M) Congurent sig^e mod N. Input paramter is exponent public key e, public key N, message need to be vriofied and signature
  2) DigitalSign.py
     a- To Generate public/private key pair          python DigitalSign.py -g key
         Command: python DigitalSign.py -g key
         Output Sample: 
                   Private key is : b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAiYOFdBbU2oP+O/kDAl6XSPCrDsMxCIQEE8EbNX0Mycu8GQFA\n-----END RSA PRIVATE KEY-----'
                   Public key is : b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9wsrSrmkkIsalf6Mwj/e1\nNwIDAQAB\n-----END PUBLIC KEY-----'
     b- To Generate hash message     python DigitalSign.py -m <message to be hashed>
         Command: python DigitalSign.py -m "This is message to Bob from Alice"
         Output:  Hashed message is: 28fe81448d4a4ed63ab9502b03b7d9a5c472fa3a46e8d8d59887c9f7fe806010
     c- To Sign using digital signature   python DigitalSign.py -s sign -m <message on which signature need to signed> -sk <private/secret key>
         Command:        python DigitalSign.py -s sign -m "this is from alice to bob" -sk "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAiYOFdBbU2oP+O/kDAl6XSPCrDsMxCIQEE8EbNX0Mycu8GQFA\n-----END RSA PRIVATE KEY-----"
         Output sample:  Signature is: 6ebc83d9d8f7286f0ec297bdd91d8660413a468305ba77279a0c90dd6dd1308dfbe490e050b38a2eb5bad236eabfcdac91a4a3a99f7c7e1208741065860958ae3507066d6d3e02c6548cc423d4f7008d9a469e367b56adcaa9d
     d- To verify the sign, python DigitalSign.py -v verify -m <message on which signature need to verify> -pk <public key> -ss <generated signature need to verify>  
         Command: python DigitalSign.py -v verify -m "this is from alice to bob" -pk "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9wsrSrmkkIsalf6Mwj/e1\nNwIDAQAB\n-----END PUBLIC KEY-----" -ss "6ebc83d9d8f7286f0ec297bdd91d8660413a468305ba77279a0c90dd6dd1308dfbe490e050b38a2eb5bad236eabfcdac91a4a3a99f7c7e1208741065860958ae3507066d6d3e02c6548cc423d4f7008d9a469e367b56adcaa9d"
         Output:  verification function returns:  1
   3) RSADigitalSign.py
     a- To Generate RSA style key based on 2 prime factor          python RSADigitalSign.py -g key
         Command: python RSADigitalSign.py -g key
         Output:   Private key 'd' is : 23
                   Public key N : 55, and e : 7
     b- To Generate RSA style hash message     python RSADigitalSign.py -m <message to be hashed>
         Command: python RSADigitalSign.py -m "This is message to Bob from Alice"
         Output:   Hashed message is: 7939163360633260683574349051226526346280008803556395345937981193656305654554197095412355453496388733286122607911905202660325143457645377185305958692540337
     c- To Sign RSA style   python RSADigitalSign.py -s sign -m <message on which signature need to signed> -d <private key> -N <public key>
         Command: python RSADigitalSign.py -s sign -m "this is the message from alice to Bob" -d 23 -N 55
         Output:  Signature is: 5
     d- To verify the sign RSA style, python RSADigitalSign.py -v verify -m <message on which signature need to verify> -e <exponent public key> -N <public key> -ss <generated signature need to verify>  
         Command: python RSADigitalSign.py -v verify -m "this is the message from alice to Bob" -e 7 -N 55 -ss 5
         Output:  verification function returns:  1

         Command: python RSADigitalSign.py -v verify -m "this is the message from to Bob" -e 7 -N 55 -ss 5
         Output:  verification function returns:  0
