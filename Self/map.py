# Self Driving car

# Import libraries

import numpy as np
from random import random, randint
import matplotlib.pyplot as plt
import time

# import kivy packages
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

# Import the DQN object from AI.py

# from ai import Dqn

# Disable right click for kivy
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# Introduce last_x and last_y variabl;es which keep track of the last point in memory when we draw the track on the map

last_x = 0
last_y = 0
n_points = 0  # Total number of points in the last drawing
length = 0  # Length of the last map

# Get our AI which contains the neural network
brain = Dqn(5, 3, 0.9) # 5 sensors, 3 actions, gamma = 0.9
action2rotation = [0,20,-20] #action = 0 = => no rotation action = 1 => rotate 20 degrees, action = 2 => rotate -20 degrees
last_reward = 0 # initialize the last reward
scores =  [] # Initialize the mean score curve with respect to time

# Init the map
first_update = True #Init the map only once
ef init():
    global sand #Sand is an array that has as many cells as our graphic interface has pixels. Each cell has a one if there is sand, 0 otherwise