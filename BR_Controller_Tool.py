'''
Title
Description
	This file contains: Controller Creation
	
How to run:
	import BR_Interface_Toolset.BR_Controller_Tool as ctrlTool
	reload (ctrlTool)
	ctrlTool.gui()
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


def gui():
	if pm.window('BR_Controller_Tool', q=1, exists=1):
		pm.deleteUI('BR_Controller_Tool')
		#BR_Controller_Tool

	global mainSystemName, mainSystem_op, system_op, finger_op, finger_text

	win_width = 300
	window_object = pm.window('BR_Controller_Tool', title="ByrdRigs' Controller Toolset", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()
	pm.rowColumnLayout( nc=4, cw=((1,80), (2, 70), (3, 40), (4, 95)), w=win_width )
	pm.text( l='Main System' )
	mainSystem_op = pm.optionMenu(cc=printNewMenuItem)
	pm.menuItem( l='Back' )
	pm.menuItem( l='Legs' )
	pm.menuItem( l='Arms' )
	pm.menuItem( l='Fingers' )
	pm.menuItem( l='Thumbs' )
	pm.menuItem( l='Tenacles')
	pm.text( l='System' )
	system_op = pm.optionMenu()
	pm.menuItem( l='Dynamic' )
	pm.menuItem( l='Fk' )
	pm.menuItem( l='Spline Ik/Rib' )
	pm.setParent( main_layout )
	pm.rowColumnLayout( nc=2, cw=((1,150), (2, 150)), w=win_width )
	finger_text = pm.text( l='Finger Selection', vis=0 )
	finger_op = pm.optionMenu( vis=0, cc=fingerPrint )
	pm.menuItem( l='Index' )
	pm.menuItem( l='Middle' )
	pm.menuItem( l='Ring' )
	pm.menuItem( l='Pinky' )
	pm.setParent( main_layout )
	mainSystemName = pm.textFieldGrp( l='System Name', text='back', w=win_width )
	pm.button( l='Create', w=win_width, c=Tags )


	pm.window('BR_Controller_Tool', e=1, wh=(300, 80), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)


def printNewMenuItem(*args):

	global mainSystem
	mainSystem = pm.optionMenu( mainSystem_op, q=1, sl=1 )

	if mainSystem == 1:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='back' )

	if mainSystem == 2:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='leg' )

	if mainSystem == 3:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='arm' )

	if mainSystem == 4:
		pm.optionMenu( finger_op, e=1, vis=1 )
		pm.text( finger_text, e=1, vis=1 )
		finger_selection = pm.optionMenu( finger_op, q=1, sl=1 )
		if finger_selection == 1:
			pm.textFieldGrp( mainSystemName, e=1, text='index' )

	if mainSystem == 5:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='thumb' )

	if mainSystem == 6:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='tentacle' )

def fingerPrint(*args):
	finger_selection = pm.optionMenu( finger_op, q=1, sl=1 )
	if finger_selection == 1:
		pm.textFieldGrp( mainSystemName, e=1, text='index' )
	if finger_selection == 2:
		pm.textFieldGrp( mainSystemName, e=1, text='middle' )
	if finger_selection == 3:
		pm.textFieldGrp( mainSystemName, e=1, text='ring' )
	if finger_selection == 4:
		pm.textFieldGrp( mainSystemName, e=1, text='pinky' )

def Tags(*args):

	mainSystem = pm.optionMenu( mainSystem_op, q=1, sl=1 )

	if mainSystem == 1:
		backTags()
		pm.textFieldGrp( e=1, text='back' )

	if mainSystem == 2:
		legTags()
		pm.textFieldGrp( e=1, text='leg' )

	if mainSystem == 3:
		armTags()
		pm.textFieldGrp( e=1, text='arm' )

	if mainSystem == 4:
		fingerTags()
		if finger_op == 1:
				pm.textFieldGrp( e=1, text='index' )

	if mainSystem == 5:
		thumbTags()

	if mainSystem == 6:
		tentacleTags()

def backTags(*args):

	limbID = pm.textFieldGrp( mainSystemName, q=1, text=1  )
	# print( limbID )

	system_selection = pm.optionMenu( system_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'dyn'

	if system_selection == 2:
		system = 'fk'

	if system_selection == 3:
		system = 'ik'

	selection = pm.ls( sl=1 )
	# print( selection )

	icon_1 = pm.ls( selection )[0]

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = icon_1[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			if not 'ct_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_, rt_, ct_' )


	limbName = whichSide + limbID

	count = 1

	

	iconHierarchy = len( selection )
	# print( iconHierarchy )

	tags = []
	for each in selection:
		tag = pm.createNode( 'controller' )
		tag_name = '{0}_0{1}_{2}_tag'.format( limbName, count, system )
		tag.rename( tag_name )
		count = count + 1

		pm.connectAttr( each + '.message', tag + '.controllerObject', f=1 )
		tags.append( tag )

	# print( tags )

	'''
	Set 1
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[5] + '.parent', tags[4] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[5] + '.prepopulate', tags[4] + '.prepopulate', f=1 )


	'''
	Set 2
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-2] + '.parent', tags[-3] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-2] + '.prepopulate', tags[-3] + '.prepopulate', f=1 )


	'''
	Set 3
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-3] + '.parent', tags[-4] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-3] + '.prepopulate', tags[-4] + '.prepopulate', f=1 )


	'''
	Set 4
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-4] + '.parent', tags[-5] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-4] + '.prepopulate', tags[-5] + '.prepopulate', f=1 )


	'''
	Set 5
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-5] + '.parent', tags[-6] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-5] + '.prepopulate', tags[-6] + '.prepopulate', f=1 )

	pm.select( cl=1 )

	if system_selection == 1:
		print( 'Dynamic Back Controls Created' )

	if system_selection == 2:
		print( 'FK Back Controls Created' )

	if system_selection == 3:
		print( 'IK Back Controls Created' )

