#!/usr/bin/env python
# -*- coding: UTF -8 -*-
import os
name = os.popen('whoami').read()
cutName = name.split("\n")
name = cutName[0]
nomFichTemoin = "/temoin.txt"
filePath = "/home/" + name + nomFichTemoin

difference = [] #Liste des differences entre la tablette témoin et la tablette a modifier.

print u"brancher une tablette témoin"
x = raw_input("bien branchée ? o/n")
if x == "o":
	os.system("adb shell pm list packages -f | grep apk* > " + filePath) #Ajout de tous les packages listés dans le shell dans un fichier.
	fichierTemoin = open(filePath, 'r')	#ouverture de ce fichier
	temoin = fichierTemoin.read() #Lecture du fichier
	fichierTemoin.close()	#Fermeture du fichier
	print "Branchez les autres tablettes"
	autreTab = 	raw_input("bien branchées ? o/n")
	if autreTab == "o":
		nomFichAutre = "/appareil1.txt"	#Chemin du fichier de la tablette a laquelle on apporte les modifications...
		filePath = "/home/" + name + nomFichAutre
		os.system("adb shell pm list packages -f | grep apk* > " + filePath)
		fichierAutreAppareil = open(filePath, 'r')
		autre = fichierAutreAppareil.read()
		fichierAutreAppareil.close()
		for ligne in autre.split("\n"): #Découpage du fichier de la tablette a laquelle on apporte les modifs
			lignesTemoin = temoin.split("\n") #Découpage dans une liste du contenu du fichier de la tablette témoin
			if ligne not in lignesTemoin:
				difference.append(ligne)
			if len(difference)!=0: #On regarde d'abord s'il y a des différences
				for i in difference:	#Et on parcours ces differences...
					lignecoupee = i.split("=")
					lignecoupee = lignecoupee[1].split("\r")
					os.system("adb uninstall " + lignecoupee[0]) #pour les désinstaller de la tablette...

