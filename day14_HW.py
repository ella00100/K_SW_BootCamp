# prob 10.10

class Laser:
    def does(self):
        return "'disintegrate' (Laser)"

class Claw:
    def does(self):
        return "'crush' (Claw)"

class Smartphone:
    def does(self):
        return "'ring' (Smartphone)"

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()

    def does(self):
        print(self.laser.does())
        print(self.claw.does())
        print(self.smartphone.does())

r = Robot()
r.does()