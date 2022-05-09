class Transport:
    _current_speed = 0

    def __init__(self, title, model, type, engine, max_speed):
        self.title = title
        self.model = model
        self.type = type
        self.engine = engine
        self.max_speed = max_speed

    def _get_current_speed(self):
        print(self._current_speed)

    def info(self):
        print(f'{self.title}\n{self.model}\n{self.type}\n{self.engine}\n')

    def gas(self):
        if self._current_speed + 50 >= self.max_speed:
            print('Check ON!')
        else:
            self._current_speed += 50
            self._get_current_speed()

class Car(Transport):

    def __init__(self, title, model, type, engine,max_speed, color):
        super().__init__(title, model, type, engine, max_speed)
        self.color = color

    def info(self):
        print(f"""
            Car name: {self.title} {self.model}
            Type: {self.type}
            Color: {self.color}
        """)


class Airplane(Transport):
    pass


bmw = Car("BMW", 'e38', 'car', 'v8', 350, 'WHITE')

boeing = Airplane('Boeing', 'x888', 'Airplane', 'v120', 1000)
