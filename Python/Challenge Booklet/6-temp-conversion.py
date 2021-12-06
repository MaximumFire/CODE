#Temp Conversion
class Temp():
    def __init__(self, type, value):
        self.type = type.lower()
        self.value = value
    def convert(self):
        result = 0
        if self.type == "celcius":
            choice = input(f"What would you like to convert celcius to? (kelvin/fahrenheit)? ").lower()
            if choice == "kelvin":
                result = self.value + 273.15
                return result
            else:
                part0 = 9/5
                part1 = self.value * part0
                result = part1 + 32
                return result
        elif self.type == "kelvin":
            choice = input(f"What would you like to convert kelvin to? (celcius/fahrenheit)? ").lower()
            if choice == "celcius":
                result = self.value - 273.15
                return result
            else:
                part0 = self.value - 273.15
                part1 = 9/5
                result = part0 * part1 + 32
                return result
        else:
            choice = input(f"What would you like to convert fahrenheit to? (kelvin/celcius)? ").lower()
            if choice == "kelvin":
                part0 = self.value - 32
                part1 = 5/9
                result = part0 * part1 + 273.15
                return result
            else:
                part0 = self.value - 32
                part1 = 5/9
                result = part0 * part1
                return result

temp1 = Temp("celcius", 25)
print(temp1.convert())