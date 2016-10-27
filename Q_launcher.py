import game
from Q_trainer import QTrainer
from game_handler import GameHandler

trainer = QTrainer(size=4, epochs=10)
print(trainer.Q)

GameHandler(size=4, player=trainer)
