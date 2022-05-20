# '''
# What is Regular Experssions?
# '''
import re
#
#
# """
#  Is valid Email?
# """
#
# email = input('email: ')
# is_valid = re.search(r"[a-zA-Z]+@(gmail|mail|yandex)\.(com|ru)", email)
#
# if not is_valid:
#     print('Write the valid email!')
# elif email[is_valid.start():is_valid.end()] == email:
#     print('email valid!')

"""
 Is valid phone number?
"""

phone = input("Phone number: ")
is_valid = re.search(r"\+996-([0-9]{3})-([0-9]{2})-([0-9]{2})-([0-9]{2})", phone)

if not is_valid:
    print('Phone number Invalid!')
elif phone[is_valid.start():is_valid.end()] == phone:
    print('Phone number Valid!')