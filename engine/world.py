"""World and Tile classes for the game engine."""

from dataclasses import dataclass, field

@dataclass
class Tile:
    """Represents a single tile in the world grid."""
    name: str = "empty"
    walkable: bool = True

@dataclass
class World:
    """A simple 2D grid world made of tiles."""
    width: int
    height: int
    tiles: list = field(init=False)

    def __post_init__(self) -> None:
        self.tiles = [[Tile() for _ in range(self.width)] for _ in range(self.height)]

    def get_tile(self, x: int, y: int) -> Tile:
        return self.tiles[y][x]

    def set_tile(self, x: int, y: int, tile: Tile) -> None:
        self.tiles[y][x] = tile
