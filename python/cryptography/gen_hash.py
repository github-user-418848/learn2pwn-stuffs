import hashlib
# Demonstrates the difference the types of hashing
password = input("Input the password to hash\n-> ")
print("\nSHA1:\n")
for i in range(3):
        setpass = bytes(password,'utf-8')
        hash_object = hashlib.sha1(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)
print("\nMD5:\n")
for i in range(3):
        setpass = bytes(password,'utf-8')
        hash_object = hashlib.md5(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)
print("\nBLAKE2B:\n")
for i in range(3):
        setpass = bytes(password,'utf-8')
        hash_object = hashlib.blake2b(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)
print("\nBLAKE2S:\n")
for i in range(3):
        setpass = bytes(password,'utf-8')
        hash_object = hashlib.blake2s(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)
input("Press any key to continue...")
