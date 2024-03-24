from Space import Space
from TileType import TileType
from typing import Dict
from pygame import image, Surface

class Map:
    def __init__(self, width, height, depth) -> None:
        self.spaces: list[list[list[Space]]] = []
        self.imageDictionary: Dict[TileType, Surface] = self.initiateImageDict() #make this a seperate class that is given upon initilzation
        self.buildBlankMap(width, height, depth)

    def buildBlankMap(self, width: int, height: int, depth: int):
        for z in range(depth):
            plane: list[list[Space]] = []
            for y in range(height):
                row: list[Space] = []
                for x in range(width):
                    s = Space(x, y, z)
                    s.floor = self.imageDictionary[TileType.Void]
                    row.append(s)
                plane.append(row)
            self.spaces.append(plane)
    
    def buildARoom(self, locationX: int, locationY: int, locationZ: int, width: int, height: int):
        for y in range(height):
            for x in range(width):
                leftSide: bool = x == 0
                rightSide: bool = x == width - 1
                topSide: bool = y == 0
                bottomSide: bool = y == height - 1
                if(leftSide or bottomSide or topSide or rightSide):
                    self.spaces[locationZ][locationY + y][locationX + x].floor = self.imageDictionary[TileType.Wall]
                else:
                    self.spaces[locationZ][locationY + y][locationX + x].floor = self.imageDictionary[TileType.Floo]

    def initiateImageDict(self) -> Dict[TileType, Surface]:
        imageDict: Dict[TileType, Surface] = {
            TileType.Floo: image.load('Assets/Floor.bmp').convert(),
            TileType.Wall: image.load('Assets/Wall.bmp').convert(),
            TileType.Void: image.load('Assets/Void.bmp').convert(),
        }
        return imageDict
    
    def drawPlane(self, planeDepth: int, ontoSurface: Surface):
        tileX: int = 0
        tileY: int = 0
        tileSize: int = 16
        plane: list[list[Space]] = self.spaces[planeDepth]
        for row in plane:
            tileX = 0
            for s in row:
                ontoSurface.blit(s.floor, (tileX, tileY))
                tileX += tileSize
            tileY += tileSize