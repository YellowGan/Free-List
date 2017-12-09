import random
import sys
import copy
import datetime
import re

from PartizioneMemoria import *
from Processo import *
from AllocatoreMemoria import *
from File import *
from Funzioni import *

def firstFit(partizioni, processiAttesa):
	numProcessiEsecuzione = len(processiAttesa)
	cicli = 0

	comodo = 0
	ver = 0
	#inizializzazione della variabile del contatore di confronti dei vari algoritmi
	count = 0
	#Inizializzazione della variabile confronti che sara' settata a ogni chiamata dell'algoritmo che restituira' il numero di confronti effettuati
	confronti = 0
	#Inizializzazione della variabile falliti che mi indica il numero delle allocazioni fallite
	falliti = 0
	#Inizializzazione della variabile framm_esterne che mi indica il valore delle frammentazioni esterne
	framm_esterne = 0

	processiEsecuzione = []

	stampa.write("\nFIRST FIT\n")

	while len(processiAttesa)>0 or numProcessiEsecuzione>0:
		decrementoEsecuzioneProcessi(processiEsecuzione)
		l = verificaTerminazioneProcessi(partizioni, processiEsecuzione)
		numProcessiEsecuzione -= l
		if len(processiAttesa)>0:
			confronti = 0
			comodo = 0
			if(processiAttesa[0].ingProcesso <= cicli): #se il processo che deve entrare e' al giusto giro di clock
				for i in range(0, len(partizioni.listaPartizioni)):
					confronti+=1
					if (partizioni.listaPartizioni[i].dimensionePartizione() >= processiAttesa[0].dimProcesso) and (partizioni.listaPartizioni[i].stato == False):
						#operazione di inserimento
						comodo = 1
						processiEsecuzione.append(processiAttesa[0])
						stampa.write("\nprocesso selezionato: "+str(processiAttesa[0].ingProcesso))
						indice = len(processiEsecuzione)-1
						allocaMemoria(partizioni, i, processiEsecuzione[indice])
						processiEsecuzione[indice].partizioneOccupata = partizioni.listaPartizioni[i]
						stampaPartizioniMemoria(partizioni)
						del processiAttesa[0]
						break

				if comodo == 0:
					stampa.write("comodo non e' diventato 1")
					falliti+=1
					stampa.write("entro nella verifica della frammentazione")
					ver=verificaFrammentazioneEsterna(processiAttesa[0].dimProcesso, partizioni)
					#framm_esterne=ver
					stampa.write("frammentazione esterna: "+str(ver))

			else:
				stampa.write("\nALLOCAZIONE FALLITA! IMPOSSIBILE ESEGUIRE ALCUN PROCESSO: ")
				stampaPartizioniMemoria(partizioni)

			framm_esterne+=ver	
			count+=confronti

		stampa.write("\nclock: "+str(cicli+1))
		cicli += 1
		#

		stampa.write("\nlifetime: "+str(numProcessiEsecuzione))

	if falliti>0:
		framm_esterne /= falliti

	AllocatoreMemoria.freeList = []

	#stampa.write("Il numero di confronti effettuati dall'algoritmo firstFit e' : "+str(count)+" con "+str(falliti)+" allocazioni fallite di cui "+str(framm_esterne)+"%  per frammentazioni esterne")
	return framm_esterne, count


def bestFit(partizioni, processiAttesa):
	numProcessiEsecuzione = len(processiAttesa)
	cicli = 0

	comodo = 0
	ver = 0
	#inizializzazione della variabile del contatore di confronti dei vari algoritmi
	count = 0
	#Inizializzazione della variabile confronti che sara' settata a ogni chiamata dell'algoritmo che restituira' il numero di confronti effettuati
	confronti = 0
	#Inizializzazione della variabile falliti che mi indica il numero delle allocazioni fallite
	falliti = 0
	#Inizializzazione della variabile framm_esterne che mi indica il valore delle frammentazioni esterne
	framm_esterne = 0


	processiEsecuzione = []

	stampa.write("\nBEST FIT\n")

	while len(processiAttesa)>0 or numProcessiEsecuzione>0:

		valIndice = -1
		valConfronto = 9999999999

		decrementoEsecuzioneProcessi(processiEsecuzione)
		l = verificaTerminazioneProcessi(partizioni, processiEsecuzione)
		numProcessiEsecuzione -= l

		if len(processiAttesa)>0:
			confronti = 0
			comodo = 0
			if (processiAttesa[0].ingProcesso <= cicli): #se il processo che deve entrare e' al giusto giro di cicli
				for i in range(0, len(partizioni.listaPartizioni)): 
					confronti+=1
					if (partizioni.listaPartizioni[i].dimensionePartizione() >= processiAttesa[0].dimProcesso) and (partizioni.listaPartizioni[i].stato == False):
						if valConfronto > partizioni.listaPartizioni[i].dimensionePartizione():
							valIndice = i
							valConfronto = partizioni.listaPartizioni[i].dimensionePartizione()
				if valIndice != -1:
					#operazione di inserimento
					comodo = 1
					processiEsecuzione.append(processiAttesa[0])
					stampa.write("\nprocesso selezionato: "+str(processiAttesa[0].ingProcesso))
					indice = len(processiEsecuzione)-1
					allocaMemoria(partizioni, valIndice, processiEsecuzione[indice])
					processiEsecuzione[indice].partizioneOccupata = partizioni.listaPartizioni[valIndice]
					stampaPartizioniMemoria(partizioni)
					del processiAttesa[0]

				if comodo == 0:
					stampa.write("comodo non e' diventato 1")
					falliti+=1
					stampa.write("entro nella verifica della frammentazione")
					ver=verificaFrammentazioneEsterna(processiAttesa[0].dimProcesso, partizioni)
					#framm_esterne=ver
					stampa.write("frammentazione esterna: "+str(ver))

			else:
				stampa.write("\nALLOCAZIONE FALLITA! IMPOSSIBILE ESEGUIRE ALCUN PROCESSO: ")
				stampaPartizioniMemoria(partizioni)

			framm_esterne+=ver	
			count+=confronti

			stampa.write("\nclock: "+str(cicli+1))
			cicli += 1

		stampa.write("\nlifetime: "+str(numProcessiEsecuzione))

	if falliti>0:
		framm_esterne /= falliti

	AllocatoreMemoria.freeList = []

	#stampa.write("Il numero di confronti effettuati dall'algoritmo firstFit e' : "+str(count)+" con "+str(falliti)+" allocazioni fallite di cui "+str(framm_esterne)+"%  per frammentazioni esterne")
	return framm_esterne, count

