# ########################################################################################################################
# Date : 15th July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################

"""
   		What the next few lines do : This code here is intended to use dogtail to open synaptic package manager and type vim.
   		Small explanation for the code : openWindow function opens the window and then types the name of program to be installed
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

def mainProgram():
	""" In this function things are hardcoded a bit.Also dogtail modules are imported inside.
	"""
	
	from observer import *                             #if i am using * then i should mention what all come under * later
	import dogtail.rawinput
	
	observer = Observer()                              
	
	
	observer.openWindow('System', 'Administration', 'Synaptic Package Manager')
	#frameName = 'Synaptic Package Manager'
	#if(not observer.frameFocussed(frameName,1)): 
	#	raise NameError("Could not focus frame " + frameName)
	"""I am debating which to include.The above three lines or the next few lines.
	The above two lines will definitely raise an error and end while with the below few lines
	a little i can even type some name in many cases"""
	time.sleep(3)
	dogtail.rawinput.typeText('vim')
	
def main():
	import subprocess
	mainProgram()
	
if __name__=='__main__' :
    main()
