import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = int(sys.argv[1])

s.connect((host, port))

while True:
    msg = input()
    if msg.lower() == "exit":
        print("hello")
        s.close()
        sys.exit()
        
    s.send(msg.encode())

s.close()
print(msg.decode('ascii'))
