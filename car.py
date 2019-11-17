import matplotlib.pyplot as plt
class Car(object):
    def __init__(self, position, velocity, world, color ='r'):
        self.state = [position,velocity]
        self.world = world

        self.color = color

        self.path = []
        self.path.append(position)

    def move(self, dt=1):
        height = len(self.world)
        width = len(self.world[0])

        position = self.state[0]
        velocity = self.state[1]

        predicted_position =[
                (position[0]+velocity[0]*dt)%height,
                (position[1]+velocity[1]*dt)%width
            ]

        self.state = [predicted_position, velocity]
        self.path.append(predicted_position)
    def turn_left(self):
        velocity = self.state[1]
        predicted_velocity = [
            -velocity[1],
            velocity[0]
        ]
        self.state[1] = predicted_velocity

    def display_world(self):

        position = self.state[0]

        plt.matshow(self.world, cmap='gray')

        ax=plt.gca()
        rows = len(self.world)
        cols = len(self.world[0])
