max_range = int(input())


def febonachi(counter, mass):
    if counter < max_range:
        mass.append(mass[len(mass) - 2] + mass[len(mass) - 1])
        print(mass)
        febonachi(counter + 1, mass)


febonachi(1, [1, 1])
