import random
import sys
import copy
import datetime
import re

from PartizioneMemoria import *

#classe che rappresenta l'insieme delle partizioni della memoria
class AllocatoreMemoria: 
	def __init__(self, dimensioneMemoria):
		self.dimensioneMemoria = dimensioneMemoria #rappresenta la dimensione totale della memoria
		self.listaPartizioni = [] #rappresenta la lista di partizioni della memoria

		self.listaPartizioni.append(PartizioneMemoria(0,self.dimensioneMemoria)) #crea la prima partizione di memoria, che sara' un blocco unico

		self.FreeList = [] #crea una FreeList