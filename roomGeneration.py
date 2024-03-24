from TileType import TileType

def makeASquareRoom(size: int) -> list[list[TileType]]:
    return makeARoom(size, size)

def makeARoom(width: int, height: int) -> list[list[TileType]]:
    room: list[list[TileType]] = []
    for y in range(height):
        roomRow: list[TileType] = []
        for x in range(width):
            leftSide: bool = x == 0
            rightSide: bool = x == width - 1
            topSide: bool = y == 0
            bottomSide: bool = y == height - 1
            if(leftSide or bottomSide or topSide or rightSide):
                roomRow.append(TileType.Wall)
            else:
                roomRow.append(TileType.Floo)
        room.append(roomRow)
    return room