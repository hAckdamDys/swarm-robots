import numpy as np

# grid corresponding to actuall map where robots move and put blocks
class BuildingGrid:
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height
        # grid will have 0 if nothing is on given tile
        # and index of tile otherwise
        self.grid = np.zeros((width,height),int)
        self.tiles = [dict(),dict()]
        self.lastTileIndex = 0
        # robots are on separate layer on grid to simplify things
        self.robots = [dict(),dict()]
        self.lastRobotIndex=0

    def addTile(self, tile):
        self.lastTileIndex += 1
        self.tiles[0][self.lastTileIndex] = tile
        self.tiles[1][tile] = self.lastTileIndex

    def addRobot(self, robot):
        self.lastRobotIndex += 1
        self.robots[0][self.lastRobotIndex] = robot
        self.robots[1][robot] = self.lastRobotIndex
