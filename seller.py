import random
import math


class CityCoordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"


def generateRandomCity(mapWidth, mapHeight):
    x = random.randint(1, mapWidth)
    y = random.randint(1, mapHeight)
    return CityCoordinate(x, y)


class Route:
    def __init__(self, cities, intialize):
        self.route = []
        self.cities = []
        if(intialize):
            self.intializeRoute()

    def intializeRoute(self):
        route = []
        citiesCount = len(self.cities)
        for index in range(0, citiesCount):
            cityIndex = 0
            while True:
                cityIndex = random.randint(0, citiesCount)
                if route.count(cityIndex) == 0:
                    break
            route.append(cityIndex)
        self.route = route

    def measureDistance(self, cityA, cityB):
        return math.sqrt(((cityB.x-cityA.x) ** 2)+((cityA.y - cityB.y) ** 2))

    def measureRouteLength(self):
        length = 0
        cities = self.cities
        route = self.route
        for index in range(1, len(route)):
            length += self.measureDistance(cities[route[index]],
                                           cities[route[index-1]])
        return length

    def calculateFittness(self):
        return 1 / self.measureRouteLength()

    def getSize(self):
        return len(self.route)

    def getRoute(self):
        return self.route

    def setRoute(self, route):
        self.route = route

    def setGene(self, index, gene):
        self.route[index] = gene

    def getGene(self, index):
        return self.route[index]

    def getGeneIndex(self, gene):
        return self.route.index(gene)


class Population:
    def __init__(self, cities, populationSize, initilaize):
        self.population = []
        self.populationSize = populationSize
        self.citiesCount = len(cities)
        self.cities = cities
        if initilaize:
            self.generateRandomPopulation()
        else:
            self.population = [None] * populationSize

    def generateRandomPopulation(self):
        for routeNumber in range(0, populationCount):
            route = Route(self.cities, True)
            self.population.append(route)

    def getIndividual(self, index):
        return self.population[index]

    def saveIndividual(self, index, indiv):
        self.population[index] = index

    def size(self):
        return len(self.population)

    def averageFittness(self):
        sum = 0
        for route in self.population:
            sum += route.calculateFittness()
        return sum / len(self.population)

    def getFittest(self):
        bestFittness = 0
        fittestRoute = None
        for index in range(0, self.populationSize):
            currentRoute = self.population[index]
            routeFittness = currentRoute.calculateFittness()
            if routeFittness > bestFittness:
                bestFittness = routeFittness
                fittestRoute = currentRoute
            return fittestRoute


def tournamentSelection(population, tournamentSize):
    tournamentPopulation = Population(cities, tournamentSize, False)
    for index in range(0, tournamentSize):
        randomIndex = random.randint(0, population.size())
        tournamentPopulation.saveIndividual(
            index, population.getIndividual(randomIndex))
    return tournamentPopulation.getFittest()


def mutate(route, mutationRate):
    for index in range(0,route.getSize()):
        if(random.random()>mutationRate):
            swapIndex = random.randint(0,route.getSize())
            swapValue = route.getGene(swapIndex)
            route.setGene(swapIndex,route.getGene(index))
            route.setGene(index,swapValue)

def crossOver(routeA,routeB,cities):
    citiesCount = len(cities)
    childRoute = Route(cities,False)
    routeAData = routeA.getRoute()
    routeBData = routeB.getRoute()
    crossIndex=len(cities)//2

    routeAGenes = routeAData[:crossIndex]
    routeBGenes = routeBData[crossIndex+1:]
    childData = routeAGenes.copy()
    for index in range(crossIndex+1,citiesCount):
        for gene in routeBGenes:
            if (childData.count(gene)==0):
                childData.append(gene)
        while True:



    
citiesCount = int(input("Please enter cities count: "))
mapWidth = int(input("Please input width of the map: "))
mapHeight = int(input("Please input height of the map: "))
populationCount = int(input("Please input count of initial population: "))
cities = []

# Intitial cities.
for cityNumber in range(citiesCount):
    city = generateRandomCity(mapWidth, mapHeight)
    cities.append(city)

# Generate random population
population = Population(populationCount, citiesCount, True)
populationHistory = [population]
