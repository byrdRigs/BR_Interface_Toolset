'''
Title
Description
	This file contains: Biped Leg Setup
	
How to run:
	import BR_Interface_Toolset.BR_bipedLeg_setup as biLeg
	reload (biLeg)
	biLeg.gui()
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
	global system_name
	if pm.window('BR_bipedLeg_setup', q=1, exists=1):
		pm.deleteUI('BR_bipedLeg_setup')
		#BR_bipedLeg_setup

	win_width = 280
	window_object = pm.window('BR_bipedLeg_setup', title="BR_bipedLeg_setup", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()

	system_name = pm.textFieldGrp( l='System Name', text='leg', w=win_width )
	pm.button( l='Go', w=win_width, c=legSetup )
	pm.button( l='Rfl Prep', w=win_width, c=rflPrep )
	pm.text( l='Move the locators to the corresponding parts of the foot', w=win_width, ww=1 )
	pm.button( l='Rfl Setup', w=win_width, c=rflSetup )


	pm.window('BR_bipedLeg_setup', e=1, wh=(280, 80), rtf=1)
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

def legSetup(*args):
	# Setup the variables which could come from the UI 

	global limbName, whichSide, jointRoot, jointHierarchy, foot_icon, knee_icon, leg_ikh, ball_ikh
	global toe_ikh, idName, iconName, switch, foot_selection, switch_selection, knee_selection, noFlip_local

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
	newJointList = [ '_ik', '_fk' ]

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
		pm.parentConstraint( (jointHierarchy[i] + '_ik'), (jointHierarchy[i] + '_fk'), jointHierarchy[i], mo=0 )

	#---------------------------------------------------------------------------------------
	# Get the ikfk switch
	#---------------------------------------------------------------------------------------
	switch = limbName + '_switch'
	# print(switch)

	# Check if the swich exists
	if pm.objExists( switch ):
		switch_selection = pm.ls( switch )[0]
	else:
		pm.error("Please make an Ik/Fk switch using the suffix _switch. Also give it the attribute of 'IkFk' as a float with a min of 0 and a max of 1")

	'''
	Lock and hide attrs
	'''
	attrs = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']
	lock_and_hide(switch_selection, attrs)


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

	# Add length attr to the first two fk icons 
	pm.addAttr( (jointHierarchy[0] + '_fk_icon'), ln='length', dv=1, min=0, at='double' )
	pm.setAttr( (jointHierarchy[0] + '_fk_icon.length'), e=1, keyable=1 )

	pm.addAttr( (jointHierarchy[1] + '_fk_icon'), ln='length', dv=1, min=0, at='double' )
	pm.setAttr( (jointHierarchy[1] + '_fk_icon.length'), e=1, keyable=1 )

	# Set sdk for the fk length
	pm.setDrivenKeyframe( (jointHierarchy[1] + '_fk.tx'), currentDriver=(jointHierarchy[0] + '_fk_icon.length') )
	pm.setAttr( (jointHierarchy[0] + '_fk_icon.length'), 0 )
	pm.setAttr( (jointHierarchy[1] + '_fk.tx'), 0 )
	pm.setDrivenKeyframe( (jointHierarchy[1] + '_fk.tx'), currentDriver=(jointHierarchy[0] + '_fk_icon.length') )
	pm.setAttr( (jointHierarchy[0] + '_fk_icon.length'), 1 )
	pm.keyTangent( (jointHierarchy[1] + '_fk'), 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline' )
	pm.mel.selectKey( (jointHierarchy[1] + '_fk.tx'), add=1, k=1, f=1 )
	pm.setInfinity( poi='linear' )


	pm.setDrivenKeyframe( (jointHierarchy[2] + '_fk.tx'), currentDriver=(jointHierarchy[1] + '_fk_icon.length') )
	pm.setAttr( (jointHierarchy[1] + '_fk_icon.length'), 0 )
	pm.setAttr( (jointHierarchy[2] + '_fk.tx'), 0 )
	pm.setDrivenKeyframe( (jointHierarchy[2] + '_fk.tx'), currentDriver=(jointHierarchy[1] + '_fk_icon.length') )
	pm.setAttr( (jointHierarchy[1] + '_fk_icon.length'), 1 )
	pm.keyTangent( (jointHierarchy[2] + '_fk'), 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline' )
	pm.mel.selectKey( (jointHierarchy[2] + '_fk.tx'), add=1, k=1, f=1 )
	pm.setInfinity( poi='linear' )

	#---------------------------------------------------------------------------------------
	# Setup IK
	#---------------------------------------------------------------------------------------
	leg_ikh = pm.ikHandle( sj=(jointHierarchy[0] + '_ik'), ee=(jointHierarchy[2] + '_ik'), n=(limbName + '_ikh') )[0]
	ball_ikh = pm.ikHandle( sj=(jointHierarchy[2] + '_ik'), ee=(jointHierarchy[3] + '_ik'), n=(whichSide + 'ball_ikh') )[0]
	toe_ikh = pm.ikHandle( sj=(jointHierarchy[3] + '_ik'), ee=(jointHierarchy[4] + '_ik'), n=(whichSide + 'toe_ikh') )[0]

	# Get the foot icon
	foot_icon = (whichSide + 'foot_icon')

	if pm.objExists(foot_icon):
		pass
	else:
		pm.error( "Please make a foot icon with name like 'lt_foot_icon'" )

	'''
	Add foot attrs
	'''
	pm.addAttr( str(foot_icon), ln='legAttrs', en='------:', at='enum' )
	pm.addAttr( str(foot_icon), ln='stretch', at='bool' )

	pm.addAttr( str(foot_icon), ln='kneeAttrs', at='enum', en='------:' )

	selection = pm.ls( foot_icon )[0]

	lockAttrs( selection, ['kneeAttrs'] )
	unhideAttrs	( selection, ['kneeAttrs'] )


	pm.addAttr( str(foot_icon), ln='kneeTwist', at='double', dv=0 )
	unlock_and_unhide( selection, ['kneeTwist'] )

	pm.addAttr( str(foot_icon), ln='autoKnee', at='bool' )
	unlock_and_unhide( selection, ['autoKnee'] )

	pm.addAttr( str(foot_icon), ln='kneeSnap', at='bool' )
	unhideAttrs( selection, ['kneeSnap'] )


	pm.addAttr( str(foot_icon), ln='footAttrs', en='------:', at='enum' )
	pm.addAttr( str(foot_icon), ln='roll', dv=0, at='double' )
	pm.addAttr( str(foot_icon), ln='bendLimitAngle', dv=45, at='double' )
	pm.addAttr( str(foot_icon), ln='toeStraightAngle', dv=75, at='double' )
	pm.addAttr( str(foot_icon), ln='tilt', dv=0, at='double' )
	pm.addAttr( str(foot_icon), ln='lean', dv=0, at='double' )
	pm.addAttr( str(foot_icon), ln='toeSpin', dv=0, at='double' )
	pm.addAttr( str(foot_icon), ln='toeTap', dv=0, at='double' )
	

	lockAttrs( selection, ['footAttrs', 'legAttrs'] )
	unhideAttrs( selection, ['footAttrs', 'legAttrs'] )
	unlock_and_unhide( selection, ['roll', 'bendLimitAngle', 'toeStraightAngle', 'tilt', 'lean', 'toeSpin', 'toeTap', 'stretch'] )

	# Parent the ikhs under the foot icon
	pm.parent( leg_ikh, ball_ikh, toe_ikh, foot_icon )

	# Create distance node and locators
	pos = pm.xform( jointRoot, q=1, t=1, ws=1 )
	loc_1 = pm.spaceLocator( p=(pos), n=(limbName + '_startLoc') )
	centerPivot()

	pos = pm.xform( jointHierarchy[2], q=1, t=1, ws=1 )
	loc_2 = pm.spaceLocator( p=(pos), n=(limbName + '_endLoc') )
	centerPivot()

	leg_dist = pm.shadingNode( 'distanceDimShape', asUtility=1, n=(limbName + '_distShape') )

	# Connect the locators to the dist node
	pm.connectAttr( loc_1 + '.worldPosition', leg_dist + '.startPoint' )
	pm.connectAttr( loc_2 + '.worldPosition', leg_dist + '.endPoint' )

	# Parent the ednLoc under the foot icon
	pm.parent( loc_2, foot_icon )

	# Get the length of the leg
	rootLength = pm.getAttr( jointHierarchy[1] + '_ik.translateX' )
	joint2Length = pm.getAttr( jointHierarchy[2]  + '_ik.translateX' )
	sumLength = ( rootLength + joint2Length )
	# print( sumLength )

	# Set the sdk of the dist node
	pm.setDrivenKeyframe( (jointHierarchy[1])+ '_ik.translateX', dv=sumLength, currentDriver=leg_dist + '.distance', at='.translateX', value=rootLength )
	pm.setDrivenKeyframe( (jointHierarchy[1])+ '_ik.translateX', dv=(sumLength*2), currentDriver=leg_dist + '.distance', at='.translateX', value=(rootLength*2) )

	pm.setDrivenKeyframe( (jointHierarchy[2]) + '_ik.translateX', dv=sumLength, currentDriver=leg_dist + '.distance', at='.translateX', value=joint2Length )
	pm.setDrivenKeyframe( (jointHierarchy[2]) + '_ik.translateX', dv=(sumLength*2), currentDriver=leg_dist + '.distance', at='.translateX', value=(joint2Length*2) )

	pm.keyTangent( (jointHierarchy[1] + '_ik'), 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline' )
	pm.selectKey( (jointHierarchy[1] + '_ik_translateX'), add=1, k=1, f=(1, 82.555611) )
	pm.setInfinity( poi='linear' )

	pm.keyTangent((jointHierarchy[2] + '_ik') , 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey( (jointHierarchy[2] + '_ik_translateX'), add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.select( leg_ikh, ball_ikh, toe_ikh)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.v', 0)

	knee_icon = (whichSide + 'knee_icon')

	if pm.objExists( knee_icon ):
		pass
	else:
		pm.error( "Please make a knee icon with name like 'lt_knee_icon'" )

	# Create the locator for the no-flip knee
	pos = pm.xform( (jointHierarchy[2] + '_ik'), q=1, t=1, ws=1 )
	noFlip_loc = pm.spaceLocator( p=(pos), n=(limbName + '_noFlip_loc') )
	centerPivot()

	if 'lt_' in whichSide:
		noFlip_loc.tx.set(2)

	if 'rt_' in whichSide:
		noFlip_loc.tx.set(-2)

	# Create the local for the no-flip knee
	pos = pm.xform( (jointHierarchy[2] + '_ik'), q=1, t=1, ws=1 )
	noFlip_local = pm.group( empty=1, n=(limbName + '_noFlip_local') )
	pm.xform( noFlip_local, t=(pos) )
	centerPivot()
	freezeTransform()

	# Parent the no-flip loc under the local
	pm.parent( noFlip_loc, noFlip_local )
	freezeTransform()

	# Parent the no-flip local under the foot icon
	pm.parent( noFlip_local, foot_icon )

	# Create the pole vector for the knee
	knee_const = pm.poleVectorConstraint( noFlip_loc, knee_icon, leg_ikh )

	const_target_1 = knee_const.getWeightAliasList()[0]
	const_target_2 = knee_const.getWeightAliasList()[1]
	# print const_target_1
	# print const_target_2

	pm.connectAttr( foot_icon + '.kneeTwist', noFlip_local + '.rotateY' )

	# Set the sdk 
	noFlip_loc.v.set( 0 )
	foot_selection = pm.ls( foot_icon )[0]
	knee_selection = pm.ls( knee_icon )[0]

	foot_selection.autoKnee.set( 1 )
	const_target_2.set( 0 )
	if 'lt_' in whichSide:
		leg_ikh.twist.set( 90 )

	if 'rt_' in whichSide:
		leg_ikh.twist.set( -90 )

	knee_selection.v.set( 0 )
	pm.setDrivenKeyframe( [knee_icon + '.visibility', const_target_1, const_target_2, leg_ikh + '.twist'], currentDriver=foot_icon + '.autoKnee' )


	foot_selection.autoKnee.set( 0 )
	const_target_1.set( 0 )
	const_target_2.set( 1 )
	leg_ikh.twist.set( 0 )
	knee_selection.v.set( 1 )
	pm.setDrivenKeyframe( [knee_icon + '.visibility', const_target_1, const_target_2, leg_ikh + '.twist'], currentDriver=foot_icon + '.autoKnee' )
	foot_selection.autoKnee.set( 1 )

	# Create the knee locator for knee snapping
	knee_loc = pm.spaceLocator( p=[0, 0, 0], n=(whichSide + 'knee_loc') )
	temp_constraint = pm.pointConstraint( knee_icon, knee_loc, mo=0 )
	pm.delete( temp_constraint )
	freezeTransform()

	# Create the knee dist nodes
	knee_dist_1 = pm.shadingNode( 'distanceDimShape', asUtility=1, n=(whichSide + 'knee_01_distShape') )
	pm.connectAttr( (loc_1 + '.worldPosition'), (knee_dist_1 + '.startPoint'), f=1 )
	pm.connectAttr( (knee_loc + '.worldPosition'), (knee_dist_1 + '.endPoint'), f=1 )

	knee_dist_2 = pm.shadingNode( 'distanceDimShape', asUtility=1, n=(whichSide + 'knee_02_distShape') )
	pm.connectAttr( (loc_2 + '.worldPosition'), (knee_dist_2 + '.startPoint'), f=1 )
	pm.connectAttr( (knee_loc + '.worldPosition'), (knee_dist_2 + '.endPoint'), f=1 )

	# Parent the knee loc under the knee icon
	pm.parent( knee_loc, knee_icon )

	# Create the blend for the knee snap
	knee_snapBlend = pm.shadingNode( 'blendColors', asUtility=1, n=(whichSide + 'knee_snapBlendShape') )

	# Connect the blend
	pm.connectAttr( knee_dist_1 + '.distance', knee_snapBlend + '.color1R', f=1)
	pm.connectAttr( knee_dist_2 + '.distance', knee_snapBlend + '.color1G', f=1)

	pm.connectAttr( (jointHierarchy[1] + '_ik_translateX.output'), knee_snapBlend + '.color2R', f=1 )
	pm.connectAttr( (jointHierarchy[2] + '_ik_translateX.output'), knee_snapBlend + '.color2G', f=1 )


	pm.connectAttr( knee_snapBlend + '.outputR', (jointHierarchy[1] +  '_ik.translateX'), f=1 )
	pm.connectAttr( knee_snapBlend + '.outputG', (jointHierarchy[2] + '_ik.translateX'), f=1)

	pm.connectAttr( foot_icon + '.kneeSnap', knee_snapBlend + '.blender')

	pm.select( knee_loc, knee_dist_1, knee_dist_2)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	#---------------------------------------------------------------------------------------
	# Clean up
	#---------------------------------------------------------------------------------------

	# Set the sdk 
	fk_icon_1 = pm.ls( jointHierarchy[0] + '_fk_icon' )[0]
	fk_icon_1.v.set(0)
	pm.setDrivenKeyframe( [foot_icon + '.visibility', fk_icon_1 + '.visibility'], currentDriver=switch + '.IkFk')
	switch_selection.IkFk.set(1)
	foot_selection.v.set(0)
	fk_icon_1.v.set(1)
	pm.setDrivenKeyframe( [foot_icon + '.visibility', fk_icon_1 + '.visibility'], currentDriver=switch + '.IkFk')
	switch_selection.IkFk.set(0)

	# Create the leg pad
	pad = pm.group( empty=1, n=(whichSide + idName + '_pad') )
	temp_constraint = pm.parentConstraint( jointRoot, pad, mo=0 )
	pm.delete(temp_constraint)
	freezeTransform()

	pm.parent( jointRoot, (jointHierarchy[0] + '_ik'), (jointHierarchy[0] +'_fk'), pad )

	pm.select( (jointHierarchy[0] + '_ik'), (jointHierarchy[0] +'_fk') )
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	# Lock and hide fk translate
	pm.select( (jointHierarchy[0] + '_fk_icon'), (jointHierarchy[1] + '_fk_icon'), (jointHierarchy[2] + '_fk_icon'), (jointHierarchy[3] + '_fk_icon') )
	selection = pm.ls(sl=1)
	for each in selection:
		lock_and_hide(each, ['tx', 'ty', 'tz', 'v'])

	lock_and_hide( foot_selection, ['v'] )

	stretchBlend = pm.shadingNode( 'blendColors', asUtility=1, n=(whichSide + idName + '_stretchBlend'))
	pm.connectAttr( leg_dist + '.distance', stretchBlend + '.color1R', f=1)
	stretchBlend.color2R.set(1)
	pm.connectAttr( stretchBlend + '.outputR', (jointHierarchy[1] + '_ik_translateX.input'), f=1 )
	pm.connectAttr(stretchBlend  + '.outputR', (jointHierarchy[2] + '_ik_translateX.input'), f=1)
	pm.connectAttr( foot_icon + '.stretch', stretchBlend + '.blender', f=1 )
	foot_selection.stretch.set(1)

	# Rename the bind joints
	for i in range(limbJoints):
		new_name = '{0}'.format( (jointHierarchy[i] + '_bind') )
		# print( new_name )
		jointHierarchy[i].rename( new_name )

	new_name = '{0}'.format( (jointHierarchy[-1] + '_waste') )
	jointHierarchy[-1].rename(new_name)

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

	dnt_grp = pm.group( knee_dist_1, knee_dist_2, leg_dist, n=(limbName + '_dnt_grp') )

	pm.parent( loc_1, pad )


	pm.select( foot_icon, knee_icon, switch )
	icons = pm.ls(sl=1)

	if 'lt_' in whichSide:
		for each in icons:
			pm.setAttr( each + '.overrideEnabled', 1 )
			pm.setAttr( each + '.overrideColor', 6 )

	if 'rt_' in whichSide:
		for each in icons:
			pm.setAttr( each + '.overrideEnabled', 1 )
			pm.setAttr( each + '.overrideColor', 13 )


	# ---------------------------------------------------------------------------------------
	# Scale Norm
	# ---------------------------------------------------------------------------------------

	# Get the main icon 
	rig_global_icon = 'ct_moveAll'

	if pm.objExists( rig_global_icon ):
		main_selection = pm.ls( rig_global_icon )[0]
	else:
		pm.error( "Please rename the main icon 'ct_moveAll', you can change this later " )

	# Create mult
	scale_norm = pm.shadingNode( 'multiplyDivide', asUtility=1, n=limbName + '_norm' )
	scale_norm.operation.set( 2 )
	pm.connectAttr( leg_dist + '.distance', scale_norm + '.input1X', f=1 )
	pm.connectAttr( rig_global_icon + '.sx', scale_norm + '.input2X', f=1 )
	pm.connectAttr( scale_norm + '.outputX', stretchBlend + '.color1R', f=1 )

	pm.connectAttr( knee_dist_1 + '.distance', scale_norm + '.input1Y', f=1 )
	pm.connectAttr( rig_global_icon + '.sx', scale_norm + '.input2Y', f=1 )
	pm.connectAttr( scale_norm + '.outputY', knee_snapBlend + '.color1G', f=1 )

	pm.connectAttr( knee_dist_2 + '.distance', scale_norm + '.input1Z', f=1 )
	pm.connectAttr( rig_global_icon + '.sx', scale_norm + '.input2Z', f=1 )
	pm.connectAttr( scale_norm + '.outputZ', knee_snapBlend + '.color1R', f=1 )


	pm.select( cl=1 )

def rflPrep(*args):
	global heel_loc, outerBank_loc, innerBank_loc, toe_loc, ball_loc, ankle_loc

	# Create the locators
	heel_loc = pm.spaceLocator( p=(0, 0, 0), n=(whichSide + 'heel_loc') )

	outerBank_loc = pm.spaceLocator( p=(0, 0, 0), n=(whichSide + 'outerBank_loc')  )

	if 'lt_' in whichSide:
		pm.xform( outerBank_loc, t=[3, 0, 6] )

	if 'rt_' in whichSide:
		pm.xform( outerBank_loc, t=[-3, 0, 6] )

	freezeTransform()

	innerBank_loc = pm.spaceLocator( p=(0, 0, 0), n=(whichSide + 'innerBank_loc')  )

	if 'lt_' in whichSide:
		pm.xform( innerBank_loc, t=[-3, 0, 6] )

	if 'rt_' in whichSide:
		pm.xform( innerBank_loc, t=[3, 0, 6] )

	freezeTransform()

	toe_loc = pm.spaceLocator(p=(0, 0, 0), n=(whichSide + 'toe_loc') )
	
	pm.xform( toe_loc, t=[0, 0, 9] )

	freezeTransform()

	ball_loc = pm.spaceLocator( p=(0, 0, 0), n=(whichSide + 'ball_loc') )
	
	pm.xform( ball_loc, t=[0, 0, 6] )

	freezeTransform()

	ankle_loc = pm.spaceLocator( p=(0, 0, 0), n=(whichSide + 'ankle_loc') )
	temp_constraint = pm.pointConstraint( jointHierarchy[2], ankle_loc, mo=0, skip=['x', 'z'] )
	pm.delete(temp_constraint)

	freezeTransform()

	# Parent the locators
	pm.parent( innerBank_loc, heel_loc )
	pm.parent( outerBank_loc, innerBank_loc )
	pm.parent( toe_loc, outerBank_loc )
	pm.parent( ball_loc, toe_loc )
	pm.parent( ankle_loc, ball_loc )

	# Constrain the heel to the leg
	temp_constraint =pm.pointConstraint( jointHierarchy[2], heel_loc, skip='y', mo=0 )
	pm.delete(temp_constraint)

	pm.select( cl=1 )

def rflSetup(*args):

	pm.select( heel_loc )
	freezeTransform( )

	
	# Create the heel rot clamp
	heel_rot_clamp = pm.shadingNode( 'clamp', asUtility=1, n=(whichSide + 'heel_rot_clamp'))


	# Create the ball rot clamp
	ball_rot_clamp = pm.shadingNode( 'clamp', asUtility=1, n=(whichSide + 'ball_0toB_clamp') )

	# Create the foot bend to straight clamp
	footBtoS_clamp = pm.shadingNode( 'clamp', asUtility=1, n=(whichSide + 'footBtoS_clamp' ))

	# Create the bend to straight range
	footBtoS_percent = pm.shadingNode( 'setRange', asUtility=1, n=(whichSide + 'footBtoS_percent') )

	# Create the roll mult 
	foot_roll_mult = pm.shadingNode( 'multiplyDivide', asUtility=1, n=(whichSide + 'roll_mult') )

	# Create the toe tap invert mult
	toeTap_invert_mult = pm.shadingNode( 'multiplyDivide', asUtility=1, n=(whichSide + 'toeTap_invert_mult') )

	# Connect the roll attr to the heel rot clamp
	pm.connectAttr( (foot_icon + '.roll'), (heel_rot_clamp + '.inputR'), f=1 )

	heel_rot_clamp.minR.set( -90 )
	pm.connectAttr( (heel_rot_clamp + '.outputR'), (heel_loc + '.rotateX'), f=1)
	pm.connectAttr( (foot_icon + '.roll'), (ball_rot_clamp + '.inputR'), f=1)
	ball_rot_clamp.maxR.set(90)
	pm.connectAttr( (ball_rot_clamp + '.outputR'), (ball_loc + '.rotateX'), f=1)


	pm.connectAttr( (foot_icon + '.toeStraightAngle'), (footBtoS_clamp + '.maxR'), f=1 )
	pm.connectAttr( (foot_icon + '.bendLimitAngle'), (footBtoS_clamp + '.minR'), f=1 )
	pm.connectAttr( (foot_icon + '.roll'), (footBtoS_clamp + '.inputR'), f=1 )

	pm.connectAttr( (footBtoS_clamp + '.maxR'), (footBtoS_percent + '.oldMaxX'), f=1 )
	pm.connectAttr( (footBtoS_clamp + '.minR'), (footBtoS_percent + '.oldMinX'), f=1 )
	pm.setAttr( (footBtoS_percent + '.maxX'), (1) )
	pm.connectAttr( (footBtoS_clamp + '.inputR'), (footBtoS_percent + '.valueX'), f=1 )

	pm.connectAttr( (footBtoS_percent + '.outValueX'), (foot_roll_mult + '.input1X'), f=1 )
	pm.connectAttr( (footBtoS_clamp + '.inputR'), (foot_roll_mult + '.input2X'), f=1 )
	pm.connectAttr( (foot_roll_mult + '.outputX'), (toe_loc + '.rotateX'), f=1 )

	pm.connectAttr( (foot_icon + '.bendLimitAngle'), (ball_rot_clamp + '.maxR'), f=1 )

	# Tilt Setup
	pm.setDrivenKeyframe( (innerBank_loc + '.rotateZ'), currentDriver=foot_icon + '.tilt' )
	pm.setDrivenKeyframe( (outerBank_loc + '.rotateZ'), currentDriver=foot_icon + '.tilt' ) 
	foot_selection.tilt.set( -90 )
	outerBank_loc.rz.set( 90 )
	# pm.setAttr("foot_icon.tilt", -90)
	# pm.setAttr("innerBank_loc.rotateZ", 90)
	pm.setDrivenKeyframe( (outerBank_loc + '.rotateZ'), currentDriver=foot_icon + '.tilt' )
	foot_selection.tilt.set( 90 )
	innerBank_loc.rz.set( -90 )
	pm.setDrivenKeyframe( (innerBank_loc + '.rotateZ'), currentDriver=foot_icon + '.tilt' )
	foot_selection.tilt.set( 0 )

	# Toe Tap setup
	toeTap_pivot = pm.group(empty=1, n=(whichSide + 'toeTap_pivot') )
	temp_constraint = pm.parentConstraint( jointHierarchy[3], toeTap_pivot )
	pm.delete(temp_constraint)
	freezeTransform()
	pm.parent( toe_ikh, toeTap_pivot )
	pm.parent( toeTap_pivot, toe_loc )
	pm.setAttr( (toeTap_invert_mult + '.input2X'), -1 )
	pm.connectAttr( (foot_icon + '.toeTap'), (toeTap_invert_mult + '.input1X'), f=1 )
	pm.connectAttr( (toeTap_invert_mult + '.input1X'), (toeTap_pivot + '.rotateX'), f=1 )

	# Create ball 0 to bend percent range
	ball_0toB_percent = pm.shadingNode( 'setRange', asUtility=1, n=(whichSide + 'ball_0toB_percent') )

	# Create foot invert percent plusAve
	foot_invert_percent = pm.shadingNode( 'plusMinusAverage', asUtility=1, n=(whichSide + 'foot_invert_percent') )

	# Create ball percent mult
	ball_percent_mult = pm.shadingNode( 'multiplyDivide', asUtility=1, n=(whichSide + 'ball_percent_mult') )

	# Create ball roll mult
	ball_roll_mult = pm.shadingNode( 'multiplyDivide', asUtility=1, n=(whichSide + 'ball_roll_mult') )


	pm.connectAttr( (ball_rot_clamp + '.maxR'), ball_0toB_percent + '.oldMaxX', f=1 )
	pm.connectAttr( (ball_rot_clamp + '.minR'), ball_0toB_percent + '.oldMinX', f=1 )
	pm.setAttr( (ball_0toB_percent + '.maxX'), 1 )
	pm.connectAttr( (ball_rot_clamp + '.inputR'), (ball_0toB_percent + '.valueX'), f=1 )

	pm.setAttr( (foot_invert_percent + '.input1D[0]'), 1 )
	pm.setAttr( (foot_invert_percent + '.input1D[1]'), 1 )
	pm.connectAttr( (footBtoS_percent + '.outValueX'), (foot_invert_percent + '.input1D[1]'), f=1 )
	pm.setAttr( (foot_invert_percent + '.operation'), 2 )

	pm.connectAttr( (ball_0toB_percent + '.outValueX'), (ball_percent_mult + '.input1X'), f=1 )
	pm.connectAttr( (foot_invert_percent + '.output1D'), (ball_percent_mult + '.input2X'), f=1 )

	pm.connectAttr( (ball_percent_mult + '.outputX'), (ball_roll_mult + '.input1X'), f=1 )
	pm.connectAttr( (foot_icon + '.roll'), (ball_roll_mult + '.input2X'), f=1 )
	pm.connectAttr( (ball_roll_mult + '.outputX'), (ball_loc + '.rotateX'), f=1 )

	pm.parent( ball_ikh, ball_loc )
	pm.parent( leg_ikh, ankle_loc )

	# Lean setup
	pm.connectAttr( (foot_icon + '.lean'), (ball_loc + '.rz'), f=1)

	# Toe spin setup
	pm.connectAttr(( foot_icon + '.toeSpin'), (toe_loc + '.ry'), f=1)


	# Parent the heel and ankle locs
	pm.parent( heel_loc, foot_icon )

	pm.parent( noFlip_local, ankle_loc)

	heel_loc.v.set(0)

	pm.select( cl=1 )

def windowResize(*args):
	if pm.window('BR_bipedLeg_setup', q=1, exists=1):
		pm.window('BR_bipedLeg_setup', e=1, wh=(280, 80), rtf=1)
	else:
		pm.warning('BR_bipedLeg_setup does not exist')

def deleteUI(*args):
	# print('Closing UI')
	pm.deleteUI('BR_bipedLeg_setup')








