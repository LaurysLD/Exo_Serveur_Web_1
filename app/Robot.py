class Robot:
    def __init__(self, name="Robo", mode="idle", speed=0):
        self.name = name
        self.mode = mode
        self.speed = speed

    def update(self, name, mode, speed):
        self.name = name
        self.mode = mode
        self.speed = speed

    def as_dict(self):
        return {
            "name": self.name,
            "mode": self.mode,
            "speed": self.speed,
        }
