'''
Title
Description
	This file contains: Biped Back Setup
	
How to run:
	import BR_Interface_Toolset.BR_bipedBack_setup as biBack
	reload (biBack)
	biBack.gui()
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
	if pm.window('BR_bipedBack_setup', q=1, exists=1):
		pm.deleteUI('BR_bipedBack_setup')
		#BR_bipedBack_setup

	global system_name

	win_width = 280
	window_object = pm.window('BR_bipedBack_setup', title="BR_bipedBack_setup", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()

	system_name = pm.textFieldGrp( l='System Name', text='back', w=win_width )
	pm.button( l='Go', w=win_width, c=backSetup )

	pm.window('BR_bipedBack_setup', e=1, wh=(280, 80), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)

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

def backSetup(*args):
	# Setup the variables which could come from the UI 

	# Input from UI
	idName = pm.textFieldGrp( system_name, q=1, text=1 )
	# print(idName)

	# Check the selection is valid
	selectionCheck = pm.ls( sl=1, type='joint' )
	
	# Error check to make sure a joint is selected
	if not selectionCheck:
		pm.error( 'Please select the root joint' )
	else:
		jointRoot = pm.ls( sl=1, type='joint' )[0]

	
	# print( jointRoot )

	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = jointRoot[0:3]

	# Make sure the prefix is usable
	if not 'ct_' in whichSide:
		pm.error( 'Please use a joint with a usable prefix of either ct_' )

				
	# Now build the names we need
	limbName = whichSide + idName 
	iconName = whichSide + idName

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

	# Check to see if there are  7 or more/less joints in the back
	if limbJoints == 7:
		pass

	if limbJoints <= 6:
		pm.error( 'Please make 7 back joints' )

	if limbJoints > 7:
		pm.error( 'Please make 7 back joints' )


	#---------------------------------------------------------------------------------------
	# Duplicate the main joint chain and rename each joint
	#---------------------------------------------------------------------------------------

	# First define what joint chains we need 
	newJointList = [ '_ik', '_drv' ]

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

	#---------------------------------------------------------------------------------------
	# Constrain the main joints to the ik and fk joints so we can blend between them
	#---------------------------------------------------------------------------------------
	for i in range( limbJoints ):
		pm.parentConstraint( (jointHierarchy[i] + '_ik'), jointHierarchy[i] + '_drv', mo=0 )

	# Create the crv bind joints
	pos = pm.xform( jointHierarchy[0], q=1, t=1, ws=1 )
	crv_bind_01 = pm.joint( p=pos, n=jointHierarchy[0] + '_crvBind' )

	pm.select( cl=1 )

	pos = pm.xform( jointHierarchy[-1], q=1, t=1, ws=1 )
	crv_bind_02 = pm.joint( p=pos, n=jointHierarchy[1] + '_crvBind' )


	# Get the back and chest icon
	back_icon = limbName + '_icon'
	if pm.objExists(back_icon):
		back_selection = pm.ls(back_icon)[0]
	else: 
		pm.error( "Please make back icon with name like 'ct_back_icon' " )


	chest_icon = whichSide + 'chest_icon'
	if pm.objExists(chest_icon):
		chest_selection = pm.ls(chest_icon)[0]
	else: 
		pm.error( "Please make chest icon with name like 'ct_chest_icon' " )


	# Move the icons to the right spot
	temp_constraint = pm.pointConstraint( jointHierarchy[-1], chest_icon, mo=0 )
	pm.delete(temp_constraint)
	pm.select(chest_icon)
	freezeTransform()

	temp_constraint = pm.pointConstraint( jointHierarchy[0], back_icon, mo=0 )
	pm.delete(temp_constraint)
	pm.select(back_icon)
	freezeTransform()


	# Change the rotate orders
	back_selection.rotateOrder.set(2)
	chest_selection.rotateOrder.set(2)
	crv_bind_01.rotateOrder.set(2)
	crv_bind_02.rotateOrder.set(2)

	crv_bind_01.jointOrientY.set( 0 )
	crv_bind_01.jointOrientX.set( 90 )
	crv_bind_01.jointOrientZ.set( 90 )

	crv_bind_02.jointOrientY.set( 0 )
	crv_bind_02.jointOrientX.set( 90 )
	crv_bind_02.jointOrientZ.set( 90 )

	pm.parentConstraint( chest_icon, crv_bind_02, mo=1 )
	pm.parentConstraint( back_icon, crv_bind_01, mo=1 )

	# Create the ik crv
	pm.select( jointHierarchy[0] )
	joint_positions( )

	ik_crv = pm.curve( p=cv_pos, d=3, n=limbName + '_crv' )

	# Create spline ik 
	ikh = pm.ikHandle( sol='ikSplineSolver', ee=jointHierarchy[6] + '_ik', sj=jointHierarchy[0] + '_ik', c=ik_crv, ccv=0, n=limbName + '_ikh' )[0]

	# Bind the crv binds to the crv
	pm.select( crv_bind_01, crv_bind_02, ik_crv )
	pm.mel.SmoothBindSkin()

	# Setup twist
	ikh.dTwistControlEnable.set(1)
	ikh.dWorldUpType.set(4)
	ikh.dWorldUpAxis.set(1)
	ikh.dWorldUpVectorY.set(-1)
	ikh.dWorldUpVectorEndY.set(-1)
	ikh.dWorldUpVectorEndZ.set(0)


	pm.connectAttr( crv_bind_01 + '.xformMatrix', ikh + '.dWorldUpMatrix', f=1 )
	pm.connectAttr( crv_bind_02 + '.xformMatrix', ikh + '.dWorldUpMatrixEnd', f=1 )


	#---------------------------------------------------------------------------------------
	# Make fk joints
	#---------------------------------------------------------------------------------------

	pm.select( cl=1 )

	pos = pm.xform( jointHierarchy[0], q=1, t=1, ws=1 )
	pm.joint( p=pos, n=jointHierarchy[0] + '_fk')


	pos = pm.xform( jointHierarchy[2], q=1, t=1, ws=1 )
	pm.joint( p=pos, n=jointHierarchy[1] + '_fk')

	pos = pm.xform( jointHierarchy[4], q=1, t=1, ws=1 )
	pm.joint( p=pos, n=jointHierarchy[2] + '_fk')

	pos = pm.xform( jointHierarchy[6], q=1, t=1, ws=1 )
	pm.joint( p=pos, n=jointHierarchy[3] + '_fk')

	pm.select(jointHierarchy[0] + '_fk')

	# Orient the fk to match 
	pm.joint(jointHierarchy[0] + '_fk', zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='zup')
	pm.joint(jointHierarchy[3] + '_fk', zso=1, ch=1, e=1, oj='none')

	pm.select( jointHierarchy[0] + '_fk' )

	selection = pm.ls( jointHierarchy[0] + '_fk', dag=1, type='joint' )

	for each in selection:
		pm.setAttr( each + '.rotateOrder', 1)

	# Create the fk icons
	pm.circle( nr=(1, 0, 0), n=jointHierarchy[0] + '_fk_icon', ch=0 )
	fk_icon_01 = pm.ls( sl=1 )[0]
	temp_constraint = pm.parentConstraint( jointHierarchy[1] + '_fk', fk_icon_01, mo=0 )
	pm.delete(temp_constraint)
	centerPivot()
	deleteHistory()
 
 	fk_local_01 = pm.group( em=1, n=jointHierarchy[0] + '_fk_local' )

 	temp_constraint = pm.parentConstraint( jointHierarchy[1] + '_fk', fk_local_01, mo=0 )
 	pm.delete(temp_constraint)

 	pm.parent( fk_icon_01, fk_local_01 )
 	freezeTransform()


	pm.circle( nr=(1, 0, 0), n=jointHierarchy[1] + '_fk_icon', ch=0 )
	fk_icon_02 = pm.ls( sl=1 )[0]
	temp_constraint = pm.parentConstraint( jointHierarchy[2] + '_fk', fk_icon_02, mo=0 )
	pm.delete(temp_constraint)
	centerPivot()
	deleteHistory()
 
 	fk_local_02 = pm.group( em=1, n=jointHierarchy[1] + '_fk_local' )

 	temp_constraint = pm.parentConstraint( jointHierarchy[2] + '_fk', fk_local_02, mo=0 )
 	pm.delete(temp_constraint)

 	pm.parent( fk_icon_02, fk_local_02 )
 	freezeTransform()

 	pm.parent( fk_local_02, fk_icon_01 )

 	pm.select( fk_icon_02, fk_icon_01 )
 	selection = pm.ls(sl=1)
 	pm.mel.TagAsControllerParent()

 	for each in selection:
 		pm.setAttr( each + '.overrideEnabled', 1 )
 		pm.setAttr( each + '.overrideColor', 18 )

 	pm.orientConstraint( fk_icon_01, jointHierarchy[1] + '_fk', mo=1 )

 	pm.orientConstraint( fk_icon_02, jointHierarchy[2] + '_fk', mo=1 )
 	
 	# Pad the back and chest icon
 	back_local = pm.group( em=1, n=limbName + '_local' )
 	temp_constraint = pm.parentConstraint( back_icon, back_local, mo=0 )
 	pm.delete(temp_constraint)

 	chest_local = pm.group( em=1, n=whichSide + 'chest_local' )
 	temp_constraint = pm.parentConstraint( chest_icon, chest_local, mo=0 )
 	pm.delete(temp_constraint)

 	pm.parent( back_icon, back_local )
 	freezeTransform()
 	pm.parent( chest_icon, chest_local )
 	freezeTransform()

 	pm.parentConstraint( fk_icon_01, back_local, mo=1 )
 	pm.parentConstraint( fk_icon_02, chest_local, mo=1 )

 	#---------------------------------------------------------------------------------------
	# Create back global icon
	#---------------------------------------------------------------------------------------
	pm.curve(p=[(0.5, 0, 0.5), (-0.5, 0, 0.5), (-0.5, 0, -0.5), (0.5, 0, -0.5), (0.5, 0, 0.5)], k=[0, 1, 2, 3, 4], d=1, n=limbName + '_global_icon')
	back_global = pm.ls(sl=1)[0]

	temp_constraint = pm.pointConstraint( jointRoot, back_global, mo=0 )
	pm.delete( temp_constraint )
	freezeTransform()

	back_global.rotateOrder.set(2)

	pad = pm.group( em=1, n=limbName + '_00_pad' )
	temp_constraint = pm.parentConstraint( jointRoot, pad, mo=0 )
	pm.delete( temp_constraint )

	pm.parent( jointHierarchy[0] + '_ik', jointHierarchy[0] + '_drv', jointHierarchy[0] + '_fk', pad )

	pm.parentConstraint( jointHierarchy[0] + '_fk', fk_local_01, mo=1 )

	pm.parentConstraint( back_global, pad, mo=1 )

	back_global.overrideEnabled.set( 1 )
	back_global.overrideColor.set( 20 )

	back_selection.overrideEnabled.set( 1 )
	back_selection.overrideColor.set( 17 )

	chest_selection.overrideEnabled.set( 1 )
	chest_selection.overrideColor.set( 17 )

 	#---------------------------------------------------------------------------------------
	# Make stretchy
	#---------------------------------------------------------------------------------------

	# Create the curve info
	crv_info = pm.shadingNode( 'curveInfo', asUtility=1, n=limbName + '_crv_info' )
	pm.connectAttr( ik_crv + '.worldSpace', crv_info + '.inputCurve', f=1 )

	# Create and connect the mult 
	stretch_mult = pm.shadingNode( 'multiplyDivide', asUtility=1, n=limbName + '_mult' )
	pm.connectAttr( crv_info + '.arcLength', stretch_mult + '.input1X', f=1 )

	stretch_mult.operation.set( 2 )

	arcLen = crv_info.arcLength.get()
	stretch_mult.input2X.set( arcLen )

	pm.connectAttr( stretch_mult + '.outputX', jointHierarchy[0] + '_ik.sx', f=1 )
	pm.connectAttr( stretch_mult + '.outputX', jointHierarchy[1] + '_ik.sx', f=1 )
	pm.connectAttr( stretch_mult + '.outputX', jointHierarchy[2] + '_ik.sx', f=1 )
	pm.connectAttr( stretch_mult + '.outputX', jointHierarchy[3] + '_ik.sx', f=1 )
	pm.connectAttr( stretch_mult + '.outputX', jointHierarchy[4] + '_ik.sx', f=1 )
	pm.connectAttr( stretch_mult + '.outputX', jointHierarchy[5] + '_ik.sx', f=1 )

	# Create and connect the square root
	stretch_squareRoot = pm.shadingNode( 'multiplyDivide', asUtility=1, n=limbName + '_squareRoot' )
	stretch_squareRoot.operation.set( 3 )

	pm.connectAttr( stretch_mult + '.outputX', stretch_squareRoot + '.input1X', f=1 )
	stretch_squareRoot.input2X.set( .5 )

	# Create and connect he invert 
	stretch_invert = pm.shadingNode( 'multiplyDivide', asUtility=1, n=limbName + '_invert' )
	stretch_invert.operation.set( 2 )

	pm.connectAttr( stretch_squareRoot + '.outputX', stretch_invert + '.input2X', f=1 )
	stretch_invert.input1X.set( 1 )

	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[0] + '_ik.sy', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[1] + '_ik.sy', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[2] + '_ik.sy', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[3] + '_ik.sy', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[4] + '_ik.sy', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[5] + '_ik.sy', f=1 )


	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[0] + '_ik.sz', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[1] + '_ik.sz', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[2] + '_ik.sz', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[3] + '_ik.sz', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[4] + '_ik.sz', f=1 )
	pm.connectAttr( stretch_invert + '.outputX', jointHierarchy[5] + '_ik.sz', f=1 )

 	#---------------------------------------------------------------------------------------
	# Scale norm
	#---------------------------------------------------------------------------------------

	# Get global icon
	rig_global_icon = 'ct_moveAll'
	if pm.objExists(rig_global_icon):
		global_selection = pm.ls( rig_global_icon )[0]

	if pm.objExists( rig_global_icon ):
		pass
	else:
		pm.error( "Please make the global icon, and name it 'ct_moveAll' The name can be changes later" )

	anim_icon = 'ct_anim'
	if pm.objExists( anim_icon ):
		anim_selection = pm.ls( anim_icon )[0]

	if pm.objExists(anim_icon):
		pm.parent( chest_local, back_local, fk_local_01, back_global, anim_icon)
	else:
		pm.parent( chest_local, back_local, fk_local_01, back_global, rig_global_icon )

	# Create and connect the scale norm
	scale_norm = pm.shadingNode( 'multiplyDivide', asUtility=1, n=limbName + '_norm' )
	scale_norm.operation.set( 2 )

	pm.connectAttr( crv_info + '.arcLength', scale_norm + '.input1X', f=1 )
	pm.connectAttr( pad + '.sx', scale_norm + '.input2X', f=1 )
	pm.connectAttr( scale_norm + '.outputX', stretch_mult + '.input1X', f=1 )


	pm.scaleConstraint( rig_global_icon, pad, mo=1 )


	#---------------------------------------------------------------------------------------
	# Clean up
	#---------------------------------------------------------------------------------------
	dnt_grp = pm.group( em=1, n=limbName + '_dnt_grp' )
	temp_constraint = pm.parentConstraint( jointRoot, dnt_grp, mo=0 )
	pm.delete( temp_constraint )
	freezeTransform()

	pm.parent( crv_bind_01, crv_bind_02, ikh, ik_crv, dnt_grp )

	ik_crv.inheritsTransform.set( 0 )
	dnt_grp.v.set( 0 )

	pm.setAttr(jointHierarchy[0] + '_fk.v', 0)
	pm.setAttr(jointHierarchy[0] + '_ik.v', 0)
	pm.setAttr(jointHierarchy[0] + '_drv.v', 0)


	pm.parentConstraint( pad, dnt_grp, mo=1 )


	# Stretch tog
	pm.addAttr( back_global, ln='stretch', at='bool' )
	unlock_and_unhide( back_global, ['stretch'] )

	stretch_switch = pm.shadingNode( 'blendColors', asUtility=1, n=limbName + '_stretch_blend' )

	stretch_switch.color2R.set( arcLen )

	pm.connectAttr( back_global + '.stretch', stretch_switch  + '.blender', f=1 )
	pm.connectAttr( crv_info + '.arcLength', stretch_switch + '.color1R', f=1 )
	pm.connectAttr( stretch_switch + '.outputR', scale_norm + '.input1X', f=1 )

	#---------------------------------------------------------------------------------------
	# Constrain the driver joints to the bind joints
	#---------------------------------------------------------------------------------------
	
	pm.select( (jointHierarchy[0] + '_drv') )
	drv_joints = pm.ls(sl=1, dag=1, type='joint')

	# Rename the bind and waste joints
	for i in range(limbJoints):
		new_name = '{0}'.format( (jointHierarchy[i] + '_bind') )
		# print( new_name )
		jointHierarchy[i].rename( new_name )

	new_name = jointRoot.replace( '01_bind', '07_waste' )

	last_joint = pm.ls(jointHierarchy[6])[0]
	last_joint.rename(new_name)

	for i in range( limbJoints ):
		pm.parentConstraint( drv_joints[i] , jointHierarchy[i] , mo=0 )

	pm.select( last_joint )
	last_constraint = pm.listConnections( type='parentConstraint' )[0]
	pm.delete( last_constraint )

	pm.select( cl=1 )

	print( 'Back Setup Complete' )

def windowResize(*args):
	if pm.window('BR_bipedBack_setup', q=1, exists=1):
		pm.window('BR_bipedBack_setup', e=1, wh=(280, 80), rtf=1)
	else:
		pm.warning('BR_bipedBack_setup does not exist')

def deleteUI(*args):
	# print('Closing UI')
	pm.deleteUI('BR_bipedBack_setup')
