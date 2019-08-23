#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Diana Rocha Botello
"""
from agente import Agente
import random
import sys

class JuegoNombres():
	def __init__(self, n, m, maxt):
		self.numeroA = n
		self.agentes = []
		self.iteraciones = maxt
		self.numeroObjetos = m
		self.objetosGeneral = []
		self.totalNombres = 0
		for i in range(self.numeroObjetos):
			self.objetosGeneral.append([])
		# Create agentes
		for i in range(self.numeroA):
			self.agentes.append(Agente(self.numeroObjetos))

	def selectAgentesObjetos(self):
		hablanteIndex = random.choice(range(self.numeroA))
		oyenteIndex = random.choice(range(self.numeroA))
		while hablanteIndex == oyenteIndex:
			oyenteIndex = random.choice(range(self.numeroA))
		objetoIndex = random.choice(range(self.numeroObjetos))
		self.agentes[hablanteIndex].enunciar(objetoIndex, self.agentes[oyenteIndex])

	def getAllNamesObjects(self):
		for i in range(self.numeroObjetos):
			for agente in self.agentes:
				for nombre in agente.objetos[i]:
					if nombre not in self.objetosGeneral[i]:
						self.objetosGeneral[i].append(nombre)
		#print(self.objetosGeneral)

	def countNamesObjects(self):
		total = 0
		for i in range(self.numeroObjetos):
			total += len(self.objetosGeneral[i])
		self.totalNombres = total
		print("1) Número total de nombres conocidos: "+ str(total))

	def countNamesByObjects(self):
		print("2) Número total de nombres para cada objeto")
		for i in range(self.numeroObjetos):
			print("Objeto "+str(i)+': '+str(len(self.objetosGeneral[i])))

	def namesLen(self):
		longitud = 0
		for i in range(self.numeroObjetos):
			for nombre in self.objetosGeneral[i]:
				longitud += len(nombre)
		prom = longitud/self.totalNombres
		print("3) Longitud promedio de todos los nombres: "+str(prom)) 

	def showMetricas(self):
		print("M É T R I C A S")
		self.getAllNamesObjects()
		self.countNamesObjects()
		self.countNamesByObjects()
		self.namesLen()	
	
	def startGame(self):
		for i in range(self.iteraciones):
			print("Iteración "+str(i+1))
			self.selectAgentesObjetos()
			self.showMetricas()
			print("-----------------------------------")
			print("-----------------------------------")
			if i == 9:
				input("Press Enter to continue...")

if __name__ == "__main__":
	if len(sys.argv) == 4: 
		jugar = JuegoNombres(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
		jugar.startGame()
	else:
		print("ERROR: Este script requiere de 3 argumentos separados por espacio.");
		print("1) Número entero que indica el número de agentes")
		print("2) Número entero que indica el número de objetos")
		print("3) Número entero que indica el número de iteraciones máximas")

