import matplotlib.pyplot as plt
import numpy as np


class SSR:
	def __init__(self, width):
		self.width = width
		self.vel_left = 0
		self.vel_right = 0
		self.theta = [0]
		self.x_pos = [0]
		self.y_pos = [0]

	def x_vel(self):
		return -1 * (self.vel_right + self.vel_left) / 2 * np.sin(self.theta[-1])

	def y_vel(self):
		return (self.vel_right + self.vel_left) / 2 * np.cos(self.theta[-1])

	def theta_vel(self):
		return (self.vel_right - self.vel_left) / self.width

	def step(self, time, dt=0.1):
		for i in range(time):
			self.x_pos.append(self.x_pos[-1] + self.x_vel() * dt)
			self.y_pos.append(self.y_pos[-1] + self.y_vel() * dt)
			self.theta.append(self.theta[-1] + self.theta_vel() * dt)


def a():
	r = SSR(0.3)

	r.vel_left = 1.0
	r.vel_right = 1.5
	r.step(50)

	r.vel_left = -1.0
	r.vel_right = -1.5
	r.step(30)

	r.vel_left = 0.8
	r.vel_right = -2
	r.step(80)

	r.vel_left = 2
	r.vel_right = 2
	r.step(100)

	plt.plot(r.x_pos, r.y_pos)
	plt.show()


def b():
	r = SSR(0.3)

	for i in range(10):
		# go straight 5 meters
		r.vel_left = 1
		r.vel_right = 1
		r.step(5000, 0.001)

		# turn right 90 degrees
		r.vel_left = 0.5
		r.vel_right = -0.5
		r.step(471, 0.001)

		# go stright 0.25m
		r.vel_left = 1
		r.vel_right = 1
		r.step(250, 0.001)

		# turn right 90 degrees
		r.vel_left = 0.5
		r.vel_right = -0.5
		r.step(471, 0.001)

		# go straight 5 meters
		r.vel_left = 1
		r.vel_right = 1
		r.step(5000, 0.001)

		# turn left 90 degrees
		r.vel_left = -0.5
		r.vel_right = 0.5
		r.step(471, 0.001)

		# go stright 0.25m (length of robot)
		r.vel_left = 1
		r.vel_right = 1
		r.step(250, 0.001)

		# turn left 90 degrees
		r.vel_left = -0.5
		r.vel_right = 0.5
		r.step(471, 0.001)

	# go straight 5 meters
	r.vel_left = 1
	r.vel_right = 1
	r.step(5000, 0.001)


	plt.plot(r.x_pos, r.y_pos)
	plt.show()


def c():
	r = SSR(0.3)

	for i in range(10):
		# go straight 5 meters
		r.vel_left = 1
		r.vel_right = 1
		r.step(5000, 0.001)

		# turn right 90 degrees
		r.theta.append(-np.pi/2)

		# go stright 0.3m (length of robot)
		r.vel_left = 1
		r.vel_right = 1
		r.step(250, 0.001)

		# turn right 90 degrees
		r.theta.append(-np.pi)

		# go straight 5 meters
		r.vel_left = 1
		r.vel_right = 1
		r.step(5000, 0.001)

		# turn left 90 degrees
		r.theta.append(-np.pi/2)

		# go stright 0.3m (length of robot)
		r.vel_left = 1
		r.vel_right = 1
		r.step(250, 0.001)

		# turn left 90 degrees
		r.theta.append(0)

	# go straight 5 meters
	r.vel_left = 1
	r.vel_right = 1
	r.step(5000, 0.001)

	plt.plot(r.x_pos, r.y_pos)
	plt.show()




if __name__== "__main__":
	a()
	b()
	c()


	







