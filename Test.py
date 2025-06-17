from engine import Game, Entity

if __name__ == "__main__":
    game = Game(5, 5)
    player = Entity(2, 2, "@")
    game.add_entity(player)
    game.run(steps=1)
    print(f"Player location: {player.x}, {player.y}")

