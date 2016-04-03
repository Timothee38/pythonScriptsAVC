#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import Image, ImageTk

from tkFileDialog import *
import os

# Main variables
afterPluggedCommand = ""
username = os.popen('echo %USERNAME%').read()
cutUsername = username.split('\n')
username = cutUsername[0]

devices = []

##Data pour suppression packages
nomFichierPackages = "\\androidDepPackages.txt"
nomFichierTemoin = "\\androidDepTemoin.txt"
apkFolder = "\\androidDepApk"
genericFilePath = "C:\\Users\\" + username + "\\Desktop"

filePathAPKs = genericFilePath + apkFolder
if not os.path.exists(filePathAPKs):
    os.makedirs(filePathAPKs)

for the_file in os.listdir(filePathAPKs):
    file_path = os.path.join(filePathAPKs, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception, e:
        print e

filePathPackages = genericFilePath + nomFichierPackages
filePathTemoin = genericFilePath + nomFichierTemoin
pathToApp = ""

diff = {}
packagelist = {}


# Gestion Branchement tablette
class PlugTablet(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\plugin.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=440, height=214)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.brancher = Label(self, text="Brancher votre appareil par USB et cliquez sur OK.")
        self.brancher.pack(pady=5, padx=5)

        self.boutonOk = Button(self, text="Ok", command=self.close_windows)
        self.boutonOk.pack(pady=(5, 10))

        self.pack()

    def close_windows(self):
        global afterPluggedCommand, filePathPackages, diff, packagelist
        self.destroy()
        self.master.withdraw()
        if afterPluggedCommand != "":
            self.newWindow = Toplevel(self.master)
            if afterPluggedCommand == "delete":
                # The packages we want to delete start with: package:/data/app whereas others that we want to be "native" start with package:/system/app
                os.system("adb.exe shell pm list packages -f > " + filePathPackages)
                fichierPackages = open(filePathPackages, 'r')
                lignes = fichierPackages.readlines()
                for ligne in lignes:
                    coupeLigne = ligne.split("=")  # List: ["package:x/y/z.domain.name.apk","tld.domain.name.package"]
                    if "package:/data/app/" in coupeLigne[0]:
                        apkName = coupeLigne[0].replace("package:/data/app/", "")
                        diff[apkName] = coupeLigne[1]
                        packagelist[apkName] = coupeLigne[1]
                fichierPackages.close()
                print diff
                self.app = DeleteAppsCheckboxes(self.newWindow)
            elif afterPluggedCommand == "add":
                self.app = AddAppsFirst(self.newWindow)
            elif afterPluggedCommand == "wifi":
                self.app = WifiFirst(self.newWindow)
            elif afterPluggedCommand == "clone":
                self.app = GetTemoin(self.newWindow)


##WIFI
class WifiFirst(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # Success because testing purposes
        self.master = master
        self.image = Image.open("img\\wifi.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(self, text="L'appareil à été connecté avec succès.")
        self.ipLabel = Label(self, text="Votre ip est x.x.x.x")

        self.canvas = Canvas(self, width=100, height=72)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.buttonOk = Button(self, text="Ok", command=self.close_windows)

        self.label.pack(pady=5, padx=5)
        self.ipLabel.pack(pady=5, padx=5)
        self.buttonOk.pack(pady=5, padx=5)

        self.pack()

    def close_windows(self):
        self.master.destroy()


##DELETE APPS
class DeleteAppsCheckboxes(Frame):
    def __init__(self, master):
        ##Diff=tous les packages - packages connus (a mettre en fichier texte)
        global diff
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\delete.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=400, height=130)
        self.canvas.create_image(135, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.frameCheckButtons = Frame(self)

        for package in diff:
            diff[package] = Variable()
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
        if status == "1":
            packageToUninstall = packagelist[apkFileName]
            uninstall = "adb.exe uninstall " + packageToUninstall
            uninstallList = uninstall.split("\n")
            uninstall = uninstallList[0].replace("\r", "")
            print uninstall
            returnVariable = os.popen(uninstall).read()
            if returnVariable != "Success\r\n":
                failureCount += 1
        self.newWindow = Toplevel(self.master)
        diff = {}  # Reinitialisation de diff
        if failureCount != 0:
            self.app = Failure(self.newWindow)
        else:
            self.app = Success(self.newWindow)


class Success(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\AndroidSuccess.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=350, height=275)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.operation = Label(self, text="Opération effectuée avec succès !")
        self.operation.pack(pady=5, padx=5)

        self.buttonOk = Button(self, text="Ok", command=self.close_windows)

        self.buttonOk.pack(pady=5)

        self.pack()

    def close_windows(self):
        self.destroy()
        self.master.withdraw()


class Failure(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\AndroidFailure.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=350, height=275)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.operation = Label(self, text="L'opération a échoué !")
        self.operation.pack(pady=5, padx=5)

        self.buttonOk = Button(self, text="Ok", command=self.close_windows)

        self.buttonOk.pack(pady=5)

        self.pack()

    def close_windows(self):
        self.destroy()
        self.master.withdraw()


##ADD APPS
class AddAppsFirst(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\FileUpload.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=330, height=170)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.operation = Label(self, text="Choisissez votre fichier a installer.")
        self.operation.pack(pady=5, padx=5)

        self.browse = Button(self, text='Parcourir...', command=self.openFileToInstall)
        self.browse.pack(pady=5)

        self.pack()

    def openFileToInstall(self):
        global pathToApp
        pathToApp = askopenfilename(filetypes=[('Android Package File', '*.apk')])
        print pathToApp
        self.destroy()
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = AddAppsConfirm(self.newWindow)


class AddAppsConfirm(Frame):
    def __init__(self, master):
        global pathToApp
        Frame.__init__(self, master)
        self.master = master

        apkList = pathToApp.split("/")
        apkName = apkList[-1]

        self.image = Image.open("img\\androidQuestion.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=174, height=70)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack(padx=10)

        self.areYouSure = Label(self, text="Installer " + apkName + " ?")
        self.frame = Frame(self)
        self.oui = Button(self.frame, text="Oui", command=self.installApp)
        self.non = Button(self.frame, text="Non", command=self.close_windows)

        self.areYouSure.pack(pady=5, padx=5)
        self.frame.pack(pady=5, padx=5)
        self.non.pack(side=RIGHT)
        self.oui.pack(side=LEFT)

        self.pack()

    def close_windows(self):
        self.destroy()
        self.master.withdraw()

    def installApp(self):
        global pathToApp
        install = 'adb.exe install "' + pathToApp + '"'
        print install
        resultat = os.popen(install).read()
        print resultat
        self.destroy()
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        if "Success\r\n" not in resultat:
            Failure(self.newWindow)
        else:
            Success(self.newWindow)


##CLONE DEVICE
class GetTemoin(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\file-transfer.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=400, height=310)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.working = Label(self, text=u"Informations récupérées")
        self.working.pack(pady=5)

        self.boutonOK = Button(self, text="OK", command=self.next_window)
        self.boutonOK.pack(pady=5)

        self.pack()

        self.recup()

    def recup(self):
        global filePathTemoin, filePathAPKs
        os.system("adb.exe shell pm list packages -f -3 > " + filePathTemoin)
        fichierTemoin = open(filePathTemoin, 'r')
        command = 'cd "' + filePathAPKs + '"'
        print command
        os.system(command)
        for ligne in fichierTemoin.readlines():
            package = ligne.split("=")
            toPull = package[0].split(":")
            os.system("adb.exe pull " + toPull[1] + ' "' + filePathAPKs + '"')

            fichierTemoin.close()

    def next_window(self):
        self.destroy()
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = UnPlugTemoin(self.newWindow)


class UnPlugTemoin(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\plugin.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=440, height=214)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.brancher = Label(self, text=u"Debranchez l'appareil témoin et cliquez sur OK.")
        self.brancher.pack(pady=5, padx=5)

        self.boutonOk = Button(self, text="Ok", command=self.close_windows)
        self.boutonOk.pack(pady=(5, 10))

        self.pack()

    def close_windows(self):
        self.destroy()
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = BranchementAutres(self.newWindow)


class BranchementAutres(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\multiple.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=450, height=336)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.brancher = Label(self, text=u"Branchez par USB les appareils à cloner et cliquez sur OK.")
        self.brancher.pack(pady=5, padx=5)

        self.boutonOk = Button(self, text="Ok", command=self.close_windows)
        self.boutonOk.pack(pady=(5, 10))

        self.pack()

    def close_windows(self):
        self.destroy()
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = HowMany(self.newWindow)


class HowMany(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\androidQuestion.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=174, height=150)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.readDevices()

        self.boutonOk = Button(self, text="Ok", command=self.close_windows)
        self.boutonOk.pack(pady=(5, 10))

        self.pack()

    def readDevices(self):
        global devices
        result = os.popen("adb.exe devices").read()
        for ligne in result.split("\n"):
            if "\tdevice" in ligne:
                devices.append(ligne)

        texte = "Il y a " + str(len(devices)) + u" appareils connectés..."
        self.howmany = Label(self, text=texte)
        self.howmany.pack(padx=5)

    def close_windows(self):
        self.destroy()
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = DoOperations(self.newWindow)


class DoOperations(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\AndroidSuccess.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=350, height=275)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.texte = Label(self, text=u"Machines clonées avec succès !")
        self.texte.pack()

        self.boutonOk = Button(self, text="Ok", command=self.close_windows)
        self.boutonOk.pack(pady=(5, 10))

        self.clonage()

        self.pack()

    def clonage(self):
        global devices, filePathPackages, filePathTemoin, filePathAPKs
        for device in devices:
            serial = device.split("\t")
            serialNo = serial[0]
            os.system("adb.exe -s " + serialNo + " shell pm list packages -f -3 > " + filePathPackages)
            install = []
            uninstall = []
            fichierTemoin = open(filePathTemoin, 'r')
            fichierAutreTab = open(filePathPackages, 'r')
            contentfichierTemoin = fichierTemoin.readlines()
            contentfichierAutre = fichierAutreTab.readlines()

            for package in contentfichierAutre:
                if package not in contentfichierTemoin:
                    uninstall.append(package)
                    for packet in contentfichierTemoin:
                        if packet not in contentfichierAutre:
                            install.append(packet)

                    fichierTemoin.close()
                    fichierAutreTab.close()
                    for uninstallPack in uninstall:
                        uninstallPackSplit = uninstallPack.split("=")
                        uninstallPack = uninstallPackSplit[1]
                        uninstallRemoveCR = uninstallPack.replace("\r", "")
                        packageToUninstall = uninstallRemoveCR.replace("\n", "")
                        command = "adb.exe -s " + serialNo + " uninstall " + packageToUninstall
                        print command
                        result = os.popen(command).read()
                        print result
                    for installPack in install:
                        installPackSplit = installPack.split("=")
                        installPack = installPackSplit[0]
                        packageToInstall = filePathAPKs + "/" + installPack.replace("package:/data/app/", "")
                        resultat = os.popen("adb.exe -s " + serialNo + ' install "' + packageToInstall + '"').read()
                        print resultat

    def close_windows(self):
        self.destroy()
        self.master.withdraw()


##MAIN MENU
class MainMenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.image = Image.open("img\\android-logo-png.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = Canvas(self, width=580, height=320)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canvas.pack()

        self.texteWifiFirst = Label(self, text="Note: pour la plupart des applications, veuillez ne brancher\n qu'une seule tablette, sauf contre-indication.",
                                    fg="red").pack(pady=5)

        self.frame = Frame(self)

        self.frameBas = Frame(self)

        self.deleteBtn = Button(self.frame, text="Supprimer des applications", width=22, height=3,
                                command=self.openDelete).pack(side=LEFT, padx=5)

        self.addBtn = Button(self.frame, text="Ajouter des applications", width=22, height=3,
                             command=self.openAdd).pack(side=LEFT, padx=5)

        # self.wifiBtn = Button(self.frameBas, text="Connection wifi", width=20, height=3, command=self.openWifi).pack(side=LEFT,padx=5)

        self.cloneBtn = Button(self.frameBas, text="Cloner vos appareils", width=47, height=3,
                               command=self.openClone).pack()

        self.frame.pack()
        self.frameBas.pack(pady=5)

        self.copyright = Label(self, text="© Craig, Landes & Hubert").pack(pady=(5, 10))
        self.pack()

    def openWifi(self):
        global afterPluggedCommand
        afterPluggedCommand = "wifi"
        self.newWindow = Toplevel(self.master)
        self.app = PlugTablet(self.newWindow)

    def openDelete(self):
        global afterPluggedCommand
        afterPluggedCommand = "delete"
        self.newWindow = Toplevel(self.master)
        self.app = PlugTablet(self.newWindow)

    def openClone(self):
        global afterPluggedCommand
        afterPluggedCommand = "clone"
        self.newWindow = Toplevel(self.master)
        self.app = PlugTablet(self.newWindow)

    def openAdd(self):
        global afterPluggedCommand
        afterPluggedCommand = "add"
        self.newWindow = Toplevel(self.master)
        self.app = PlugTablet(self.newWindow)


def main():
    root = Tk()
    app = MainMenu(root)
    root.title(u"Déploiement Android")
    root.iconbitmap("img\\icone.ico")
    root.resizable(height=FALSE, width=FALSE)
    root.mainloop()
    root.destroy()


if __name__ == '__main__':
    main()
