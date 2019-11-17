class Ai:
    def __init__(self):
        print("I am Ai")
        
    class Brain:
        def __init__(self):
            print("I am Brain")
        def mywork(self):
            print("I am For calculation")

obj_ai = Ai()
Ai.Brain().mywork()
