'''
Title
Description
	This file contains:
	
How to run:
	import BR_Interface_Toolset.BR_iconMirror as iconMirror
	reload (iconMirror)
	iconMirror.gui()
'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os.path


tab_bgc=(0.4718592, 0.13568, 239)
subTab_bgc = (0.4915200, 0.32256, 241)
window_bgc = (.2,.2,.2)
fileName = __file__ 
red = 13
blue = 6
yellow = 17
cyan = 18
color_1	= (0, .51, .612)
color_2	= (.008, .6, .706)
color_3	= (0, .678, .784)
color_4	= (.157, .773, .847)
color_5	= (.451, .82, .867)	
color_6	= (.557, .906, .949)
color_7	= (0, .522, .557)
color_8	= (.012, .596, .675)
color_9	= (0, .718, .773)
color_10 = (.176, .776, .839)
color_11 = (.498, .843, .859)
color_12 = (.604, .902, .914)
color_13 = (0, .529, .541)
color_14 = (.02, .612, .639)
color_15 = (.302, .812, .82)
color_16 = (.576, .867, .863)
color_17 = (.788, .914, .871)
color_18 = (.855, .945, .914)
color_19 = (.047, .098, .459)
color_20 = (.18, .2, .561)
color_21 = (.349, .373, .659)
color_22 = (.498, .549, .753)
color_23 = (.651, .686, .839)
color_24 = (.757, .776, .863)
color_25 = (.059, .169, .357)
color_26 = (.204, .337, .525)
color_27 = (.427, .529, .659)
color_28 = (.608, .667, .749)
color_29 = (.757, .773, .82)
color_30 = (.843, .847, .859)

def gui():
	if pm.window('BR_iconMirror', q=1, exists=1):
		pm.deleteUI('BR_iconMirror')
		#BR_iconMirror

	win_width = 260
	window_object = pm.window('BR_iconMirror', title="ByrdRig's Icon Mirror Toolset", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()
	pm.button( l='Go', w=win_width, c=mirror )


	pm.window('BR_iconMirror', e=1, wh=(260, 80), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)

def mirror(*args):
	# Get all the icons
	pm.select( '*_icon', '*_switch' )

	lt_icons = pm.ls( sl=1 )
	# print(lt_icons)

	tempGrp = pm.group( em=1, n='temp_grp' )

	pm.parent( lt_icons, tempGrp )

	mirrorGrp = pm.duplicate( tempGrp, n='mirror_grp' )[0]

	mirrorGrp.sx.set( -1 )

	pm.select(mirrorGrp)
	freezeTransform()

	pm.parent( lt_icons, w=1 )
	pm.delete(tempGrp)

	rt_icons = pm.ls( mirrorGrp, dag=1 )
	print(rt_icons)

	pm.select( lt_icons[0] )
	icon = pm.ls( sl=1 )[0]



def freezeTransform(*agrs):
	pm.makeIdentity(apply=1, t=1, r=1, s=1, n=0, pn=1)
	# print 'Transform Frozen'

def windowResize(*args):
	if pm.window('BR_iconMirror', q=1, exists=1):
		pm.window('BR_iconMirror', e=1, wh=(260, 80), rtf=1)
	else:
		pm.warning('BR_iconMirror does not exist')

def deleteUI(*args):
	# print('Closing UI')
	pm.deleteUI('BR_iconMirror')















