'''
ByrdRigs Renamer Window
'''

'''
How to run:
	import BR_Interface_Toolset.BR_renamerTool as renamer
	reload (renamer)
	renamer.gui()
'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os.path


tab_bgc=(0.4718592, 0.13568, 239)
subTab_bgc = (0.4915200, 0.32256, 241)
window_bgc = (.2,.2,.2)

class colors:
	red = 13
	blue = 6
	yellow = 17
	cyan = 18
	color_1 = (.141,.725,.627)
	color_2 = (.078, .678, .557)
	color_3 = (.059, .612, .749)
	color_4 = (.059, .475, .616)
	color_5 = (.059, .392, .663)
	color_6 = (.224, .259, .894)
	color_7 = (.475, .278, .925)
	color_8 = (.447, .145, .965)
	color_9 = (.475, .078, .678)
	color_10 = (.576, .039, .839)

def gui():
	if pm.window('ByrdRigs_Renamer', q=1, exists=1):
		pm.deleteUI('ByrdRigs_Renamer')
		#ByrdRigs_Biped_Body_Auto_Rigger

	win_width = 313
	window_object = pm.window('ByrdRigs_Renamer', title="ByrdRigs' Renamer", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()

	#======================================================================
	# Rename Tools
	pm.rowColumnLayout(w=win_width)
	BR_RenameTFG = pm.textFieldGrp(l='Rename', text='', cw=[(1, 70), (2, 235)])
	pm.rowColumnLayout(cw=[(1, 130), (2, 170)], nc=2)
	BR_StartIFG = pm.intFieldGrp(l='Start #:', v1=1, cw=[(1, 68), (2, 60)])
	BR_PaddingIFG = pm.intFieldGrp(l='Padding:', v1=2, cw=[(1, 64), (2, 60)])
	pm.setParent(main_layout)
	pm.button(l='Rename and Number', w=win_width, bgc=tab_bgc)
	pm.separator(st="in", w=win_width)

	#======================================================================
	# Remove
	pm.rowColumnLayout(cw=[(1, 84), (2, 104), (3, 104)], nc=3, cs=[(1, 10), (3, 4)])
	pm.text(l='Remove...', al='left')
	pm.button(l='First Character--->', w=60, bgc=tab_bgc)
	pm.button(l='<---Last Character', w=60, bgc=tab_bgc, c=remove_lastChr)
	pm.setParent(main_layout)
	pm.separator(st="in", w=win_width)

	#======================================================================
	# Hash Rename
	pm.rowColumnLayout(cw=[(1, 70), (2, 170), (3, 56)], nc=3, cs=(1, 10))
	pm.text(l='Hash Rename')
	BR_hashRenmaeTFG = pm.textFieldGrp(l='', text='name_####_suffix', cw=[(1, 10), (2, 153)])
	pm.button(l='Rename', w=48, bgc=tab_bgc)
	pm.setParent(main_layout)
	pm.separator(st='in', w=win_width)

	#======================================================================
	# Prefix - Suffix
	pm.rowColumnLayout(cw=[(1, 55), (2, 185), (3, 56)], nc=3, cs=(1, 10))
	pm.text(l='(Before)')
	BR_prefixTFG = pm.textFieldGrp(l='', text='prefix_', cw=[(1, 10), (2, 168)])
	pm.button(l='Add', bgc=tab_bgc)
	pm.setParent(main_layout)
	pm.rowColumnLayout(cw=[(1, 55), (2, 185), (3, 56)], nc=3, cs=(1, 10))
	pm.text(l='(After)')
	BR_suffixTFG = pm.textFieldGrp(l='', text='suffix_', cw=[(1, 10), (2, 168)])
	pm.button(l='Add', bgc=tab_bgc)
	pm.setParent(main_layout)
	pm.separator(st='in', w=win_width)

	#======================================================================
	# Quick suffix
	pm.rowColumnLayout(nc=5, cw=[(1, 61), (2, 61), (3, 61), (4, 61), (5, 62)])
	pm.button(l='grp', bgc=tab_bgc)
	pm.button(l='geo', bgc=tab_bgc)
	pm.button(l='icon', bgc=tab_bgc)
	pm.button(l='bind', bgc=tab_bgc)
	pm.button(l='waste', bgc=tab_bgc)
	pm.setParent(main_layout)
	pm.separator(st='in', w=win_width)

	#======================================================================
	# Search and Replace 
	pm.columnLayout(w=win_width)
	BR_searchTFG = pm.textFieldGrp(l='Search:', cw=[(1, 70), (2, 233)])
	BR_replaceTFG = pm.textFieldGrp(l='Replace:', cw=[(1, 70), (2, 233)])
	BR_optionRBG = pm.radioButtonGrp(l='', nrb=3, la3=('Hierarchy', 'Selected', 'All'), sl=1, cw=[(1, 78), (2, 78), (3, 78)])
	pm.setParent(main_layout)
	pm.button(l='Apply', bgc=tab_bgc, w=win_width)


	pm.window('ByrdRigs_Renamer', e=1, wh=(313, 302), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)
	

def remove_lastChr(*args):
	selection = pm.ls(sl=1, long=1)
	print('Selection:', selection)
	selectionSize = len(selection)
	print('Selection Size:', selectionSize)
	for i in range(selectionSize - 1, 0-1, -1):
		obj = selection[i]
		print(obj)
		pathNodes = []
		print(pathNodes)
		# numToken = int(pathNodes = obj.split("|"))	
		# myObj = pathNodes[numToken - 1]
		# stringSize = len(myObj)
		# if stringSize>1:
		# 	new_name = myObj[0:stringSize - 1]
		# 	pm.rename(obj, new_name)