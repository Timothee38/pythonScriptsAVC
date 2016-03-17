#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import os
import subprocess

#Main variables
afterPluggedCommand = ""
username = os.popen('whoami').read()
cutUsername = username.split('\n')
username = cutUsername[0]

##Data pour suppression packages
nomFichierPackages = "/packages.txt"
genericFilePath = "/home/" + username
filePathPackages =  genericFilePath + nomFichierPackages

diff = {}
packagelist = {}

#Gestion Brancement tablette
class PlugTablet(Frame):
	def __init__(self,master):
		Frame.__init__(self, master)
		self.master = master

		self.photo = PhotoImage(file="~/plugin.png")

		self.canvas = Canvas(self, width=440, height=214)
		self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		self.brancher = Label(self, text="Brancher la tablette par USB et cliquez sur OK.")
		self.brancher.pack(pady=5, padx=5)

		self.boutonOk = Button(self, text="Ok", command=self.close_windows)
		self.boutonOk.pack(pady=(5,10))

		self.pack()

	def close_windows(self):
		global afterPluggedCommand, filePathPackages, diff, packagelist
		self.destroy()
		self.master.withdraw()
		if afterPluggedCommand != "":
			self.newWindow = Toplevel(self.master)
			if afterPluggedCommand=="delete":
				#The packages we want to delete start with: package:/data/app whereas others that we want to be "native" start with package:/system/app
				os.system("adb shell pm list packages -f | grep apk* > " + filePathPackages)
				fichierPackages = open(filePathPackages, 'r')
				lignes = fichierPackages.readlines()
				for ligne in lignes:
					coupeLigne = ligne.split("=") #List: ["package:x/y/z.domain.name.apk","tld.domain.name.package"]
					if "package:/data/app/" in coupeLigne[0]:
						apkName = coupeLigne[0].replace("package:/data/app/","")
						diff[apkName] = coupeLigne[1]
						packagelist[apkName] = coupeLigne[1]
				self.app = DeleteAppsCheckboxes(self.newWindow)
			elif afterPluggedCommand=="add":
				self.app = AddAppsFirst(self.newWindow)
			elif afterPluggedCommand=="wifi":
				self.app = WifiFirst(self.newWindow)


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

class WifiLoading(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		self.photo = PhotoImage(file="~/wifi.png")
		self.label = Label(self, text="Connection et récuperation de l'IP en cours...")

		self.canvas = Canvas(self,width=100, height=72)
		self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		self.label.pack(pady=5, padx=5)

		self.pack()

##DELETE APPS
class DeleteAppsCheckboxes(Frame):
	def __init__(self, master):
		##Diff=tous les packages - packages connus (a mettre en fichier texte)
		global diff
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
			self.l.deselect()
			self.l.pack()

		self.frame = Frame(self)
		self.boutonOK = Button(self.frame, text="Supprimer", command=self.delete_files)
		self.boutonCancel = Button(self.frame, text="Annuler", command=self.close_windows)
		self.boutonOK.pack(side=LEFT, padx=5)
		self.boutonCancel.pack(side=LEFT, padx=5)
		self.frameCheckButtons.pack(pady=5)
		self.frame.pack(pady=5)
		self.pack()

	def close_windows(self):
		self.master.destroy()

	def delete_files(self):
		global diff, packagelist
		self.destroy()
		self.master.withdraw()
		failureCount = 0

		for apkFileName in diff:
			status = diff[apkFileName].get()
			if status=="1":
				packageToUninstall = packagelist[apkFileName]
				uninstall = "adb uninstall " + packageToUninstall
				uninstallList = uninstall.split("\n")
				uninstall = uninstallList[0].replace("\r","")
				print uninstall
				returnVariable = os.popen(uninstall).read()
				if returnVariable != "Success\r\n":
					failureCount+=1
		self.newWindow = Toplevel(self.master)
		diff = {} #Reinitialisation de diff
		if failureCount!=0:
			self.app = DeletingFilesFailure(self.newWindow)
		else:
			self.app = DeletingFilesSuccess(self.newWindow)

	def delete_success(self):
		self.destroy()
		self.master.withdraw()
		self.newWindow = Toplevel(self.master)
		self.app = DeletingFilesSuccess(self.newWindow)

class DeletingFilesSuccess(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.master = master

		self.photo = PhotoImage(file="~/AndroidSuccess.png")

		self.canvas = Canvas(self, width=350, height=275)
		self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		self.operation = Label(self, text="Operation effectuée avec succès !")
		self.operation.pack(pady=5, padx=5)

		self.buttonOk = Button(self,text="Ok",command=self.close_windows)

		self.buttonOk.pack(pady=5)

		self.pack()

	def close_windows(self):
		self.destroy()
		self.master.withdraw()


class DeletingFilesFailure(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.master = master

		self.photo = PhotoImage(file="~/AndroidFailure.png")

		self.canvas = Canvas(self, width=350, height=275)
		self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
		self.canvas.pack()

		self.operation = Label(self, text="La suppresion a échoué !")
		self.operation.pack(pady=5, padx=5)

		self.buttonOk = Button(self,text="Ok",command=self.close_windows)

		self.buttonOk.pack(pady=5)

		self.pack()

	def close_windows(self):
		self.destroy()
		self.master.withdraw()



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
		global afterPluggedCommand
		afterPluggedCommand="wifi"
		self.newWindow = Toplevel(self.master)
		self.app = PlugTablet(self.newWindow)
	def openDelete(self):
		global afterPluggedCommand
		afterPluggedCommand="delete"
		self.newWindow = Toplevel(self.master)
		self.app = PlugTablet(self.newWindow)

	def openClone(self):
		self.newWindow = Toplevel(self.master)
		self.app = CloneFirst(self.newWindow)
	def openAdd(self):
		global afterPluggedCommand
		afterPluggedCommand="add"
		self.newWindow = Toplevel(self.master)
		self.app = PlugTablet(self.newWindow)


def main():
	root = Tk()
	app = MainMenu(root)
	root.title(u"Déploiement Android")
	root.resizable(height=FALSE, width=FALSE)
	root.mainloop()
	root.destroy()

if __name__ == '__main__':
	main()
