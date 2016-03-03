#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

def wifiConnected(ip):
	wifiInterfaceWindow = Tk() #Initialisation d'une fenetre Tk vide

	wifiInterfaceWindow.title("Connection au wifi.")

	photo = PhotoImage(file="~/wifi.png")
	label = Label(wifiInterfaceWindow, text="L'appareil à été connecté avec succès.")
	ipLabel = Label(wifiInterfaceWindow, text="Votre ip est "+ip)

	canvas = Canvas(wifiInterfaceWindow,width=100, height=72)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	label.pack()
	ipLabel.pack()

	wifiInterfaceWindow.mainloop()

wifiConnected("192.168.5.2")