from Cryptodome.Cipher import AES
import binascii
key = b'abcdefghijklmnop' # key 的長度須為16字節
text = "HelloWorld"
text = text + (16 - (len(text) % 16)) * '='
aes = AES.new(key, AES.MODE_ECB)
encrypto_text = aes.encrypt(text.encode())
encryptResult = binascii.b2a_hex(encrypto_text)
print(text)
print(encryptResult)

decryptResult = aes.decrypt(encrypto_text)
print(decryptResult)