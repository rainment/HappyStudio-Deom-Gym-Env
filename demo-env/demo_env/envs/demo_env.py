import gym
from gym import error, spaces, utils
from gym.utils import seeding
import random

class DemoEnv(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		self.state = []
		for i in range(10):
			self.state.append(0)
		self.count = 0
		self.done = 0
		self.info = {'action': 0, 'count': self.count}
		self.reward = 0
		self.action_space = spaces.Discrete(3)
		self.observation_space = spaces.MultiDiscrete([3]*10)

	def setseed(self, seed):
		random.seed(seed)

	def step(self, action):
		self.reward = 0
		self.info = {'action': action, 'count': self.count}
		if self.done == 1:
			print("Game Over")
			return [self.state, self.reward, self.done, self.info]
		else:
			
			self.count += 1
			self.reward = 0
			winner = self.count%3 #random.randint(0,2) #self.count%3
			if action == winner:
				self.reward = 1 # normalization
				
			for i in range(9):
				self.state[9-i] = self.state[9-i-1]
			
			self.state[0] = winner	
	 
			if self.count > 101:
				self.done = 1

		return [self.state, self.reward, self.done, self.info]

	def reset(self):
		for i in range(10):
			self.state[i] = 0
		self.count = 0
		self.done = 0
		self.info = {'action': 0, 'count': self.count}
		self.reward = 0
		return self.state

	def render(self):
		for i in range(10):
			print(self.state[i],end=" ")
		# print("")
		print("step:",self.count,"reward:",self.reward)

