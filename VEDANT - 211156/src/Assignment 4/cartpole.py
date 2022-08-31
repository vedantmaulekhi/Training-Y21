import sys
sys.path.append('/home/gym') 
# location of the module needed to be added to import gym
import gym
from matplotlib import pyplot as plt
env = gym.make("CartPole-v1")
observation = env.reset()

kp = 150
ki = 100
kd = 50

force = 0
integral = 0
for _ in range(30000):
  env.render()

  observation, reward, done, info = env.step(force)

  velocity = observation[1]
  angle = observation[2]
  angular_velocity = observation[3]

  integral = integral + angle

  F = kp*(angle) + kd*(angular_velocity) + ki*(integral)

  force = 1 if F > 0 else 0
  if done:
    observation = env.reset()
    integral = 0
env.close()
