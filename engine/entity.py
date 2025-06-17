"""Base entity classes used in the game engine."""

from dataclasses import dataclass

@dataclass
class Entity:
    x: int
    y: int
    char: str = "@"

    def move(self, dx: int, dy: int, world) -> None:
        """Move the entity by the given delta if the target tile is walkable."""
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < world.width and 0 <= ny < world.height:
            tile = world.get_tile(nx, ny)
            if tile.walkable:
                self.x, self.y = nx, ny
