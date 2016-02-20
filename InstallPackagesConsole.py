#!/usr/bin/env python
# -*- coding: UTF -8 -*-
import os
print "Branchez l'appareil SVP."
branche = raw_input(u"Appareil bien branché? o/n ")
if branche=='o':
	filePath = raw_input(u"Veuillez entrer le chemin du .apk situé sur votre ordinateur : ")
	os.system("adb install " + filePath)
