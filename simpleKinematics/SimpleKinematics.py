import matplotlib.pyplot as plt
import math
import time

class Point:
	x = 0.0
	y = 0.0

	def __str__(self):
		return "x: {}, y: {}".format(self.x, self.y)

class Joint:

	def __init__(self, parent, length, angle):
		self.originPos = Point()
		self.endPos = Point()

		if parent != None:
			self.parent = parent
			self.length = length
			self.angle = angle

			self.updatePosition()
			self.calculateEndPos()
		else:
			self.parent = None
			self.length = 0
			self.angle = 0


		print("Origin: {}, length: {}, angle: {}".format(self.originPos, self.length, self.angle))

	def updatePosition(self):
		if self.parent is not None:
			self.originPos.x = self.parent.endPos.x
			self.originPos.y = self.parent.endPos.y
		else:
			self.originPos.x = 0
			self.originPos.y = 0

	def calculateEndPos(self):
		if self.parent is not None:
			self.endPos.x = self.originPos.x + self.length * math.sin(self.angle)
			self.endPos.y = self.originPos.y - self.length * math.cos(self.angle)
		else:
			self.endPos.x = 0
			self.endPos.y = 0

	def updateAngle(self, angle):
		if self.parent != None:
			self.angle = angle + self.parent.angle
		else:
			self.angle = 0

if __name__ == '__main__':
	print("Simple Kinematics")

	print("Create origin joint")
	joint = []
	joint.append(Joint(None, 0, 0))

	numberOfJoins = 10

	for j in range(numberOfJoins):
		joint.append(Joint(joint[j], 5/(j+1) , math.pi))

	angle = 0

	while(1):
		angle += 0.01
		print(angle)
		plt.clf()

		for j in joint:
			j.updateAngle(angle)
			j.calculateEndPos()
			j.updatePosition()
			plt.plot([j.originPos.x, j.endPos.x], [j.originPos.y, j.endPos.y])
		# plt.plot([joint1.originPos.x,joint1.endPos.x],[joint1.originPos.y, joint1.endPos.y])
		# plt.plot([joint2.originPos.x, joint2.endPos.x], [joint2.originPos.y, joint2.endPos.y])
		axes = plt.gca()
		axes.set_xlim([-15,15])
		axes.set_ylim([-15,15])
		plt.draw()
		plt.pause(0.01)
