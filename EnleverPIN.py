# -*- coding: utf8 -*-
# Imports necessaires
import re
import sys
import os
import random
name = os.popen('whoami').read()
cutName = name.split("\n")
name = cutName[0]
sys.path.append('~/AndroidViewClient/src/')
from com.dtmilano.android.viewclient import ViewClient
from com.dtmilano.android.adb.adbclient import AdbClient
device, serialno = ViewClient.connectToDeviceOrExit()
if not device:
	raise Exception("Connection avec l'appareil impossible.")
#retour à la page d'accueuil du téléphone pour commencer les manips (on appuie sur la touche de retour a l'accueuil du téléphone)
device.press('KEYCODE_HOME')
#Lancement de paramètres
package = 'com.android.settings'
activity = '.Settings'
componentName = package + "/" + activity
device.startActivity(componentName)
#Creation d'un objet ViewClient
vc = ViewClient(device=device, serialno=serialno)
# on défile l'écran pour faire apparaître “Sécurité”
device.drag((100,600),(100,100),1,20)
vc.sleep(0.1) #pause pour charger l'affichage
vc.dump() #dump récupère l'arbre de l'IHM dans ViewClient
# On clique sur l'onglet "Sécurité"
security = vc.findViewWithText(u"Ecran de verrouillage") # utf-8
security.touch() # on declenche l'appui
vc.sleep(0.1) #pause
vc.dump()
#On clique sur l'onglet "Verrouillage de l'écran"
mode = vc.findViewWithText(u"Glissement")
if mode is None:
	verrou = vc.findViewWithText(u"Déverrouillage de l'écran")
	verrou.touch()
	vc.sleep(0.1)
	vc.dump()
	fichier = open("/home/"+name+"/AVCData/CodesPIN.txt", "r")
	codePin = 0
	for ligne in fichier.readlines():
		ligneSeparee = ligne.split(" : ")
		codePin = ligneSeparee[1]
		if ligneSeparee[0]==("PIN"+serialno):
			print codePin
	fichier.close()
	password = vc.findViewByIdOrRaise("id/no_id/18")
	password.type(codePin)
	vc.sleep(0.1)
	vc.dump()
	ctn = vc.findViewWithText('Continuer')
	ctn.touch()
	vc.sleep(0.1)
	vc.dump()
	gliss = vc.findViewWithText(u"Glissement")
	gliss.touch() #On "clique" ici en touchant l'écran.
	vc.sleep(0.2)
	vc.dump()

	
else:
	print "Cet appareil n'est pas verouillé par code PIN"
