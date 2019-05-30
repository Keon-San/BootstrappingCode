import random

units = []
gotten = []
differences = []
class Unit:
    def __init__(self, value):
        self.value = value
        units.append(self)

def indexOf(value, array):
    for x in range(0, len(array)):
        if array[x] >= value:
            return x

def highIndexOf(value, array):
    for x in range(0, len(array)):
        if array[x] > value:
            return x

sampX = 16
n = 20
ci = 0.95

for x in range(0, n):
    if x < sampX:
        temp = Unit(True)
    else:
        temp = Unit(False)

amount = 100000
for x in range(0, amount):
    for x in range(0, 20):
        gotten.append(units[random.randint(0, 19)])
    success = 0
    for x in gotten:
        if x.value == True:
            success += 1
    differences.append(success)
    gotten.clear()

differences.sort()
lowNum = differences[int(amount * ((1 - ci) / 2))]
highNum = differences[int(amount * (((1 - ci) / 2) + ci))]

lowIndex = highIndexOf(lowNum, differences)
highIndex = indexOf(highNum, differences)

print((highIndex - lowIndex) / amount)
print(lowNum/n)
print(highNum/n)
