import os
import gym
import demo_env
from stable_baselines import DQN
from demo_env.envs.demo_env import DemoEnv
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines import PPO2

def run_dqn_policy():
    env = DummyVecEnv([lambda: DemoEnv()])
    model = DQN.load("deepq_DemoEnv", env)
    obs = env.reset()
    sum_rew = 0
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render()
        sum_rew += rewards[0]
        if dones[0] == True:
            print("Total reward: ", sum_rew)
            break
    return sum_rew

def run_ppo2_policy():
    env = DummyVecEnv([lambda: DemoEnv()])
    model = PPO2.load("ppo2_DemoEnv", env)
    obs = env.reset()
    sum_rew = 0
    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render()
        sum_rew += rewards[0]
        if dones[0] == True:
            print("Total reward: ", sum_rew)
            break
    env.close()
    return sum_rew

def run_random_policy():
    env = gym.make('demo-v0')
    env.reset()
    sum_rew = 0
    while True:        
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        env.render()
        sum_rew += reward 
        if done == True:
            print("Total reward: ", sum_rew)
            break
    env.close()
    return sum_rew   	

if __name__ == '__main__':
    reward_ppo = run_ppo2_policy()
    print("------Line-----")
    reward_random = run_random_policy()
    print("------Line-----")
    reward_dqn = run_dqn_policy()
    print("------Line-----")
    print("RL_ppo reward: ", reward_ppo)
    print("RL_dqn reward: ", reward_dqn)
    print("Random_policy reward: ", reward_random)
