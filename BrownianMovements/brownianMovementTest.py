import matplotlib.pyplot as plt
import random
import math
import time

class PointPosition:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: {}, y: {}".format(self.x,self.y)


class BrownianTraversal:
    def __init__(self):
        self.pos = PointPosition(0,0)

    def update_position(self):
        self.pos.x += random.random() - 0.5
        self.pos.y += random.random() - 0.5

if __name__ == '__main__':
    print("Implementation of a simple brownian movements and its representation in 2d plot")

    bt = BrownianTraversal()

    iter = 500
    xPos = []
    yPos = []

    while iter > 0:
        iter -= 1

        bt.update_position()
        xPos.append(bt.pos.x)
        yPos.append(bt.pos.y)
        axes = plt.gca()
        axes.set_xlim([-15, 15])
        axes.set_ylim([-15, 15])
        plt.draw()
        plt.pause(0.01)
        # plt.plot(bt.pos.x, bt.pos.y)
        plt.plot(xPos   , yPos , 'b')

        # time.sleep(0.01)