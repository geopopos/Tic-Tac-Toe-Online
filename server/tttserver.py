import socket, sys, threading, time

from Room import Room

from Player import Player

player_id = 0
room_id = 0
PLAYERS = []
ROOMS = []
clientThreads = []

host = socket.gethostname()

port = int(sys.argv[1])

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created")

try:
    serversocket.bind((host, port))
except(socket.error, msg):
    print("Bind failed. Error Code: " + str(msg[0]) + " Message " + msg[1])
    sys.exit

print("Socket Bind Complete")

serversocket.listen(2)

print("Socket now listening")

class ClientThread(threading.Thread):
    def __init__(self, conn, player_id, room_id):
        super(ClientThread, self).__init__()
        self.player = Player(player_id, conn)
        PLAYERS.append(self.player)
        player_id += 1
        if len(ROOMS) == 0 or ROOMS[-1].size == ROOMS[-1].maxSize:
            self.room = Room(room_id, 2)
            ROOMS.append(self.room)
            self.player.setRoom(self.room.ID)
            room_id += 1

    def run(self):
        while True:
            print(conn.recv(1024))
        conn.close()
    

while True:
    #establish a connection
    conn, addr = serversocket.accept()

    print ("Got a connection from %s" % str(addr))

    clientThread = ClientThread(conn, player_id, room_id)

    clientThread.start()

serversocket.close()

    
    
