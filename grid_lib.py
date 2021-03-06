from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))
