import random

class player:
    def __init__(self, spawn, id):

        self.position = [spawn[0], spawn[1]]
        self.colour = self.generate_random_hex()
        self.id = id

        if(id == 0):
            self.controls = ["W", "A", "S", "D"]
        elif(id == 1):
            self.controls = [""]


    def generate_random_hex(self) -> str:
        """
        Generate a random color in hexadecimal format (#RRGGBB).
        """
        # Generate random values for red, green, and blue components
        red:int = random.randint(0, 255)
        green:int = random.randint(0, 255)
        blue:int = random.randint(0, 255)

        # Convert the values to hexadecimal format and concatenate them
        color_hex:str = f"#{red:02x}{green:02x}{blue:02x}"

        return color_hex
    
    def move(self, direction:str):

        if(direction == "up"):
            self.position[0] -= 1
        elif(direction == "down"):
            self.position[0] += 1
        elif(direction == "left"):
            self.position[1] -= 1
        elif(direction == "right"):
            self.position[1] += 1

        print("new position: ", self.position)