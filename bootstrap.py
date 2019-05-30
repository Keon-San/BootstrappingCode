import random

#units will represent my pooled sample
units = []
#controls is the controls in that bootstrap run
controls = []
#treatments is the treatments in that run
treatments = []
#This represents the sampling distribution, by holding the difference in num successes found during each bootstrap
differences = []

def findIndex(array, value):
    for x in range(0, len(array)):
        if array[x] >= value:
            return x

class Unit:
    def __init__(self, value):
        self.value = value
        units.append(self)

#X is number of successes, n is total count
controlX = 10
controlN = 20
treatmentX = 16
treatmentN = 20

direction = True #true for upper tail
twotailed = False

#Generate X success and N-X fails for control
for x in range(0, controlN):
    if x < controlX:
        temp = Unit(True)
    else:
        temp = Unit(False)

#Same for treatment
for x in range(0, treatmentN):
    if x < treatmentX:
        temp = Unit(True)
    else:
        temp = Unit(False)

bootstrapAmount = 1000000
for x in range(0, bootstrapAmount):
    #Order numbers from 1-40 in random order
    samples = random.sample(range(0, 40), 40)
    #Put into groups
    for x in range(0, 20):
        controls.append(units[samples[x]])
    for x in range(20, 40):
        treatments.append(units[samples[x]])
    #Get bootstrap Xes
    sampControlX = 0
    for x in controls:
        if x.value == True:
            sampControlX += 1
    sampTreatX = 0
    for x in treatments:
        if x.value == True:
            sampTreatX += 1
    #Calc diff and add to distr
    differences.append(sampTreatX - sampControlX)
    controls.clear()
    treatments.clear()

differences.sort()
foundDifference = treatmentX - controlX
location = findIndex(differences, foundDifference)
p = 0
if twotailed:
    if (location > bootstrapAmount/2):
        p = ((bootstrapAmount - location) / bootstrapAmount) * 2
    else:
        p = (location / boostrapAmount) * 2
else:
    if direction:
        p = (bootstrapAmount - location) / bootstrapAmount
    else:
        p = location / bootstrapAmount

print(p)
