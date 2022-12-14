'''
Title
Description
	This file contains: Joint renamer for auto rig prep
	
How to run:
	import BR_Interface_Toolset.BR_name_tool as BR_name
	reload (BR_name)
	BR_name.gui()
'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel


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
	if pm.window('BR_name_tool', q=1, exists=1):
		pm.deleteUI('BR_name_tool')
		#BR_name_tool

	global auto_jointSystemName, auto_oriName, jointSystemName, oriName
	global mainSystemName, mainSystem_op, ori_op, finger_op, finger_text
	global oriShape_op, shapeSystemName
	global oriIcon_op, mainIconSystem_op, fingerIcon_text, fingerIcon_op, mainIconSystemName
	global oriIconMult_op, mainIconMultSystem_op, fingerIconMult_text, fingerIconMult_op, mainIconMultSystemName
	win_width = 280
	window_object = pm.window('BR_name_tool', title="BR_name_tool", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()
	frame_01 = pm.frameLayout(w=win_width, l='Prep', bgc=color_1, cl=1, cll=1, ann='Prep', cc=windowResize)
	pm.text( l='Prep Renamer', w=win_width )
	pm.rowColumnLayout( nc=2, cw=((1,140), (2, 140), (3, 40), (4, 95)), w=win_width )
	pm.text( l='Ori' )
	ori_op = pm.optionMenu()
	pm.menuItem( l='ct' )
	pm.menuItem( l='lt' )
	pm.menuItem( l='rt' )
	pm.text( l='System' )
	mainSystem_op = pm.optionMenu(cc=printNewMenuItem)
	pm.menuItem( l='Head')
	pm.menuItem( l='Back' )
	pm.menuItem( l='Legs' )
	pm.menuItem( l='Clavicles')
	pm.menuItem( l='Arms' )
	pm.menuItem( l='Hand')
	pm.menuItem( l='Fingers' )
	pm.menuItem( l='Thumbs' )
	pm.menuItem( l='Hip')
	pm.menuItem( l='Butt')
	pm.menuItem( l='Neck')
	pm.setParent( frame_01 )
	pm.rowColumnLayout( nc=2, cw=((1,150), (2, 150)), w=win_width )
	finger_text = pm.text( l='Finger Selection', vis=0 )
	finger_op = pm.optionMenu( vis=0, cc=fingerPrint )
	pm.menuItem( l='Index' )
	pm.menuItem( l='Middle' )
	pm.menuItem( l='Ring' )
	pm.menuItem( l='Pinky' )
	pm.setParent( frame_01 )
	mainSystemName = pm.textFieldGrp( l='System Name', text='head', w=win_width )

	pm.button( l='Rename', w=win_width, c=autoPrep_jointNamer )

	pm.setParent( main_layout )
	frame_02 = pm.frameLayout(w=win_width, l='Shapes', bgc=color_2, cl=1, cll=1, ann='Shapes', cc=windowResize)
	pm.text( l='Shape Renamer', w=win_width )
	pm.rowColumnLayout( nc=2, cw=((1,140), (2, 140), (3, 40), (4, 95)), w=win_width )
	pm.text( l='Ori' )
	oriShape_op = pm.optionMenu()
	pm.menuItem( l='ct' )
	pm.menuItem( l='lt' )
	pm.menuItem( l='rt' )
	shapeSystemName = pm.textFieldGrp( l='System', w=win_width )
	
	pm.setParent( frame_02 )

	pm.button( l='Rename', w=win_width, c=shapeNamer )

	pm.setParent(main_layout)
	frame_03 = pm.frameLayout(w=win_width, l='Single Icons', bgc=color_3, cl=1, cll=1, ann='Single Icons', cc=windowResize)
	pm.text( l='Single Icon Renamer', w=win_width )
	pm.rowColumnLayout( nc=2, cw=((1,140), (2, 140), (3, 40), (4, 95)), w=win_width )
	pm.text( l='Ori' )
	oriIcon_op = pm.optionMenu()
	pm.menuItem( l='ct' )
	pm.menuItem( l='lt' )
	pm.menuItem( l='rt' )
	pm.text( l='System' )
	mainIconSystem_op = pm.optionMenu(cc=printNewMenuIconItem)
	pm.menuItem( l='Head')
	pm.menuItem( l='Back' )
	pm.menuItem( l='Legs' )
	pm.menuItem( l='Clavicles')
	pm.menuItem( l='Arms' )
	pm.menuItem( l='Hand')
	pm.menuItem( l='Fingers' )
	pm.menuItem( l='Thumbs' )
	pm.menuItem( l='Hip')
	pm.menuItem( l='Butt')
	pm.menuItem( l='Neck')
	pm.menuItem( l='Foot' )
	pm.menuItem( l='Knee' )
	pm.menuItem( l='Elbow' )
	pm.menuItem( l='IkFk Switch' )
	pm.menuItem( l='COG' )
	pm.menuItem( l='chest' )
	pm.setParent( frame_03 )
	pm.rowColumnLayout( nc=2, cw=((1,150), (2, 150)), w=win_width )
	fingerIcon_text = pm.text( l='Finger Selection', vis=0 )
	fingerIcon_op = pm.optionMenu( vis=0, cc=fingerPrint )
	pm.menuItem( l='Index' )
	pm.menuItem( l='Middle' )
	pm.menuItem( l='Ring' )
	pm.menuItem( l='Pinky' )
	pm.setParent( frame_03 )
	mainIconSystemName = pm.textFieldGrp( l='System Name', text='head', w=win_width )
	pm.button( l='Icon Rename', w=win_width, c=iconRenamer )
	pm.setParent(main_layout)
	frame_04 = pm.frameLayout(w=win_width, l='Multiple Icons', bgc=color_4, cl=1, cll=1, ann='Multiple Icons', cc=windowResize)
	pm.text( l='Multiple Icon Renamer', w=win_width )
	pm.rowColumnLayout( nc=2, cw=((1,140), (2, 140), (3, 40), (4, 95)), w=win_width )
	pm.text( l='Ori' )
	oriIconMult_op = pm.optionMenu()
	pm.menuItem( l='ct' )
	pm.menuItem( l='lt' )
	pm.menuItem( l='rt' )
	pm.text( l='System' )
	mainIconMultSystem_op = pm.optionMenu(cc=printNewMenuIconMultItem)
	pm.menuItem( l='Head')
	pm.menuItem( l='Back' )
	pm.menuItem( l='Legs' )
	pm.menuItem( l='Clavicles')
	pm.menuItem( l='Arms' )
	pm.menuItem( l='Hand')
	pm.menuItem( l='Fingers' )
	pm.menuItem( l='Thumbs' )
	pm.menuItem( l='Hip')
	pm.menuItem( l='Butt')
	pm.menuItem( l='Neck')
	pm.menuItem( l='Foot' )
	pm.menuItem( l='Knee' )
	pm.menuItem( l='Elbow' )
	pm.menuItem( l='IkFk Switch' )
	pm.setParent( frame_04 )
	pm.rowColumnLayout( nc=2, cw=((1,150), (2, 150)), w=win_width )
	fingerIconMult_text = pm.text( l='Finger Selection', vis=0 )
	fingerIconMult_op = pm.optionMenu( vis=0, cc=fingerPrint )
	pm.menuItem( l='Index' )
	pm.menuItem( l='Middle' )
	pm.menuItem( l='Ring' )
	pm.menuItem( l='Pinky' )
	pm.setParent( frame_04 )
	mainIconMultSystemName = pm.textFieldGrp( l='System Name', text='head', w=win_width )
	pm.button( l='Icon Rename', w=win_width, c=iconMultRenamer )



	pm.window('BR_name_tool', e=1, wh=(280, 65), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)


def printNewMenuItem(*args):

	global mainSystem
	mainSystem = pm.optionMenu( mainSystem_op, q=1, sl=1 )

	if mainSystem == 1:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='head' )

	if mainSystem == 2:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='back' )

	if mainSystem == 3:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='leg' )

	if mainSystem == 4:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='clav' )

	if mainSystem == 5:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='arm' )

	if mainSystem == 6:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='hand' )

	if mainSystem == 7:
		pm.optionMenu( finger_op, e=1, vis=1 )
		pm.text( finger_text, e=1, vis=1 )
		finger_selection = pm.optionMenu( finger_op, q=1, sl=1 )
		if finger_selection == 1:
			pm.textFieldGrp( mainSystemName, e=1, text='index' )

	if mainSystem == 8:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='thumb' )

	if mainSystem == 9:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='hip' )

	if mainSystem == 10:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='butt' )

	if mainSystem == 11:
		pm.optionMenu( finger_op, e=1, vis=0 )
		pm.text( finger_text, e=1, vis=0 )
		pm.textFieldGrp( mainSystemName, e=1, text='neck' )


def printNewMenuIconItem(*args):

	global mainIconSystem
	mainIconSystem = pm.optionMenu( mainIconSystem_op, q=1, sl=1 )

	if mainIconSystem == 1:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='head' )

	if mainIconSystem == 2:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='back' )

	if mainIconSystem == 3:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='leg' )

	if mainIconSystem == 4:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='shoulder' )

	if mainIconSystem == 5:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='arm' )

	if mainIconSystem == 6:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='hand' )

	if mainIconSystem == 7:
		pm.optionMenu( fingerIcon_op, e=1, vis=1 )
		pm.text( fingerIcon_text, e=1, vis=1 )
		finger_selection = pm.optionMenu( fingerIcon_op, q=1, sl=1 )
		if finger_selection == 1:
			pm.textFieldGrp( mainIconSystemName, e=1, text='index' )

	if mainIconSystem == 8:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='thumb' )

	if mainIconSystem == 9:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='hip' )

	if mainIconSystem == 10:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='butt' )

	if mainIconSystem == 11:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='neck' )

	if mainIconSystem == 12:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='foot' )

	if mainIconSystem == 13:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='knee' )

	if mainIconSystem == 14:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='elbow' )

	if mainIconSystem == 15:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='IkFk' )

	if mainIconSystem == 16:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='COG' )

	if mainIconSystem == 17:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='chest' )


def printNewMenuIconMultItem(*args):

	global mainIconMultSystem
	mainIconMultSystem = pm.optionMenu( mainIconMultSystem_op, q=1, sl=1 )

	if mainIconMultSystem == 1:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='head' )

	if mainIconMultSystem == 2:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='back' )

	if mainIconMultSystem == 3:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='leg' )

	if mainIconMultSystem == 4:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='shoulder' )

	if mainIconMultSystem == 5:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='arm' )

	if mainIconMultSystem == 6:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='hand' )

	if mainIconMultSystem == 7:
		pm.optionMenu( fingerIconMult_op, e=1, vis=1 )
		pm.text( fingerIconMult_text, e=1, vis=1 )
		finger_selection = pm.optionMenu( fingerIconMult_op, q=1, sl=1 )
		if finger_selection == 1:
			pm.textFieldGrp( mainIconMultSystemName, e=1, text='index' )

	if mainIconMultSystem == 8:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='thumb' )

	if mainIconMultSystem == 9:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='hip' )

	if mainIconMultSystem == 10:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='butt' )

	if mainIconMultSystem == 11:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='neck' )

	if mainIconMultSystem == 12:
		pm.optionMenu( fingerIconMult_op, e=1, vis=0 )
		pm.text( fingerIconMult_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='foot' )
	if mainIconSystem == 13:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='knee' )

	if mainIconSystem == 14:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='elbow' )

	if mainIconSystem == 15:
		pm.optionMenu( fingerIcon_op, e=1, vis=0 )
		pm.text( fingerIcon_text, e=1, vis=0 )
		pm.textFieldGrp( mainIconSystemName, e=1, text='IkFk' )


def fingerPrint(*args):
	finger_selection = pm.optionMenu( finger_op, q=1, sl=1 )
	fingerIcon_selection = pm.optionMenu( fingerIcon_op, q=1, sl=1 )
	fingerIconMult_selection = pm.optionMenu( fingerIconMult_op, q=1, sl=1 )
	if finger_selection == 1:
		pm.textFieldGrp( mainSystemName, e=1, text='index' )
	if finger_selection == 2:
		pm.textFieldGrp( mainSystemName, e=1, text='middle' )
	if finger_selection == 3:
		pm.textFieldGrp( mainSystemName, e=1, text='ring' )
	if finger_selection == 4:
		pm.textFieldGrp( mainSystemName, e=1, text='pinky' )
	if fingerIcon_selection == 1:
		pm.textFieldGrp( mainIconSystemName, e=1, text='index' )
	if fingerIcon_selection == 2:
		pm.textFieldGrp( mainIconSystemName, e=1, text='middle' )
	if fingerIcon_selection == 3:
		pm.textFieldGrp( mainIconSystemName, e=1, text='ring' )
	if fingerIcon_selection == 4:
		pm.textFieldGrp( mainIconSystemName, e=1, text='pinky' )
	if fingerIconMult_selection == 1:
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='index' )
	if fingerIconMult_selection == 2:
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='middle' )
	if fingerIconMult_selection == 3:
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='ring' )
	if fingerIconMult_selection == 4:
		pm.textFieldGrp( mainIconMultSystemName, e=1, text='pinky' )


def autoPrep_jointNamer(*args):
	# Setup the variables which could come from the UI 

	# Input from UI
	idName = pm.textFieldGrp( mainSystemName, q=1, text=1 )
	# print(idName)

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1 )

	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joint' )
	else:
		jointRoot = pm.ls( sl=1 )[0]


	system_selection = pm.optionMenu( ori_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'ct'

	if system_selection == 2:
		system = 'lt'

	if system_selection == 3:
		system = 'rt'

	#---------------------------------------------------------------------------------------
	# Build the list of joints we are working with, using the root joint as a starting point
	#---------------------------------------------------------------------------------------

	# Find it's children
	jointHierarchy = pm.listRelatives( jointRoot, ad=1, type='joint' )

	# Add selected joint to the list 
	jointHierarchy.append( jointRoot )

	# Reverse the list  
	jointHierarchy.reverse(  )

	# Clear the selection
	pm.select( cl=1 )

	# How many joints are we working on? This will come from UI.
	limbJoints = len(jointHierarchy)
	# print(limbJoints)

	count = 1

	# Rename the bind joints

	if mainSystem == 9:
		for i in range(limbJoints):
			new_name = '{0}_{1}_0{2}_bind'.format( system, idName, count )
			# print( new_name )
			jointHierarchy[i].rename( new_name )
			count = count + 1

	count = 1

	for i in range(limbJoints):
		new_name = '{0}_{1}_0{2}'.format( system, idName, count )
		# print( new_name )
		jointHierarchy[i].rename( new_name )
		count = count + 1

	count = 1
	if mainSystem == 9:
		for i in range(limbJoints):
			new_name = '{0}_{1}_0{2}_bind'.format( system, idName, count )
			# print( new_name )
			jointHierarchy[i].rename( new_name )
			count = count + 1


def jointNamer(*args):
	# Setup the variables which could come from the UI 

	# Input from UI
	idName = pm.textFieldGrp( jointSystemName, q=1, text=1 )
	# print(idName)

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1 )

	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joint' )
	else:
		jointRoot = pm.ls( sl=1, type='joint' )[0]

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = pm.textFieldGrp( oriName, q=1, text=1 )


	#---------------------------------------------------------------------------------------
	# Build the list of joints we are working with, using the root joint as a starting point
	#---------------------------------------------------------------------------------------

	# Find it's children
	jointHierarchy = pm.listRelatives( jointRoot, ad=1)

	# Add selected joint to the list 
	jointHierarchy.append( jointRoot )

	# Reverse the list  
	jointHierarchy.reverse(  )

	# Clear the selection
	pm.select( cl=1 )

	# How many joints are we working on? This will come from UI.
	limbJoints = len(jointHierarchy)
	# print(limbJoints)

	count = 1

	# Rename the bind joints
	for i in range(limbJoints):
		new_name = '{0}_{1}_0{2}_{3}'.format( whichSide, idName, count, + 'bind' )
		print( new_name )
		jointHierarchy[i].rename( new_name )
		count = count + 1


	# suffix = 'waste'

	# new_name = jointHierarchy[-1].replace( 'bind', suffix)
	# jointHierarchy[-1].rename( new_name )


def shapeNamer(*args):

	# Setup the variables which could come from the UI 

	# Input from UI
	idName = pm.textFieldGrp( shapeSystemName, q=1, text=1 )
	# print(idName)

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1 )

	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joint' )
	else:
		jointRoot = pm.ls( sl=1 )[0]


	system_selection = pm.optionMenu( oriShape_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'ct'

	if system_selection == 2:
		system = 'lt'

	if system_selection == 3:
		system = 'rt'


	curveSelection = pm.ls( sl=1 )
	print( curveSelection )

	shapes = pm.ls ( curveSelection, dag=1, type='shape' )
	print( shapes )


	# How many joints are we working on? This will come from UI.
	shapeLen = len(shapes)
	print(shapeLen)


	for i in range(shapeLen):
		new_name = '{0}_{1}Shape'.format( system, idName)
		# print( new_name )
		shapes[i].rename( new_name )
		


	# shapeName = 'Shape'


def iconRenamer(*args):
	# Setup the variables which could come from the UI 

	# Input from UI
	idName = pm.textFieldGrp( mainIconSystemName, q=1, text=1 )
	# print(idName)

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1 )[0]
	# print(selectionCheck)

	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joint' )
	else:
		jointRoot = pm.ls( sl=1 )[0]

	system_selection = pm.optionMenu( oriIcon_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'ct'

	if system_selection == 2:
		system = 'lt'

	if system_selection == 3:
		system = 'rt'
	#---------------------------------------------------------------------------------------
	# Build the list of joints we are working with, using the root joint as a starting point
	#---------------------------------------------------------------------------------------

	# Find it's children
	jointHierarchy = pm.listRelatives( jointRoot, ad=1)

	# Add selected joint to the list 
	jointHierarchy.append( jointRoot )

	# Reverse the list  
	jointHierarchy.reverse(  )

	# Clear the selection
	pm.select( cl=1 )

	# How many joints are we working on? This will come from UI.
	limbJoints = len(jointHierarchy)
	# print(limbJoints)

	# Rename the bind joints
	for i in range(limbJoints):
		new_name = '{0}_{1}_icon'.format( system, idName)
		# print( new_name )
		jointHierarchy[i].rename( new_name )

	count = 1
	if mainIconSystem == 15:
		for i in range(limbJoints):
			new_name = '{0}_{1}_switch'.format( system, idName)
			# print( new_name )
			jointHierarchy[i].rename( new_name )
			count = count + 1


def iconMultRenamer(*args):
	# Setup the variables which could come from the UI 

	# Input from UI
	idName = pm.textFieldGrp( mainIconMultSystemName, q=1, text=1 )
	# print(idName)

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1 )[0]
	# print(selectionCheck)

	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joint' )
	else:
		jointRoot = pm.ls( sl=1 )[0]

	system_selection = pm.optionMenu( oriIconMult_op, q=1, sl=1 )

	if system_selection == 1:
		system = 'ct'

	if system_selection == 2:
		system = 'lt'

	if system_selection == 3:
		system = 'rt'
	#---------------------------------------------------------------------------------------
	# Build the list of joints we are working with, using the root joint as a starting point
	#---------------------------------------------------------------------------------------

	# Find it's children
	jointHierarchy = pm.listRelatives( jointRoot, ad=1)

	# Add selected joint to the list 
	jointHierarchy.append( jointRoot )

	# Reverse the list  
	jointHierarchy.reverse(  )

	# Clear the selection
	pm.select( cl=1 )

	# How many joints are we working on? This will come from UI.
	limbJoints = len(jointHierarchy)
	# print(limbJoints)

	count = 1

	for i in range(limbJoints):
		new_name = '{0}_{1}_0{2}_icon'.format( system, idName, count )
		# print( new_name )
		jointHierarchy[i].rename( new_name )
		count = count + 1

	count = 1
	if mainIconMultSystem == 15:
		for i in range(limbJoints):
			new_name = '{0}_{1}_switch'.format( system, idName)
			# print( new_name )
			jointHierarchy[i].rename( new_name )
			count = count + 1


def windowResize(*args):
	if pm.window('BR_name_tool', q=1, exists=1):
		pm.window('BR_name_tool', e=1, wh=(280, 65), rtf=1)
	else:
		pm.warning('BR_name_tool does not exist')

def deleteUI(*args):
	# print('Closing UI')
	pm.deleteUI('BR_name_tool')

