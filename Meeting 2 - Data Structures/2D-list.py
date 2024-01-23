temperature = [
    [25, 27, 28, 27],
    [23, 24, 26, 26],
    [24, 24, 27, 27],
    [22, 24, 25, 24]
]

print()
print(temperature)
print(len(temperature))

print()
print(temperature[0])
print(temperature[0][0])

temperature.append([23, 24, 24, 26])

print()
print(temperature)
print(len(temperature))

temperature[1][2] = 27

print()
print(temperature)
