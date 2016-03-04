#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

def mainWindow():
	mainWindowDep = Tk()
	mainWindowDep.title("Déploiement Android")
	mainWindowDep.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/android-logo-png.png")

	canvas = Canvas(mainWindowDep,width=580, height=320)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	texteWifiFirst = Label(mainWindowDep, text="Attention: Veuillez d'abord configurer tous vos appareils en wifi.", fg="red")
	texteWifiFirst.pack(pady=5)

	frame = Frame(mainWindowDep)
	frame.pack()

	frameBas = Frame(mainWindowDep)
	frameBas.pack(pady=5)

	deleteBtn = Button(frame, text="Supprimer des applications", width=20, height=3)
	deleteBtn.pack(side=LEFT,padx=5)

	addBtn = Button(frame, text="Ajouter des applications", width=20, height=3)
	addBtn.pack(side=LEFT,padx=5)

	wifiBtn = Button(frameBas, text="Connection wifi", width=20, height=3)
	wifiBtn.pack(side=LEFT,padx=5)

	pinBtn = Button(frameBas, text="Configurer PIN", width=20, height=3)
	pinBtn.pack(side=LEFT,padx=5)

	cloneBtn = Button(mainWindowDep, text="Cloner une tablette témoin", height=3, width=45)
	cloneBtn.pack(pady=(2.5,15))

	mainWindowDep.mainloop()

mainWindow()
