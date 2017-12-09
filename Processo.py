import random
import sys
import copy
import datetime
import re

#classe che rappresenta la singola istanza Processo
class Processo:
	def __init__(self, dimProcesso, ingProcesso, exProcesso):
		self.dimProcesso = dimProcesso #dimensione del processo
		self.ingProcesso = ingProcesso #rappresenta il ciclo in cui deve, se puo', entrare il processo
		self.exProcesso = exProcesso #rappresenta quanti cicli necessita il processo per terminare
		self.partizioneOccupata = None #rappresenta la partizione di memoria con riferimento al processo assegnato
