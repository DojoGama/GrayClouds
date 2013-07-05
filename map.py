from random import randint
import math
class Map():

	def __init__(self,width,heigth):
		self.width = width
		self.heigth = heigth
		self.map = self.createMap()

	def size(self):
		return self.width * self.heigth

	def getMap(self):
		return self.map

	def createMap(self):
		return [['.' for j in range(self.heigth)] for i in range(self.width)]

	def validateAirportsPosition(self, posI, posJ):

		if self.map[posI][posJ] == 'A':
			return True
		else:
			return False	


	def putAirports(self, number):
		verifyAirpots = False	

		for i in range(number):
			posI = randint(0,self.width-1)
			posJ = randint(0,self.heigth-1)

			while self.validateAirportsPosition(posI, posJ) and not self.verifyAirportNearBy(posI,posJ):
				posI = randint(0,self.width-1)
				posJ = randint(0,self.heigth-1)

			self.map[posI][posJ] = 'A'

	def verifyAirportNearBy(self, posI, posJ):
		sum = posI + posJ
		if (self.map[posI + 1][posJ] == 'A' or
		self.map[posI + 1][posJ + 1] == 'A' or
		self.map[posI][posJ + 1] == 'A' or
		self.map[posI - 1][posJ] == 'A' or
		self.map[posI - 1][posJ - 1] == 'A' or
		self.map[posI][posJ - 1] == 'A' or
		self.map[posI - 1][posJ + 1] == 'A' or
		self.map[posI + 1][posJ - 1] == 'A'):
			return True

		return False