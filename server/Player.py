class Player:
    def __init__(self, ID, conn):
        self.ID = ID
        self.conn = conn
        self.room = None

    def setRoom(self, room):
        self.room = room
