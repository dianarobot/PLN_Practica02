#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Diana Rocha Botello
"""
import random

class Agente():
	# m = número total de objetos en el contexto
	def __init__(self, m):
		self.m = m

		self.objetos = []

	def nombrar(self):
		silabas = random.randint(1,9)
		vowels = ['a','e','i','o','u']
		consonants = ['b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z']
		word = ''
		for i in range(silabas):
			silaba = random.choice(consonants) + random.choice(vowels)
			word = word + silaba
		return word

	# k = número de objeto
	# agenteO = Agente Oyente
	def enunciar(self, k, agenteO):
		nombres = objetos[k]
		if smallerN == '':
			smallerN = generateObjectName()

	def generateObjectName(self, k):


	def getSmallerName(self, nombres):
		smallerN = ''
		for nombre in nombres:
			if smallerN == '':
				smallerN = nombre
			elif len(smallerN) > len(nombre):
				smallerN = nombre
		return smallerN

if __name__ == "__main__":
	agente = Agente(5)
	#print(agente.nombrar())
	lista = []
	print(agente.getSmallerName(lista))