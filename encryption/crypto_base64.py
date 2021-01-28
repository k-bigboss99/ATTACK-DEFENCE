import base64
string = "ABC"
string_en = base64.b64encode(string.encode("utf-8"))
print(string_en)
string_de = str(base64.b64decode(string_en.decode("utf-8")))
print(string_de)