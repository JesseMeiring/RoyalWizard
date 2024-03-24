

class Action:
    def __init__(self) -> None:
        self.name: str = "Walk"
        self.description: str = "Move to an adjacent space"
        self.range: int = 1