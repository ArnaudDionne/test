from engine import Game, Entity

if __name__ == "__main__":
    game = Game(10, 10)
    player = Entity(5, 5, "@")
    game.add_entity(player)
    # Run with a Pygame window until it is closed
    game.run(steps=None)

