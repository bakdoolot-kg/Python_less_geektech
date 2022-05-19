try:
    from Cars import Create_Car, get_car_info, CAR_USER

    user_car = Create_Car.create_car_def(**CAR_USER)
    get_car_info.CarInfo.car_info(user_car)

except:
    print('Ошибка. Введите данные снова!')
