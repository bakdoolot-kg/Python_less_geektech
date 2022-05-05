
class Car:

    current_speed = 0

    """ __init__ - это Dunder method """
    def __init__(self, title, model, max_speed, color):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'{self.title} {self.model} start engined!')

    def gas(self):
        self.current_speed += 20
        print(self.current_speed)

#Instance Car
bmw = Car('BMW', 'x5 e53', 350, 'BLACK')
bmw.start_engine()
bmw.gas()
bmw.gas()

mercedes = Car('Mercedes-Benz', 'e63 //AMG', 400, 'BLUE')