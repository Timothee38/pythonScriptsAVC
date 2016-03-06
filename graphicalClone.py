#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

def cloning():
	cloneWindow	= Toplevel()
	cloneWindow.title("Clonage de tablettes")
	cloneWindow.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/cloning.png")

	canvas = Canvas(cloneWindow, width=640, height=400)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	patientez = Label(cloneWindow, text="Veuillez Patienter...")

	patientez.pack(pady=5)
	cloneWindow.mainloop()

def successCloning():
	cloneWindow = Toplevel()
	cloneWindow.title("Clonage de tablettes")
	cloneWindow.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/AndroidSuccess.png")

	canvas = Canvas(cloneWindow, width=350, height=275)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	operation = Label(cloneWindow, text="Operation effectuée avec succès !")
	operation.pack(pady=5, padx=5)

	buttonOk = Button(cloneWindow,text="Ok")

	buttonOk.pack(pady=5)
	cloneWindow.mainloop()

def failureCloning():
	cloneWindow = Toplevel()
	cloneWindow.title("Clonage de tablettes")
	cloneWindow.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/AndroidFailure.png")

	canvas = Canvas(cloneWindow, width=284, height=276)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	operation = Label(cloneWindow, text="Le clonage a échoué !")
	operation.pack(pady=5, padx=5)

	buttonOk = Button(cloneWindow,text="Ok")

	buttonOk.pack(pady=5)
	cloneWindow.mainloop()

def pluginTemoin():
	cloneWindow = Toplevel()
	cloneWindow.title("Clonage de tablettes")
	cloneWindow.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/plugin.png")

	canvas = Canvas(cloneWindow, width=440, height=214)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	brancher = Label(cloneWindow, text="Brancher la tablette témoin.")
	brancher.pack(pady=5, padx=5)

	boutonOk = Button(cloneWindow, text="Ok")
	boutonOk.pack(pady=(5,10))

	cloneWindow.mainloop()

