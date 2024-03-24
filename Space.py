from actor import Actor
from pygame import Surface, Vector2, image
from Team import Team

class Space:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.actors: list[Actor] = []
        self.floor: Surface
        self.neighborSpaces: list[Space] = []

    def drawActors(self, onto: Surface, screenPosition: Vector2):
        if self.floor is not None:
            onto.blit(self.floor, screenPosition)
        for actor in self.actors:
            if actor.sprite is not None:
                onto.blit(actor.sprite, screenPosition)
    
    def traversable(self, team: Team = None):
        for actor in self.actors:
            if Team is not None and actor.team != team and not actor.passable:
                return False
        return True