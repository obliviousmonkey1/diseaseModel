from http.client import CONTINUE
import json
import names
from random import random, randint, choice

json_file_to_load = 'Broncitis'

## Constants

BLOOD_TYPES  = ['A','B','O']

with open(f'{json_file_to_load}.json', 'r') as f:
    CONSTANTS = json.load(f)

# Easy to grab the data from the .json  file instead of creating new variables in 
# the .py file to put them in.

class Person:
    def __init__(self) -> None:
        ## Personal details [1]
        self.firstname : str = names.get_first_name()
        self.lastname : str = names.get_last_name()
        self.age : int = randint(1,100)
        self.bloodType : str = choice(BLOOD_TYPES)
        self.alive : bool = True 
        
        # age modifiers
        self.getAgeBasedModifiers(0)
        self.getAgeBasedModifiers(1)

        # need to change should take into account age
        self.overallHealth = self.getOH()

        ## Personal variables
        self.social : float = random()
        # need to have it take into account overallHealth
        self.fullImmunityChance : float = random() 
        self.hasHadInfection : bool = False

        ## Disease variables
        self.infected : bool = False
        self.incubating : bool = False
        self.contagious : bool = False
        self.immune : bool = False
        self.pImmune : bool = False

        self.totalInfectedDays : int = 0
        self.incubationDays : int = 0
        self.contagiousDays : int  = 0
        self.particalImmunityDays : int = 0

        ## Stats 
        self.daysLastedWithoutInfection = 0
        self.groundZero : bool = False
        self.peopleWhoInfectedThem : list[(str, int)] = []
        self.peopleInfected : list[(str, int)] = []
        self.assist : list[(str, int)] = []
    
    # reeeeefactor timeeee
    def getOH(self):
        # Need to take into account age , need to take into account overall public health
        # Need to change calculation , random at the moment
        CONSTANTS['peopleConstants']['overallPublicHealth']
    
        return random() * CONSTANTS['peopleConstants']['overallPublicHealth'] + self.ageModifier

    # refacted.com has visited this place
    def getAgeBasedModifiers(self, type):
        if type == 0:
            aRL = 'ageRangeLeastSusceptible'
            aRM = 'ageRangeMostSusceptible'
            aE = 'ageSusceptibilityEffects'
        else:
            aRL = 'ageRangeLeastEffected'
            aRM = 'ageRangeMostEffected'
            aE = 'ageEffect'
        # Fist one appended is the susceptibilty[0] and second one is effect[1]
        # susceptibilty effects chance to catch it and effect , effects chance to die
        if self.age >= CONSTANTS['diseaseConstants'][aRL][0] and self.age <= CONSTANTS['diseaseConstants'][aRL][1]:
            self.ageEffects.append(CONSTANTS['diseaseConstants'][aE])
        elif self.age >= CONSTANTS['diseaseConstants'][aRM][0] and self.age <= CONSTANTS['diseaseConstants'][aRM][1]:
            self.ageEffects.append(-CONSTANTS['diseaseConstants'][aE])
        else:
            self.ageEffects.append(0)

    def getStats(self, value, index):
        value += f"{population[index].firstname} {population[index].lastname} , "
        return value

    def display_personal_info(self, population):
        # Infected By
        i = ""
        for index in self.peopleWhoInfectedThem:
            i = self.getStats(i, index)
        # People infected 
        pI = ""
        for index in self.peopleInfected:
            pI = self.getStats(pI, index)
        # Assists 
        aI = ""
        for index in self.assist:
            aI = self.getStats(aI. index)
        print(f"""
        Firstname : {self.firstname}
        Surname : {self.lastname}
        Age : {self.age}
        Bloodtype : {self.bloodType}
        Alive : {self.alive}
        Overall health : {self.overallHealth}

                STATS

        Infected : {self.infected}
        First Infected : {self.groundZero}
        Infected by : {i[:-2]}
        People Infected : {pI[:-2]}
        Assits : {aI[:-2]}
        Days lasted without getting infected : {self.daysLastedWithoutInfection}

        """)
    
    def getInfected(self):
        self.infected = True
        self.incubating = True
        self.incubationDays +=1
        self.daysLastedWithoutInfection = 0

    # time baby refactor
    def getImmunity(self):
        # Need to take into account other stuff
        # Need to change calculation
        partialImmunityChance = random()

        if self.fullImmunityChance > partialImmunityChance:
            self.immune = True 
        else:
            self.pImmune = True

    # refactor time
    def chanceOfDying(self):
        ## Need to take into account age effect data 
        # need to take into account disease dange 
        if not self.incubating:

            # Have to take into account overall health, and decrease it if person doesn't get killed based on 
            # Take into account age 
            # CONSTANTS['diseaseConstants']['ageEffectModifier']
            deathChance = random()
            if self.bloodType == CONSTANTS['diseaseConstants']['bloodTypeMostSusceptible']:
                bloodTypeModifer = 0.25
            else:
                bloodTypeModifer = 0 

            defiDeath = self.ageModifier + self.overallHealth + self.ageModifier
            if defiDeath < deathChance:
                self.alive = False
                self.overallHealth = 0.0
                # do this outside of the function 
                if self.peopleWhoInfectedThem:
                    population[self.peopleWhoInfectedThem[-1]].assist.append(infectedPersonIndex)
    
    def newDay(self):
        if self.incubating:
            if self.incubationDays > CONSTANTS['diseaseConstants']['incubationPeriod']:
                self.incubating = False
                self.contagious = True 
            else:
                self.incubationDays += 1
        else:
            if self.contagiousDays > CONSTANTS['diseaseConstants']['contagiousPeriod']:  
                self.contagious = False
                self.infected = False
                self.getImmunity()
            else:
                self.contagiousDays +=1

