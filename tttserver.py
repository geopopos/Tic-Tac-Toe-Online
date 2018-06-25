import socket

from Room import Room

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

serversocket.bind((host, port))

serversocket.listen(2)

room = Room(1, 2)

"""while True:
    #establish a connection
    clientsocket, addr = serversocket.accept()

    print ("Got a connection from %s" % str(addr))

    msg = "Thank you for connecting" + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
"""
