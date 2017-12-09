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
from Algoritmi import *

#numero Simulazioni
stampa.write("\nIMMETTI NUMERO DI SIMULAZIONI:\n")
numSimulazioni = int(raw_input())
stampa.write("Bisogna effettuare "+str(numSimulazioni)+" simulazioni\n")

#opzioni menu'
i=0

opzioni = menu()

while(opzioni<1 or opzioni>4):
	opzioni = menu()

#nel caso in cui si digita 1 viene eseguito il first fit
if opzioni==1:
	#inizializzazione di variabili di statistica
	framm_esterne = 0
	frammEsterne = 0
	count = 0
	cCount = 0
	#si effettuano i simulazioni
	while (i<numSimulazioni):
		stampa.write("Simulazione numero "+str(i+1))

		dimMemoria = 20480
		memoria = AllocatoreMemoria(dimMemoria)

		processiAttesa = creaProcessiAttesa()
		stampa.write(str(len(processiAttesa))+" processi iniziali")
		for j in range(0, len(processiAttesa)):
			stampa.write("ingresso: "+str(processiAttesa[j].ingProcesso)+"\tdimensione: "+str(processiAttesa[j].dimProcesso)+"\ttempo esecuzione: "+str(processiAttesa[j].exProcesso))

		stampa.write("\n")

		ordinaProcessi(processiAttesa)
		stampa.write("Processi ordinati per ingresso: "+str(len(processiAttesa)))
		for j in range(0, len(processiAttesa)):
			stampa.write("ingresso: "+str(processiAttesa[j].ingProcesso)+"\tdimensione: "+str(processiAttesa[j].dimProcesso)+"\ttempo esecuzione: "+str(processiAttesa[j].exProcesso))
			
		framm_esterne, count = firstFit(memoria, processiAttesa)
		frammEsterne+=framm_esterne
		cCount+=count

		i+=1

	cCount=(cCount*1.0/numSimulazioni*1.0)
	frammEsterne=(frammEsterne*1.0/numSimulazioni*1.0)*100

	stampa.write("La media dei confronti effettuati dall'algoritmo first-fit e': "+str(cCount))
	stampa.write("e la media di frammentazioni esterne e' "+str(round(frammEsterne,2))+"%\n")
	
			
#nel caso in cui si digita 2 viene eseguito il best fit
elif opzioni==2:
	#inizializzazione di variabili di statistica
	framm_esterne = 0
	frammEsterne = 0
	count = 0
	cCount = 0
	#si effettuano i simulazioni
	while (i<numSimulazioni):
		stampa.write("simulazione numero "+str(i+1))

		dimMemoria = 20480
		memoria = AllocatoreMemoria(dimMemoria)

		processiAttesa = creaProcessiAttesa()
		stampa.write(str(len(processiAttesa))+" processi iniziali")
		for j in range(0, len(processiAttesa)):
			stampa.write("ingresso: "+str(processiAttesa[j].ingProcesso)+"\tdimensione: "+str(processiAttesa[j].dimProcesso)+"\ttempo esecuzione: "+str(processiAttesa[j].exProcesso))

		stampa.write("\n")

		ordinaProcessi(processiAttesa)
		stampa.write("Processi ordinati per ingresso: "+str(len(processiAttesa)))
		for j in range(0, len(processiAttesa)):
			stampa.write("ingresso: "+str(processiAttesa[j].ingProcesso)+"\tdimensione: "+str(processiAttesa[j].dimProcesso)+"\ttempo esecuzione: "+str(processiAttesa[j].exProcesso))
		

		framm_esterne, count = bestFit(memoria, processiAttesa)
		frammEsterne+=framm_esterne
		cCount+=count

		i+=1

	cCount=(cCount*1.0/numSimulazioni*1.0)
	frammEsterne=(frammEsterne*1.0/numSimulazioni*1.0)*100

	stampa.write("La media dei confronti effettuati dall'algoritmo best-fit e': "+str(cCount))
	stampa.write("e la media di frammentazioni esterne e': "+str(round(frammEsterne,2))+"%\n")

