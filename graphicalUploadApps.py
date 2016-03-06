#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog

def askopenfile(self):
    return tkFileDialog.askopenfile(mode='r', **self.file_opt)


def uploadFileSuccess():
	interface = Tk()
	interface.title("Installer des fichiers")
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

def uploadFileFailure():
	interface = Tk()
	interface.title("Installer des fichiers")
	interface.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/AndroidFailure.png")

	canvas = Canvas(interface, width=350, height=275)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	operation = Label(interface, text="L'installation a échouée !")
	operation.pack(pady=5, padx=5)

	buttonOk = Button(interface,text="Ok")

	buttonOk.pack(pady=5)
	interface.mainloop()

def uploadingFile():
	interface = Tk() #Initialisation d'une fenetre Tk vide

	interface.title("Installer des fichiers")

	photo = PhotoImage(file="~/file-transfer.png")
	label = Label(interface, text="Envoi et installation des fichiers en cours...")

	canvas = Canvas(interface,width=400, height=310)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	label.pack(pady=5, padx=5)

	interface.mainloop()

def uploadFilePrompt():

	interface = Tk()
	interface.title("Installer des fichiers")
	interface.resizable(width=FALSE, height=FALSE)

	photo = PhotoImage(file="~/FileUpload.png")

	canvas = Canvas(interface, width=330, height=170)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	canvas.pack()

	operation = Label(interface, text="Choisissez votre fichier.")
	operation.pack(pady=5, padx=5)

	browse = Button(interface, text='Parcourir...')
	browse.pack(pady=5)

	interface.mainloop()

