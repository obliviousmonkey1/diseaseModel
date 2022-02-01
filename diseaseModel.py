from asyncio import constants
from dataclasses import dataclass
from functools import partial
from http.client import CONTINUE
import json
import os
import pstats
import names
from random import random, randint, choice
import threading

from pyparsing import ParseExpression

json_file_to_load = 'Broncitis'

## Constants

BLOOD_TYPES  = ['A','B','O']

with open(f'{json_file_to_load}.json', 'r') as f:
    CONSTANTS = json.load(f)

# Easy to grab the data from the .json  file instead of creating new variables in 
# the .py file to put them in.

# NEED TO CHANGE THE CLASS 

class Person:
    def __init__(self) -> None:
        ## Personal details [1]
        self.firstname : str = names.get_first_name()
        self.lastname : str = names.get_last_name()
        self.age : int = randint(1,100)
        self.bloodType : str = choice(BLOOD_TYPES)
        self.alive : bool = True 
        
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
    
    def getOH(self):
        # Need to take into account age , need to take into account overall public health
        # Need to change calculation , random at the moment
        CONSTANTS['peopleConstants']['overallPublicHealth']
        if self.age >= 1 and self.age < 25:
            self.ageModifier = 0.1
        elif self.age >= 25 and self.age < 50:
            self.ageModifier = 0.075
        elif self.age >= 50 and self.age < 75:
            self.ageModifier = 0.050
        elif self.age >= 75 and self.age <= 100:
            self.ageModifier = 0.010
    
        return random() * CONSTANTS['peopleConstants']['overallPublicHealth'] + self.ageModifier

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
    
    def infect(self):
        self.infected = True
        self.incubating = True
        self.incubationDays +=1
        self.daysLastedWithoutInfection = 0


    def getImmunity(self):
        # Need to take into account other stuff
        # Need to change calculation
        partialImmunityChance = random()

        if self.fullImmunityChance > partialImmunityChance:
            self.immune = True 
        else:
            self.pImmune = True

    def isDead(self,population,infectedPersonIndex):
        ## Need to take into account age effect data 
        # need to take into account disease dange 
        if self.contagious == True:

            # Have to take into account overall health, and decrease it if person doesn't get killed based on 
            # Take into account blood type and age 
            # Need to change calculation 
            deathChance = random()
            if self.bloodType == CONSTANTS['diseaseConstants']['bloodTypeMostSusceptible']:
                bloodTypeModifer = 0.25
            else:
                bloodTypeModifer = 0 

            defiDeath = self.ageModifier + self.overallHealth + self.ageModifier - bloodTypeModifer
            if deathChance > defiDeath:
                self.alive = False
                self.overallHealth = 0.0
                if self.peopleWhoInfectedThem:
                    population[self.peopleWhoInfectedThem[-1]].assist.append(infectedPersonIndex)

    def spread(self,population, infected, infectedPersonIndex):
        ## Need to take into account age suseptiable data 
        # Change calculation
        diseaseTR = CONSTANTS['diseaseConstants']['diseaseTransmisionRate']
        while True:
            encounterChance = random()
            # need to take into account CONSTANTS['diseaseConstants']['diseaseTransmisionRate']
            if encounterChance-diseaseTR > self.social:
                break
            else:
                difference = self.social-diseaseTR
                diseaseTR = difference / 2 
                # need to fix constant loop
                person = randint(CONSTANTS['cityConstants']['overallPopulation'])
                if population[person].infected == False and population[person].immune == False or population[person].pImmune == False and population[person].alive == True:
                    population[person].infect()
                    infected.append(person)
                    self.peopleInfected.append(person)
                    population[person].peopleWhoInfectedThem.append(infectedPersonIndex)
        return population, infected

    def day(self, population, infected, infectedPersonIndex):
        if self.incubating:
            if self.incubationDays == CONSTANTS['diseaseConstants']['incubationPeriod']:
                self.incubating = False
                self.contagious = True 
            else:
                self.incubationDays += 1
        else:
            if self.contagiousDays == CONSTANTS['diseaseConstants']['contagiousPeriod']:  
                self.contagious = False
                self.infected = False
                self.getImmunity()
            else:
                self.contagiousDays +=1
                self.spread(population, infected, infectedPersonIndex)
        
        return population, infected

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

# Should change way to store and get this data
day = 0
# Number of people not infected 
numNotInfected = CONSTANTS['cityConstants']['overallPopulation']-1
# Number of people infected 
numInfected = 1
# Number of people pImmune
numPartiallyimune = 0
# Number of people immune
numImmune = 0
# Number of people dead
numMortality = 0

outD = int(input('Please input wether you would like data on a per day[0], per week[1], per month[2] or per year[3] basis [0,1,2,3] > '))

while True:
    # Shoul refactor
    day += 1
    for i in partialImmunityList:
        if population[i].particalImmunityDays == CONSTANTS['diseaseConstants']['partialImmunityPeriod']:
            population[i].pImmune = False
            a = partialImmunityList.pop(i)
        population[i].particalImmunityDays += 1

    for i in infected:
        population[i].isDead(population, i)
        if population[i].alive == True:
            population[i].day(population, infected, i)

        if population[i].immune == True:
            a = infected.pop(i)
            immunityList.append(a)
            numImmune += 1
        elif population[i].pImmune == True:
            a = infected.pop(i)
            partialImmunityList.append(a)
            numPartiallyimune += 1
        elif population[i].alive == False:
            a = infected.pop(i)
            moralityList.append(a)
            numNotInfected -= 1
            numMortality +=1

    #for people in population:
        #if people.infected == False:
         #   people.daysLastedWithoutInfection +=1
    
    # Adding up the values
    numNotInfected = len(population) - len(infected)
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
        

for i in range(CONSTANTS['cityConstants']['overallPopulation']):
    population[i].display_personal_info()
    input('Next Person > ')

## one day 

