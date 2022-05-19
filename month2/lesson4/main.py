# import math
# import datetime
#
# num = 9
# print(math.sqrt(num))
# print(math.pi)
# print(math.cos(6.5))
#
# print(datetime.datetime.now())

# import message

# secret_key = input('Your secret key: ')

# message.message('Hello world!',message.fore.RED, 'upper', secret_key)

from Person import CreatePerson, fake_person

person_jack = CreatePerson.create_person(**fake_person)
person_jack.get_info()