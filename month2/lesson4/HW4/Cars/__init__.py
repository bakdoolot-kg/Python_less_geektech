try:
    CAR_USER = {
        "car": input('Car name: ') or "unknown car",
        "engine": input('Car engine: ') or "unknown engine",
        "color": input('Car color: ') or "unknown color",
        "max_speed": int(input('Car max speed: ')) or "unknown max speed",
    }
except ValueError:
    print(f'Неверные данные')