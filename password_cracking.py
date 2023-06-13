import hashlib
import time
hash=str(input("Enter your hash:"))
start=time.time()
for i in range(1,99999999999):
    a=hashlib.md5(repr(i).encode('utf-8')).hexdigest()
    if a==hash:
        print("your pass is:",i)
        break
    end=time.time()
