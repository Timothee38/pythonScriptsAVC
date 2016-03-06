#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

diff = {"fr.timotheecraig.tim.appli1-2.apk": "fr.timotheecraig.tim.appli1" ,"fr.timotheecraig.tim.cycledevie-1.apk":"fr.timotheecraig.tim.cycledevie", "fr.timotheecraig.tim.cycledevie2-1.apk":"fr.timotheecraig.tim.cycledevie2","fr.timotheecraig.tim.logo1-2.apk":"fr.timotheecraig.tim.logo1", "org.jfedor.frozenbubble-1.apk": "org.jfedor.frozenbubble", "SmartcardService.apk": "org.simalliance.openmobileapi.service"}


##WIFI
class WifiFirst(Frame):
	def __init__(self,master):
		Frame.__init__(self, master)
		#Success because testing purposes
		self.master = master
		self.photo = PhotoImage(file="~/wifi.png")
		self.label = Label(self, text="L'appareil à été connecté avec succès.")
		self.ipLabel = Label(self, text="Votre ip est x.x.x.x")

		self.canvas = Canvas(self,width=100, height=72)
		self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		self.buttonOk = Button(self,text="Ok",command=self.close_windows)

		self.label.pack(pady=5, padx=5)
		self.ipLabel.pack(pady=5, padx=5)
		self.buttonOk.pack(pady=5, padx=5)

		self.pack()

	def close_windows(self):
		self.master.destroy()

##DELETE APPS
class DeleteAppsFirst(Frame):

	##Diff=tous les packages - packages connus (a mettre en fichier texte)
	global diff
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master=master

		self.photo = PhotoImage(file="~/delete.png")

		self.canvas = Canvas(self, width=400, height=130)
		self.canvas.create_image(135, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		self.frameCheckButtons = Frame(self)

		for package in diff:
			diff[package]= Variable()
			self.l = Checkbutton(self.frameCheckButtons, text=package, variable=diff[package])
			self.l.pack()

		self.frame = Frame(self)
		self.boutonOK = Button(self.frame, text="Supprimer")
		self.boutonCancel = Button(self.frame, text="Annuler", command=self.close_windows)
		self.boutonOK.pack(side=LEFT, padx=5)
		self.boutonCancel.pack(side=LEFT, padx=5)
		self.frameCheckButtons.pack(pady=5)
		self.frame.pack(pady=5)
		self.pack()

	def close_windows(self):
		self.master.destroy()

##CLONE DEVICE
class CloneFirst(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master

		self.photo = PhotoImage(file="~/plugin.png")

		self.canvas = Canvas(self, width=440, height=214)
		self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		self.brancher = Label(self, text="Brancher la tablette témoin.")
		self.brancher.pack(pady=5, padx=5)

		self.boutonOk = Button(self, text="Ok")
		self.boutonOk.pack(pady=(5,10))

		self.pack()



##ADD APPS
class AddAppsFirst(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master

		self.photo = PhotoImage(file="~/FileUpload.png")

		self.canvas = Canvas(self, width=330, height=170)
		self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		operation = Label(self, text="Choisissez votre fichier.")
		operation.pack(pady=5, padx=5)

		browse = Button(self, text='Parcourir...')
		browse.pack(pady=5)

		self.pack()

##MAIN MENU
class MainMenu(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master=master

		self.photo = PhotoImage(file="~/android-logo-png.png")

		self.canvas = Canvas(self,width=580, height=320)
		self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		self.texteWifiFirst = Label(self, text="Attention: Veuillez d'abord configurer tous vos appareils en wifi.", fg="red").pack(pady=5)

		self.frame = Frame(self)

		self.frameBas = Frame(self)

		self.deleteBtn = Button(self.frame, text="Supprimer des applications", width=20, height=3,command=self.openDelete).pack(side=LEFT,padx=5)

		self.addBtn = Button(self.frame, text="Ajouter des applications", width=20, height=3, command=self.openAdd).pack(side=LEFT,padx=5)

		self.wifiBtn = Button(self.frameBas, text="Connection wifi", width=20, height=3, command=self.openWifi).pack(side=LEFT,padx=5)

		self.cloneBtn = Button(self.frameBas, text="Cloner une tablette témoin", width=20, height=3, command=self.openClone).pack(side=LEFT,padx=5)

		self.frame.pack()
		self.frameBas.pack(pady=5)

		self.copyright = Label(self, text="© Craig, Landes & Hubert").pack(pady=(5,10))
		self.pack()

	def openWifi(self):
		self.newWindow = Toplevel(self.master)
		self.app = WifiFirst(self.newWindow)

	def openDelete(self):
		self.newWindow = Toplevel(self.master)
		self.app = DeleteAppsFirst(self.newWindow)

	def openClone(self):
		self.newWindow = Toplevel(self.master)
		self.app = CloneFirst(self.newWindow)

	def openAdd(self):
		self.newWindow = Toplevel(self.master)
		self.app = AddAppsFirst(self.newWindow)



def main():
	root = Tk()
	app = MainMenu(root)
	root.title(u"Déploiement Android")
	root.resizable(height=FALSE, width=FALSE)
	root.mainloop()
	root.destroy()

if __name__ == '__main__':
    main()