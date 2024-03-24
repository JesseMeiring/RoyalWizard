from actor import Actor

class Team:
    def __init__(self, name: str) -> None:
        self.name = name
        self.members: list[Actor] = []