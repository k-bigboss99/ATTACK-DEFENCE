from Cryptodome.Cipher import DES
import binascii
key = b'abcdefgh'  # key 的長度須為8字節
des = DES.new(key, DES.MODE_ECB)
text = "HelloWorld"
text = text + (8 - (len(text) % 8)) * '='
encrypt_text = des.encrypt(text.encode())
encryptResult = binascii.b2a_hex(encrypt_text)
print(text)
print(encryptResult)

decryptResult = des.decrypt(encrypt_text)
print(decryptResult)