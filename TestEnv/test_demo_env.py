import gym
import demo_env
env = gym.make('demo-v0')
env.setseed(10)
for i_episode in range(1):
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
