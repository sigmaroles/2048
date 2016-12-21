from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
from game_handler import GameHandler
from ai import AIPlayer
import random
import game
import numpy as np

model = Sequential()
model.add(Dense(64, init='lecun_uniform', input_shape=(16,)))
model.add(Activation('relu'))
# model.add(Dropout(0.2)) I'm not using dropout, but maybe you wanna give it a try?

model.add(Dense(64, init='lecun_uniform'))
model.add(Activation('relu'))
# model.add(Dropout(0.2))

model.add(Dense(4, init='lecun_uniform'))
model.add(Activation('linear'))  # linear output so we can have range of real-valued outputs

rms = RMSprop()
model.compile(loss='mse', optimizer=rms)

epochs = 10000
gamma = 0.9  # since it may take several moves to goal, making gamma high
epsilon = 1
for i in range(epochs):
    randomState = np.random.RandomState(0)
    state = game.init_board(size=4, state=randomState)
    status = 1
    c = 0
    # while game still in progress
    while status == 1:
        c += 1
        # We are in state S
        # Let's run our Q function on S to get Q values for all possible actions
        qval = model.predict(state.reshape(1, 16), batch_size=1)
        if random.random() < epsilon:  # choose random action
            action = np.random.randint(0, 4)
        else:  # choose best action from Q(s,a) values
            action = np.argmax(qval)

        # Take action, observe new state S'
        score = game.play_move(state, action, randomState)
        # Observe reward
        reward = game.get_reward(state, score)
        # Get max_Q(S',a)
        newQ = model.predict(state.reshape(1, 16), batch_size=1)
        maxQ = np.max(newQ)
        y = np.zeros((1, 4))
        y[:] = qval[:]

        if score == 0:
            update = np.exp(c)
        else:
            update = score + gamma * maxQ

        y[0][action] = update  # target output
        model.fit(state.reshape(1, 16), y, batch_size=1, nb_epoch=1, verbose=0)
        if score == 0:
            status = 0

    if i % 10 == 0:
        print("Game #: %s Score: %s" % (i, c))
    epsilon -= 1 / epochs

randomState = np.random.RandomState(0)
GameHandler(size=4, player=AIPlayer(model), state=randomState)
