class Car:

    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'{self.title} {self.model} engine started!')

    def stop_engine(self):
        print(f'{self.title} {self.model} engine stoped!')

    def info(self):
        print(f'{self.title}\n'
              f'{self.model}\n'
              f'Weight: {self.weight} kg\n'
              f'HP: {self.hp}\n'
              f'Torque nm: {self.nm}\n'
              f'Max speed: {self.max_speed}\n'
              f'Color: {self.color}')

# TESLA
tesla = Car('Tesla', 'Model S Plaid', 2161.81, 1020, 527, 175, 'RED')

tesla.start_engine()
tesla.stop_engine()

tesla.info()
# TOYOTA
toyota = Car('Toyota', 'Prius', 1530, 121, 142, 101, 'WHITE')

toyota.start_engine()
toyota.stop_engine()

toyota.info()