import random
import sys
import copy
import datetime
import re

#Classe per creare file di log e stamparvi dentro informazioni
class File:
	def __init__(self, filename, permission):
		#se non esiste crea un file di log, mentre se esiste lo sovrascrive
		self.log = open(filename + ".txt", permission)

	def write(self, text):
		#stampa su shell
		print text

		#Log del testo su file
		self.log.write(text + "\n")

stampa = File("log", "w")