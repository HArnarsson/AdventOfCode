import hashlib

input = "bgvyzdsv"


num = 0
while(True):
    test = input + str(num)    
    encoded = hashlib.md5(test.encode('utf-8'))
    digest = encoded.hexdigest()
    if digest[:5] == "00000":
        break
    num += 1

print(num)
print(encoded.hexdigest())