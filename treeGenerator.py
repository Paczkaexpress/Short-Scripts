import matplotlib.pyplot as plt
import math
import random

class PointPosition:
    x = 0
    y = 0

    def __str__(self):
        return "x: {}, y: {}".format(self.x,self.y)


class Tree:
    pass

class Joint:
    # needs to have angle -> init and chaning
    # lenght -> const
    # child -> connected joints

    leftNode = None
    rightNode = None

    def __init__(self, originPos, length, angle):
        self.originPos = originPos
        self.length = length
        self.angle = angle

        self.endPos = PointPosition()
        self.updateEndPos()

    def updateEndPos(self):
        self.endPos.x = self.originPos.x + self.length * math.sin(self.angle)
        self.endPos.y = self.originPos.y + self.length * math.cos(self.angle)

    def generateTree(self, numberOfLayers):
        print(self.endPos)

        if numberOfLayers <= 0:
            return

        branchNumber = random.randrange(0, 20)
        print(branchNumber)

        if branchNumber == 0:
            self.leftNode = None
            self.rightNode = None
        elif branchNumber % 6 == 1:
            self.leftNode = Joint(self.endPos, self.length/(8-numberOfLayers), random.random()-0.5)
            self.leftNode.generateTree(numberOfLayers - 1)
            print("Left node: {}".format(self.leftNode))
        elif branchNumber % 6 == 2:
            self.rightNode = Joint(self.endPos, self.length/(8-numberOfLayers), random.random()-0.5)
            self.rightNode.generateTree(numberOfLayers - 1)
            self.leftNode = None
            print("Right node: {}".format(self.rightNode))
        else:
            self.leftNode = Joint(self.endPos, self.length/(8-numberOfLayers), random.random()-0.5)
            self.leftNode.generateTree(numberOfLayers - 1)
            self.rightNode = Joint(self.endPos, self.length/(8-numberOfLayers), random.random()-0.5)
            self.rightNode.generateTree(numberOfLayers - 1)
            print("Left node: {}".format(self.leftNode))
            print("Right node: {}".format(self.rightNode))
        return

def dfs(node):
    # what should be returned / printed ?
    # I need position from every node to be printed
    if node.leftNode == None and node.rightNode == None:
        return

    plt.plot([node.originPos.x, node.endPos.x],
             [node.originPos.y, node.endPos.y])

    if node.leftNode != None:
        print(node.leftNode.originPos)

        dfs(node.leftNode)
    if node.rightNode != None:
        print(node.rightNode.originPos)
        dfs(node.rightNode)


if __name__ == '__main__':
    print("Generate tree")

    iter = 10

    # plt.plot()
    # plt.draw()
    # plt.show()

    rootPos = PointPosition()
    root = Joint(rootPos, 10, 0)

    # how to generate tree?
    # method generate?

    root.generateTree(7)

    print(root)

    while iter > 0:
        iter -= 1
        axes = plt.gca()
        axes.set_xlim([-15, 15])
        axes.set_ylim([0, 30])
        plt.draw()
        plt.pause(0.01)

        dfs(root)