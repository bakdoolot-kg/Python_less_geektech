from random import randint


def get_list() -> list:
    return list(range(0, 1_000_000_000, 2))


"""
 What is Binary search?
 then do Solution for search target in list
"""


class Solution:

    def __init__(self, userList):
        self.userList = userList

    def find_target(self, target):
        low = 0
        high = len(self.userList) - 1
        i = 0
        print(i)

        while low <= high:
            middle = (low + high) // 2
            guess = self.userList[middle]

            if guess < target:
                print(f"Больше {guess}!")
                low = middle + 1
                i += 1

            if guess > target:
                print(f"Меньше {guess}!")
                high = middle - 1
                i += 1
            else:
                print(f"Выполнено {i} шаг")
                return print(f"True>>> {target}")
        return -1


target = Solution(get_list())
# target.find_target(randint(1, 1000000))
target.find_target(10000000000123)
