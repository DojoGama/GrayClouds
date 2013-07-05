import unittest
from map import *

class TestGrayClouds(unittest.TestCase):
	def setUp(self):
		self.map = Map(8,8)

	def testCreateMap(self):
		numCells = 64
		self.assertEqual(numCells, self.map.size())

	def testCreateMatrix(self):
		matrix = self.map.getMap()
		for line in matrix:
			for column in line:
				self.assertEqual('.', column)

	def testInitMatrixWithAirports(self):
		countAirports = 0
		self.map.putAirports(4)
		matrix = self.map.getMap()
		for line in matrix:
			for column in line:
				if column == 'A':
					countAirports +=1
		
		self.assertEqual(4, countAirports)

	def testAirportNearAiport(self):
		self.map.putAirports(4)
		matrix = self.map.getMap()
		for i in range(len(matrix)):
			line = matrix[i]
			for j in range(len(line)):
				column = line[j]
				if column == 'A':
					self.assertEqual(False, self.map.verifyAirportNearBy(i,j))

if __name__ == "__main__":
	unittest.main()