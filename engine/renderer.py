"""Simple Pygame renderer for the tile-based engine."""

from __future__ import annotations

import pygame

from .world import World
from .entity import Entity

TILE_SIZE = 32

class Renderer:
    """Handles drawing of the world and entities using Pygame."""

    def __init__(self, world: World, entities: list[Entity]) -> None:
        self.world = world
        self.entities = entities
        pygame.init()
        self.screen = pygame.display.set_mode(
            (world.width * TILE_SIZE, world.height * TILE_SIZE)
        )
        pygame.display.set_caption("Game")
        self.font = pygame.font.SysFont(None, 24)

    def draw_world(self) -> None:
        for y in range(self.world.height):
            for x in range(self.world.width):
                tile = self.world.get_tile(x, y)
                color = (200, 200, 200) if tile.walkable else (100, 100, 100)
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, color, rect)

    def draw_entities(self) -> None:
        for entity in self.entities:
            text = self.font.render(entity.char, True, (0, 0, 0))
            self.screen.blit(text, (entity.x * TILE_SIZE, entity.y * TILE_SIZE))

    def render(self) -> None:
        self.screen.fill((0, 0, 0))
        self.draw_world()
        self.draw_entities()
        pygame.display.flip()

    def shutdown(self) -> None:
        pygame.quit()
