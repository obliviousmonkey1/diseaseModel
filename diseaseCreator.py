import json
from random import random, randint, choice, getrandbits

x = ["diseaseConstants" , [('contagiousPeriod', 'int'),
                           ('incubationPeriod', 'int'),
                           ('partialImmunityPeriod', 'int'),
                           ("diseaseDanger", 'float'),
                           ("diseaseTransmisionRate", 'float'),
                           ("bloodTypeMostSusceptible", 'str'),
                           ("bloodTypeMostSusceptible", 'float'),
                           ("ageRangeMostSusceptible", '2 int i.e 50,100'),
                           ("ageRangeLeastSusceptible",'2 int i.e 1,20'),
                           ("ageSusceptibilityEffects", 'float'),
                           ("ageRangeMostEffected" , "2 int i.e 50,100"),
                           ("ageRangeLeastEffected", "2 int i.e 1,20"),
                           ("ageEffect", 'float')],
     "cityConstants", [("overallPopulation", "int")],
     "peopleConstants", [("overallPublicHealth","float")]
]

data = {}

bloodTypes = ['A', 'B', 'O']

print('please name the disease')
dName = input('> ')

randomConfig = int(input('''Would you the values to be randomized ?, [1, 0]
 > ''' ))
if randomConfig == 0:
    randomConfig = False
else:
    randomConfig = True

for i in range(3):
    if i == 0:
        name = "diseaseConstants"
        qIndex = 1
        data[name] = {}
    elif i == 1:
        name = "cityConstants"
        qIndex = x.index(name)+1
        data[name] = {}
    elif i == 2:
        name = "peopleConstants"
        qIndex = x.index(name)+1
        data[name] = {}

    for index in range(len(x[qIndex])):
        print(f'Please enter the {x[qIndex][index][0]} , DataType : {x[qIndex][index][1]}')
        if x[qIndex][index][1][0] == '2':
            if randomConfig:
                if x[qIndex][index][0][8] == 'M':
                    y= [randint(50,70),randint(70,100)]
                else:
                    y= [randint(1,25),randint(25,49)]
                print(y)
            else:
                y = input('> ')
                y = y.split(',')
                y[0], y[1] = int(y[0]), int(y[1])
            data[name][x[qIndex][index][0]] = y
        elif x[qIndex][index][1] == 'int':
            if randomConfig:
                if qIndex == 1:
                    y = randint(0,20)
                elif qIndex == 3:
                    y = randint(500,1000)
                else:
                    pass
                print(y)
            else:
                y = int(input('> '))
            data[name][x[qIndex][index][0]] = y
        elif x[qIndex][index][1] == 'float':
            if randomConfig:
                y = random()
                print(y)
            else:
                y = float(input('> '))
            data[name][x[qIndex][index][0]] = y
        elif x[qIndex][index][1] == 'str':
            if randomConfig:
                if qIndex == 1:
                    if x[qIndex][index][0][0] == 'b':
                        y = choice(bloodTypes)
                elif qIndex == 3:
                    pass
                else:
                    pass
                print(y)
            else:
                y = input('> ')
            data[name][x[qIndex][index][0]] = y
        elif x[qIndex][index][1] == 'bool':
            if randomConfig:
                y = bool(getrandbits(1))
                print(y)
            else:
                y = bool(input('> '))
            data[name][x[qIndex][index][0]] = y  

json_string = json.dumps(data)

with open(f'{dName}.json', 'w') as outfile:
    outfile.write(json_string)

