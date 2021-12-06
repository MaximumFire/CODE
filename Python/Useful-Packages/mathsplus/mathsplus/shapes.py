class Shapes():
    def __init__(self, num_sides):
        self.num_sides = num_sides
        
    def sum_interior(self):
        return 180 * (self.num_sides - 2)
    
    def one_interior(self):
        return 180 * (self.num_sides - 2) / self.num_sides

    def one_exterior(self):
        return 360 / self.num_sides
