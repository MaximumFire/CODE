class Pi():
    def __init__(self, radius, pi_value, type):
        self.radius = radius
        self.pi_value = pi_value
        self.type = type
    
    def diameter(self):
        return self.radius * 2
    
    def circumference(self):
        return 2 * self.pi_value * self.radius
    
    def area(self):
        if self.type == "circle":
            return self.pi_value * self.radius * self.radius
        else:
            print("You can't find the area of a sphere!")
            return

    def volume_of_sphere(self):
        if self.type == "sphere":
            part1 = 4/3
            part2 = self.pi_value * self.radius**3
            return part1 * part2
        else:
            print("You can't find the volume of a circle!")
            return