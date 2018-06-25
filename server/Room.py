class Room:
    def __init__(self, ID, maxSize):
        self.ID = ID
        self.size = 0
        self.maxSize = 2
        self.players = []
        self.board = [" " for i in range(9)]

    def addPlayer(self, player):
        if (self.size <maxSize):
            self.players.append(player)
            self.size += 1
            return "Room Success: Player " + str(player) + " added to room"
        else:
            return "Room Error: room is already at maximum capacity"

    def removePlayer(self, player):
        if player in players:
            self.players.remove(player)
            return "Room Success: Player successfully removed!"
        else:
            return "Room Error: player is not currently in this room..."
