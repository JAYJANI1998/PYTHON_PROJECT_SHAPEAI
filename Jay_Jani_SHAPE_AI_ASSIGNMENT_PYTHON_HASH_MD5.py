import hashlib
hash_input = input('Please input the string you want to encrypt:')
hash_output=hashlib.md5(hash_input.encode())
print('Your Encrypted Hash output is :',hash_output.hexdigest())
