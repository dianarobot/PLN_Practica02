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

		for i in range(self.m):
			self.objetos.append([])

	def nombrar(self):
		silabas = random.randint(1,8)
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
		#print("OYENTE")
		#print(agenteO.objetos)
		#print("HABLANTE")
		#print(self.objetos)
		nombres = self.objetos[k]
		nombre =  self.getSmallerName(nombres)
		if nombre == '':
			nombre = self.generateObjectName(k)

		# Caso 1: El hablante y oyente coinciden en el nombre
		if nombre in agenteO.objetos[k]:
			self.objetos[k] = [nombre]
			agenteO.objetos[k]= [nombre]
		# Caso 2: El oyente no tiene nombres para el k-objeto
		# Caso 3: El oyente tiene nombres pero no el del hablante
		else:
			agenteO.objetos[k].append(nombre) 

		#print("OYENTE")
		#print(agenteO.objetos)
		#print("HABLANTE")
		#print(self.objetos)

	def generateObjectName(self, k):
		nombre = self.nombrar()
		lista = [nombre]
		self.objetos[k] = lista
		return nombre

	def getSmallerName(self, nombres):
		smallerN = ''
		for nombre in nombres:
			if smallerN == '':
				smallerN = nombre
			elif len(smallerN) > len(nombre):
				smallerN = nombre
		return smallerN

#if __name__ == "__main__":
#	agenteH = Agente(5)
#	agenteH.objetos[3] = ["cosa", "cosados", "cosadoble"]
#	agenteO = Agente(5)
#	agenteO.objetos[3]=["cosa", "nocosa", "cosita"]
	#print(agente.nombrar())
#	lista = []
#	agenteH.enunciar(3,agenteO)