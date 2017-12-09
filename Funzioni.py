import random
import sys
import copy
import datetime
import re

from PartizioneMemoria import *
from Processo import *
from AllocatoreMemoria import *
from File import *

#la funzione permette di verificare la frammentazione esterna
def verificaFrammentazioneEsterna(dim_processo,blocchi):
	# inizializzazione di una variabile che indica la dimensione dei blocchi liberi
	dim_blocchi = 0
	# inizializzazione di una variabile che indica il blocco con la dimensione massima
	blocco_max = 0

	framm_esterna = 0
	i = 0
	# ciclo che termina alla fine dei blocchi di memoria e che permette di calcolare la dimensione di tutti i blocchi liberi
	while( i < len(blocchi.listaPartizioni) ):
		# confornto se il blocco di memoria con indice i e' vuoto
		if( blocchi.listaPartizioni[i].stato == False ):
			# Incremento della variabile dim_blocchi con la dimensione del blocco di indice i vuoto
			dim_blocchi = dim_blocchi + blocchi.listaPartizioni[i].dimensionePartizione()
		i = i + 1

	i = 0
	# ciclo che mi permette di verificare qual'e' il blocco libero piu' grande tra i blocchi di memoria
	while( i < len(blocchi.listaPartizioni) ):
		# condizione che permette di verificare se il bocco e' vuoto e se e' maggiore della variabile che indica la dimensione del blocco libero piu' grande
		if( blocchi.listaPartizioni[i].stato == False and blocchi.listaPartizioni[i].dimensionePartizione() > blocco_max ):
			# setto la variabile blocco_max con la dimensione del blocco libero piu' grande
			blocco_max = blocchi.listaPartizioni[i].dimensionePartizione()
		i = i + 1
	stampa.write("questo e' il blocco max: "+str(blocco_max)+" dimensione blocchi: "+str(dim_blocchi))		
	# Controllo se la dimensione dei blocchi liberi potrebbe contenere il processo che non e' stato allocato
	if( dim_blocchi >= dim_processo ):
		# Formula per il calcolo della frammentazione esterna
		stampa.write(str(blocco_max)+"  "+str(dim_blocchi))
		framm_esterna=(1.0 * 1)-(( 1.0 * blocco_max ) / ( 1.0 * dim_blocchi))
		# ritorno della variabile framm_esterna
		return framm_esterna
	return 0

#la funzione permette di creare tutti i processi
def creaProcessiAttesa():
	nProcessi = random.randint(20,40)

	processiAttesa = []

	for i in range(0, nProcessi):
		dim = random.randint(500,5000)
		ingProcesso = random.randint(0,20)
		tEx = random.randint(20,40)
		processiAttesa.append(Processo(dim, ingProcesso, tEx))

	return processiAttesa

#la funzione permette di ordinare i processi generati in base al loro tempo di ingresso
def ordinaProcessi(lista):
    for pnum in range(len(lista)-1,0,-1):
        for i in range(pnum):
            if lista[i].ingProcesso>lista[i+1].ingProcesso:
                x = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = x

#la funzione permette di stampare lo stato della memoria
def stampaPartizioniMemoria(partMemoria):
	stringa = ""
	stampa.write("stampa della memoria!\n")
	for i in range (0, len(partMemoria.listaPartizioni)):
		if partMemoria.listaPartizioni[i].stato == True:
			stringa+=(" |"+str(partMemoria.listaPartizioni[i].dimensionePartizione())+"| ")
		else:
			stringa+=(" *"+str(partMemoria.listaPartizioni[i].dimensionePartizione())+"* ")

	stampa.write(stringa)

#la funzione permette di decrementare il tempo di vita dei processi in esecuzione ad ogni ciclo
def decrementoEsecuzioneProcessi(pEsecuzione):
	for i in range(0, len(pEsecuzione)):
		pEsecuzione[i].exProcesso -= 1

#la funzione permette di verificare se un processo ha terminato il proprio tempo di esecuzione
def verificaTerminazioneProcessi(memoria, processiEsecuzione):
	l = 0
	i = 0
	numProcessi = len(processiEsecuzione)
	while(i<numProcessi):
		if processiEsecuzione[i].exProcesso == 0: #se il processo ha terminato la sua esecuzione
			processiEsecuzione[i].partizioneOccupata.stato = False
			
			#freelist
			memoria.FreeList.append(processiEsecuzione[i].partizioneOccupata)

			del processiEsecuzione[i]
			numProcessi-=1
			
			unionePartizioni(memoria)

			stampa.write("Processo terminato; Stato della nuova memoria: ")
			stampaPartizioniMemoria(memoria)

			i-=1
			l+=1
		i+=1
	return l

#la funzione permette di unire due partizioni di memoria vicine
def unionePartizioni(partMemoria):
	i = 0
	numBlocchi = len(partMemoria.listaPartizioni)-1
	while (i<numBlocchi):
		if partMemoria.listaPartizioni[i].stato == False and partMemoria.listaPartizioni[i+1].stato == False:
			k = partMemoria.listaPartizioni[i+1].valFine
			del partMemoria.listaPartizioni[i+1]
			partMemoria.listaPartizioni[i].valFine = k
			i-=1
			numBlocchi-=1
		i+=1

#la funzione permette di allocare la memoria, e quindi permette di inserire nella lista delle partizioni quelle generate
def allocaMemoria(partMemoria, i, processo):
	iniziob1 = partMemoria.listaPartizioni[i].valInizio 
	split = iniziob1 + processo.dimProcesso 
	fineb2 = partMemoria.listaPartizioni[i].valFine 

	del partMemoria.listaPartizioni[i]

	b1 = PartizioneMemoria(iniziob1, split)
	b1.stato = True

	b2 = PartizioneMemoria(split, fineb2)

	partMemoria.listaPartizioni.insert(i, b1)
	
	partMemoria.listaPartizioni.insert(i+1, b2)

#la funzione permette di generare un menu'
def menu():
	return int(raw_input("\nSELEZIONA METODO\n\n1- First Fit\n2- Best Fit\n3- Worst Fit\n4- Tutti i precedenti\n"))
