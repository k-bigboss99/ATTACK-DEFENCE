from hashlib import md5

s1 = 'ms08067.com'
new_md5 = md5()
new_md5.update(s1.encode(encoding='utf-8'))
decryptResult = new_md5.hexdigest()

print(decryptResult)