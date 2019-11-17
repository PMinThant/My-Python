import numpy as np
import car
import matplotlib 
#Creat the 2D world
height = 4
width = 6
world = np.zeros((height,width))

#Define initial car state
initial_position = [0,0] #[y,x] (top left corner)
velocity = [0,1]#[vy,vx] (moving to the right)
carla = car.Car(initial_position, velocity, world)
print("Carla/'s initial state is:"+str(carla.state))
carla.display_world()