# Refactor time baby 
def spread(population, infected, infectedPersonIndex):
    ## Need to take into account age suseptiable data 
    # Change calculation, really needs to change
    if population[infectedPersonIndex].contagious:
        diseaseTR = CONSTANTS['diseaseConstants']['diseaseTransmisionRate']
        while True:
            encounterChance = random()
            # need to take into account CONSTANTS['diseaseConstants']['diseaseTransmisionRate']
            if encounterChance-diseaseTR > self.social:
                break
            else:
                difference = self.social-diseaseTR
                diseaseTR = difference / 2
                person = randint(0, (CONSTANTS['cityConstants']['overallPopulation']-1))
                if population[person].immune == False or population[person].pImmune == False and population[person].alive == True:
                    if population[person].infected == False:
                        population[person].infect()
                        infected.append(person)
                        population[].peopleInfected.append(person)
                        population[person].peopleWhoInfectedThem.append(infectedPersonIndex)
        
# Visual display of the city, will be converted to matplotlib after the refactor 
def cityData(numNotInfected, numInfected, numImmune, numPartiallyimune, numMortality):
    # Should display number of days/weeks/months/years
    print(f'''
    Total population in city: {CONSTANTS['cityConstants']['overallPopulation']-numMortality}
    Not Infected : {numNotInfected} 
    Infected : {numInfected}
    Immune : {numImmune}
    Partially Immune : {numPartiallyimune}
    Mortality : {numMortality}''')

population = [Person() for _ in range(CONSTANTS['cityConstants']['overallPopulation'])]
population[0].infect()

# Store's the index of the infected people
infected = []
infected.append(0)
population[0].groundZero = True
partialImmunityList = []
immunityList = []
moralityList = []

outD = int(input('Please input wether you would like data on a per day[0], per week[1], per month[2] or per year[3] basis [0,1,2,3] > '))

day = 0
while True:
    # Should refactor
    day += 1

    # updates the partialImmunity people
    for person in partialImmunityList:
        if population[person].particalImmunityDays > CONSTANTS['diseaseConstants']['partialImmunityPeriod']:
            population[person].pImmune = False
            a = partialImmunityList.pop(person)
            population[person].particalImmunityDays = 0
        else:
            population[person].particalImmunityDays += 1

    # updates an infected persons day 
    for person in infected:
        population[person].newDay()
        if population[person].immune == True:
            immunityList.append(infected.pop(person))
        elif population[person].pImmune == True:
            partialImmunityList.append(infected.pop(person))

    # spreads the disease 
    for person in infected:
        spread(population, infected, person)
    
    for person in infected:
        population[person].chanceOfDying()

## This code should be fine-ish 

    # Adding up the values
    numNotInfected = CONSTANTS['cityConstants']['overallPopulation'] - len(infected) - len(moralityList)
    numInfected = len(infected)
    numImmune = len(immunityList)
    numPartiallyimune = len(partialImmunityList)
    numMortality = len(moralityList)

    if outD == 0:
        cityData(numNotInfected, numInfected, numImmune, numPartiallyimune, numMortality)
        input(f'Next day {day} > ')
    elif outD == 1:
        if day % 7 == 0:
            cityData(numNotInfected, numInfected, numImmune, numPartiallyimune, numMortality)
            input('Next week > ')
    elif outD == 2:
        if day % 28 == 0:
            cityData(numNotInfected, numInfected, numImmune, numPartiallyimune, numMortality)
            input('Next Month > ')
    elif outD == 3:
        if day % 360 == 0:
            cityData(numNotInfected, numInfected, numImmune, numPartiallyimune, numMortality)
            input('Next Year > ') 