def legTags(*args):

	limbID = pm.textFieldGrp( mainSystemName, q=1, text=1  )
	# print( limbID )

	system_selection = pm.optionMenu( system_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'dyn'

	if system_selection == 2:
		system = 'fk'

	if system_selection == 3:
		system = 'ik'

	selection = pm.ls( sl=1 )
	# print( selection )

	icon_1 = pm.ls( selection )[0]

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = icon_1[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			if not 'ct_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_, rt_, ct_' )


	limbName = whichSide + limbID

	count = 1

	

	iconHierarchy = len( selection )
	# print( iconHierarchy )

	tags = []
	for each in selection:
		tag = pm.createNode( 'controller' )
		tag_name = '{0}_0{1}_{2}_tag'.format( limbName, count, system )
		tag.rename( tag_name )
		count = count + 1

		pm.connectAttr( each + '.message', tag + '.controllerObject', f=1 )
		tags.append( tag )

	# print( tags )

	'''
	Set 1
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-1] + '.parent', tags[-2] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-1] + '.prepopulate', tags[-2] + '.prepopulate', f=1 )


	'''
	Set 2
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-2] + '.parent', tags[-3] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-2] + '.prepopulate', tags[-3] + '.prepopulate', f=1 )


	'''
	Set 3
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-3] + '.parent', tags[-4] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-3] + '.prepopulate', tags[-4] + '.prepopulate', f=1 )


	# '''
	# Set 4
	# '''
	# # Connect child.parent >> parent.child
	# pm.connectAttr( tags[-4] + '.parent', tags[-5] + '.children[0]', f=1 )

	# # Connect child.prepopulate >> parent.prepopulate
	# pm.connectAttr( tags[-4] + '.prepopulate', tags[-5] + '.prepopulate', f=1 )

	pm.select( cl=1 )

	if system_selection == 1:
		print( 'Dynamic Back Controls Created' )

	if system_selection == 2:
		print( 'FK Back Controls Created' )

	if system_selection == 3:
		print( 'IK Back Controls Created' )

