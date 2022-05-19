class CarInfo:
    def __init__(self, car, engine, color, max_speed):
        self.car = car
        self.engine = engine
        self.color = color
        self.max_speed = max_speed

    def car_info(self):
        print(f"""
        Car name: {self.car}
        Engine: {self.engine}
        Color: {self.color}
        Max speed: {self.max_speed | 0}
        """)