def worstFit(partizioni, processiAttesa):
	numProcessiEsecuzione = len(processiAttesa)
	cicli = 0

	comodo = 0
	ver = 0
	#inizializzazione della variabile del contatore di confronti dei vari algoritmi
	count = 0
	#Inizializzazione della variabile confronti che sara' settata a ogni chiamata dell'algoritmo che restituira' il numero di confronti effettuati
	confronti = 0
	#Inizializzazione della variabile falliti che mi indica il numero delle allocazioni fallite
	falliti = 0
	#Inizializzazione della variabile framm_esterne che mi indica il valore delle frammentazioni esterne
	framm_esterne = 0

	processiEsecuzione = []

	stampa.write("\nWORST FIT\n")

	while len(processiAttesa)>0 or numProcessiEsecuzione>0:

		valIndice = -1
		valConfronto = None

		decrementoEsecuzioneProcessi(processiEsecuzione)
		l = verificaTerminazioneProcessi(partizioni, processiEsecuzione)
		numProcessiEsecuzione -= l

		if len(processiAttesa)>0:
			confronti = 0
			comodo = 0
			if (processiAttesa[0].ingProcesso <= cicli): #se il processo che deve entrare e' al giusto giro di cicli
				for i in range(0, len(partizioni.listaPartizioni)): 
					confronti+=1
					if (partizioni.listaPartizioni[i].dimensionePartizione() >= processiAttesa[0].dimProcesso) and (partizioni.listaPartizioni[i].stato == False):
						if valConfronto < partizioni.listaPartizioni[i].dimensionePartizione():
							valIndice = i
							valConfronto = partizioni.listaPartizioni[i].dimensionePartizione()
				if valIndice != -1:
					#operazione di inserimento
					comodo = 1
					processiEsecuzione.append(processiAttesa[0])
					stampa.write("\nprocesso selezionato: "+str(processiAttesa[0].ingProcesso))
					indice = len(processiEsecuzione)-1
					allocaMemoria(partizioni, valIndice, processiEsecuzione[indice])
					processiEsecuzione[indice].partizioneOccupata = partizioni.listaPartizioni[valIndice]
					stampaPartizioniMemoria(partizioni)
					del processiAttesa[0]
				if comodo == 0:
					stampa.write("comodo non e' diventato 1")
					falliti+=1
					stampa.write("entro nella verifica della frammentazione")
					ver=verificaFrammentazioneEsterna(processiAttesa[0].dimProcesso, partizioni)
					#framm_esterne=ver
					stampa.write("frammentazione esterna: "+str(ver))
			else:
				stampa.write("\nALLOCAZIONE FALLITA! IMPOSSIBILE ESEGUIRE ALCUN PROCESSO: ")
				stampaPartizioniMemoria(partizioni)

			framm_esterne+=ver	
			count+=confronti

			stampa.write("\nclock: "+str(cicli+1))
			cicli += 1

		stampa.write("\nlifetime: "+str(numProcessiEsecuzione))

	if falliti>0:
		framm_esterne /= falliti

	AllocatoreMemoria.freeList = []

	#stampa.write("Il numero di confronti effettuati dall'algoritmo firstFit e' : "+str(count)+" con "+str(falliti)+" allocazioni fallite di cui "+str(framm_esterne)+"%  per frammentazioni esterne")
	return framm_esterne, count