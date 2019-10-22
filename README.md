# HappyStudio-Deom-Gym-Env
This is an implementation of a Demo game as a gym environment. It can be used to make the computer learn playing this Demo game.



First you need Gym-Env

http://gym.openai.com/docs/

Then to install the environment, just go to the demo-env folder and run the command 

pip install -e .

This will install the gym environment. Now, we can use our gym environment with the following 

import gym
import demo_env
env = gym.make('demo-v0')
