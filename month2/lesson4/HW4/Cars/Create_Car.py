class Car:

    def __init__(self,
                 car: str,
                 engine: str,
                 color: str,
                 max_speed: int
                 ):
        self.car = car
        self.engine = engine
        self.color = color
        self.max_speed = max_speed

    def start_engine(self):
        print(f'car: {self.car}, engine: {self.engine} started')

    def stop_engine(self):
        print(f'car: {self.car}, engine: {self.engine} started')


def create_car_def(
        car: str,
        engine: str,
        color: str,
        max_speed: int,
) -> Car:
    return Car(car, engine, color, max_speed)