#nel caso in cui si digita 3 viene eseguito il worst fit
elif opzioni==3:
	#inizializzazione di variabili per le statistiche
	framm_esterne = 0
	frammEsterne = 0
	count = 0
	cCount = 0
	#si effettuano i simulazioni
	while (i<numSimulazioni):
		stampa.write("simulazione numero "+str(i+1))

		dimMemoria = 20480
		memoria = AllocatoreMemoria(dimMemoria)

		processiAttesa = creaProcessiAttesa()
		stampa.write(str(len(processiAttesa))+" processi iniziali")
		for j in range(0, len(processiAttesa)):
			stampa.write("ingresso: "+str(processiAttesa[j].ingProcesso)+"\tdimensione: "+str(processiAttesa[j].dimProcesso)+"\ttempo esecuzione: "+str(processiAttesa[j].exProcesso))

		stampa.write("\n")

		ordinaProcessi(processiAttesa)
		stampa.write("Processi ordinati per ingresso: "+str(len(processiAttesa)))
		for j in range(0, len(processiAttesa)):
			stampa.write("ingresso: "+str(processiAttesa[j].ingProcesso)+"\tdimensione: "+str(processiAttesa[j].dimProcesso)+"\ttempo esecuzione: "+str(processiAttesa[j].exProcesso))
			
		framm_esterne, count = worstFit(memoria, processiAttesa)
		frammEsterne+=framm_esterne
		cCount+=count

		i+=1

	cCount=(cCount*1.0/numSimulazioni*1.0)
	frammEsterne=(frammEsterne*1.0/numSimulazioni*1.0)*100

	stampa.write("La media dei confronti effettuati dall'algoritmo best-fit e': "+str(cCount))
	stampa.write("e la media di frammentazioni esterne e': "+str(round(frammEsterne,2))+"%\n")

#se si digita 4 vengono effettuati tutti gli algoritmi
else:
	#inizializzazione di variabili di statistica per tutti e tre gli algoritmi
	framm_esterneF = 0
	frammEsterneF = 0
	countF = 0
	cCountF = 0
	framm_esterneB = 0
	frammEsterneB = 0
	countB = 0
	cCountB = 0
	framm_esterneW = 0
	frammEsterneW = 0
	countW = 0
	cCountW = 0

	#si effettuano i simulazioni
	while (i<numSimulazioni):
		stampa.write("simulazione numero "+str(i+1))

		dimMemoria = 20480
		memoria = AllocatoreMemoria(dimMemoria)

		processiAttesa = creaProcessiAttesa()
		stampa.write(str(len(processiAttesa))+" processi iniziali")
		for j in range(0, len(processiAttesa)):
			stampa.write("ingresso: "+str(processiAttesa[j].ingProcesso)+"\tdimensione: "+str(processiAttesa[j].dimProcesso)+"\ttempo esecuzione: "+str(processiAttesa[j].exProcesso))

		stampa.write("\n")

		ordinaProcessi(processiAttesa)
		stampa.write("Processi ordinati per ingresso: "+str(len(processiAttesa)))
		for j in range(0, len(processiAttesa)):
			stampa.write("ingresso: "+str(processiAttesa[j].ingProcesso)+"\tdimensione: "+str(processiAttesa[j].dimProcesso)+"\ttempo esecuzione: "+str(processiAttesa[j].exProcesso))
		
		#copie della lista da poter utilizzare per best fit e worst fit
		processiAttesa2 = copy.deepcopy(processiAttesa)
		processiAttesa3 = copy.deepcopy(processiAttesa)

		#calcolo delle statistiche
		framm_esterneF, countF = firstFit(memoria, processiAttesa)
		frammEsterneF+=framm_esterneF
		cCountF+=countF

		framm_esterneB, countB = bestFit(memoria, processiAttesa2)
		frammEsterneB+=framm_esterneB
		cCountB+=countB

		framm_esterneW, countW = worstFit(memoria, processiAttesa3)
		frammEsterneW+=framm_esterneW
		cCountW+=countW

		i+=1

	cCountF=(cCountF*1.0/numSimulazioni*1.0)
	frammEsterneF=(frammEsterneF*1.0/numSimulazioni*1.0)*100

	stampa.write("La media dei confronti effettuati dall'algoritmo first-fit e': "+str(cCountF))
	stampa.write("e la media di frammentazioni esterne e': "+str(round(frammEsterneF,2))+"%\n")

	cCountB=(cCountB*1.0/numSimulazioni*1.0)
	frammEsterneB=(frammEsterneB*1.0/numSimulazioni*1.0)*100

	stampa.write("La media dei confronti effettuati dall'algoritmo best-fit e': "+str(cCountB))
	stampa.write("e la media di frammentazioni esterne e': "+str(round(frammEsterneB,2))+"%\n")

	cCountW=(cCountW*1.0/numSimulazioni*1.0)
	frammEsterneW=(frammEsterneW*1.0/numSimulazioni*1.0)*100

	stampa.write("La media dei confronti effettuati dall'algoritmo worst-fit e': "+str(cCountW))
	stampa.write("e la media di frammentazioni esterne e': "+str(round(frammEsterneW,2))+"%\n")



