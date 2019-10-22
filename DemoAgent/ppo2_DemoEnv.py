import os

from demo_env.envs.demo_env import DemoEnv
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines import PPO2

def train():
    n_cpu = os.cpu_count()
    env = SubprocVecEnv([lambda: DemoEnv() for i in range(n_cpu)])
    model = PPO2(MlpPolicy, env, verbose=1, policy_kwargs={'net_arch': [dict(vf=[4], pi=[4])]})
    model.learn(total_timesteps=int(1e6))
    model.save("ppo2_DemoEnv")
    env.close()
    del model

def run():
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

if __name__ == '__main__':
    train()
    run()