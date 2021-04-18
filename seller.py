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


def measureDistance(cityA, cityB):
    return math.sqrt(((cityB.x-cityA.x) ** 2)+((cityA.y - cityB.y) ** 2))

def measureRouteLength(route,cities):
  length = 0
  for index in range(1,len(route)):
    length += measureDistance(cities[route[index]],cities[route[index-1]])
  return length

def generateRandomChromosome(citiesCount):
    route = []
    for index in range(0,citiesCount):
        cityIndex = 0
        while True:
            cityIndex = random.randint(0,citiesCount)
            if(route.count(cityIndex)==0)
                break
        route.append(cityIndex)
    return route
citiesCount = int(input("Please enter cities count: "))
mapWidth = int(input("Please input width of the map: "))
mapHeight = int(input("Please input height of the map: "))
cities = []

# Intitial cities.
for cityNumber in range(citiesCount):
    city = generateRandomCity(mapWidth, mapHeight)
    cities.append(city)
print(cities)
print(measureRouteLength(cities))

population = []
