'''
Title
Description
	This file contains: Biped Arm Setup
	
How to run:
	import BR_Interface_Toolset.BR_bipedArm_setup as biArm
	reload (biArm)
	biArm.gui()
'''

'''
The starting joints shouldn't have a suffix at the moment.

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
	global shoulder_system_name, arm_system_name, hand_system_name, index_system_name, middle_system_name, ring_system_name, pinky_system_name, thumb_system_name
	global index_j1, index_j2,index_j3, middle_j1, middle_j2, middle_j3,ring_j1,ring_j2, ring_j3, pinky_j1, pinky_j2, pinky_j3, thumb_j1, thumb_j2, thumb_j3, thumb_j4

	if pm.window('BR_bipedArm_setup', q=1, exists=1):
		pm.deleteUI('BR_bipedArm_setup')
		#BR_bipedArm_setup

	win_width = 280
	window_object = pm.window('BR_bipedArm_setup', title="BR_bipedArm_setup", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()

	pm.button( l='Import Shoulder joints', w=win_width, c=shoulderImport )
	pm.button( l='Finalize Import', w=win_width, c=shoulderCheck)
	shoulder_system_name = pm.textFieldGrp( l='System Name', text='shoulder', w=win_width )
	pm.text( l='Select the clav and arm root joints', w=win_width, ww=1 )
	pm.button( l='Go', w=win_width, c=shoulderSetup )
	pm.text( l='Select the arm root joint', w=win_width, ww=1 )
	arm_system_name = pm.textFieldGrp( l='System Name', text='arm', w=win_width )
	pm.button( l='Go', w=win_width, c=armSetup )
	pm.text( l='Select the hand root joint', w=win_width, ww=1 )
	hand_system_name = pm.textFieldGrp( l='System Name', text='hand', w=win_width )
	pm.button( l='Go', w=win_width, c=handSetup )	
	pm.text( l="Select the index, middle, ring, pinky, and thumb root joints. It's ok if there is a fewer amount of fingers.", w=win_width, ww=1 )
	pm.text( l='There are presets for five fingers, three fingers with a thumb, and two fingers with a thumb', w=win_width, ww=1 )
	index_system_name = pm.textFieldGrp( l='Index System Name', text='index', w=win_width )
	middle_system_name = pm.textFieldGrp( l='Middle System Name', text='middle', w=win_width )
	ring_system_name = pm.textFieldGrp( l='Ring System Name', text='ring', w=win_width )
	pinky_system_name = pm.textFieldGrp( l='Pinky System Name', text='pinky', w=win_width )
	thumb_system_name = pm.textFieldGrp( l='Thumb System Name', text='thumb', w=win_width )
	pm.button( l='Go', w=win_width, c=finger_setup )

	# rotation_frame = pm.frameLayout( l='Rotation Min/Max', cl=0, cll=1, w=win_width, bgc=color_1 )
	# pm.rowColumnLayout(nc=5, cw=[(50, 30), (30, 30), (30, 30), (30, 30), (30,30)])
	# pm.text(l='Index', w=55)
	# index_j1 = pm.textField('index_j1', w=55, ed=0, text='jnt_01')
	# index_j2 = pm.textField('index_j2', w=55, ed=0, text='jnt_02')
	# index_j3 = pm.textField('index_j3', w=55, ed=0, text='jnt_03')
	# pm.button(l='set', w=55, c=indexRotSet)
	# pm.text(l='Middle', w=55)
	# middle_j1 = pm.textField('middle_j1', w=55, ed=0, text='jnt_01')
	# middle_j2 = pm.textField('middle_j2', w=55, ed=0, text='jnt_02')
	# middle_j3 = pm.textField('middle_j3', w=55, ed=0, text='jnt_03')
	# pm.button(l='set', w=55, c=middleRotSet)
	# pm.text(l='Ring', w=55)
	# ring_j1 = pm.textField('ring_j1', w=55, ed=0, text='jnt_01')
	# ring_j2 = pm.textField('ring_j2', w=55, ed=0, text='jnt_02')
	# ring_j3 = pm.textField('ring_j3', w=55, ed=0, text='jnt_03')
	# pm.button(l='set', w=55, c=ringRotSet)
	# pm.text(l='Pinky', w=55)
	# pinky_j1 = pm.textField('pinky_j1', w=55, ed=0, text='jnt_01')
	# pinky_j2 = pm.textField('pinky_j2', w=55, ed=0, text='jnt_02')
	# pinky_j3 = pm.textField('pinky_j3', w=55, ed=0, text='jnt_03')
	# pm.button(l='set', w=55, c=pinkyRotSet)
	# pm.setParent( rotation_frame )
	# pm.rowColumnLayout(nc=6, cw=[(50, 30), (30, 30), (30, 30), (30, 30), (30,30), (30,30)])
	# pm.text(l='Thumb', w=55)
	# thumb_j1 = pm.textField('thumb_j1', w=45, ed=0, text='jnt_01')
	# thumb_j2 = pm.textField('thumb_j2', w=45, ed=0, text='jnt_02')
	# thumb_j3 = pm.textField('thumb_j3', w=45, ed=0, text='jnt_03')
	# thumb_j4 = pm.textField('thumb_j4', w=45, ed=0, text='jnt_04')
	# pm.button(l='set', w=45, c=thumbRotSet)

	pm.window('BR_bipedArm_setup', e=1, wh=(280, 80), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)

def getDir():
	global file_name
	file_name = os.path.dirname(fileName)
	extension = os.path.splitext(file_name)
	# print file_name
	

	listOfFiles = getListOfFiles(file_name)
	# print (listOfFiles)
	# print (listOfFiles[13])
	cmds.file(listOfFiles[13], pr=1, rpr="ByrdRigs", ignoreVersion=1, i=1, type="mayaAscii", importTimeRange="combine", rdn=1, mergeNamespacesOnClash=False, options="v=0;")

def getListOfFiles(file_name):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(file_name)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(file_name, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def lock_and_hide(icon, attrs):
	for current_attr in attrs:
		attr = icon.attr(current_attr)
		attr.set(lock=1, keyable=0)

def lockAttrs(icon, attrs):
	for current_attr in attrs:
		attr = icon.attr(current_attr)
		attr.set(lock=1)

def unlock_and_unhide(icon, attrs):
	for current_attr in attrs:
		attr = icon.attr(current_attr)
		attr.set(lock=0, keyable=1)

def unlockAttrs(icon, attrs):
	for current_attr in attrs:
		attr = icon.attr(current_attr)
		attr.set(lock=0)

def unhideAttrs(icon, attrs):
	for current_attr in attrs:
		attr = icon.attr(current_attr)
		attr.set(keyable=1)

def joint_positions():
	global cv_pos
  	# Get selection
  	selection = pm.ls(sl=1, dag=1)
  	# print( selection )

  	cv_pos = []

  	# Get the position for each joint
  	for each in selection:
  		position = pm.xform( each, q=1, t=1, ws=1 )
  		# print( position )

  		cv_pos.append( position )
  	# print( cv_pos 

def deleteHistory(*args):
	pm.delete(ch=1)
	# print 'History Deleted'

def centerPivot(*args):
	pm.xform(cpc=1)
	# print 'Selected pivot centered.'

def freezeTransform(*args):
	selection = pm.ls( sl=1 )
	for each in selection:
		pm.makeIdentity( each, apply=1, t=1, r=1, s=1, n=0, pn=1)
		# print 'Transform Frozen'

def shoulderImport(*args):
	import BR_Interface_Toolset
	getDir()

def shoulderCheck(*args):
	global shoulder_grp_selection, BR_shoulder_grp

	# Check to see if the joints were imported and the name of them
	BR_shoulder_grp = []

	if pm.objExists('shoulder_joint_grp'):
		BR_shoulder_grp.append( ['shoulder_joint_grp'] )
		if pm.objExists( BR_shoulder_grp[0] ):
			pm.select( BR_shoulder_grp[0] )
			shoulder_grp_selection = pm.ls( BR_shoulder_grp )[0]
			print( shoulder_grp_selection)
	else:
		pass

	print(BR_shoulder_grp)

	if pm.objExists('ByrdRigs_shoulder_joint_grp'):
		BR_shoulder_grp.append( ['ByrdRigs_shoulder_joint_grp'] )
		if pm.objExists( BR_shoulder_grp[0] ):
			pm.select( BR_shoulder_grp[0] )
			shoulder_grp_selection = pm.ls( BR_shoulder_grp )[0]
			print( shoulder_grp_selection)
	else:
		pass

	if pm.objExists(shoulder_grp_selection):
		pass
	else:
		pm.error( 'Please import the shoudler joints and position them' )

	# Freeze grp transform
	freezeTransform(  )

	pm.select( cl=1 )

	# # Unparent the right joints from the grp
	# temp_selection =  pm.ls( BR_shoulder_grp[0], dag=1 )
	# print( temp_selection )

	# unparent = []

	# unparent.append( [temp_selection[1], temp_selection[2], temp_selection[6], temp_selection[7], temp_selection[8], temp_selection[10], temp_selection[11], temp_selection[12], temp_selection[14], temp_selection[18]] )
	# # print( unparent )

	# pm.select( unparent )

	# # pm.parent( w=1 )

	# # pm.select( cl=1 )

def shoulderSetup(*args):
	# Setup the variables which could come from the UI 

	global armPoint_joint, shoulder_icon, shoulder_jointRoot, arm_jointRoot
	# Input from UI
	idName = pm.textFieldGrp( shoulder_system_name, q=1, text=1 )
	# print(idName)

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1, type='joint' )
	
	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joints' )
	else:
		shoulder_jointRoot = pm.ls( sl=1, type='joint' )[0]
		arm_jointRoot = pm.ls( sl=1, type='joint' )[1]
	
	# print( shoulder_jointRoot, arm_jointRoot )

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = shoulder_jointRoot[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			pm.error( 'Please use a joint with a usable prefix of either lt_ or rt_' )


	# Now build the names we need
	limbName = whichSide + idName 
	iconName = whichSide + idName + '_icon'

	soften_joint = whichSide + 'arm_soften_bind'
	pm.parent( soften_joint, w=1  )
	
	scapRot_joint = whichSide + 'scapRot_01'
	pm.parent( scapRot_joint, w=1 )

	scap_root = whichSide + 'scap_01'

	armPoint_joint = whichSide + 'armPoint_waste'
	pm.parent( armPoint_joint, w=1  )

	lat_joint = whichSide + 'lat_01'
	pm.parent( lat_joint, w=1 )

	pec_joint = whichSide + 'pec_01'
	pm.parent( pec_joint, w=1 )

	trap_joint = whichSide + 'trap_01'
	pm.parent( trap_joint, w=1 )


	# When the back is done
	# back_joint_04 = 'ct_back_04_drv'
	# back_joint_06 = 'ct_back_06_drv'
	# back_joint_07 = 'ct_back_07_drv'
	back_joint_04 = 'ct_back_04_bind'
	back_joint_06 = 'ct_back_06_bind'
	back_joint_07 = 'ct_back_07_waste'

	neck_root = 'ct_neck_01_bind'

	#---------------------------------------------------------------------------------------
	# Build the list of joints we are working with, using the root joint as a starting point
	#---------------------------------------------------------------------------------------

	# Find it's children
	jointHierarchy = pm.listRelatives( shoulder_jointRoot, ad=1, type='joint' )

	# Add selected joint to the list 
	jointHierarchy.append( shoulder_jointRoot )

	# Reverse the list  
	jointHierarchy.reverse(  )

	# Clear the selection
	pm.select( cl=1 )

	# How many joints are we working on? This will come from UI.
	limbJoints = len(jointHierarchy)
	# print(limbJoints)


	#---------------------------------------------------------------------------------------
	# Setup muscle joints part 1
	#---------------------------------------------------------------------------------------
	
	# Move the soften and point joints
	temp_constraint = pm.parentConstraint( arm_jointRoot, soften_joint, mo=0 )
	pm.delete( temp_constraint )
	freezeTransform()

	temp_constraint = pm.pointConstraint( arm_jointRoot, armPoint_joint, mo=0 )
	pm.delete( temp_constraint )
	freezeTransform()

	# Parent the arm point under the clav_02
	pm.parent( armPoint_joint, jointHierarchy[1])

	# Parent the scapRot under arm point
	pm.parent( scapRot_joint, armPoint_joint ) 

	# Parent the trap under clav 02
	pm.parent( trap_joint, jointHierarchy[1])

	# Parent the lat under the back 04
	pm.parent( lat_joint, back_joint_04 )

	# Pad the clav and pec
	clav_pad = pm.group( em=1, n=limbName + '_pad' )
	temp_constraint = pm.parentConstraint( jointHierarchy[0], clav_pad, mo=0)
	pm.delete(temp_constraint)

	pm.parent( jointHierarchy[0], clav_pad )


	pec_pad = pm.group( em=1, n=whichSide + 'pec_00_pad' )
	temp_constraint = pm.parentConstraint( pec_joint, pec_pad, mo=0)
	pm.delete(temp_constraint)

	pm.parent( pec_joint, pec_pad )

	# Parent con the back 06 to the clav pad
	pm.parentConstraint( back_joint_06, clav_pad, mo=1 )

	# Parent con the back 04 to the pec pad
	pm.parentConstraint( back_joint_04, pec_pad, mo=1 )

	# Point con the clav 02 and back 04 to the pec joint in y & z
	pec_constraint = pm.pointConstraint( jointHierarchy[1], back_joint_04, pec_joint, skip='x', mo=1, w=.5 )

	# Set the weights to .5
	getWeights = pm.pointConstraint( pec_constraint, q=1, wal=1 )
	# print( getWeights )

	# pm.setAttr( getWeights[0], .5 )
	# pm.setAttr( getWeights[1], .5 )


	# Point con the clav 02 and back 04 to the trap joint in x
	trap_constraint = pm.pointConstraint( jointHierarchy[1], back_joint_04, trap_joint, skip=['y', 'z'], mo=1, w=.5 )

	# Set the weights to .5
	getWeights = pm.pointConstraint( trap_constraint, q=1, wal=1 )
	# print( getWeights )

	# pm.setAttr( getWeights[0], .5 )
	# pm.setAttr( getWeights[1], .5 )


	#---------------------------------------------------------------------------------------
	# Setup ik and control
	#---------------------------------------------------------------------------------------

	# Create the clav ikh
	clav_ikh = pm.ikHandle( sol='ikSCsolver', sj=jointHierarchy[0], ee=jointHierarchy[1], n=(whichSide + 'clav_ikh') )[0]

	# Get the shoulder icon
	shoulder_icon = pm.ls( iconName )

	if pm.objExists( shoulder_icon ):
		shoulder_selection = pm.ls( shoulder_icon )[0]
	else:
		pm.error( "Please create a shoulder icon with a name like 'lt_shoulder_icon'" )

	# Move the pivot to the ikh
	pivot = clav_ikh.getTranslation(  )

	shoulder_selection.setPivots( pivot )

	# Parent the ikh under the icon
	pm.parent( clav_ikh, shoulder_selection )

	# Create local
	local = pm.group( empty=1, n=limbName + '_local' )
	temp_constraint = pm.parentConstraint( jointHierarchy[1], local, mo=0 )
	pm.delete( temp_constraint )

	pm.parent( shoulder_icon, local )
	freezeTransform( shoulder_icon )

	chest_icon = 'ct_chest_icon'

	if pm.objExists( chest_icon ):
		pm.parentConstraint( chest_icon, local, mo=1 )
	else:
		pass

	
	# Lock and hide icon r, s, and v
	lock_and_hide( shoulder_selection, ['rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'] )


	#---------------------------------------------------------------------------------------
	# Setup muscle joints part 2 Aim Constraints
	#---------------------------------------------------------------------------------------
	
	# Create a would up object
	pos = pm.xform( back_joint_04, q=1, t=1, ws=1) 
	wuo_loc = pm.spaceLocator( p=(pos), n= limbName + '_wup_loc' )
	centerPivot()

	# Par con the back 04 to the wuo loc
	pm.parentConstraint( back_joint_04, wuo_loc, mo=1  )

	# Aim the trap to neck if it exists if no the back 07

	if pm.objExists( neck_root ):
		pm.aimConstraint( neck_root, trap_joint, w=1, u=(0, 1, 0), mo=1, wuo=(wuo_loc), wut='objectrotation', aim=(1, 0, 0), wu=(0, 1, 0)  )
	else:
		pm.aimConstraint( back_joint_07, trap_joint, w=1, u=(0, 1, 0), mo=1, wuo=(wuo_loc), wut='objectrotation', aim=(1, 0, 0), wu=(0, 1, 0)  )

	# Aim the scapRot to neck if it exists if no the back 07

	if pm.objExists( neck_root ):
		pm.aimConstraint( neck_root, scapRot_joint, w=1, u=(0, 1, 0), mo=1, wuo=(wuo_loc), wut='objectrotation', aim=(1, 0, 0), wu=(0, 1, 0)  )
	else:
		pm.aimConstraint( back_joint_07, scapRot_joint, w=1, u=(0, 1, 0), mo=1, wuo=(wuo_loc), wut='objectrotation', aim=(1, 0, 0), wu=(0, 1, 0)  )

	# Aim the scap to bak 04
	pm.aimConstraint( back_joint_04, scap_root, w=1, u=(0, 1, 0), mo=1, wuo=(wuo_loc), wut='objectrotation', aim=(1, 0, 0), wu=(0, 1, 0)  )

	#---------------------------------------------------------------------------------------
	# Soft joint Setup
	#---------------------------------------------------------------------------------------
	
	# Create mult node
	soft_mult = pm.createNode( 'multiplyDivide', n=limbName + '_soft_mult' )

	pm.connectAttr( arm_jointRoot + '.ry', soft_mult + '.input1X', f=1 )
	pm.connectAttr( arm_jointRoot + '.rz', soft_mult + '.input1Y', f=1 )

	pm.connectAttr( soft_mult + '.outputX', soften_joint + '.ry', f=1 )
	pm.connectAttr( soft_mult + '.outputY', soften_joint + '.rz', f=1 )

	soft_mult.input2X.set( .25 )
	soft_mult.input2Y.set( .25 )

	# #---------------------------------------------------------------------------------------
	# # Scap back rot fix Can't get values right
	# #---------------------------------------------------------------------------------------
	
	# # Create set range node 
	# scap_range = pm.createNode( 'setRange', n=whichSide + 'scapRange' )

	# # Create the scap condition
	# scap_cond = pm.createNode( 'condition', n=whichSide + 'scapCond' )

	# # Connect the clav 01 ry to range v x & z
	# pm.connectAttr( jointHierarchy[0] + '.ry', scap_range + '.valueX', f=1 )
	# pm.connectAttr( jointHierarchy[0] + '.ry', scap_range + '.valueZ', f=1 )

	# # Set the old max and min of X
	# scap_range.oldMinX.set( 5 )
	# scap_range.oldMaxX.set( 20 )

	# # Get the default tx of the scap joint
	# def_x = pm.getAttr( scap_root + '.tx' )
	# # print( def_x )

	# # Set the new min and max X
	# # Min X should be the default tx value
	# scap_range.minX.set( def_x )
	# scap_range.maxX.set( .6 )

	# # Set the old max and min of Z
	# scap_range.oldMinZ.set( -20 )
	# scap_range.oldMaxZ.set( 0 )

	# # Set the new min and max Z
	# # Max Z should be the default tx value
	# scap_range.minZ.set( 1 )
	# scap_range.maxZ.set( def_x )

	# # Connect the clav 01 ry to the first term
	# pm.connectAttr( jointHierarchy[0] + '.ry', scap_cond + '.firstTerm' )

	# # Set the operation to greater than
	# scap_cond.operation.set( 2 )

	# # Connect the outX to the color if true R
	# pm.connectAttr( scap_range + '.outValueX', scap_cond + '.colorIfTrueR', f=1 )

	# # Connect the outZ to the color if false R
	# pm.connectAttr( scap_range + '.outValueZ', scap_cond + '.colorIfFalseR', f=1 )

	# # Connect the out color R to the scap tx
	# pm.connectAttr( scap_cond + '.outColorR', scap_root + '.tx' )

	#---------------------------------------------------------------------------------------
	# Clean up
	#---------------------------------------------------------------------------------------
	
	if 'lt_' in whichSide:
		pm.setAttr( shoulder_selection + '.overrideEnabled', 1 )
		pm.setAttr( shoulder_selection + '.overrideColor', 6 )

	if 'rt_' in whichSide:
		pm.setAttr( shoulder_selection + '.overrideEnabled', 1 )
		pm.setAttr( shoulder_selection + '.overrideColor', 13 )

	clav_ikh.v.set(0)

	# Rename muscle joints
	pm.select( pec_joint, lat_joint, scap_root, jointHierarchy[0], trap_joint )
	rename_grp = pm.ls( sl=1 )

	for each in rename_grp:
		jointHierarchy[0].replace( '01', '01_bind' )

	# Rename muscle joints

	
	trap_selection = pm.ls( trap_joint, sl=1, dag=1 )
	# print( trap_selection )
	# new_name = '{0}_{1}_01_bind'.format( whichSide, 'trap' )
	# trap_selection.rename( new_name )

	# # new_name = '{0}_{1}_01_waste'.format( whichSide, 'trap' )
	# # trap_selection[1].rename( new_name )
	
	pm.select( jointHierarchy[1], trap_selection[1] )
	rename_grp = pm.ls( sl=1 )

	for each in rename_grp:
		jointHierarchy[1].replace( '02', '02_waste' )

	pm.select( scapRot_joint )
	scapRot_selection = pm.ls( sl=1 )[0]

	new_name = scapRot_selection.replace( '01', '01_waste' )
	scapRot_selection.rename( new_name )


	# # Get icon_grp
	# icon_grp = 'icon_grp'

	# if pm.objExists( icon_grp ):
	# 	pass
	# else:
	# 	pm.error( "Please rename the icon group to 'icon_grp', you can change this later" )


	pm.select( cl=1 )
 
def armSetup(*args):
	# Setup the variables which could come from the UI 

	# Input from UI
	idName = pm.textFieldGrp( arm_system_name, q=1, text=1 )
	# print(idName)

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1, type='joint' )
	
	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joint' )
	else:
		jointRoot = pm.ls( sl=1, type='joint' )[0]
	
	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = jointRoot[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			pm.error( 'Please use a joint with a usable prefix of either lt_ or rt_' )

	# Now build the names we need
	limbName = whichSide + idName 
	iconName = whichSide + idName + '_icon'

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

	#---------------------------------------------------------------------------------------
	# Duplicate the main joint chain and rename each joint
	#---------------------------------------------------------------------------------------

	# First define what joint chains we need 
	newJointList = ['_ik', '_fk', '_stretch']

	# Build the joints
	for newJoint in newJointList:
		for i in range( limbJoints ):
			newJointName = jointHierarchy[i] + newJoint
			# print( newJointName )
			pm.joint( n=newJointName )	
			temp_constraint = pm.parentConstraint( jointHierarchy[i], newJointName, mo=0 )
			pm.delete( temp_constraint )
			pm.makeIdentity( newJointName, a=1, t=0, r=1, s=0 )

		pm.select( cl=1 )


	# Get the ikfk switch
	switch = limbName + '_switch'
	# print(switch)

	# Check if the swich exists
	if pm.objExists( switch ):
		switch_selection = pm.ls( switch )[0]
	else:
		pm.error("Please make an Ik/Fk switch using the suffix _switch. i.e lt_arm_switch")

	pm.addAttr( switch_selection, ln='IkFk', nn='Ik/Fk', min=0, max=1, at='double' )
	unlock_and_unhide( switch_selection, ['IkFk'] )

	
	# Constrain the main joints to the ik and fk joints so we can blend between them
	for i in range( limbJoints ):
		pm.parentConstraint( jointHierarchy[i] + '_ik', jointHierarchy[i] + '_fk', jointHierarchy[i], mo=0 )

	# IkFk blending 
	ikfk_rev = pm.shadingNode( 'reverse', asUtility=1, n=(limbName + '_ikfk_rev') )
	pm.connectAttr( (switch + '.IkFk'), (ikfk_rev + '.inputX'), f=1 )
	for i in range( limbJoints ):
		getConstraint = pm.listConnections(jointHierarchy[i], t='parentConstraint')[0]
		getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
		# print(getConstraint)
		# print(getWeights)
		pm.connectAttr( (switch + '.IkFk'), (getWeights[1]), f=1)
		pm.connectAttr( ikfk_rev + '.outputX', (getWeights[0]), f=1)

	pm.parentConstraint( jointHierarchy[2], switch, mo=1 )

	# Lock and hide attrs
	lock_and_hide(switch_selection, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])



	#---------------------------------------------------------------------------------------
	# Setup FK
	#---------------------------------------------------------------------------------------
	# Create the controls
	for i in range( limbJoints ):
		crv = pm.circle( c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=4.54965e-09, nr=(1, 0, 0), n=(jointHierarchy[i] + '_fk_icon') )
		crv = pm.ls(sl=1)[0]
		# print(crv)
		temp_constraint = pm.parentConstraint( jointHierarchy[i], crv, mo=0 )
		pm.delete( temp_constraint )
		pad = pm.group( empty=1, n=(jointHierarchy[i] + '_fk_local') )
		temp_constraint = pm.parentConstraint( jointHierarchy[i], pad, mo=0 )
		pm.delete( temp_constraint )
		pm.parent( crv, pad )
		pm.makeIdentity( crv, a=1, t=1, r=1 )
		pm.delete(crv, ch=1)

		pm.setAttr( (crv + '.overrideEnabled'), 1 )

		if 'lt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 6 )

		if 'rt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 13 )

		# Parent the pads to the icons 
		if i>=1:
			pm.parent( (jointHierarchy[i] + '_fk_local'), (jointHierarchy[i - 1] + '_fk_icon') )
		
		# Constrain the icon and the joints
		pm.parentConstraint( (jointHierarchy[i] + '_fk_icon'), (jointHierarchy[i] + '_fk'), mo=1 )


	# Delete the last fk pad and icon
	pm.delete((jointHierarchy[-1] + '_fk_local'))

	arm_icon = limbName + '_icon'
	# Get the arm icon
	if pm.objExists( arm_icon ):
		arm_selection = pm.ls( arm_icon )[0]
	else:
		pm.error( "Please make an arm icon with a name like 'lt_arm_icon'" )

	#---------------------------------------------------------------------------------------
	# Create the Gimbal icon
	#---------------------------------------------------------------------------------------

	gimbal_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0), n=(limbName + '_01_gimbal_core') )[0]

	gimbal_icon_2 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=0.2, tol=0.01, nr=(1, 0, 0), n=(limbName + '_02_gimbal_core') )[0]

	gimbal_icon_2.ty.set(1)
	freezeTransform(gimbal_icon_2)

	pm.select(gimbal_icon, gimbal_icon_2)

	selection = pm.ls(sl=True, dag=True, s=True)
	shape_1 = selection[0]
	shape_2 = selection[1]
	# print shape_1
	# print shape_2

	core_icon = pm.group(empty=True, n=(limbName + '_gimbal_core_icon'))

	pm.parent( shape_1, shape_2, core_icon, r=True, s=True )

	pm.delete( gimbal_icon, gimbal_icon_2 ) 

	pm.setAttr( core_icon + '.sx', 1.5 )
	pm.setAttr( core_icon + '.sy', 1.5 )
	pm.setAttr( core_icon + '.sz', 1.5 )

	temp_constraint = pm.pointConstraint( jointRoot, core_icon, mo=0 )
	pm.delete(temp_constraint)
	temp_constraint = pm.orientConstraint( jointRoot, core_icon, skip='x', mo=0)
	pm.delete(temp_constraint)
	pm.select(core_icon)
	freezeTransform()
	deleteHistory()

	pm.orientConstraint( core_icon, jointHierarchy[0] + '_fk_local', mo=1 )

	gimbal_core_tog = pm.shadingNode('blendColors', asUtility=1, n=(limbName + '_gimbal_core_tog'))

	pm.connectAttr(core_icon + '.r', gimbal_core_tog + '.color2', f=1)
	gimbal_core_tog.color1R.set(0)
	gimbal_core_tog.color1G.set(0)
	gimbal_core_tog.color1B.set(0)
	pm.connectAttr(switch + '.IkFk', gimbal_core_tog + '.blender', f=1)
	pm.connectAttr(switch + '.IkFk', core_icon + '.v', f=1)


	if 'lt_' in whichSide:
		pm.setAttr( core_icon + '.overrideEnabled', 1 )
		pm.setAttr( core_icon + '.overrideColor', 15 )

	if 'rt_' in whichSide:
		pm.setAttr( core_icon + '.overrideEnabled', 1 )
		pm.setAttr( core_icon + '.overrideColor', 4 )

	gimbal_local = pm.group(empty=1, n=(limbName + '_gimbal_local'))

	temp_constraint = pm.parentConstraint(core_icon, gimbal_local, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	pm.parent(core_icon, gimbal_local)
	freezeTransform()


	lock_and_hide( core_icon , ['v', 'tx', 'ty', 'tz', 'sx', 'sy', 'sz'] )



	# Get the elbow icon
	elbow_icon = (whichSide + 'elbow_icon')
	if pm.objExists( elbow_icon ):
		elbow_selection = pm.ls( elbow_icon )[0]
	else:
		pm.error( "Please make elbow icon with a name like 'lt_elbow_icon'" )

	#---------------------------------------------------------------------------------------
	# Setup IK
	#---------------------------------------------------------------------------------------
	arm_ikh = pm.ikHandle( sj=jointHierarchy[0] + '_ik', ee=jointHierarchy[2] + '_ik', n=(limbName + '_ikh') )[0]

	# Create pole vector
	pm.poleVectorConstraint( elbow_icon, arm_ikh )

	# Parent the ikh under the arm_icon
	pm.parent( arm_ikh, arm_icon )

	#---------------------------------------------------------------------------------------
	# Stretch
	#---------------------------------------------------------------------------------------

	# Create 2 distBetween nodes 
	upper_dist = pm.createNode( 'distanceBetween', n=limbName + '_upper_dist' )

	lower_dist = pm.createNode( 'distanceBetween', n=limbName + '_lower_dist' )


	# Create 1 distDim node and locs
	stretch_dist = pm.createNode( 'distanceDimShape', n=limbName + '_stretch_distShape' )

	# Create start loc at root
	start_loc = pm.spaceLocator( n=limbName + '_startLoc' )
	temp_constraint = pm.pointConstraint( jointHierarchy[0], start_loc, mo=0 )
	pm.delete( temp_constraint )

	# Create loc at the icon
	stretch_loc = pm.spaceLocator( n=limbName + '_stretchEnd_loc' )
	temp_constraint = pm.pointConstraint( jointHierarchy[2], stretch_loc, mo=0 )
	pm.delete(temp_constraint)

	pm.parent( stretch_loc, arm_icon )

	# Connect the locs to the start and end point 
	pm.connectAttr( start_loc  + '.worldPosition', stretch_dist + '.startPoint', f=1 )
	pm.connectAttr( stretch_loc + '.worldPosition', stretch_dist + '.endPoint', f=1 )


	# Connect the iks to the dist nodes
	pm.connectAttr( jointHierarchy[0] + '_stretch.worldMatrix' , upper_dist + '.inMatrix1', f=1 )
	pm.connectAttr( jointHierarchy[1] + '_stretch.worldMatrix' , upper_dist + '.inMatrix2', f=1 )

	pm.connectAttr( jointHierarchy[1] + '_stretch.worldMatrix' , lower_dist + '.inMatrix1', f=1 )
	pm.connectAttr( jointHierarchy[2] + '_stretch.worldMatrix' , lower_dist + '.inMatrix2', f=1 )

	# Create a addDoubleLinear node
	full_Dist = pm.createNode( 'addDoubleLinear', n=limbName + '_full_dist_dubLin' )

	# Connect the dist to the duLin
	pm.connectAttr( upper_dist + '.distance', full_Dist + '.input1', f=1 )
	pm.connectAttr( lower_dist + '.distance', full_Dist + '.input2', f=1 )

	# Pad the arm joints 
	arm_pad = pm.group( em=1, n=limbName + '_00_pad' )
	temp_constraint = pm.pointConstraint( jointHierarchy[0], arm_pad, mo=0 )
	pm.delete(temp_constraint)
	freezeTransform(arm_pad)

	pm.parent( jointHierarchy[0], jointHierarchy[0] + '_ik', jointHierarchy[0] + '_fk', jointHierarchy[0] + '_stretch', arm_pad )

	# Create a condition node
	stretch_con = pm.createNode( 'condition', n=limbName+ '_con' )

	# Connect the stretch dist to first term and the full dist to seond term
	pm.connectAttr( stretch_dist + '.distance', stretch_con + '.firstTerm', f=1 )
	pm.connectAttr( full_Dist + '.output', stretch_con + '.secondTerm', f=1 )

	# Set con to greater than
	stretch_con.operation.set( 2 )

	# Create a multi node
	stretch_mult = pm.createNode( 'multiplyDivide', n=limbName + '_stretch_mult' )

	# Connect the stretch and full dist to the mult
	pm.connectAttr( stretch_dist + '.distance', stretch_mult + '.input1X', f=1 )
	pm.connectAttr( full_Dist + '.output', stretch_mult + '.input2X', f=1 )

	# Set the operation to 1
	stretch_mult.operation.set( 2 )

	# Connect the mult to the con
	pm.connectAttr( stretch_mult + '.outputX', stretch_con + '.colorIfTrueR', f=1 )

	# Connect the con to the ik joints 
	pm.connectAttr( stretch_con + '.outColorR', jointHierarchy[0] + '_ik.sx', f=1 )
	pm.connectAttr( stretch_con + '.outColorR', jointHierarchy[1] + '_ik.sx', f=1 )


	#---------------------------------------------------------------------------------------
	# Scale Norm
	#---------------------------------------------------------------------------------------

	# Get the main icon 
	rig_global_icon = 'ct_moveAll'
	

	if pm.objExists( rig_global_icon ):
		rig_global_selection = pm.ls( rig_global_icon )[0]
	else:
		pm.error( "Please rename the main icon 'ct_moveAll', you can change this later " )


	#---------------------------------------------------------------------------------------
	# Clean up part 2
	#---------------------------------------------------------------------------------------

	# Get icon_grp
	anim_icon = 'ct_anim'

	if pm.objExists( anim_icon ):
		anim_selection = pm.ls( anim_icon )[0]

	if pm.objExists( anim_icon ):
		pm.parent( arm_icon, elbow_icon, switch, gimbal_local, anim_icon )
	else:
		pm.parent( arm_icon, elbow_icon, switch, gimbal_local, rig_global_icon )

	# pm.scaleConstraint( main_icon, icon_grp, mo=1 )


	# Par con the arm point to the arm pad, gimbal pad, and dnt grp
	pm.parentConstraint( armPoint_joint, arm_pad, mo=1 )
	pm.parentConstraint( armPoint_joint, gimbal_local, mo=1 )
	# pm.parentConstraint( armPoint_joint, arm_dnt_grp, mo=1 )


	# Rename the bind joints
	for i in range(limbJoints):
		new_name = '{0}'.format( (jointHierarchy[i] + '_bind') )
		# print( new_name )
		jointHierarchy[i].rename( new_name )

	pm.select( arm_icon, elbow_icon, switch )
	icons = pm.ls(sl=1)

	if 'lt_' in whichSide:
		for each in icons:
			pm.setAttr( each + '.overrideEnabled', 1 )
			pm.setAttr( each + '.overrideColor', 6 )

	if 'rt_' in whichSide:
		for each in icons:
			pm.setAttr( each + '.overrideEnabled', 1 )
			pm.setAttr( each + '.overrideColor', 13 )

	# Name the waste joint
	new_name = '{0}'.format((limbName + '_03_waste'))
	jointHierarchy[-1].rename( new_name )

	global jointRoot, arm_jointRoot

	pm.select( cl=1 )

def handSetup(*args):
	# Setup the variables which could come from the UI 

	global hand_root, hand_icon, hand_selection

	# Input from UI
	idName = pm.textFieldGrp( hand_system_name, q=1, text=1 )
	# print(idName)

	# Get the last arm joint
	arm_joint_3 = pm.ls(arm_jointRoot, dag=1)[2]
	# print( arm_joint_3 )

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1, type='joint' )
	
	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joint' )
	else:
		jointRoot = pm.ls( sl=1, type='joint' )[0]
	
	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = jointRoot[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			pm.error( 'Please use a joint with a usable prefix of either lt_ or rt_' )

	# Now build the names we need
	limbName = whichSide + idName 
	iconName = whichSide + idName + '_icon'

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

	# Get the hand icon
	hand_icon = (iconName)


	if pm.objExists( hand_icon ):
		pass
	else:
		pm.error( "Please make a hand icon with a name like 'lt_hand_icon'" ) 

	hand_selection = pm.ls( hand_icon )[0]

	# Create the icon local
	icon_local = pm.group( empty=1, n=(limbName + '_local') )
	temp_constraint = pm.parentConstraint( jointRoot, icon_local, mo=0 )
	pm.delete( temp_constraint )

	# Set the hand icon pivot to the hand joint
	pivot = icon_local.getTranslation()

	hand_selection.setPivots( pivot )

	# Parent the icon under the local
	pm.parent( hand_icon, icon_local )

	#  Freeze the transforms of the icon
	freezeTransform()
	deleteHistory()

	local_const = pm.parentConstraint(arm_joint_3, icon_local, mo=1)

	# world_pad = pm.group( empty=1, n=(limbName + '_world') )
	# temp_constraint = pm.parentConstraint( jointRoot, world_pad, mo=0)
	# pm.delete(temp_constraint)

	pm.parentConstraint( hand_icon, jointRoot, mo=1 )

	# const = pm.orientConstraint( arm_joint_3, world_pad, icon_local, mo=1 )
	# local_const = const.getWeightAliasList()[0]
	# world_const = const.getWeightAliasList()[1]

	# print 'Local Const:', local_const
	# print 'World Const:', world_const

	# pm.addAttr(hand_icon, ln="localWorld", max=1, dv=0, at='double', min=0)
	# hand_selection.localWorld.set(e=1, keyable=True)

	# world_const.set(0)
	# pm.setDrivenKeyframe(world_const, local_const, currentDriver= hand_icon + '.localWorld')
	# hand_selection.localWorld.set(1)
	# world_const.set(1)
	# local_const.set(0)
	# pm.setDrivenKeyframe(world_const, local_const, currentDriver= hand_icon + '.localWorld')
	# hand_selection.localWorld.set(0)

	new_name = '{0}'.format((limbName + '_01_bind'))
	jointRoot.rename( new_name )

	new_name = '{0}'.format((limbName + '_02_waste'))
	jointHierarchy[1].rename( new_name )

	if 'lt_' in whichSide:
		pm.setAttr( hand_selection + '.overrideEnabled', 1 )
		pm.setAttr( hand_selection + '.overrideColor', 6 )

	if 'rt_' in whichSide:
		pm.setAttr( hand_selection + '.overrideEnabled', 1 )
		pm.setAttr( hand_selection + '.overrideColor', 13 )

	hand_root = pm.ls( jointRoot, dag=1 )

def fingerSelection(*args):
	# Setup the variables which could come from the UI 

	global index_idName, middle_idName, ring_idName, pinky_idName, thumb_idName
	global index_jointRoot, middle_jointRoot, ring_jointRoot, pinky_jointRoot, thumb_jointRoot
	global index_jointHierarchy, middle_jointHierarchy, ring_jointHierarchy, pinky_jointHierarchy, thumb_jointHierarchy 
	global index_limbName, middle_limbName, ring_limbName, pinky_limbName, thumb_limbName
	global index_iconName, middle_iconName, ring_iconName, pinky_iconName, thumb_iconName
	global index_limbJoints, middle_limbJoints, ring_limbJoints, pinky_limbJoints, thumb_limbJoints
	global selection_len, whichSide

	# Input from UI
	index_idName = pm.textFieldGrp( index_system_name, q=1, text=1 )
	# print(index_idName)

	middle_idName = pm.textFieldGrp( middle_system_name, q=1, text=1 )
	# print(middle_idName)

	ring_idName = pm.textFieldGrp( ring_system_name, q=1, text=1 )
	# print(ring_idName)

	pinky_idName = pm.textFieldGrp( pinky_system_name, q=1, text=1 )
	# print(pinky_idName)

	thumb_idName = pm.textFieldGrp( thumb_system_name, q=1, text=1 )
	# print(thumb_idName)


	# Check the selection is valid
	selectionCheck = pm.ls( sl=1, type='joint' )

	selection_len = len(selectionCheck)
	print( selection_len )

	if selection_len == 5:
		# Error check to make sure a joint is selected
		if not selectionCheck:
			pm.error( 'Please select the root joint' )
		else:
			index_jointRoot = pm.ls( sl=1, type='joint' )[0]
			middle_jointRoot = pm.ls( sl=1, type='joint' )[1]
			ring_jointRoot = pm.ls( sl=1, type='joint' )[2]
			pinky_jointRoot = pm.ls( sl=1, type='joint' )[3]
			thumb_jointRoot = pm.ls( sl=1, type='joint' )[4]
		# print( index_jointRoot, middle_jointRoot, ring_jointRoot, pinky_jointRoot, thumb_jointRoot )
		
		# Now we have a selected joint we can check for the prefix to see wht side it's on
		whichSide = index_jointRoot[0:3]

		# Make sure the prefix is usable
		if not 'lt_' in whichSide:
			if not 'rt_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_ or rt_' )

		# Now build the names we need
		index_limbName = whichSide + index_idName 
		index_iconName = whichSide + index_idName + '_icon'

		middle_limbName = whichSide + middle_idName 
		middle_iconName = whichSide + middle_idName + '_icon'

		ring_limbName = whichSide + ring_idName 
		ring_iconName = whichSide + ring_idName + '_icon'

		pinky_limbName = whichSide + pinky_idName 
		pinky_iconName = whichSide + pinky_idName + '_icon'

		thumb_limbName = whichSide + thumb_idName 
		thumb_iconName = whichSide + thumb_idName + '_icon'

		#---------------------------------------------------------------------------------------
		# Build the list of joints we are working with, using the root joint as a starting point
		#---------------------------------------------------------------------------------------

		# Index
		# Find it's children
		index_jointHierarchy = pm.listRelatives( index_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		index_jointHierarchy.append( index_jointRoot )

		# Reverse the list  
		index_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		# How many joints are we working on? This will come from UI.
		index_limbJoints = len(index_jointHierarchy)
		# print(index_limbJoints)

		# Middle
		middle_jointHierarchy = pm.listRelatives( middle_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		middle_jointHierarchy.append( middle_jointRoot )

		# Reverse the list  
		middle_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		middle_limbJoints = len(middle_jointHierarchy)
		# print(middle_limbJoints)

		# Ring
		ring_jointHierarchy = pm.listRelatives( ring_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		ring_jointHierarchy.append( ring_jointRoot )

		# Reverse the list  
		ring_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		ring_limbJoints = len(ring_jointHierarchy)
		# print(ring_limbJoints)

		# Pinky
		pinky_jointHierarchy = pm.listRelatives( pinky_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		pinky_jointHierarchy.append( pinky_jointRoot )

		# Reverse the list  
		pinky_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		pinky_limbJoints = len(pinky_jointHierarchy)
		# print(pinky_limbJoints)

		# Thumb
		thumb_jointHierarchy = pm.listRelatives( thumb_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		thumb_jointHierarchy.append( thumb_jointRoot )

		# Reverse the list  
		thumb_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		thumb_limbJoints = len(thumb_jointHierarchy)
		# print(thumb_limbJoints)

	if selection_len == 4:
		# Error check to make sure a joint is selected
		if not selectionCheck:
			pm.error( 'Please select the root joint' )
		else:
			index_jointRoot = pm.ls( sl=1, type='joint' )[0]
			middle_jointRoot = pm.ls( sl=1, type='joint' )[1]
			pinky_jointRoot = pm.ls( sl=1, type='joint' )[2]
			thumb_jointRoot = pm.ls( sl=1, type='joint' )[3]
		# print( index_jointRoot, middle_jointRoot, pinky_jointRoot, thumb_jointRoot )
		
		
		# Now we have a selected joint we can check for the prefix to see wht side it's on
		whichSide = index_jointRoot[0:3]

		# Make sure the prefix is usable
		if not 'lt_' in whichSide:
			if not 'rt_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_ or rt_' )

		# Now build the names we need
		index_limbName = whichSide + index_idName 
		index_iconName = whichSide + index_idName + '_icon'

		middle_limbName = whichSide + middle_idName 
		middle_iconName = whichSide + middle_idName + '_icon'

		pinky_limbName = whichSide + pinky_idName 
		pinky_iconName = whichSide + pinky_idName + '_icon'

		thumb_limbName = whichSide + thumb_idName 
		thumb_iconName = whichSide + thumb_idName + '_icon'

		# Index
		# Find it's children
		index_jointHierarchy = pm.listRelatives( index_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		index_jointHierarchy.append( index_jointRoot )

		# Reverse the list  
		index_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		# How many joints are we working on? This will come from UI.
		index_limbJoints = len(index_jointHierarchy)
		# print(index_limbJoints)

		# Middle
		middle_jointHierarchy = pm.listRelatives( middle_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		middle_jointHierarchy.append( middle_jointRoot )

		# Reverse the list  
		middle_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		middle_limbJoints = len(middle_jointHierarchy)
		# print(middle_limbJoints)

		# Pinky
		pinky_jointHierarchy = pm.listRelatives( pinky_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		pinky_jointHierarchy.append( pinky_jointRoot )

		# Reverse the list  
		pinky_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		pinky_limbJoints = len(pinky_jointHierarchy)
		# print(pinky_limbJoints)

		# Thumb
		thumb_jointHierarchy = pm.listRelatives( thumb_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		thumb_jointHierarchy.append( thumb_jointRoot )

		# Reverse the list  
		thumb_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		thumb_limbJoints = len(thumb_jointHierarchy)
		# print(thumb_limbJoints)

	if selection_len == 3:
		# Error check to make sure a joint is selected
		if not selectionCheck:
			pm.error( 'Please select the root joint' )
		else:
			index_jointRoot = pm.ls( sl=1, type='joint' )[0]
			pinky_jointRoot = pm.ls( sl=1, type='joint' )[1]
			thumb_jointRoot = pm.ls( sl=1, type='joint' )[2]
		# print( index_jointRoot, pinky_jointRoot, thumb_jointRoot )
		
		# Now we have a selected joint we can check for the prefix to see wht side it's on
		whichSide = index_jointRoot[0:3]

		# Make sure the prefix is usable
		if not 'lt_' in whichSide:
			if not 'rt_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_ or rt_' )

		# Now build the names we need
		index_limbName = whichSide + index_idName 
		index_iconName = whichSide + index_idName + '_icon'

		pinky_limbName = whichSide + pinky_idName 
		pinky_iconName = whichSide + pinky_idName + '_icon'

		thumb_limbName = whichSide + thumb_idName 
		thumb_iconName = whichSide + thumb_idName + '_icon'

		# Index
		# Find it's children
		index_jointHierarchy = pm.listRelatives( index_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		index_jointHierarchy.append( index_jointRoot )

		# Reverse the list  
		index_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		# How many joints are we working on? This will come from UI.
		index_limbJoints = len(index_jointHierarchy)
		# print(index_limbJoints)

		# Pinky
		pinky_jointHierarchy = pm.listRelatives( pinky_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		pinky_jointHierarchy.append( pinky_jointRoot )

		# Reverse the list  
		pinky_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		pinky_limbJoints = len(pinky_jointHierarchy)
		# print(pinky_limbJoints)

		# Thumb
		thumb_jointHierarchy = pm.listRelatives( thumb_jointRoot, ad=1, type='joint' )

		# Add selected joint to the list 
		thumb_jointHierarchy.append( thumb_jointRoot )

		# Reverse the list  
		thumb_jointHierarchy.reverse(  )

		# Clear the selection
		pm.select( cl=1 )

		thumb_limbJoints = len(thumb_jointHierarchy)
		# print(thumb_limbJoints)

def finger_setup(*args):
	# Get finger selection
	fingerSelection()

	if selection_len == 5:
		indexSetup()
		middleSetup()
		ringSetup()
		pinkySetup()
		thumbSetup()
		parentIcon_setup()
		indexSDK()
		middleSDK()
		ringSDK()
		pinkySDK()
		thumbSDK()
		pm.select( cl=1 )

	if selection_len == 4:
		indexSetup()
		middleSetup()
		pinkySetup()
		thumbSetup()
		parentIcon_setup()
		indexSDK()
		middleSDK()
		pinkySDK()
		thumbSDK()
		pm.select( cl=1 )


	if selection_len == 3:
		indexSetup()
		pinkySetup()
		thumbSetup()
		parentIcon_setup()
		indexSDK()
		pinkySDK()
		thumbSDK()
		pm.select( cl=1 )

	# rename()

def indexSetup(*args):

	# First define what joint chains we need 
	newJointList = ['_ik', '_fk']

	# Build the joints
	for newJoint in newJointList:
		for i in range( index_limbJoints ):
			newJointName = index_jointHierarchy[i] + newJoint
			# print( newJointName )
			pm.joint( n=newJointName )	
			temp_constraint = pm.parentConstraint( index_jointHierarchy[i], newJointName, mo=0 )
			pm.delete( temp_constraint )
			pm.makeIdentity( newJointName, a=1, t=0, r=1, s=0 )

		pm.select( cl=1 )

	#---------------------------------------------------------------------------------------
	# Setup FK
	#---------------------------------------------------------------------------------------
	# Create the controls
	for i in range( index_limbJoints ):
		crv = pm.circle( c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=.15, tol=4.54965e-09, nr=(1, 0, 0), n=(index_jointHierarchy[i] + '_fk_icon') )
		crv = pm.ls(sl=1)[0]
		# print(crv)
		temp_constraint = pm.parentConstraint( index_jointHierarchy[i], crv, mo=0 )
		pm.delete( temp_constraint )
		pad = pm.group( empty=1, n=(index_jointHierarchy[i] + '_fk_local') )
		temp_constraint = pm.parentConstraint( index_jointHierarchy[i], pad, mo=0 )
		pm.delete( temp_constraint )
		pm.parent( crv, pad )
		pm.makeIdentity( crv, a=1, t=1, r=1 )
		pm.delete(crv, ch=1)

		pm.setAttr( (crv + '.overrideEnabled'), 1 )

		if 'lt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 6 )

		if 'rt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 13 )

		# Parent the pads to the icons 
		if i>=1:
			pm.parent( (index_jointHierarchy[i] + '_fk_local'), (index_jointHierarchy[i - 1] + '_fk_icon') )
		
		# Constrain the icon and the joints
		pm.parentConstraint( (index_jointHierarchy[i] + '_fk_icon'), (index_jointHierarchy[i] + '_fk'), mo=1 )
		


	# Delete the last fk pad and icon
	pm.delete((index_jointHierarchy[-1] + '_fk_local'))

 
	# Connect the ik and fk to the bind joints
	for i in range( index_limbJoints ):
		# Constrain the fk and the bind joints
		pm.parentConstraint( (index_jointHierarchy[i] + '_ik'), (index_jointHierarchy[i] + '_fk'), (index_jointHierarchy[i]), mo=1 )

	# Pad the joints
	pad = pm.group( empty=1, n=(index_limbName + '_00_pad') )
	temp_constraint = pm.parentConstraint( index_jointHierarchy[0], pad, mo=0 )
	pm.delete( temp_constraint )

	pm.parent( index_jointHierarchy[0], index_jointHierarchy[0] + '_fk', index_jointHierarchy[0] + '_ik', pad )

	# Constrain the hand to the fingers
	pm.parentConstraint( hand_root, pad, mo=1 )


	# Change vis for ikfk joints
	pm.select( index_jointHierarchy[0] + '_ik', index_jointHierarchy[0] + '_fk' )
	joints = pm.ls( sl=1 )

	for each in joints:
		each.v.set(0)

	pm.select( cl=1 )

def middleSetup(*args):

	# First define what joint chains we need 
	newJointList = ['_ik', '_fk']

	# Build the joints
	for newJoint in newJointList:
		for i in range( middle_limbJoints ):
			newJointName = middle_jointHierarchy[i] + newJoint
			# print( newJointName )
			pm.joint( n=newJointName )	
			temp_constraint = pm.parentConstraint( middle_jointHierarchy[i], newJointName, mo=0 )
			pm.delete( temp_constraint )
			pm.makeIdentity( newJointName, a=1, t=0, r=1, s=0 )

		pm.select( cl=1 )

	#---------------------------------------------------------------------------------------
	# Setup FK
	#---------------------------------------------------------------------------------------
	# Create the controls
	for i in range( middle_limbJoints ):
		crv = pm.circle( c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=.15, tol=4.54965e-09, nr=(1, 0, 0), n=(middle_jointHierarchy[i] + '_fk_icon') )
		crv = pm.ls(sl=1)[0]
		# print(crv)
		temp_constraint = pm.parentConstraint( middle_jointHierarchy[i], crv, mo=0 )
		pm.delete( temp_constraint )
		pad = pm.group( empty=1, n=(middle_jointHierarchy[i] + '_fk_local') )
		temp_constraint = pm.parentConstraint( middle_jointHierarchy[i], pad, mo=0 )
		pm.delete( temp_constraint )
		pm.parent( crv, pad )
		pm.makeIdentity( crv, a=1, t=1, r=1 )
		pm.delete(crv, ch=1)

		pm.setAttr( (crv + '.overrideEnabled'), 1 )

		if 'lt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 6 )

		if 'rt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 13 )

		# Parent the pads to the icons 
		if i>=1:
			pm.parent( (middle_jointHierarchy[i] + '_fk_local'), (middle_jointHierarchy[i - 1] + '_fk_icon') )
		
		# Constrain the icon and the joints
		pm.parentConstraint( (middle_jointHierarchy[i] + '_fk_icon'), (middle_jointHierarchy[i] + '_fk'), mo=1 )

		


	# Delete the last fk pad and icon
	pm.delete((middle_jointHierarchy[-1] + '_fk_local'))

 
	# Connect the ik and fk to the bind joints
	for i in range( middle_limbJoints ):
		# Constrain the fk and the bind joints
		pm.parentConstraint( (middle_jointHierarchy[i] + '_ik'), (middle_jointHierarchy[i] + '_fk'), (middle_jointHierarchy[i]), mo=1 )

	# Pad the joints
	pad = pm.group( empty=1, n=(middle_limbName + '_00_pad') )
	temp_constraint = pm.parentConstraint( middle_jointHierarchy[0], pad, mo=0 )
	pm.delete( temp_constraint )

	pm.parent( middle_jointHierarchy[0], middle_jointHierarchy[0] + '_fk', middle_jointHierarchy[0] + '_ik', pad )

	# Constrain the hand to the fingers
	pm.parentConstraint( hand_root, pad, mo=1 )

	# Change vis for ikfk joints
	pm.select( middle_jointHierarchy[0] + '_ik', middle_jointHierarchy[0] + '_fk' )
	joints = pm.ls( sl=1 )

	for each in joints:
		each.v.set(0)

	pm.select( cl=1 )

def ringSetup(*args):

	# First define what joint chains we need 
	newJointList = ['_ik', '_fk']

	# Build the joints
	for newJoint in newJointList:
		for i in range( ring_limbJoints ):
			newJointName = ring_jointHierarchy[i] + newJoint
			# print( newJointName )
			pm.joint( n=newJointName )	
			temp_constraint = pm.parentConstraint( ring_jointHierarchy[i], newJointName, mo=0 )
			pm.delete( temp_constraint )
			pm.makeIdentity( newJointName, a=1, t=0, r=1, s=0 )

		pm.select( cl=1 )

	#---------------------------------------------------------------------------------------
	# Setup FK
	#---------------------------------------------------------------------------------------
	# Create the controls
	for i in range( ring_limbJoints ):
		crv = pm.circle( c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=.15, tol=4.54965e-09, nr=(1, 0, 0), n=(ring_jointHierarchy[i] + '_fk_icon') )
		crv = pm.ls(sl=1)[0]
		# print(crv)
		temp_constraint = pm.parentConstraint( ring_jointHierarchy[i], crv, mo=0 )
		pm.delete( temp_constraint )
		pad = pm.group( empty=1, n=(ring_jointHierarchy[i] + '_fk_local') )
		temp_constraint = pm.parentConstraint( ring_jointHierarchy[i], pad, mo=0 )
		pm.delete( temp_constraint )
		pm.parent( crv, pad )
		pm.makeIdentity( crv, a=1, t=1, r=1 )
		pm.delete(crv, ch=1)

		pm.setAttr( (crv + '.overrideEnabled'), 1 )

		if 'lt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 6 )

		if 'rt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 13 )

		# Parent the pads to the icons 
		if i>=1:
			pm.parent( (ring_jointHierarchy[i] + '_fk_local'), (ring_jointHierarchy[i - 1] + '_fk_icon') )
		
		# Constrain the icon and the joints
		pm.parentConstraint( (ring_jointHierarchy[i] + '_fk_icon'), (ring_jointHierarchy[i] + '_fk'), mo=1 )

	

	# Delete the last fk pad and icon
	pm.delete((ring_jointHierarchy[-1] + '_fk_local'))

 
	# Connect the ik and fk to the bind joints
	for i in range( ring_limbJoints ):
		# Constrain the fk and the bind joints
		pm.parentConstraint( (ring_jointHierarchy[i] + '_ik'), (ring_jointHierarchy[i] + '_fk'), (ring_jointHierarchy[i]), mo=1 )

	# Pad the joints
	pad = pm.group( empty=1, n=(ring_limbName + '_00_pad') )
	temp_constraint = pm.parentConstraint( ring_jointHierarchy[0], pad, mo=0 )
	pm.delete( temp_constraint )

	pm.parent( ring_jointHierarchy[0], ring_jointHierarchy[0] + '_fk', ring_jointHierarchy[0] + '_ik', pad )

	# Constrain the hand to the fingers
	pm.parentConstraint( hand_root, pad, mo=1 )

	# Change vis for ikfk joints
	pm.select( ring_jointHierarchy[0] + '_ik', ring_jointHierarchy[0] + '_fk' )
	joints = pm.ls( sl=1 )

	for each in joints:
		each.v.set(0)

	pm.select( cl=1 )

def pinkySetup(*args):

	# First define what joint chains we need 
	newJointList = ['_ik', '_fk']

	# Build the joints
	for newJoint in newJointList:
		for i in range( pinky_limbJoints ):
			newJointName = pinky_jointHierarchy[i] + newJoint
			# print( newJointName )
			pm.joint( n=newJointName )	
			temp_constraint = pm.parentConstraint( pinky_jointHierarchy[i], newJointName, mo=0 )
			pm.delete( temp_constraint )
			pm.makeIdentity( newJointName, a=1, t=0, r=1, s=0 )

		pm.select( cl=1 )

	#---------------------------------------------------------------------------------------
	# Setup FK
	#---------------------------------------------------------------------------------------
	# Create the controls
	for i in range( pinky_limbJoints ):
		crv = pm.circle( c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=.15, tol=4.54965e-09, nr=(1, 0, 0), n=(pinky_jointHierarchy[i] + '_fk_icon') )
		crv = pm.ls(sl=1)[0]
		# print(crv)
		temp_constraint = pm.parentConstraint( pinky_jointHierarchy[i], crv, mo=0 )
		pm.delete( temp_constraint )
		pad = pm.group( empty=1, n=(pinky_jointHierarchy[i] + '_fk_local') )
		temp_constraint = pm.parentConstraint( pinky_jointHierarchy[i], pad, mo=0 )
		pm.delete( temp_constraint )
		pm.parent( crv, pad )
		pm.makeIdentity( crv, a=1, t=1, r=1 )
		pm.delete(crv, ch=1)

		pm.setAttr( (crv + '.overrideEnabled'), 1 )

		if 'lt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 6 )

		if 'rt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 13 )

		# Parent the pads to the icons 
		if i>=1:
			pm.parent( (pinky_jointHierarchy[i] + '_fk_local'), (pinky_jointHierarchy[i - 1] + '_fk_icon') )
		
		# Constrain the icon and the joints
		pm.parentConstraint( (pinky_jointHierarchy[i] + '_fk_icon'), (pinky_jointHierarchy[i] + '_fk'), mo=1 )

		


	# Delete the last fk pad and icon
	pm.delete((pinky_jointHierarchy[-1] + '_fk_local'))

 
	# Connect the ik and fk to the bind joints
	for i in range( pinky_limbJoints ):
		# Constrain the fk and the bind joints
		pm.parentConstraint( (pinky_jointHierarchy[i] + '_ik'), (pinky_jointHierarchy[i] + '_fk'), (pinky_jointHierarchy[i]), mo=1 )

	# Pad the joints
	pad = pm.group( empty=1, n=(pinky_limbName + '_00_pad') )
	temp_constraint = pm.parentConstraint( pinky_jointHierarchy[0], pad, mo=0 )
	pm.delete( temp_constraint )

	pm.parent( pinky_jointHierarchy[0], pinky_jointHierarchy[0] + '_fk', pinky_jointHierarchy[0] + '_ik', pad )

	# Constrain the hand to the fingers
	pm.parentConstraint( hand_root, pad, mo=1 )

	# Change vis for ikfk joints
	pm.select( pinky_jointHierarchy[0] + '_ik', pinky_jointHierarchy[0] + '_fk' )
	joints = pm.ls( sl=1 )

	for each in joints:
		each.v.set(0)

	pm.select( cl=1 )

def thumbSetup(*args):

	# First define what joint chains we need 
	newJointList = ['_ik', '_fk']

	# Build the joints
	for newJoint in newJointList:
		for i in range( thumb_limbJoints ):
			newJointName = thumb_jointHierarchy[i] + newJoint
			# print( newJointName )
			pm.joint( n=newJointName )	
			temp_constraint = pm.parentConstraint( thumb_jointHierarchy[i], newJointName, mo=0 )
			pm.delete( temp_constraint )
			pm.makeIdentity( newJointName, a=1, t=0, r=1, s=0 )

		pm.select( cl=1 )

	#---------------------------------------------------------------------------------------
	# Setup FK
	#---------------------------------------------------------------------------------------
	# Create the controls
	for i in range( thumb_limbJoints ):
		crv = pm.circle( c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=.15, tol=4.54965e-09, nr=(1, 0, 0), n=(thumb_jointHierarchy[i] + '_fk_icon') )
		crv = pm.ls(sl=1)[0]
		# print(crv)
		temp_constraint = pm.parentConstraint( thumb_jointHierarchy[i], crv, mo=0 )
		pm.delete( temp_constraint )
		pad = pm.group( empty=1, n=(thumb_jointHierarchy[i] + '_fk_local') )
		temp_constraint = pm.parentConstraint( thumb_jointHierarchy[i], pad, mo=0 )
		pm.delete( temp_constraint )
		pm.parent( crv, pad )
		pm.makeIdentity( crv, a=1, t=1, r=1 )
		pm.delete(crv, ch=1)

		pm.setAttr( (crv + '.overrideEnabled'), 1 )

		if 'lt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 6 )

		if 'rt_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 13 )

		# Parent the pads to the icons 
		if i>=1:
			pm.parent( (thumb_jointHierarchy[i] + '_fk_local'), (thumb_jointHierarchy[i - 1] + '_fk_icon') )
		
		# Constrain the icon and the joints
		pm.parentConstraint( (thumb_jointHierarchy[i] + '_fk_icon'), (thumb_jointHierarchy[i] + '_fk'), mo=1 )

		


	# Delete the last fk pad and icon
	pm.delete((thumb_jointHierarchy[-1] + '_fk_local'))

 
	# Connect the ik and fk to the bind joints
	for i in range( thumb_limbJoints ):
		# Constrain the fk and the bind joints
		pm.parentConstraint( (thumb_jointHierarchy[i] + '_ik'), (thumb_jointHierarchy[i] + '_fk'), (thumb_jointHierarchy[i]), mo=1 )

	# Pad the joints
	pad = pm.group( empty=1, n=(thumb_limbName + '_00_pad') )
	temp_constraint = pm.parentConstraint( thumb_jointHierarchy[0], pad, mo=0 )
	pm.delete( temp_constraint )

	pm.parent( thumb_jointHierarchy[0], thumb_jointHierarchy[0] + '_fk', thumb_jointHierarchy[0] + '_ik', pad )

	# Constrain the hand to the fingers
	pm.parentConstraint( hand_root, pad, mo=1 )

	# Change vis for ikfk joints
	pm.select( thumb_jointHierarchy[0] + '_ik', thumb_jointHierarchy[0] + '_fk' )
	joints = pm.ls( sl=1 )

	for each in joints:
		each.v.set(0)

	pm.select( cl=1 )

def parentIcon_setup(*args):
	global parent_icon, index_icon, middle_icon, ring_icon, pinky_icon
	
	# Create the finger parent icon
	parent_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=16, r=1, tol=0.01, nr=(1, 0, 0), n=(whichSide + 'finger_icon'))[0]

	pm.addAttr( parent_icon, ln='fk', at='bool', dv=0 )
	pm.setAttr( parent_icon + '.fk', e=1, keyable=1 )

	# Shape the parent icon
	pm.select(parent_icon + '.cv[0]', parent_icon + '.cv[1]', parent_icon + '.cv[9]', parent_icon + '.cv[10]', parent_icon + '.cv[11]', parent_icon + '.cv[12]', parent_icon + '.cv[13]', parent_icon + '.cv[14]', parent_icon + '.cv[15]')            
	first_cv_set = pm.ls(sl=1)
	cmds.move(0, 0, -2, r=1, os=1, wd=1)

	pm.select(parent_icon + '.cv[0]', parent_icon + '.cv[10]', parent_icon + '.cv[11]', parent_icon + '.cv[12]', parent_icon + '.cv[13]', parent_icon + '.cv[14]', parent_icon + '.cv[15]')            
	second_cv_set = pm.ls(sl=1)
	cmds.move(0, 0, -4, r=1, os=1, wd=1)
	pm.select(parent_icon)
	deleteHistory()

	if selection_len == 5:
		# Create finger icons
		index_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0), n=(index_iconName))[0]
		index_icon.sy.set(.6)
		index_icon.sz.set(.6)
		freezeTransform()
		deleteHistory()

		middle_icon = pm.duplicate(index_icon, n=(middle_iconName))[0]
		middle_icon.tz.set(-2)
		freezeTransform()

		ring_icon = pm.duplicate(index_icon, n=(ring_iconName))[0]
		ring_icon.tz.set(-4)
		freezeTransform()

		pinky_icon = pm.duplicate(index_icon, n=(pinky_iconName))[0]
		pinky_icon.tz.set(-6)
		freezeTransform()

		# Parent the finger icons under the parent icon
		pm.parent( index_icon, middle_icon, ring_icon, pinky_icon, parent_icon )

		pm.select( index_icon, middle_icon, ring_icon, pinky_icon )
		selection = pm.ls( sl=1 )

		for each in selection:
			pm.addAttr( each, ln='fk', at='bool', dv=0 )
			pm.setAttr( each + '.fk', e=1, keyable=1 )

		#---------------------------------------------------------------------------------------
		# Fk blending
		#---------------------------------------------------------------------------------------
		index_rev = pm.shadingNode( 'reverse', asUtility=1, n=(index_limbName + '_rev') )
		pm.connectAttr( (index_icon + '.fk'), (index_rev + '.inputX'), f=1 )

		for i in range( index_limbJoints ):
			getConstraint = pm.listConnections(index_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (index_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( index_rev + '.outputX', (getWeights[0]), f=1)
	
		index_icon.fk.set(0)
		pm.setAttr( index_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( index_jointHierarchy[0] + '_fk_local.v', currentDriver=index_icon + '.fk' )

		index_icon.fk.set(1)
		pm.setAttr( index_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( index_jointHierarchy[0] + '_fk_local.v', currentDriver=index_icon + '.fk' )
		

		middle_rev = pm.shadingNode( 'reverse', asUtility=1, n=(middle_limbName + '_rev') )
		pm.connectAttr( (middle_icon + '.fk'), (middle_rev + '.inputX'), f=1 )

		for i in range( middle_limbJoints ):
			getConstraint = pm.listConnections(middle_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (middle_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( middle_rev + '.outputX', (getWeights[0]), f=1)

		middle_icon.fk.set(0)
		pm.setAttr( middle_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( middle_jointHierarchy[0] + '_fk_local.v', currentDriver=middle_icon + '.fk' )

		middle_icon.fk.set(1)
		pm.setAttr( middle_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( middle_jointHierarchy[0] + '_fk_local.v', currentDriver=middle_icon + '.fk' )
		
		ring_rev = pm.shadingNode( 'reverse', asUtility=1, n=(ring_limbName + '_rev') )
		pm.connectAttr( (ring_icon + '.fk'), (ring_rev + '.inputX'), f=1 )



		for i in range( ring_limbJoints ):
			getConstraint = pm.listConnections(ring_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (ring_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( ring_rev + '.outputX', (getWeights[0]), f=1)
	
		ring_icon.fk.set(0)
		pm.setAttr( ring_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( ring_jointHierarchy[0] + '_fk_local.v', currentDriver=ring_icon + '.fk' )

		ring_icon.fk.set(1)
		pm.setAttr( ring_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( ring_jointHierarchy[0] + '_fk_local.v', currentDriver=ring_icon + '.fk' )
		

		pinky_rev = pm.shadingNode( 'reverse', asUtility=1, n=(pinky_limbName + '_rev') )
		pm.connectAttr( (pinky_icon + '.fk'), (pinky_rev + '.inputX'), f=1 )

		for i in range( pinky_limbJoints ):
			getConstraint = pm.listConnections(pinky_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (pinky_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( pinky_rev + '.outputX', (getWeights[0]), f=1)

		pinky_icon.fk.set(0)
		pm.setAttr( pinky_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( pinky_jointHierarchy[0] + '_fk_local.v', currentDriver=pinky_icon + '.fk' )

		pinky_icon.fk.set(1)
		pm.setAttr( pinky_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( pinky_jointHierarchy[0] + '_fk_local.v', currentDriver=pinky_icon + '.fk' )
		

		thumb_rev = pm.shadingNode( 'reverse', asUtility=1, n=(thumb_limbName + '_rev') )
		pm.connectAttr( (parent_icon + '.fk'), (thumb_rev + '.inputX'), f=1 )

		for i in range( thumb_limbJoints ):
			getConstraint = pm.listConnections(thumb_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (parent_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( thumb_rev + '.outputX', (getWeights[0]), f=1)
		
		parent_icon.fk.set(0)
		pm.setAttr( thumb_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( thumb_jointHierarchy[0] + '_fk_local.v', currentDriver=parent_icon + '.fk' )

		parent_icon.fk.set(1)
		pm.setAttr( thumb_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( thumb_jointHierarchy[0] + '_fk_local.v', currentDriver=parent_icon + '.fk' )

	if selection_len == 4:
		# Create finger icons
		index_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0), n=(index_iconName))[0]
		index_icon.sy.set(.6)
		index_icon.sz.set(.6)
		freezeTransform()
		deleteHistory()

		middle_icon = pm.duplicate(index_icon, n=(middle_iconName))[0]
		middle_icon.tz.set(-3)
		freezeTransform()

		pinky_icon = pm.duplicate(index_icon, n=(pinky_iconName))[0]
		pinky_icon.tz.set(-6)
		freezeTransform()

		# Parent the finger icons under the parent icon
		pm.parent( index_icon, middle_icon, pinky_icon, parent_icon )

		pm.select( index_icon, middle_icon, pinky_icon )
		selection = pm.ls( sl=1 )

		for each in selection:
			pm.addAttr( each, ln='fk', at='bool', dv=0 )
			pm.setAttr( each + '.fk', e=1, keyable=1 )

		#---------------------------------------------------------------------------------------
		# Fk blending
		#---------------------------------------------------------------------------------------
		index_rev = pm.shadingNode( 'reverse', asUtility=1, n=(index_limbName + '_rev') )
		pm.connectAttr( (index_icon + '.fk'), (index_rev + '.inputX'), f=1 )

		for i in range( index_limbJoints ):
			getConstraint = pm.listConnections(index_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (index_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( index_rev + '.outputX', (getWeights[0]), f=1)
	
		index_icon.fk.set(0)
		pm.setAttr( index_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( index_jointHierarchy[0] + '_fk_local.v', currentDriver=index_icon + '.fk' )

		index_icon.fk.set(1)
		pm.setAttr( index_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( index_jointHierarchy[0] + '_fk_local.v', currentDriver=index_icon + '.fk' )
		

		middle_rev = pm.shadingNode( 'reverse', asUtility=1, n=(middle_limbName + '_rev') )
		pm.connectAttr( (middle_icon + '.fk'), (middle_rev + '.inputX'), f=1 )

		for i in range( middle_limbJoints ):
			getConstraint = pm.listConnections(middle_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (middle_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( middle_rev + '.outputX', (getWeights[0]), f=1)

		middle_icon.fk.set(0)
		pm.setAttr( middle_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( middle_jointHierarchy[0] + '_fk_local.v', currentDriver=middle_icon + '.fk' )

		middle_icon.fk.set(1)
		pm.setAttr( middle_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( middle_jointHierarchy[0] + '_fk_local.v', currentDriver=middle_icon + '.fk' )
		

		pinky_rev = pm.shadingNode( 'reverse', asUtility=1, n=(pinky_limbName + '_rev') )
		pm.connectAttr( (pinky_icon + '.fk'), (pinky_rev + '.inputX'), f=1 )

		for i in range( pinky_limbJoints ):
			getConstraint = pm.listConnections(pinky_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (pinky_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( pinky_rev + '.outputX', (getWeights[0]), f=1)

		pinky_icon.fk.set(0)
		pm.setAttr( pinky_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( pinky_jointHierarchy[0] + '_fk_local.v', currentDriver=pinky_icon + '.fk' )

		pinky_icon.fk.set(1)
		pm.setAttr( pinky_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( pinky_jointHierarchy[0] + '_fk_local.v', currentDriver=pinky_icon + '.fk' )
		

		thumb_rev = pm.shadingNode( 'reverse', asUtility=1, n=(thumb_limbName + '_rev') )
		pm.connectAttr( (parent_icon + '.fk'), (thumb_rev + '.inputX'), f=1 )

		for i in range( thumb_limbJoints ):
			getConstraint = pm.listConnections(thumb_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (parent_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( thumb_rev + '.outputX', (getWeights[0]), f=1)
		
		parent_icon.fk.set(0)
		pm.setAttr( thumb_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( thumb_jointHierarchy[0] + '_fk_local.v', currentDriver=parent_icon + '.fk' )

		parent_icon.fk.set(1)
		pm.setAttr( thumb_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( thumb_jointHierarchy[0] + '_fk_local.v', currentDriver=parent_icon + '.fk' )
	
	if selection_len == 3:
		# Create finger icons
		index_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0), n=(index_iconName))[0]
		index_icon.sy.set(.6)
		index_icon.sz.set(.6)
		freezeTransform()
		deleteHistory()

		pinky_icon = pm.duplicate(index_icon, n=(pinky_iconName))[0]
		pinky_icon.tz.set(-6)
		freezeTransform()

		# Parent the finger icons under the parent icon
		pm.parent( index_icon, pinky_icon, parent_icon )

		pm.select( index_icon, pinky_icon )
		selection = pm.ls( sl=1 )

		for each in selection:
			pm.addAttr( each, ln='fk', at='bool', dv=0 )
			pm.setAttr( each + '.fk', e=1, keyable=1 )

		#---------------------------------------------------------------------------------------
		# Fk blending
		#---------------------------------------------------------------------------------------
		index_rev = pm.shadingNode( 'reverse', asUtility=1, n=(index_limbName + '_rev') )
		pm.connectAttr( (index_icon + '.fk'), (index_rev + '.inputX'), f=1 )

		for i in range( index_limbJoints ):
			getConstraint = pm.listConnections(index_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (index_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( index_rev + '.outputX', (getWeights[0]), f=1)
	
		index_icon.fk.set(0)
		pm.setAttr( index_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( index_jointHierarchy[0] + '_fk_local.v', currentDriver=index_icon + '.fk' )

		index_icon.fk.set(1)
		pm.setAttr( index_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( index_jointHierarchy[0] + '_fk_local.v', currentDriver=index_icon + '.fk' )
		

		pinky_rev = pm.shadingNode( 'reverse', asUtility=1, n=(pinky_limbName + '_rev') )
		pm.connectAttr( (pinky_icon + '.fk'), (pinky_rev + '.inputX'), f=1 )

		for i in range( pinky_limbJoints ):
			getConstraint = pm.listConnections(pinky_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (pinky_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( pinky_rev + '.outputX', (getWeights[0]), f=1)

		pinky_icon.fk.set(0)
		pm.setAttr( pinky_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( pinky_jointHierarchy[0] + '_fk_local.v', currentDriver=pinky_icon + '.fk' )

		pinky_icon.fk.set(1)
		pm.setAttr( pinky_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( pinky_jointHierarchy[0] + '_fk_local.v', currentDriver=pinky_icon + '.fk' )
		

		thumb_rev = pm.shadingNode( 'reverse', asUtility=1, n=(thumb_limbName + '_rev') )
		pm.connectAttr( (parent_icon + '.fk'), (thumb_rev + '.inputX'), f=1 )

		for i in range( thumb_limbJoints ):
			getConstraint = pm.listConnections(thumb_jointHierarchy[i], t='parentConstraint')[0]
			getWeights = pm.parentConstraint( getConstraint, q=1, wal=1 )
			# print(getConstraint)
			# print(getWeights)
			pm.connectAttr( (parent_icon + '.fk'), (getWeights[1]), f=1)
			pm.connectAttr( thumb_rev + '.outputX', (getWeights[0]), f=1)
		
		parent_icon.fk.set(0)
		pm.setAttr( thumb_jointHierarchy[0] + '_fk_local.v', 0 )
		pm.setDrivenKeyframe( thumb_jointHierarchy[0] + '_fk_local.v', currentDriver=parent_icon + '.fk' )

		parent_icon.fk.set(1)
		pm.setAttr( thumb_jointHierarchy[0] + '_fk_local.v', 1 )
		pm.setDrivenKeyframe( thumb_jointHierarchy[0] + '_fk_local.v', currentDriver=parent_icon + '.fk' )

	pm.select( parent_icon )
	centerPivot()

	temp_constraint = pm.parentConstraint( hand_root, parent_icon, mo=0 )
	pm.delete( temp_constraint )
	freezeTransform()
	
	# parent_icon.ty.set(4)
	# freezeTransform()

	parent_icon.sx.set( 0.07 )
	parent_icon.sy.set( 0.07 )
	parent_icon.sz.set( 0.07 )

	if selection_len == 5:
		pm.select(index_icon, middle_icon, ring_icon, pinky_icon)
		icon_selection = pm.ls(sl=1)
		for each in icon_selection:
			pm.addAttr( each, ln='fingerCtrl', at='enum', en='-------' )
			pm.setAttr( each + '.fingerCtrl', lock=1, e=1, keyable=1 )

			pm.addAttr( each, ln='curl', max=10, dv=0, at='double', min=-10 )
			unlock_and_unhide( each, ['curl'] )

			pm.addAttr( each, ln='relax', max=10, dv=0, at='double', min=0 )
			unlock_and_unhide( each, ['relax'] )

			pm.addAttr( each, ln='scrunch', dv=0, max=10, min=-10, at='double' )
			unlock_and_unhide( each , ['scrunch'] )

			pm.addAttr( each, ln='spread', dv=0, max=10, min=-10, at='double' )
			unlock_and_unhide( each, ['spread'] )

	if selection_len == 4:
		pm.select(index_icon, middle_icon, pinky_icon)
		icon_selection = pm.ls(sl=1)
		for each in icon_selection:
			pm.addAttr( each, ln='fingerCtrl', at='enum', en='-------' )
			pm.setAttr( each + '.fingerCtrl', lock=1, e=1, keyable=1 )

			pm.addAttr( each, ln='curl', max=10, dv=0, at='double', min=-10 )
			unlock_and_unhide( each, ['curl'] )

			pm.addAttr( each, ln='relax', max=10, dv=0, at='double', min=0 )
			unlock_and_unhide( each, ['relax'] )

			pm.addAttr( each, ln='scrunch', dv=0, max=10, min=-10, at='double' )
			unlock_and_unhide( each , ['scrunch'] )

			pm.addAttr( each, ln='spread', dv=0, max=10, min=-10, at='double' )
			unlock_and_unhide( each, ['spread'] )

	if selection_len == 3:
		pm.select(index_icon, pinky_icon)
		icon_selection = pm.ls(sl=1)
		for each in icon_selection:
			pm.addAttr( each, ln='fingerCtrl', at='enum', en='-------' )
			pm.setAttr( each + '.fingerCtrl', lock=1, e=1, keyable=1 )

			pm.addAttr( each, ln='curl', max=10, dv=0, at='double', min=-10 )
			unlock_and_unhide( each, ['curl'] )

			pm.addAttr( each, ln='relax', max=10, dv=0, at='double', min=0 )
			unlock_and_unhide( each, ['relax'] )

			pm.addAttr( each, ln='scrunch', dv=0, max=10, min=-10, at='double' )
			unlock_and_unhide( each , ['scrunch'] )

			pm.addAttr( each, ln='spread', dv=0, max=10, min=-10, at='double' )
			unlock_and_unhide( each, ['spread'] )

	# Parent icon attrs


	pm.addAttr(parent_icon, ln='fingerCtrls',  at='enum', en ='-------')
	parent_icon.fingerCtrls.set(lock=1, e=1, keyable=1)

	pm.addAttr(parent_icon, ln='fist', at='double', max=10, min=0, dv=0)
	unlock_and_unhide(parent_icon, ['fist'])

	pm.addAttr(parent_icon, ln='relax', at='double', max=10, min=-10, dv=0)
	unlock_and_unhide(parent_icon, ['relax'])

	pm.addAttr(parent_icon, ln='scrunch', at='double', max=10, min=-10, dv=0)
	unlock_and_unhide(parent_icon, ['scrunch'])

	pm.addAttr(parent_icon, ln='spread', at='double', max=10, min=-10, dv=0)
	unlock_and_unhide(parent_icon, ['spread'])

	pm.addAttr(parent_icon, ln='thumbCtrls',  at='enum', en ='-------')
	parent_icon.thumbCtrls.set(lock=1, e=1, keyable=1)

	lockAttrs(parent_icon, ['thumbCtrls'])

	pm.addAttr(parent_icon, ln='curl', at='double', max=10, min=-10, dv=0)
	unlock_and_unhide(parent_icon, ['curl'])

	pm.addAttr(parent_icon, ln='drop', at='double', min=0, max=10, dv=0)
	unlock_and_unhide(parent_icon, ['drop'])

	pm.addAttr(parent_icon, ln='thumbRelax', nn='Relax', at='double', max=10, min=0, dv=0)
	unlock_and_unhide(parent_icon, ['thumbRelax'])

	pm.addAttr(parent_icon, ln='thumbSpread', nn='Spread', at='double', max=10, min=-10, dv=0)
	unlock_and_unhide(parent_icon, ['thumbSpread'])

	pm.parent( parent_icon, hand_icon )
	freezeTransform( hand_icon )

	color_index = 27

	for each in icon_selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideColor', color_index)
		color_index = color_index + 1

	if 'lt_' in whichSide:
		parent_icon.overrideEnabled.set(1)
		parent_icon.overrideColor.set(6)

	if 'rt_' in whichSide:
		parent_icon.overrideEnabled.set(1)
		parent_icon.overrideColor.set(13)

def indexSDK(*args):
	# Curl
	index_drivenAttr_curl = [index_jointHierarchy[0] + '_ik' + '.rz', index_jointHierarchy[1] + '_ik' + '.rz', index_jointHierarchy[2] + '_ik' + '.rz', index_jointHierarchy[3] + '_ik' + '.rz']
	index_driver_curl = (index_icon + '.curl')
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)

	# print "Driven:", index_driven
	index_driven_curl= [index_jointHierarchy[0] + '_ik', index_jointHierarchy[1] + '_ik', index_jointHierarchy[2] + '_ik', index_jointHierarchy[3] + '_ik']
	index_icon.curl.set(10)
	pm.xform(index_driven_curl, ro=(0, 0, -90))
	pm.setAttr(index_jointHierarchy[0] + '_ik.rz', -15)
	pm.setAttr(index_jointHierarchy[2] + '_ik.rz', -75)
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)
	index_icon.curl.set(-10)
	pm.xform(index_driven_curl, ro=(0, 0, 10))
	pm.setAttr(index_jointHierarchy[1] + '_ik.rz', 20)
	pm.setAttr(index_jointHierarchy[2] + '_ik.rz', 25)
	pm.setAttr(index_jointHierarchy[3] + '_ik.rz', 30)
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)
	index_drivenKeyframes_curl = (index_jointHierarchy[0] + '_ik' + '_rotateZ', index_jointHierarchy[1] + '_ik' + '_rotateZ', index_jointHierarchy[2] + '_ik' + '_rotateZ', index_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.curl.set(0)

	# Scrunch
	index_drivenAttr_scrunch = [index_jointHierarchy[1] + '_ik' + '.rz', index_jointHierarchy[2] + '_ik' + '.rz', index_jointHierarchy[3] + '_ik' + '.rz']
	index_driver_scrunch = (index_icon + '.scrunch')
	pm.setDrivenKeyframe(index_drivenAttr_scrunch, currentDriver=index_driver_scrunch)
	# print "Driven:", index_driven
	index_driven_scrunch= [index_jointHierarchy[1] + '_ik', index_jointHierarchy[2] + '_ik', index_jointHierarchy[3] + '_ik']
	index_icon.scrunch.set(10)
	pm.setAttr( index_jointHierarchy[1] + '_ik.rz', 50)
	pm.setAttr( index_jointHierarchy[2] + '_ik.rz', -110)
	pm.setAttr( index_jointHierarchy[3] + '_ik.rz', 30)
	pm.setDrivenKeyframe(index_drivenAttr_scrunch, currentDriver=index_driver_scrunch)
	index_icon.scrunch.set(-10)
	pm.setAttr( index_jointHierarchy[1] + '_ik.rz', 3)
	pm.setAttr( index_jointHierarchy[2] + '_ik.rz', 4)
	pm.setAttr( index_jointHierarchy[3] + '_ik.rz', 10)
	pm.setDrivenKeyframe(index_drivenAttr_scrunch, currentDriver=index_driver_scrunch)
	index_drivenKeyframes_scrunch = (index_jointHierarchy[0] + '_ik' + '_rotateZ', index_jointHierarchy[1] + '_ik' + '_rotateZ', index_jointHierarchy[2] + '_ik' + '_rotateZ', index_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_scrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.scrunch.set(0)

	# Spread
	index_drivenAttr_spread = (index_jointHierarchy[0] + '_ik' + '.ry', index_jointHierarchy[1] + '_ik' + '.ry')
	index_driven_spread= (index_jointHierarchy[0] + '_ik', index_jointHierarchy[1] + '_ik')
	index_driver_spread = (index_icon + '.spread')
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(10)
	pm.xform(index_driven_spread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(-10)
	pm.xform(index_driven_spread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(0)

	index_drivenKeyframes_spread = (index_jointHierarchy[0] + '_ik' + '_rotateY', index_jointHierarchy[1] + '_ik' + '_rotateY')
	pm.keyTangent(index_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Relax
	index_drivenAttr_relax = [index_jointHierarchy[0] + '_ik' + '.rz', index_jointHierarchy[1] + '_ik' + '.rz', index_jointHierarchy[2] + '_ik' + '.rz', index_jointHierarchy[3] + '_ik' + '.rz']
	index_driven_relax = [index_jointHierarchy[0] + '_ik', index_jointHierarchy[1] + '_ik', index_jointHierarchy[2] + '_ik', index_jointHierarchy[3] + '_ik']
	index_driver_relax = (index_icon + '.relax')
	pm.setDrivenKeyframe(index_drivenAttr_relax, currentDriver=index_driver_relax)
	index_icon.relax.set(10)
	pm.setAttr( index_jointHierarchy[0] + '_ik.rz', -12 )
	pm.setAttr( index_jointHierarchy[1] + '_ik.rz', -15 )
	pm.setAttr( index_jointHierarchy[2] + '_ik.rz', -18 )
	pm.setAttr( index_jointHierarchy[3] + '_ik.rz', -21 )
	pm.setDrivenKeyframe(index_drivenAttr_relax, currentDriver=index_driver_relax)
	index_icon.relax.set(0)

	pm.keyTangent(index_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Fist
	index_drivenAttr_fist = [index_jointHierarchy[0] + '_ik' + '.rz', index_jointHierarchy[1] + '_ik' + '.rz', index_jointHierarchy[2] + '_ik' + '.rz', index_jointHierarchy[3] + '_ik' + '.rz']
	index_driver_fist = (parent_icon + '.fist')
	index_driven_fist= [index_jointHierarchy[0] + '_ik', index_jointHierarchy[1] + '_ik', index_jointHierarchy[2] + '_ik', index_jointHierarchy[3] + '_ik']
	pm.setDrivenKeyframe(index_drivenAttr_fist, currentDriver=index_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(index_driven_fist, ro=(0, 0, -90))
	pm.setAttr( index_jointHierarchy[0] + '_ik.rz', -15 )
	pm.setAttr( index_jointHierarchy[2] + '_ik.rz', -75 )
	pm.setAttr( index_jointHierarchy[3] + '_ik.rz', -25 )
	pm.setDrivenKeyframe(index_drivenAttr_fist, currentDriver=index_driver_fist)
	parent_icon.fist.set(0)

	# Scrunch
	index_drivenAttr_allScrunch = [index_jointHierarchy[1] + '_ik' + '.rz', index_jointHierarchy[2] + '_ik' + '.rz', index_jointHierarchy[3] + '_ik' + '.rz']
	index_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	# print "Driven:", index_driven
	index_driven_allScrunch= [index_jointHierarchy[1] + '_ik', index_jointHierarchy[2] + '_ik', index_jointHierarchy[3] + '_ik']
	parent_icon.scrunch.set(10)
	pm.setAttr(index_jointHierarchy[1] + '_ik.rz', 50 )
	pm.setAttr(index_jointHierarchy[2] + '_ik.rz', -110 )
	pm.setAttr(index_jointHierarchy[3] + '_ik.rz', 30 )
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	pm.setAttr(index_jointHierarchy[1] + '_ik.rz', 3 )
	pm.setAttr(index_jointHierarchy[2] + '_ik.rz', 4 )
	pm.setAttr(index_jointHierarchy[3] + '_ik.rz', 10 )
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	index_drivenKeyframes_allScrunch = (index_jointHierarchy[0] + '_ik' + '_rotateZ', index_jointHierarchy[1] + '_ik' + '_rotateZ', index_jointHierarchy[2] + '_ik' + '_rotateZ', index_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	# allSpread
	index_drivenAttr_allSpread = (index_jointHierarchy[0] + '_ik' + '.ry', index_jointHierarchy[1] + '_ik' + '.ry')
	index_driven_allSpread= (index_jointHierarchy[0] + '_ik', index_jointHierarchy[1] + '_ik')
	index_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(index_driven_allSpread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(index_driven_allSpread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(0)

	index_drivenKeyframes_allSpread = (index_jointHierarchy[0] + '_ik' + '_rotateY', index_jointHierarchy[1] + '_ik' + '_rotateY')
	pm.keyTangent(index_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	# allRelax
	index_drivenAttr_allRelax = [index_jointHierarchy[0] + '_ik' + '.rz', index_jointHierarchy[1] + '_ik' + '.rz', index_jointHierarchy[2] + '_ik' + '.rz', index_jointHierarchy[3] + '_ik' + '.rz']
	index_driven_allRelax = [index_jointHierarchy[0] + '_ik', index_jointHierarchy[1] + '_ik', index_jointHierarchy[2] + '_ik', index_jointHierarchy[3] + '_ik']
	index_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(10)
	pm.setAttr(index_jointHierarchy[0] + '_ik.rz', -3 )
	pm.setAttr(index_jointHierarchy[1] + '_ik.rz', -3.75 )
	pm.setAttr(index_jointHierarchy[2] + '_ik.rz', -4.5 )
	pm.setAttr(index_jointHierarchy[3] + '_ik.rz', -8.4 )
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(-10)
	pm.setAttr(index_jointHierarchy[0] + '_ik.rz', -12 )
	pm.setAttr(index_jointHierarchy[1] + '_ik.rz', -15 )
	pm.setAttr(index_jointHierarchy[2] + '_ik.rz', -18 )
	pm.setAttr(index_jointHierarchy[3] + '_ik.rz', -21 )
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(index_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

def middleSDK(*args):
	# Curl
	middle_drivenAttr_curl = [middle_jointHierarchy[0] + '_ik' + '.rz', middle_jointHierarchy[1] + '_ik' + '.rz', middle_jointHierarchy[2] + '_ik' + '.rz', middle_jointHierarchy[3] + '_ik' + '.rz']
	middle_driver_curl = (middle_icon + '.curl')
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)

	# print "Driven:", middle_driven
	middle_driven_curl= [middle_jointHierarchy[0] + '_ik', middle_jointHierarchy[1] + '_ik', middle_jointHierarchy[2] + '_ik', middle_jointHierarchy[3] + '_ik']
	middle_icon.curl.set(10)
	pm.xform(middle_driven_curl, ro=(0, 0, -90))
	pm.setAttr(middle_jointHierarchy[0] + '_ik.rz', -15)
	pm.setAttr(middle_jointHierarchy[2] + '_ik.rz', -75)
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)
	middle_icon.curl.set(-10)
	pm.xform(middle_driven_curl, ro=(0, 0, 10))
	pm.setAttr(middle_jointHierarchy[1] + '_ik.rz', 20)
	pm.setAttr(middle_jointHierarchy[2] + '_ik.rz', 25)
	pm.setAttr(middle_jointHierarchy[3] + '_ik.rz', 30)
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)
	middle_drivenKeyframes_curl = (middle_jointHierarchy[0] + '_ik' + '_rotateZ', middle_jointHierarchy[1] + '_ik' + '_rotateZ', middle_jointHierarchy[2] + '_ik' + '_rotateZ', middle_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	middle_icon.curl.set(0)

	# Scrunch
	middle_drivenAttr_scrunch = [middle_jointHierarchy[1] + '_ik' + '.rz', middle_jointHierarchy[2] + '_ik' + '.rz', middle_jointHierarchy[3] + '_ik' + '.rz']
	middle_driver_scrunch = (middle_icon + '.scrunch')
	pm.setDrivenKeyframe(middle_drivenAttr_scrunch, currentDriver=middle_driver_scrunch)
	# print "Driven:", middle_driven
	middle_driven_scrunch= [middle_jointHierarchy[1] + '_ik', middle_jointHierarchy[2] + '_ik', middle_jointHierarchy[3] + '_ik']
	middle_icon.scrunch.set(10)
	pm.setAttr( middle_jointHierarchy[1] + '_ik.rz', 50)
	pm.setAttr( middle_jointHierarchy[2] + '_ik.rz', -110)
	pm.setAttr( middle_jointHierarchy[3] + '_ik.rz', 30)
	pm.setDrivenKeyframe(middle_drivenAttr_scrunch, currentDriver=middle_driver_scrunch)
	middle_icon.scrunch.set(-10)
	pm.setAttr( middle_jointHierarchy[1] + '_ik.rz', 3)
	pm.setAttr( middle_jointHierarchy[2] + '_ik.rz', 4)
	pm.setAttr( middle_jointHierarchy[3] + '_ik.rz', 10)
	pm.setDrivenKeyframe(middle_drivenAttr_scrunch, currentDriver=middle_driver_scrunch)
	middle_drivenKeyframes_scrunch = (middle_jointHierarchy[0] + '_ik' + '_rotateZ', middle_jointHierarchy[1] + '_ik' + '_rotateZ', middle_jointHierarchy[2] + '_ik' + '_rotateZ', middle_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_scrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	middle_icon.scrunch.set(0)

	# Spread
	middle_drivenAttr_spread = (middle_jointHierarchy[0] + '_ik' + '.ry', middle_jointHierarchy[1] + '_ik' + '.ry')
	middle_driven_spread= (middle_jointHierarchy[0] + '_ik', middle_jointHierarchy[1] + '_ik')
	middle_driver_spread = (middle_icon + '.spread')
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(10)
	pm.xform(middle_driven_spread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(-10)
	pm.xform(middle_driven_spread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(0)

	middle_drivenKeyframes_spread = (middle_jointHierarchy[0] + '_ik' + '_rotateY', middle_jointHierarchy[1] + '_ik' + '_rotateY')
	pm.keyTangent(middle_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Relax
	middle_drivenAttr_relax = [middle_jointHierarchy[0] + '_ik' + '.rz', middle_jointHierarchy[1] + '_ik' + '.rz', middle_jointHierarchy[2] + '_ik' + '.rz', middle_jointHierarchy[3] + '_ik' + '.rz']
	middle_driven_relax = [middle_jointHierarchy[0] + '_ik', middle_jointHierarchy[1] + '_ik', middle_jointHierarchy[2] + '_ik', middle_jointHierarchy[3] + '_ik']
	middle_driver_relax = (middle_icon + '.relax')
	pm.setDrivenKeyframe(middle_drivenAttr_relax, currentDriver=middle_driver_relax)
	middle_icon.relax.set(10)
	pm.setAttr( middle_jointHierarchy[0] + '_ik.rz', -12 )
	pm.setAttr( middle_jointHierarchy[1] + '_ik.rz', -15 )
	pm.setAttr( middle_jointHierarchy[2] + '_ik.rz', -18 )
	pm.setAttr( middle_jointHierarchy[3] + '_ik.rz', -21 )
	pm.setDrivenKeyframe(middle_drivenAttr_relax, currentDriver=middle_driver_relax)
	middle_icon.relax.set(0)

	pm.keyTangent(middle_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Fist
	middle_drivenAttr_fist = [middle_jointHierarchy[0] + '_ik' + '.rz', middle_jointHierarchy[1] + '_ik' + '.rz', middle_jointHierarchy[2] + '_ik' + '.rz', middle_jointHierarchy[3] + '_ik' + '.rz']
	middle_driver_fist = (parent_icon + '.fist')
	middle_driven_fist= [middle_jointHierarchy[0] + '_ik', middle_jointHierarchy[1] + '_ik', middle_jointHierarchy[2] + '_ik', middle_jointHierarchy[3] + '_ik']
	pm.setDrivenKeyframe(middle_drivenAttr_fist, currentDriver=middle_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(middle_driven_fist, ro=(0, 0, -90))
	pm.setAttr( middle_jointHierarchy[0] + '_ik.rz', -15 )
	pm.setAttr( middle_jointHierarchy[2] + '_ik.rz', -75 )
	pm.setAttr( middle_jointHierarchy[3] + '_ik.rz', -25 )
	pm.setDrivenKeyframe(middle_drivenAttr_fist, currentDriver=middle_driver_fist)
	parent_icon.fist.set(0)

	# Scrunch
	middle_drivenAttr_allScrunch = [middle_jointHierarchy[1] + '_ik' + '.rz', middle_jointHierarchy[2] + '_ik' + '.rz', middle_jointHierarchy[3] + '_ik' + '.rz']
	middle_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	# print "Driven:", middle_driven
	middle_driven_allScrunch= [middle_jointHierarchy[1] + '_ik', middle_jointHierarchy[2] + '_ik', middle_jointHierarchy[3] + '_ik']
	parent_icon.scrunch.set(10)
	pm.setAttr(middle_jointHierarchy[1] + '_ik.rz', 50 )
	pm.setAttr(middle_jointHierarchy[2] + '_ik.rz', -110 )
	pm.setAttr(middle_jointHierarchy[3] + '_ik.rz', 30 )
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	pm.setAttr(middle_jointHierarchy[1] + '_ik.rz', 3 )
	pm.setAttr(middle_jointHierarchy[2] + '_ik.rz', 4 )
	pm.setAttr(middle_jointHierarchy[3] + '_ik.rz', 10 )
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	middle_drivenKeyframes_allScrunch = (middle_jointHierarchy[0] + '_ik' + '_rotateZ', middle_jointHierarchy[1] + '_ik' + '_rotateZ', middle_jointHierarchy[2] + '_ik' + '_rotateZ', middle_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	# allSpread
	middle_drivenAttr_allSpread = (middle_jointHierarchy[0] + '_ik' + '.ry', middle_jointHierarchy[1] + '_ik' + '.ry')
	middle_driven_allSpread= (middle_jointHierarchy[0] + '_ik', middle_jointHierarchy[1] + '_ik')
	middle_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(middle_driven_allSpread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(middle_driven_allSpread, ro=(0, 0, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(0)

	middle_drivenKeyframes_allSpread = (middle_jointHierarchy[0] + '_ik' + '_rotateY', middle_jointHierarchy[1] + '_ik' + '_rotateY')
	pm.keyTangent(middle_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	# allRelax
	middle_drivenAttr_allRelax = [middle_jointHierarchy[0] + '_ik' + '.rz', middle_jointHierarchy[1] + '_ik' + '.rz', middle_jointHierarchy[2] + '_ik' + '.rz', middle_jointHierarchy[3] + '_ik' + '.rz']
	middle_driven_allRelax = [middle_jointHierarchy[0] + '_ik', middle_jointHierarchy[1] + '_ik', middle_jointHierarchy[2] + '_ik', middle_jointHierarchy[3] + '_ik']
	middle_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(10)
	pm.setAttr(middle_jointHierarchy[0] + '_ik.rz', -6 )
	pm.setAttr(middle_jointHierarchy[1] + '_ik.rz', -7.5 )
	pm.setAttr(middle_jointHierarchy[2] + '_ik.rz', -9 )
	pm.setAttr(middle_jointHierarchy[3] + '_ik.rz', -12.6 )
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(-10)
	pm.setAttr(middle_jointHierarchy[0] + '_ik.rz', -9 )
	pm.setAttr(middle_jointHierarchy[1] + '_ik.rz', -11.25 )
	pm.setAttr(middle_jointHierarchy[2] + '_ik.rz', -13.5 )
	pm.setAttr(middle_jointHierarchy[3] + '_ik.rz', -16.8 )
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(middle_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

def ringSDK(*args):
	# Curl
	ring_drivenAttr_curl = [ring_jointHierarchy[0] + '_ik' + '.rz', ring_jointHierarchy[1] + '_ik' + '.rz', ring_jointHierarchy[2] + '_ik' + '.rz', ring_jointHierarchy[3] + '_ik' + '.rz']
	ring_driver_curl = (ring_icon + '.curl')
	pm.setDrivenKeyframe(ring_drivenAttr_curl, currentDriver=ring_driver_curl)

	# print "Driven:", ring_driven
	ring_driven_curl= [ring_jointHierarchy[0] + '_ik', ring_jointHierarchy[1] + '_ik', ring_jointHierarchy[2] + '_ik', ring_jointHierarchy[3] + '_ik']
	ring_icon.curl.set(10)
	pm.xform(ring_driven_curl, ro=(0, 0, -90))
	pm.setAttr(ring_jointHierarchy[0] + '_ik.rz', -15)
	pm.setAttr(ring_jointHierarchy[2] + '_ik.rz', -75)
	pm.setDrivenKeyframe(ring_drivenAttr_curl, currentDriver=ring_driver_curl)
	ring_icon.curl.set(-10)
	pm.xform(ring_driven_curl, ro=(0, 0, 10))
	pm.setAttr(ring_jointHierarchy[1] + '_ik.rz', 20)
	pm.setAttr(ring_jointHierarchy[2] + '_ik.rz', 25)
	pm.setAttr(ring_jointHierarchy[3] + '_ik.rz', 30)
	pm.setDrivenKeyframe(ring_drivenAttr_curl, currentDriver=ring_driver_curl)
	ring_drivenKeyframes_curl = (ring_jointHierarchy[0] + '_ik' + '_rotateZ', ring_jointHierarchy[1] + '_ik' + '_rotateZ', ring_jointHierarchy[2] + '_ik' + '_rotateZ', ring_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(ring_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	ring_icon.curl.set(0)

	# Scrunch
	ring_drivenAttr_scrunch = [ring_jointHierarchy[1] + '_ik' + '.rz', ring_jointHierarchy[2] + '_ik' + '.rz', ring_jointHierarchy[3] + '_ik' + '.rz']
	ring_driver_scrunch = (ring_icon + '.scrunch')
	pm.setDrivenKeyframe(ring_drivenAttr_scrunch, currentDriver=ring_driver_scrunch)
	# print "Driven:", ring_driven
	ring_driven_scrunch= [ring_jointHierarchy[1] + '_ik', ring_jointHierarchy[2] + '_ik', ring_jointHierarchy[3] + '_ik']
	ring_icon.scrunch.set(10)
	pm.setAttr( ring_jointHierarchy[1] + '_ik.rz', 50)
	pm.setAttr( ring_jointHierarchy[2] + '_ik.rz', -110)
	pm.setAttr( ring_jointHierarchy[3] + '_ik.rz', 30)
	pm.setDrivenKeyframe(ring_drivenAttr_scrunch, currentDriver=ring_driver_scrunch)
	ring_icon.scrunch.set(-10)
	pm.setAttr( ring_jointHierarchy[1] + '_ik.rz', 3)
	pm.setAttr( ring_jointHierarchy[2] + '_ik.rz', 4)
	pm.setAttr( ring_jointHierarchy[3] + '_ik.rz', 10)
	pm.setDrivenKeyframe(ring_drivenAttr_scrunch, currentDriver=ring_driver_scrunch)
	ring_drivenKeyframes_scrunch = (ring_jointHierarchy[0] + '_ik' + '_rotateZ', ring_jointHierarchy[1] + '_ik' + '_rotateZ', ring_jointHierarchy[2] + '_ik' + '_rotateZ', ring_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(ring_drivenKeyframes_scrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	ring_icon.scrunch.set(0)

	# Spread
	ring_drivenAttr_spread = (ring_jointHierarchy[0] + '_ik' + '.ry', ring_jointHierarchy[1] + '_ik' + '.ry')
	ring_driven_spread= (ring_jointHierarchy[0] + '_ik', ring_jointHierarchy[1] + '_ik')
	ring_driver_spread = (ring_icon + '.spread')
	pm.setDrivenKeyframe(ring_drivenAttr_spread, currentDriver=ring_driver_spread)
	ring_icon.spread.set(10)
	pm.xform(ring_driven_spread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(ring_drivenAttr_spread, currentDriver=ring_driver_spread)
	ring_icon.spread.set(-10)
	pm.xform(ring_driven_spread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(ring_drivenAttr_spread, currentDriver=ring_driver_spread)
	ring_icon.spread.set(0)

	ring_drivenKeyframes_spread = (ring_jointHierarchy[0] + '_ik' + '_rotateY', ring_jointHierarchy[1] + '_ik' + '_rotateY')
	pm.keyTangent(ring_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Relax
	ring_drivenAttr_relax = [ring_jointHierarchy[0] + '_ik' + '.rz', ring_jointHierarchy[1] + '_ik' + '.rz', ring_jointHierarchy[2] + '_ik' + '.rz', ring_jointHierarchy[3] + '_ik' + '.rz']
	ring_driven_relax = [ring_jointHierarchy[0] + '_ik', ring_jointHierarchy[1] + '_ik', ring_jointHierarchy[2] + '_ik', ring_jointHierarchy[3] + '_ik']
	ring_driver_relax = (ring_icon + '.relax')
	pm.setDrivenKeyframe(ring_drivenAttr_relax, currentDriver=ring_driver_relax)
	ring_icon.relax.set(10)
	pm.setAttr( ring_jointHierarchy[0] + '_ik.rz', -12 )
	pm.setAttr( ring_jointHierarchy[1] + '_ik.rz', -15 )
	pm.setAttr( ring_jointHierarchy[2] + '_ik.rz', -18 )
	pm.setAttr( ring_jointHierarchy[3] + '_ik.rz', -21 )
	pm.setDrivenKeyframe(ring_drivenAttr_relax, currentDriver=ring_driver_relax)
	ring_icon.relax.set(0)

	pm.keyTangent(ring_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Fist
	ring_drivenAttr_fist = [ring_jointHierarchy[0] + '_ik' + '.rz', ring_jointHierarchy[1] + '_ik' + '.rz', ring_jointHierarchy[2] + '_ik' + '.rz', ring_jointHierarchy[3] + '_ik' + '.rz']
	ring_driver_fist = (parent_icon + '.fist')
	ring_driven_fist= [ring_jointHierarchy[0] + '_ik', ring_jointHierarchy[1] + '_ik', ring_jointHierarchy[2] + '_ik', ring_jointHierarchy[3] + '_ik']
	pm.setDrivenKeyframe(ring_drivenAttr_fist, currentDriver=ring_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(ring_driven_fist, ro=(0, 0, -90))
	pm.setAttr( ring_jointHierarchy[0] + '_ik.rz', -15 )
	pm.setAttr( ring_jointHierarchy[2] + '_ik.rz', -75 )
	pm.setAttr( ring_jointHierarchy[3] + '_ik.rz', -25 )
	pm.setDrivenKeyframe(ring_drivenAttr_fist, currentDriver=ring_driver_fist)
	parent_icon.fist.set(0)

	# Scrunch
	ring_drivenAttr_allScrunch = [ring_jointHierarchy[1] + '_ik' + '.rz', ring_jointHierarchy[2] + '_ik' + '.rz', ring_jointHierarchy[3] + '_ik' + '.rz']
	ring_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(ring_drivenAttr_allScrunch, currentDriver=ring_driver_allScrunch)
	# print "Driven:", ring_driven
	ring_driven_allScrunch= [ring_jointHierarchy[1] + '_ik', ring_jointHierarchy[2] + '_ik', ring_jointHierarchy[3] + '_ik']
	parent_icon.scrunch.set(10)
	pm.setAttr(ring_jointHierarchy[1] + '_ik.rz', 50 )
	pm.setAttr(ring_jointHierarchy[2] + '_ik.rz', -110 )
	pm.setAttr(ring_jointHierarchy[3] + '_ik.rz', 30 )
	pm.setDrivenKeyframe(ring_drivenAttr_allScrunch, currentDriver=ring_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	pm.setAttr(ring_jointHierarchy[1] + '_ik.rz', 3 )
	pm.setAttr(ring_jointHierarchy[2] + '_ik.rz', 4 )
	pm.setAttr(ring_jointHierarchy[3] + '_ik.rz', 10 )
	pm.setDrivenKeyframe(ring_drivenAttr_allScrunch, currentDriver=ring_driver_allScrunch)
	ring_drivenKeyframes_allScrunch = (ring_jointHierarchy[0] + '_ik' + '_rotateZ', ring_jointHierarchy[1] + '_ik' + '_rotateZ', ring_jointHierarchy[2] + '_ik' + '_rotateZ', ring_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(ring_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	# allSpread
	ring_drivenAttr_allSpread = (ring_jointHierarchy[0] + '_ik' + '.ry', ring_jointHierarchy[1] + '_ik' + '.ry')
	ring_driven_allSpread= (ring_jointHierarchy[0] + '_ik', ring_jointHierarchy[1] + '_ik')
	ring_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(ring_drivenAttr_allSpread, currentDriver=ring_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(ring_driven_allSpread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(ring_drivenAttr_allSpread, currentDriver=ring_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(ring_driven_allSpread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(ring_drivenAttr_allSpread, currentDriver=ring_driver_allSpread)
	parent_icon.spread.set(0)

	ring_drivenKeyframes_allSpread = (ring_jointHierarchy[0] + '_ik' + '_rotateY', ring_jointHierarchy[1] + '_ik' + '_rotateY')
	pm.keyTangent(ring_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# allRelax
	ring_drivenAttr_allRelax = [ring_jointHierarchy[0] + '_ik' + '.rz', ring_jointHierarchy[1] + '_ik' + '.rz', ring_jointHierarchy[2] + '_ik' + '.rz', ring_jointHierarchy[3] + '_ik' + '.rz']
	ring_driven_allRelax = [ring_jointHierarchy[0] + '_ik', ring_jointHierarchy[1] + '_ik', ring_jointHierarchy[2] + '_ik', ring_jointHierarchy[3] + '_ik']
	ring_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(ring_drivenAttr_allRelax, currentDriver=ring_driver_allRelax)
	parent_icon.relax.set(10)
	pm.setAttr(ring_jointHierarchy[0] + '_ik.rz', -9 )
	pm.setAttr(ring_jointHierarchy[1] + '_ik.rz', -11.25 )
	pm.setAttr(ring_jointHierarchy[2] + '_ik.rz', -13.5 )
	pm.setAttr(ring_jointHierarchy[3] + '_ik.rz', -16.8 )
	pm.setDrivenKeyframe(ring_drivenAttr_allRelax, currentDriver=ring_driver_allRelax)
	parent_icon.relax.set(-10)
	pm.setAttr(ring_jointHierarchy[0] + '_ik.rz', -6 )
	pm.setAttr(ring_jointHierarchy[1] + '_ik.rz', -7.5 )
	pm.setAttr(ring_jointHierarchy[2] + '_ik.rz', -9 )
	pm.setAttr(ring_jointHierarchy[3] + '_ik.rz', -12.6 )
	pm.setDrivenKeyframe(ring_drivenAttr_allRelax, currentDriver=ring_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(ring_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

def pinkySDK(*args):
	# Curl
	pinky_drivenAttr_curl = [pinky_jointHierarchy[0] + '_ik' + '.rz', pinky_jointHierarchy[1] + '_ik' + '.rz', pinky_jointHierarchy[2] + '_ik' + '.rz', pinky_jointHierarchy[3] + '_ik' + '.rz']
	pinky_driver_curl = (pinky_icon + '.curl')
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)

	# print "Driven:", pinky_driven
	pinky_driven_curl= [pinky_jointHierarchy[0] + '_ik', pinky_jointHierarchy[1] + '_ik', pinky_jointHierarchy[2] + '_ik', pinky_jointHierarchy[3] + '_ik']
	pinky_icon.curl.set(10)
	pm.xform(pinky_driven_curl, ro=(0, 0, -90))
	pm.setAttr(pinky_jointHierarchy[0] + '_ik.rz', -15)
	pm.setAttr(pinky_jointHierarchy[2] + '_ik.rz', -75)
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)
	pinky_icon.curl.set(-10)
	pm.xform(pinky_driven_curl, ro=(0, 0, 10))
	pm.setAttr(pinky_jointHierarchy[1] + '_ik.rz', 20)
	pm.setAttr(pinky_jointHierarchy[2] + '_ik.rz', 25)
	pm.setAttr(pinky_jointHierarchy[3] + '_ik.rz', 30)
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)
	pinky_drivenKeyframes_curl = (pinky_jointHierarchy[0] + '_ik' + '_rotateZ', pinky_jointHierarchy[1] + '_ik' + '_rotateZ', pinky_jointHierarchy[2] + '_ik' + '_rotateZ', pinky_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.curl.set(0)

	# Scrunch
	pinky_drivenAttr_scrunch = [pinky_jointHierarchy[1] + '_ik' + '.rz', pinky_jointHierarchy[2] + '_ik' + '.rz', pinky_jointHierarchy[3] + '_ik' + '.rz']
	pinky_driver_scrunch = (pinky_icon + '.scrunch')
	pm.setDrivenKeyframe(pinky_drivenAttr_scrunch, currentDriver=pinky_driver_scrunch)
	# print "Driven:", pinky_driven
	pinky_driven_scrunch= [pinky_jointHierarchy[1] + '_ik', pinky_jointHierarchy[2] + '_ik', pinky_jointHierarchy[3] + '_ik']
	pinky_icon.scrunch.set(10)
	pm.setAttr( pinky_jointHierarchy[1] + '_ik.rz', 50)
	pm.setAttr( pinky_jointHierarchy[2] + '_ik.rz', -110)
	pm.setAttr( pinky_jointHierarchy[3] + '_ik.rz', 30)
	pm.setDrivenKeyframe(pinky_drivenAttr_scrunch, currentDriver=pinky_driver_scrunch)
	pinky_icon.scrunch.set(-10)
	pm.setAttr( pinky_jointHierarchy[1] + '_ik.rz', 3)
	pm.setAttr( pinky_jointHierarchy[2] + '_ik.rz', 4)
	pm.setAttr( pinky_jointHierarchy[3] + '_ik.rz', 10)
	pm.setDrivenKeyframe(pinky_drivenAttr_scrunch, currentDriver=pinky_driver_scrunch)
	pinky_drivenKeyframes_scrunch = (pinky_jointHierarchy[0] + '_ik' + '_rotateZ', pinky_jointHierarchy[1] + '_ik' + '_rotateZ', pinky_jointHierarchy[2] + '_ik' + '_rotateZ', pinky_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_scrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.scrunch.set(0)

	# Spread
	pinky_drivenAttr_spread = (pinky_jointHierarchy[0] + '_ik' + '.ry', pinky_jointHierarchy[1] + '_ik' + '.ry')
	pinky_driven_spread= (pinky_jointHierarchy[0] + '_ik', pinky_jointHierarchy[1] + '_ik')
	pinky_driver_spread = (pinky_icon + '.spread')
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(10)
	pm.xform(pinky_driven_spread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(-10)
	pm.xform(pinky_driven_spread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(0)

	pinky_drivenKeyframes_spread = (pinky_jointHierarchy[0] + '_ik' + '_rotateY', pinky_jointHierarchy[1] + '_ik' + '_rotateY')
	pm.keyTangent(pinky_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Relax
	pinky_drivenAttr_relax = [pinky_jointHierarchy[0] + '_ik' + '.rz', pinky_jointHierarchy[1] + '_ik' + '.rz', pinky_jointHierarchy[2] + '_ik' + '.rz', pinky_jointHierarchy[3] + '_ik' + '.rz']
	pinky_driven_relax = [pinky_jointHierarchy[0] + '_ik', pinky_jointHierarchy[1] + '_ik', pinky_jointHierarchy[2] + '_ik', pinky_jointHierarchy[3] + '_ik']
	pinky_driver_relax = (pinky_icon + '.relax')
	pm.setDrivenKeyframe(pinky_drivenAttr_relax, currentDriver=pinky_driver_relax)
	pinky_icon.relax.set(10)
	pm.setAttr( pinky_jointHierarchy[0] + '_ik.rz', -12 )
	pm.setAttr( pinky_jointHierarchy[1] + '_ik.rz', -15 )
	pm.setAttr( pinky_jointHierarchy[2] + '_ik.rz', -18 )
	pm.setAttr( pinky_jointHierarchy[3] + '_ik.rz', -21 )
	pm.setDrivenKeyframe(pinky_drivenAttr_relax, currentDriver=pinky_driver_relax)
	pinky_icon.relax.set(0)

	pm.keyTangent(pinky_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Fist
	pinky_drivenAttr_fist = [pinky_jointHierarchy[0] + '_ik' + '.rz', pinky_jointHierarchy[1] + '_ik' + '.rz', pinky_jointHierarchy[2] + '_ik' + '.rz', pinky_jointHierarchy[3] + '_ik' + '.rz']
	pinky_driver_fist = (parent_icon + '.fist')
	pinky_driven_fist= [pinky_jointHierarchy[0] + '_ik', pinky_jointHierarchy[1] + '_ik', pinky_jointHierarchy[2] + '_ik', pinky_jointHierarchy[3] + '_ik']
	pm.setDrivenKeyframe(pinky_drivenAttr_fist, currentDriver=pinky_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(pinky_driven_fist, ro=(0, 0, -90))
	pm.setAttr( pinky_jointHierarchy[0] + '_ik.rz', -15 )
	pm.setAttr( pinky_jointHierarchy[2] + '_ik.rz', -75 )
	pm.setAttr( pinky_jointHierarchy[3] + '_ik.rz', -25 )
	pm.setDrivenKeyframe(pinky_drivenAttr_fist, currentDriver=pinky_driver_fist)
	parent_icon.fist.set(0)

	# Scrunch
	pinky_drivenAttr_allScrunch = [pinky_jointHierarchy[1] + '_ik' + '.rz', pinky_jointHierarchy[2] + '_ik' + '.rz', pinky_jointHierarchy[3] + '_ik' + '.rz']
	pinky_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	# print "Driven:", pinky_driven
	pinky_driven_allScrunch= [pinky_jointHierarchy[1] + '_ik', pinky_jointHierarchy[2] + '_ik', pinky_jointHierarchy[3] + '_ik']
	parent_icon.scrunch.set(10)
	pm.setAttr(pinky_jointHierarchy[1] + '_ik.rz', 50 )
	pm.setAttr(pinky_jointHierarchy[2] + '_ik.rz', -110 )
	pm.setAttr(pinky_jointHierarchy[3] + '_ik.rz', 30 )
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	pm.setAttr(pinky_jointHierarchy[1] + '_ik.rz', 3 )
	pm.setAttr(pinky_jointHierarchy[2] + '_ik.rz', 4 )
	pm.setAttr(pinky_jointHierarchy[3] + '_ik.rz', 10 )
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	pinky_drivenKeyframes_allScrunch = (pinky_jointHierarchy[0] + '_ik' + '_rotateZ', pinky_jointHierarchy[1] + '_ik' + '_rotateZ', pinky_jointHierarchy[2] + '_ik' + '_rotateZ', pinky_jointHierarchy[3] + '_ik' + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	# allSpread
	pinky_drivenAttr_allSpread = (pinky_jointHierarchy[0] + '_ik' + '.ry', pinky_jointHierarchy[1] + '_ik' + '.ry')
	pinky_driven_allSpread= (pinky_jointHierarchy[0] + '_ik', pinky_jointHierarchy[1] + '_ik')
	pinky_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(pinky_driven_allSpread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(pinky_driven_allSpread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(0)

	pinky_drivenKeyframes_allSpread = (pinky_jointHierarchy[0] + '_ik' + '_rotateY', pinky_jointHierarchy[1] + '_ik' + '_rotateY')
	pm.keyTangent(pinky_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# allRelax
	pinky_drivenAttr_allRelax = [pinky_jointHierarchy[0] + '_ik' + '.rz', pinky_jointHierarchy[1] + '_ik' + '.rz', pinky_jointHierarchy[2] + '_ik' + '.rz', pinky_jointHierarchy[3] + '_ik' + '.rz']
	pinky_driven_allRelax = [pinky_jointHierarchy[0] + '_ik', pinky_jointHierarchy[1] + '_ik', pinky_jointHierarchy[2] + '_ik', pinky_jointHierarchy[3] + '_ik']
	pinky_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(10)
	pm.setAttr(pinky_jointHierarchy[0] + '_ik.rz', -12 )
	pm.setAttr(pinky_jointHierarchy[1] + '_ik.rz', -15 )
	pm.setAttr(pinky_jointHierarchy[2] + '_ik.rz', -18 )
	pm.setAttr(pinky_jointHierarchy[3] + '_ik.rz', -21 )
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(-10)
	pm.setAttr(pinky_jointHierarchy[0] + '_ik.rz', -3 )
	pm.setAttr(pinky_jointHierarchy[1] + '_ik.rz', -3.75 )
	pm.setAttr(pinky_jointHierarchy[2] + '_ik.rz', -4.5 )
	pm.setAttr(pinky_jointHierarchy[3] + '_ik.rz', -8.4 )
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(pinky_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

def thumbSDK(*args):

	# Thumb Curl
	thumb_drivenAttr_curl = [thumb_jointHierarchy[1] + '_ik' + '.ry', thumb_jointHierarchy[2] + '_ik'  + '.ry', thumb_jointHierarchy[3] + '_ik'  + '.ry' ]
	thumb_driven_curl = [thumb_jointHierarchy[1] + '_ik' , thumb_jointHierarchy[2] + '_ik' , thumb_jointHierarchy[3] + '_ik' ]
	thumb_driver_curl = (parent_icon + '.curl')
	pm.setDrivenKeyframe( thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(10)
	pm.setAttr( thumb_jointHierarchy[1] + '_ik.ry', 25 )
	pm.setAttr( thumb_jointHierarchy[2] + '_ik.ry', 30 )
	pm.setAttr( thumb_jointHierarchy[3] + '_ik.ry', 32 )
	pm.setDrivenKeyframe( thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(-10)
	pm.setAttr( thumb_jointHierarchy[1] + '_ik.ry', -40 )
	pm.setAttr( thumb_jointHierarchy[2] + '_ik.ry', -30 )
	pm.setAttr( thumb_jointHierarchy[3] + '_ik.ry', -32 )
	pm.setDrivenKeyframe( thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(0)

	pm.keyTangent( thumb_driven_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)



	# Thumb Drop
	if 'lt_' in whichSide:
		thumb_drivenAttr_drop = [thumb_jointHierarchy[0] + '_ik'  + '.rx']
		thumb_driven_drop = [thumb_jointHierarchy[0] + '_ik' ]
		thumb_driver_drop = (parent_icon + '.drop')
		pm.setDrivenKeyframe( thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
		parent_icon.drop.set(10)
		pm.setAttr( thumb_jointHierarchy[0] + '_ik.rx', -64 )
		pm.setDrivenKeyframe( thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
		parent_icon.drop.set(0)

		pm.keyTangent( thumb_driven_drop, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	if 'rt_' in whichSide:
		thumb_drivenAttr_drop = [thumb_jointHierarchy[0] + '_ik'  + '.rx']
		thumb_driven_drop = [thumb_jointHierarchy[0] + '_ik' ]
		thumb_driver_drop = (parent_icon + '.drop')
		pm.setDrivenKeyframe( thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
		parent_icon.drop.set(10)
		pm.setAttr( thumb_jointHierarchy[0] + '_ik.rx', 64 )
		pm.setDrivenKeyframe( thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
		parent_icon.drop.set(0)

		pm.keyTangent( thumb_driven_drop, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)
		

	# Thumb Relax
	if 'lt_' in whichSide:
		thumb_drivenAttr_relax = [thumb_jointHierarchy[1] + '_ik' + '.ry', thumb_jointHierarchy[2] + '_ik'  + '.ry', thumb_jointHierarchy[3] + '_ik'  + '.ry', thumb_jointHierarchy[1] + '_ik' + '.rz', thumb_jointHierarchy[2] + '_ik'  + '.rz', thumb_jointHierarchy[3] + '_ik'  + '.rz' ]
		thumb_driven_relax = [thumb_jointHierarchy[1] + '_ik' , thumb_jointHierarchy[2] + '_ik' , thumb_jointHierarchy[3] + '_ik' ]
		thumb_driver_relax = (parent_icon + '.thumbRelax')
		pm.setDrivenKeyframe( thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
		parent_icon.thumbRelax.set(10)
		pm.setAttr( thumb_jointHierarchy[1] + '_ik.ry', -9 )
		pm.setAttr( thumb_jointHierarchy[2] + '_ik.ry', -6 )
		pm.setAttr( thumb_jointHierarchy[3] + '_ik.ry', -12 )
		pm.setAttr( thumb_jointHierarchy[1] + '_ik.rz', 4 )
		pm.setAttr( thumb_jointHierarchy[2] + '_ik.rz', 7 )
		pm.setAttr( thumb_jointHierarchy[3] + '_ik.rz', 12 )
		pm.setDrivenKeyframe( thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
		parent_icon.thumbRelax.set(0)

		pm.keyTangent( thumb_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	if 'rt_' in whichSide:
		thumb_drivenAttr_relax = [thumb_jointHierarchy[1] + '_ik' + '.ry', thumb_jointHierarchy[2] + '_ik'  + '.ry', thumb_jointHierarchy[3] + '_ik'  + '.ry', thumb_jointHierarchy[1] + '_ik' + '.rz', thumb_jointHierarchy[2] + '_ik'  + '.rz', thumb_jointHierarchy[3] + '_ik'  + '.rz' ]
		thumb_driven_relax = [thumb_jointHierarchy[1] + '_ik' , thumb_jointHierarchy[2] + '_ik' , thumb_jointHierarchy[3] + '_ik' ]
		thumb_driver_relax = (parent_icon + '.thumbRelax')
		pm.setDrivenKeyframe( thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
		parent_icon.thumbRelax.set(10)
		pm.setAttr( thumb_jointHierarchy[1] + '_ik.ry', 9 )
		pm.setAttr( thumb_jointHierarchy[2] + '_ik.ry', 6 )
		pm.setAttr( thumb_jointHierarchy[3] + '_ik.ry', 12 )
		pm.setAttr( thumb_jointHierarchy[1] + '_ik.rz', -4 )
		pm.setAttr( thumb_jointHierarchy[2] + '_ik.rz', -7 )
		pm.setAttr( thumb_jointHierarchy[3] + '_ik.rz', -12 )
		pm.setDrivenKeyframe( thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
		parent_icon.thumbRelax.set(0)

		pm.keyTangent( thumb_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	# Thumb Spread
	thumb_drivenAttr_spread = [thumb_jointHierarchy[1] + '_ik' + '.rz']
	thumb_driven_spread = [thumb_jointHierarchy[1] + '_ik' ]
	thumb_driver_spread = (parent_icon + '.thumbSpread')
	pm.setDrivenKeyframe( thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(10)
	pm.setAttr( thumb_jointHierarchy[1] + '_ik.rz', -45 )
	pm.setDrivenKeyframe( thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(-10)
	pm.setAttr( thumb_jointHierarchy[1] + '_ik.rz', 40 )
	pm.setDrivenKeyframe( thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(0)

	pm.keyTangent( thumb_driven_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	# Thumb fist
	if 'lt_' in whichSide:
		thumb_drivenAttr_fist = [thumb_jointHierarchy[0] + '_ik'  + '.rx', thumb_jointHierarchy[0] + '_ik'  + '.ry', thumb_jointHierarchy[0] + '_ik'  + '.rz', thumb_jointHierarchy[1] + '_ik'  + '.ry', thumb_jointHierarchy[2] + '_ik'  + '.ry', thumb_jointHierarchy[3] + '_ik'  + '.ry']
		thumb_driver_fist  = (parent_icon + '.fist')
		thumb_driven_fist = [thumb_jointHierarchy[0] + '_ik' , thumb_jointHierarchy[0] + '_ik' , thumb_jointHierarchy[0] + '_ik' , thumb_jointHierarchy[1] + '_ik' , thumb_jointHierarchy[2] + '_ik' , thumb_jointHierarchy[3] + '_ik' ]
		pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
		parent_icon.fist.set(10)
		pm.xform(thumb_jointHierarchy[0] + '_ik' , ro=(-32, 12, 7))
		pm.setAttr( thumb_jointHierarchy[1] + '_ik.ry', 16 )
		pm.setAttr( thumb_jointHierarchy[2] + '_ik.ry', 25 )
		pm.setAttr( thumb_jointHierarchy[3] + '_ik.ry', 8 )
		pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
		parent_icon.fist.set(0)

		thumb_drivenKeyframes_allSpread = (thumb_jointHierarchy[0] + '_ik'  + '_rotateX', thumb_jointHierarchy[0] + '_ik'  + '_rotateY', thumb_jointHierarchy[0] + '_ik'  + '_rotateZ', thumb_jointHierarchy[1] + '_ik'  + '_rotateY', thumb_jointHierarchy[2] + '_ik'  + '_rotateY', thumb_jointHierarchy[3] + '_ik'  + '_rotateY')
		pm.keyTangent(thumb_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	if 'rt_' in whichSide:
		thumb_drivenAttr_fist = [thumb_jointHierarchy[0] + '_ik'  + '.rx', thumb_jointHierarchy[0] + '_ik'  + '.ry', thumb_jointHierarchy[0] + '_ik'  + '.rz', thumb_jointHierarchy[1] + '_ik'  + '.ry', thumb_jointHierarchy[2] + '_ik'  + '.ry', thumb_jointHierarchy[3] + '_ik'  + '.ry']
		thumb_driver_fist  = (parent_icon + '.fist')
		thumb_driven_fist = [thumb_jointHierarchy[0] + '_ik' , thumb_jointHierarchy[0] + '_ik' , thumb_jointHierarchy[0] + '_ik' , thumb_jointHierarchy[1] + '_ik' , thumb_jointHierarchy[2] + '_ik' , thumb_jointHierarchy[3] + '_ik' ]
		pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
		parent_icon.fist.set(10)
		pm.xform(thumb_jointHierarchy[0] + '_ik' , ro=(32, -12, -7))
		pm.setAttr( thumb_jointHierarchy[1] + '_ik.ry', 16 )
		pm.setAttr( thumb_jointHierarchy[2] + '_ik.ry', 25 )
		pm.setAttr( thumb_jointHierarchy[3] + '_ik.ry', 8 )
		pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
		parent_icon.fist.set(0)

		thumb_drivenKeyframes_allSpread = (thumb_jointHierarchy[0] + '_ik'  + '_rotateX', thumb_jointHierarchy[0] + '_ik'  + '_rotateY', thumb_jointHierarchy[0] + '_ik'  + '_rotateZ', thumb_jointHierarchy[1] + '_ik'  + '_rotateY', thumb_jointHierarchy[2] + '_ik'  + '_rotateY', thumb_jointHierarchy[3] + '_ik'  + '_rotateY')
		pm.keyTangent(thumb_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

def indexRotSet(*args):

	global index_1_rotY, index_1_rotZ, index_2_rotY, index_2_rotZ, index_3_rotY, index_3_rotZ

	index_joints = pm.ls( sl=1, dag=1 )

	# Get the rotations of the first joint
	index_1_rotY = pm.getAttr( index_joints[0].ry )
	print( index_1_rotY )
	index_1_rotZ = pm.getAttr( index_joints[0].rz )
	print( index_1_rotZ )
	pm.textField( index_j1, e=1, text='Done')

	index_2_rotY = pm.getAttr( index_joints[1].ry )
	print( index_2_rotY )
	index_2_rotZ = pm.getAttr( index_joints[1].rz )
	print( index_2_rotZ )
	pm.textField( index_j2, e=1, text='Done')

	index_3_rotY = pm.getAttr( index_joints[0].ry )
	# print( index_3_rotY )
	index_3_rotZ = pm.getAttr( index_joints[0].rz )
	# print( index_3_rotZ )
	pm.textField( index_j3, e=1, text='Done')


def middleRotSet(*args):
	global middle_1_rotY, middle_1_rotZ, middle_2_rotY, middle_2_rotZ, middle_3_rotY, middle_3_rotZ

	middle_joints = pm.ls( sl=1, dag=1 )

	# Get the rotations of the first joint
	middle_1_rotY = pm.getAttr( middle_joints[0].ry )
	print( middle_1_rotY )
	middle_1_rotZ = pm.getAttr( middle_joints[0].rz )
	print( middle_1_rotZ )
	pm.textField( middle_j1, e=1, text='Done')

	middle_2_rotY = pm.getAttr( middle_joints[1].ry )
	print( middle_2_rotY )
	middle_2_rotZ = pm.getAttr( middle_joints[1].rz )
	print( middle_2_rotZ )
	pm.textField( middle_j2, e=1, text='Done')

	middle_3_rotY = pm.getAttr( middle_joints[0].ry )
	# print( middle_3_rotY )
	middle_3_rotZ = pm.getAttr( middle_joints[0].rz )
	# print( middle_3_rotZ )
	pm.textField( middle_j3, e=1, text='Done')

def ringRotSet(*args):
	pass

def pinkyRotSet(*args):
	pass

def thumbRotSet(*args):
	pass

def rename(*args):
	if selection_len == 5:
		# Rename the bind joints
		for i in range(index_limbJoints):
			new_name = '{0}'.format( (index_jointHierarchy[i] + '_bind') )
			# print( new_name )
			index_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
		for i in range(middle_limbJoints):
			new_name = '{0}'.format( (middle_jointHierarchy[i] + '_bind') )
			# print( new_name )
			middle_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
		for i in range(ring_limbJoints):
			new_name = '{0}'.format( (ring_jointHierarchy[i] + '_bind') )
			# print( new_name )
			ring_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
			for i in range(pinky_limbJoints):
				new_name = '{0}'.format( (pinky_jointHierarchy[i] + '_bind') )
				# print( new_name )
				pinky_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
		for i in range(thumb_limbJoints):
			new_name = '{0}'.format( (thumb_jointHierarchy[i] + '_bind') )
			# print( new_name )
			thumb_jointHierarchy[i].rename( new_name )

		new_name = '{0}'.format( (thumb_jointHierarchy[0] + '_pivot'))
		thumb_jointHierarchy[0].rename(new_name)

	if selection_len == 4:
		# Rename the bind joints
		for i in range(index_limbJoints):
			new_name = '{0}'.format( (index_jointHierarchy[i] + '_bind') )
			# print( new_name )
			index_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
		for i in range(middle_limbJoints):
			new_name = '{0}'.format( (middle_jointHierarchy[i] + '_bind') )
			# print( new_name )
			middle_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
			for i in range(pinky_limbJoints):
				new_name = '{0}'.format( (pinky_jointHierarchy[i] + '_bind') )
				# print( new_name )
				pinky_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
		for i in range(thumb_limbJoints):
			new_name = '{0}'.format( (thumb_jointHierarchy[i] + '_bind') )
			# print( new_name )
			thumb_jointHierarchy[i].rename( new_name )

		new_name = '{0}'.format( (thumb_jointHierarchy[0] + '_pivot'))
		thumb_jointHierarchy[0].rename(new_name)

	if selection_len == 3:
		# Rename the bind joints
		for i in range(index_limbJoints):
			new_name = '{0}'.format( (index_jointHierarchy[i] + '_bind') )
			# print( new_name )
			index_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
			for i in range(pinky_limbJoints):
				new_name = '{0}'.format( (pinky_jointHierarchy[i] + '_bind') )
				# print( new_name )
				pinky_jointHierarchy[i].rename( new_name )

		# Rename the bind joints
		for i in range(thumb_limbJoints):
			new_name = '{0}'.format( (thumb_jointHierarchy[i] + '_bind') )
			# print( new_name )
			thumb_jointHierarchy[i].rename( new_name )

		new_name = '{0}'.format( (thumb_jointHierarchy[0] + '_pivot'))
		thumb_jointHierarchy[0].rename(new_name)

def windowResize(*args):
	if pm.window('BR_bipedArm_setup', q=1, exists=1):
		pm.window('BR_bipedArm_setup', e=1, wh=(280, 80), rtf=1)
	else:
		pm.warning('BR_bipedArm_setup does not exist')

def deleteUI(*args):
	# print('Closing UI')
	pm.deleteUI('BR_bipedArm_setup')








