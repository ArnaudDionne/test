"""Minimal game engine loop and management."""

from typing import List, Optional

import pygame

from .world import World
from .entity import Entity
from .renderer import Renderer


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

    def run(self, steps: Optional[int] = 1) -> None:
        """Run the game loop.

        If ``steps`` is ``None``, run with a Pygame window until quit.
        Otherwise, advance the simulation for the given number of steps.
        """
        self.running = True

        if steps is None:
            renderer = Renderer(self.world, self.entities)
            clock = pygame.time.Clock()
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.stop()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.stop()
                        self._handle_movement(event)

                self.step()
                renderer.render()
                clock.tick(60)
            renderer.shutdown()
            return

        for _ in range(steps):
            if not self.running:
                break
            self.step()

    def stop(self) -> None:
        self.running = False

    def _handle_movement(self, event: pygame.event.Event) -> None:
        """Handle arrow key movement for the first entity, if any."""
        if not self.entities:
            return
        player = self.entities[0]
        if event.key == pygame.K_UP:
            player.move(0, -1, self.world)
        elif event.key == pygame.K_DOWN:
            player.move(0, 1, self.world)
        elif event.key == pygame.K_LEFT:
            player.move(-1, 0, self.world)
        elif event.key == pygame.K_RIGHT:
            player.move(1, 0, self.world)
