# -*- coding: utf8 -*-
# Imports necessaires
import re
import sys
import os
import random
sys.path.append('C:\\Python27\\Lib\\site-packages\\androidviewclient-11.1.0-py2.7.egg\\')
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
#device.drag((100,600),(100,100),1,20)
vc.sleep(0.1) #pause pour charger l'affichage
vc.dump() #dump récupère l'arbre de l'IHM dans ViewClient

bouton = vc.findViewByIdOrRaise("id/no_id/24")
bouton.touch()
vc.sleep(0.1) #pause pour charger l'affichage
vc.dump()
#On clique sur l'onglet "Verrouillage de l'écran"
mode = vc.findViewWithText(u"Projet Android RT")
mode.touch()
vc.sleep(0.1) #pause pour charger l'affichage
vc.dump()

password = vc.findViewByIdOrRaise("id/no_id/16")
password.type("toto1234")
vc.sleep(0.1)
vc.dump()
ok = vc.findViewWithText('Connexion')
ok.touch()