def armTags(*args):
	limbID = pm.textFieldGrp( mainSystemName, q=1, text=1  )
	# print( limbID )

	system_selection = pm.optionMenu( system_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'dyn'

	if system_selection == 2:
		system = 'fk'

	if system_selection == 3:
		system = 'ik'

	selection = pm.ls( sl=1 )
	# print( selection )

	icon_1 = pm.ls( selection )[0]

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = icon_1[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			if not 'ct_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_, rt_, ct_' )


	limbName = whichSide + limbID

	count = 1

	

	iconHierarchy = len( selection )
	# print( iconHierarchy )

	tags = []
	for each in selection:
		tag = pm.createNode( 'controller' )
		tag_name = '{0}_0{1}_{2}_tag'.format( limbName, count, system )
		tag.rename( tag_name )
		count = count + 1

		pm.connectAttr( each + '.message', tag + '.controllerObject', f=1 )
		tags.append( tag )

	# print( tags )

	'''
	Set 1
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-1] + '.parent', tags[-2] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-1] + '.prepopulate', tags[-2] + '.prepopulate', f=1 )


	pm.select( cl=1 )

	if system_selection == 1:
		print( 'Dynamic Back Controls Created' )

	if system_selection == 2:
		print( 'FK Back Controls Created' )

	if system_selection == 3:
		print( 'IK Back Controls Created' )

def fingerTags(*args):
	limbID = pm.textFieldGrp( mainSystemName, q=1, text=1  )
	# print( limbID )

	system_selection = pm.optionMenu( system_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'dyn'

	if system_selection == 2:
		system = 'fk'

	if system_selection == 3:
		system = 'ik'

	selection = pm.ls( sl=1 )
	# print( selection )

	icon_1 = pm.ls( selection )[0]

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = icon_1[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			if not 'ct_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_, rt_, ct_' )


	limbName = whichSide + limbID

	count = 1

	

	iconHierarchy = len( selection )
	# print( iconHierarchy )

	tags = []
	for each in selection:
		tag = pm.createNode( 'controller' )
		tag_name = '{0}_0{1}_{2}_tag'.format( limbName, count, system )
		tag.rename( tag_name )
		count = count + 1

		pm.connectAttr( each + '.message', tag + '.controllerObject', f=1 )
		tags.append( tag )

	# print( tags )

	'''
	Set 1
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-1] + '.parent', tags[-2] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-1] + '.prepopulate', tags[-2] + '.prepopulate', f=1 )


	'''
	Set 2
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-2] + '.parent', tags[-3] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-2] + '.prepopulate', tags[-3] + '.prepopulate', f=1 )

	pm.select( cl=1 )

	if system_selection == 1:
		print( 'Dynamic Back Controls Created' )

	if system_selection == 2:
		print( 'FK Back Controls Created' )

	if system_selection == 3:
		print( 'IK Back Controls Created' )

def thumbTags(*args):
	limbID = pm.textFieldGrp( mainSystemName, q=1, text=1  )
	# print( limbID )

	system_selection = pm.optionMenu( system_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'dyn'

	if system_selection == 2:
		system = 'fk'

	if system_selection == 3:
		system = 'ik'

	selection = pm.ls( sl=1 )
	# print( selection )

	icon_1 = pm.ls( selection )[0]

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = icon_1[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			if not 'ct_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_, rt_, ct_' )


	limbName = whichSide + limbID

	count = 1

	

	iconHierarchy = len( selection )
	# print( iconHierarchy )

	tags = []
	for each in selection:
		tag = pm.createNode( 'controller' )
		tag_name = '{0}_0{1}_{2}_tag'.format( limbName, count, system )
		tag.rename( tag_name )
		count = count + 1

		pm.connectAttr( each + '.message', tag + '.controllerObject', f=1 )
		tags.append( tag )

	# print( tags )

	'''
	Set 1
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-1] + '.parent', tags[-2] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-1] + '.prepopulate', tags[-2] + '.prepopulate', f=1 )


	'''
	Set 2
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-2] + '.parent', tags[-3] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-2] + '.prepopulate', tags[-3] + '.prepopulate', f=1 )


	'''
	Set 3
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-3] + '.parent', tags[-4] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-3] + '.prepopulate', tags[-4] + '.prepopulate', f=1 )


	pm.select( cl=1 )

	if system_selection == 1:
		print( 'Dynamic Back Controls Created' )

	if system_selection == 2:
		print( 'FK Back Controls Created' )

	if system_selection == 3:
		print( 'IK Back Controls Created' )

