import random
import sys
import copy
import datetime
import re

#classe che rappresenta le partizioni della memoria
class PartizioneMemoria:
	def __init__(self, valInizio, valFine):
		self.valInizio = valInizio #rappresenta il "byte" di memoria iniziale
		self.valFine = valFine #rappresenta il "byte" di memoria finale
		self.stato = False #indica se la partizione memoria e' stata assegnata a un processo (True) o e' libera (False)

	def dimensionePartizione(self): #restituisce la dimensione della partizione
		return (self.valFine- self.valInizio) 