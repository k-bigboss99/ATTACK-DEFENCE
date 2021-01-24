import socket
language = {'what is your name':'i am shizu', 'how old are you':'18', 'bye':'88'}
HOST = "127.0.0.1"
PORT = 6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("listening at port 6666")
conn, addr = s.accept()
print('connect by: ',addr)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print('received message:' + data)
    conn.sendall(language.get(data, 'Nothing').encode())
conn.close()
s.close