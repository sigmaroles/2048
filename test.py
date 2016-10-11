from main import Main
from trainer import Trainer

n = 3

t = Trainer()
nn = t.train(1000, size=n)
print(nn.neural_network)
m = Main(neural_network=nn, size=n)
