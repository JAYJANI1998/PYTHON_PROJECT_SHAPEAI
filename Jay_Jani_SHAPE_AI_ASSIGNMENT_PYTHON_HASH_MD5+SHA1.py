#Here I have used Double Hash Algorithms (MD5 and SHA1) to encrypt the text

import hashlib
hash_input = input('Please input the string you want to encrypt:')#Taking the input
hash_output=hashlib.md5(hash_input.encode())#Applying MD5
hash_final_md5=hash_output.hexdigest()# Using Hexdigest to view the code in gibberish format
print('Your Encrypted Hash output is :',hash_final_md5)
hash_sha=hashlib.sha1(hash_final_md5.encode())#Using SHA1 on abouve generated hash
print('Your Sha Hash is :',hash_sha.hexdigest())
