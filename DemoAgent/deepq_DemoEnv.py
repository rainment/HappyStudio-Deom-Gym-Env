from demo_env.envs.demo_env import DemoEnv
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN

def train():
    env = DummyVecEnv([lambda: DemoEnv()]) # DQN does not support parrelization through SubprocVecEnv
    model = DQN(MlpPolicy, env, verbose=1, policy_kwargs={'layers': [4]})
    model.learn(total_timesteps=int(2e5))
    model.save("deepq_DemoEnv")
    env.close()
    del model

def run():
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

if __name__ == '__main__':
    train()
    run()