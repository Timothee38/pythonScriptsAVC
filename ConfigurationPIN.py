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
vc.sleep(0.01) #pause pour charger l'affichage
vc.dump() #dump récupère l'arbre de l'IHM dans ViewClient
# On clique sur l'onglet "Sécurité"
security = vc.findViewWithText(u"Ecran de verrouillage") # utf-8
security.touch() # on declenche l'appui
vc.sleep(0.01) #pause
vc.dump()
#On clique sur l'onglet "Verrouillage de l'écran"
mode = vc.findViewWithText(u"Glissement")
if mode	is not None: 
	mode.touch() #On "clique" ici en touchant l'écran.
	vc.sleep(0.02)
	vc.dump()
	#Setup du code pin
	pin = vc.findViewWithText('Code PIN')
	pin.touch()# On clique sur le bouton "PIN"
	vc.sleep(0.02)
	vc.dump()
	# On choisit la zone de saisie de texte
	# choix par id car l'Edit Text n'a pas de nom
	password = vc.findViewByIdOrRaise("id/no_id/18")
	#Creation d'un code PIN aleatoire entre 1000 & 9999
	rand = str(random.randint(1000,9999))
	print rand # affichage console du code PIN
	#Creation/ouverture d'un fichier txt
	fichier = open("/home/"+name+"/AVCData/CodesPIN.txt", "a")
	#Inscription du PIN dans ce fichier txt
	fichier.write("PIN"+serialno+" : "+rand+"\n")
	fichier.close()
	password.type(rand) #écriture du mot de passe
	vc.sleep(0.01)
	vc.dump()
	ctn = vc.findViewWithText('Continuer')
	ctn.touch() # appui sur Continuer
	vc.sleep(0.01)
	vc.dump()
	password = vc.findViewByIdOrRaise("id/no_id/18")
	password.type(rand) # 2ème saisie du mot de passe
	vc.sleep(0.01)
	vc.dump()
	ok = vc.findViewWithText('OK')
	ok.touch() # confirmation
else:
	print "Ce Smartphone déjà sécurisé par code PIN"