def tentacleTags(*args):
	limbID = pm.textFieldGrp( mainSystemName, q=1, text=1  )
	# print( limbID )

	system_selection = pm.optionMenu( system_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'dyn'

	if system_selection == 2:
		system = 'fk'

	if system_selection == 3:
		system = 'ik'

	selection = pm.ls( sl=1 )
	# print( selection )

	icon_1 = pm.ls( selection )[0]

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = icon_1[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			if not 'ct_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_, rt_, ct_' )


	limbName = whichSide + limbID

	count = 1

	

	iconHierarchy = len( selection )
	# print( iconHierarchy )

	tags = []
	for each in selection:
		tag = pm.createNode( 'controller' )
		tag_name = '{0}_0{1}_{2}_tag'.format( limbName, count, system )
		tag.rename( tag_name )
		count = count + 1

		pm.connectAttr( each + '.message', tag + '.controllerObject', f=1 )
		tags.append( tag )

	# print( tags )

	'''
	Set 1
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-1] + '.parent', tags[-2] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-1] + '.prepopulate', tags[-2] + '.prepopulate', f=1 )


	'''
	Set 2
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-2] + '.parent', tags[-3] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-2] + '.prepopulate', tags[-3] + '.prepopulate', f=1 )


	'''
	Set 3
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-3] + '.parent', tags[-4] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-3] + '.prepopulate', tags[-4] + '.prepopulate', f=1 )


	'''
	Set 4
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-4] + '.parent', tags[-5] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-4] + '.prepopulate', tags[-5] + '.prepopulate', f=1 )


	'''
	Set 5
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-5] + '.parent', tags[-6] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-5] + '.prepopulate', tags[-6] + '.prepopulate', f=1 )


	'''
	Set 6
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-6] + '.parent', tags[-7] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-6] + '.prepopulate', tags[-7] + '.prepopulate', f=1 )


	'''
	Set 7
	'''

	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-7] + '.parent', tags[-8] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-7] + '.prepopulate', tags[-8] + '.prepopulate', f=1 )


	'''
	Set 8
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-8] + '.parent', tags[-9] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-8] + '.prepopulate', tags[-9] + '.prepopulate', f=1 )


	'''
	Set 9
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-9] + '.parent', tags[-10] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-9] + '.prepopulate', tags[-10] + '.prepopulate', f=1 )


	'''
	Set 10
	'''
	# Connect child.parent >> parent.child
	pm.connectAttr( tags[-10] + '.parent', tags[-11] + '.children[0]', f=1 )

	# Connect child.prepopulate >> parent.prepopulate
	pm.connectAttr( tags[-10] + '.prepopulate', tags[-11] + '.prepopulate', f=1 )

	pm.select( cl=1 )

	if system_selection == 1:
		print( 'Dynamic Back Controls Created' )

	if system_selection == 2:
		print( 'FK Back Controls Created' )

	if system_selection == 3:
		print( 'IK Back Controls Created' )


def windowResize(*args):
	if pm.window('BR_Controller_Tool', q=1, exists=1):
		pm.window('BR_Controller_Tool', e=1, wh=(300, 80), rtf=1)
	else:
		pm.warning("ByrdRigs' Controller Toolset does not exist")

def deleteUI(*args):
	# print('Closing UI')
	pm.deleteUI('BR_Controller_Tool')















