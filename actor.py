from pygame import Surface, Vector2
# from Team import Team

class Actor:
    def __init__(self) -> None:
        self.sprite: Surface
        self.position: Vector2
        self.conditions = []
        self.isPlayer: bool = False
        self.actions = []
        # self.team: Team
        self.passable: bool = False