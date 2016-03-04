#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

def mainWindowDel(diff):
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
	boutonOK = Button(frame, text="Supprimer")
	boutonCancel = Button(frame, text="Annuler")
	boutonOK.pack(side=LEFT, padx=5)
	boutonCancel.pack(side=LEFT, padx=5)
	frameCheckButtons.pack(pady=5)
	frame.pack(pady=5)
	mainWindow.mainloop()


diff = {"fr.timotheecraig.tim.appli1-2.apk": "fr.timotheecraig.tim.appli1" ,"fr.timotheecraig.tim.cycledevie-1.apk":"fr.timotheecraig.tim.cycledevie", "fr.timotheecraig.tim.cycledevie2-1.apk":"fr.timotheecraig.tim.cycledevie2","fr.timotheecraig.tim.logo1-2.apk":"fr.timotheecraig.tim.logo1", "org.jfedor.frozenbubble-1.apk": "org.jfedor.frozenbubble", "SmartcardService.apk": "org.simalliance.openmobileapi.service"}
mainWindowDel(diff)