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

	buttonOk = Button(wifiInterfaceWindow,text="Ok")

	label.pack(pady=5, padx=5)
	ipLabel.pack(pady=5, padx=5)
	buttonOk.pack(pady=5, padx=5)

	wifiInterfaceWindow.mainloop()

def wifiNotWorking():
	wifiInterfaceWindow = Tk() #Initialisation d'une fenetre Tk vide

	wifiInterfaceWindow.title("Connection au wifi.")

	photo = PhotoImage(file="~/wifi.png")
	label = Label(wifiInterfaceWindow, text="L'appareil n'as pas pu être connecté.")

	canvas = Canvas(wifiInterfaceWindow,width=100, height=72)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	buttonOk = Button(wifiInterfaceWindow,text="Ok")

	label.pack(pady=5, padx=5)
	buttonOk.pack(pady=5, padx=5)

	wifiInterfaceWindow.mainloop()

def wifiConnecting():
	wifiInterfaceWindow = Tk() #Initialisation d'une fenetre Tk vide

	wifiInterfaceWindow.title("Connection au wifi.")

	photo = PhotoImage(file="~/wifi.png")
	label = Label(wifiInterfaceWindow, text="Connection et récuperation de l'IP en cours...")

	canvas = Canvas(wifiInterfaceWindow,width=100, height=72)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	label.pack(pady=5, padx=5)

	wifiInterfaceWindow.mainloop()

