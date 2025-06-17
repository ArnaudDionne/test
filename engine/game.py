"""Minimal game engine loop and management."""

from typing import List

from .world import World
from .entity import Entity


class Game:
    """A very small game engine managing the world and entities."""

    def __init__(self, width: int = 10, height: int = 10) -> None:
        self.world = World(width, height)
        self.entities: List[Entity] = []
        self.running = False

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)

    def step(self) -> None:
        """Advance the simulation by one tick."""
        for entity in self.entities:
            # For now, entities do nothing in each step.
            pass

    def run(self, steps: int = 1) -> None:
        self.running = True
        for _ in range(steps):
            if not self.running:
                break
            self.step()

    def stop(self) -> None:
        self.running = False
