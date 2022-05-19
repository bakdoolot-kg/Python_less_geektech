# import math
# import datetime
#
# num = 9
#
# print(math.sqrt(num))
#
# print(math.pi)
#
# print(math.cos(6.5))
#
# print(math.sin(6.5))
#
# print(datetime.datetime.now())

# import message
#
# secret_key = input("Your Secret Key: ")
#
# message.message(
#     text="Hello, World!",
#     color=message.fore.CYAN,
#     font_style="upper",
#     secret_key=secret_key
# )

from Person import CreatePerson, fake_person

person_jack = CreatePerson.create_person(**fake_person)
print(person_jack)
person_jack.get_info()
print(person_jack.get_salary())
print(person_jack.get_salary())
print(person_jack.get_salary())
print(person_jack.get_salary())
