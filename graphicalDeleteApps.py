#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import time

def mainWindowDel():
	mainWindow = Tk()
	mainWindow.title("Supprimer des applications")
	mainWindow.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/delete.png")

	canvas = Canvas(mainWindow, width=400, height=130)
	canvas.create_image(135, 0, anchor=NW, image=photo)
	canvas.pack()

	frameCheckButtons = Frame(mainWindow)

	for package in diff:
		diff[package]= Variable()
		l = Checkbutton(frameCheckButtons, text=package, variable=diff[package])
		l.pack()

	frame = Frame(mainWindow)
	boutonOK = Button(frame, text="Supprimer", command=deletingFiles)
	boutonCancel = Button(frame, text="Annuler")
	boutonOK.pack(side=LEFT, padx=5)
	boutonCancel.pack(side=LEFT, padx=5)
	frameCheckButtons.pack(pady=5)
	frame.pack(pady=5)
	mainWindow.mainloop()

def deletingFiles():
	interface = Tk() #Initialisation d'une fenetre Tk vide

	interface.title("Supprimer des applications")

	photo = PhotoImage(file="~/file-transfer.png")
	label = Label(interface, text="Supression des fichiers en cours...")

	canvas = Canvas(interface,width=400, height=310)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	label.pack(pady=5, padx=5)

	interface.mainloop()

def deletingFilesSuccess():
	interface = Tk()
	interface.title("Supprimes des applications")
	interface.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/AndroidSuccess.png")

	canvas = Canvas(interface, width=350, height=275)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	operation = Label(interface, text="Operation effectuée avec succès !")
	operation.pack(pady=5, padx=5)

	buttonOk = Button(interface,text="Ok")

	buttonOk.pack(pady=5)
	interface.mainloop()

def deletingFilesFailure():
	interface = Tk()
	interface.title("Supprimer des applications")
	interface.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/AndroidFailure.png")

	canvas = Canvas(interface, width=350, height=275)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	operation = Label(interface, text="La suppresion a échouée !")
	operation.pack(pady=5, padx=5)

	buttonOk = Button(interface,text="Ok")

	buttonOk.pack(pady=5)
	interface.mainloop()

diff = {"fr.timotheecraig.tim.appli1-2.apk": "fr.timotheecraig.tim.appli1" ,"fr.timotheecraig.tim.cycledevie-1.apk":"fr.timotheecraig.tim.cycledevie", "fr.timotheecraig.tim.cycledevie2-1.apk":"fr.timotheecraig.tim.cycledevie2","fr.timotheecraig.tim.logo1-2.apk":"fr.timotheecraig.tim.logo1", "org.jfedor.frozenbubble-1.apk": "org.jfedor.frozenbubble", "SmartcardService.apk": "org.simalliance.openmobileapi.service"}
