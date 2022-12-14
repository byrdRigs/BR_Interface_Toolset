'''
Title: BR_dynamicIkFk
Description
	This file contains: Dynamic IK/FK setup
	
How to run:
	# If you have my folder 
		import BR_Interface_Toolset.BR_dynamicIkFk as dynIkFk 
		reload(dynIkFk)
		dynIkFk.gui()
	# If you don't have my folder
		import BR_dynamicIkFk as dynIkFk 
		reload(dynIkFk)
		dynIkFk.gui()

'''

#-----------------------------------------------------------------------------------
# ByrdRigs Dynamic IK/FK tool v01
#-----------------------------------------------------------------------------------

'''
The starting joints shouldn't have a suffix at the moment.

'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel


tab_bgc=(0.4718592, 0.13568, 239)
subTab_bgc = (0.4915200, 0.32256, 241)
window_bgc = (.2,.2,.2)

def gui():
	if pm.window( 'BR_Dynamic_IKFK_v01', q=1, exists=1 ):
		pm.deleteUI( 'BR_Dynamic_IKFK_v01' )
		#BR_Dynamic_IKFK_v01

	global system_name
	win_width = 300
	window_object = pm.window( 'BR_Dynamic_IKFK_v01', title="ByrdRigs' Dynamic IK/FK Tool", w=win_width, bgc=window_bgc )
	main_layout = pm.columnLayout()
	pm.text( l='This works best with an odd number of joints.', w=win_width, ww=1 )
	system_name = pm.textFieldGrp( l='System Name', text='tail', w=win_width )
	pm.button(l='Go', w=win_width, c=dyn)
	
	

	pm.window( 'BR_Dynamic_IKFK_v01', e=1, wh=(300, 80), rtf=1 )
	pm.showWindow( window_object )

	print( 'Window Created:', window_object )

def deleteHistory(*args):
	pm.delete(ch=1)
	# print 'History Deleted'

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
  	# print( cv_pos )

def dyn(*args):
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
	
	# Now we have a selected joint we can check for the prefix to see wht side it's on
	whichSide = jointRoot[0:3]

	# Make sure the prefix is usable
	if not 'lt_' in whichSide:
		if not 'rt_' in whichSide:
			if not 'ct_' in whichSide:
				pm.error( 'Please use a joint with a usable prefix of either lt_ or rt_ or ct_' )

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

	#---------------------------------------------------------------------------------------
	# Duplicate the main joint chain and rename each joint
	#---------------------------------------------------------------------------------------

	# First define what joint chains we need 
	newJointList = ['_ik', '_fk', '_dyn']

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

	pm.select( jointRoot )
	joint_positions()

	ik_crv = pm.curve( d=3, p=(cv_pos), n=(limbName + '_ik_crv') )

	fk_crv = pm.curve( d=3, p=(cv_pos), n=(limbName + '_fk_crv') )

	dyn_crv = pm.curve( d=3, p=(cv_pos), n=(limbName + '_dyn_crv') )
	
	#---------------------------------------------------------------------------------------
	# Constrain the main joints to the ik and fk joints so we can blend between them
	#---------------------------------------------------------------------------------------
	for i in range( limbJoints ):
		pm.parentConstraint( jointHierarchy[i] + '_dyn', jointHierarchy[i], mo=0 )

	#---------------------------------------------------------------------------------------
	# Get the ikfk switch
	#---------------------------------------------------------------------------------------
	switch = limbName + '_switch'
	# print(switch)

	# Check if the swich exists
	if pm.objExists( switch ):
		pass
	else:
		pm.error("Please make an Ik/Fk switch using the suffix _switch. Also give it the attribute of 'IkFk' as a float with a min of 0 and a max of 1")

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

		if 'ct_' in whichSide:
			pm.setAttr( (crv + '.overrideColor'), 17 )

		# Parent the pads to the icons 
		if i>=1:
			pm.parent( (jointHierarchy[i] + '_fk_local'), (jointHierarchy[i - 1] + '_fk_icon') )
		
		# Constrain the icon and the joints
		pm.parentConstraint( (jointHierarchy[i] + '_fk_icon'), (jointHierarchy[i] + '_fk'), mo=1 )

	# Get cv and create clusters for the fk_crv
	curveCVs = pm.ls( (fk_crv + ".cv[0:]"), fl=True )

	clusterList = []

	for i, cv in enumerate( curveCVs ):
	    clust = pm.cluster( cv, cv, n=(jointHierarchy[i] + '_fk_clust') )
	    clusterList.append( clust )
	    local = pm.group( clust, n=(jointHierarchy[i] + '_clustLocal') )
	    # print(local)
	    pm.parent( (jointHierarchy[i] + '_clustLocal'), (jointHierarchy[i] + '_fk_icon') )
	    pm.setAttr( (jointHierarchy[i] + '_fk_clustHandle.visibility'), 0)

	# Parent the last cluster under the icon before 
	pm.parent( (jointHierarchy[-1] + '_clustLocal'), (jointHierarchy[-2] + '_fk_icon') )

	# Delete the last fk pad and icon
	pm.delete((jointHierarchy[-1] + '_fk_local'))



	# ---------------------------------------------------------------------------------------
	# Setup ik
	# ---------------------------------------------------------------------------------------

	# Create the spline ik 
	pm.ikHandle(c=ik_crv, sj=(jointHierarchy[0] + '_ik'), ee=(jointHierarchy[-1] + '_ik'), ccv=False, pcv=False, sol='ikSplineSolver', n=(limbName + '_ikh') )

	# Duplicate the bind joints
	pm.select(cl=1)
	curveBindList = []
	for i in range(len(jointHierarchy)):
		crvBind = pm.joint( n=(jointHierarchy[i] + '_curveBind'), rad=2, )
		temp_constraint = pm.parentConstraint( jointHierarchy[i], (jointHierarchy[i] + '_curveBind'), mo=0 )
		pm.delete( temp_constraint )
		pm.select(cl=1)
		curveBindList.append(crvBind)
	
	# print( curveBindList )

	# Bind the ik binding joints to the ik_crv
	pm.select( curveBindList, ik_crv )
	pm.mel.SmoothBindSkin()

	# Create the main ik icons 
	ik_icons = []
	ik_locals = []

	for i in curveBindList[0::2]:
		ik_icon = pm.curve( d=1, p=[(1, 1, 1),(1, 1, -1),(-1, 1, -1),(-1, 1, 1),(1, 1, 1),(1, -1, 1),(1, -1, -1),(1, 1, -1),(-1, 1, -1),(-1, -1, -1),(1, -1, -1),(-1, -1, -1),(-1, -1, 1),(-1, 1, 1),(-1, -1, 1),(1, -1, 1)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] )
		temp_constraint = pm.parentConstraint( i, ik_icon, mo=0 )
		pm.delete( temp_constraint )
		pm.xform( scale=[0.25, 1, 1] )
		ik_local = pm.group( empty=1 )
		temp_constraint = pm.parentConstraint( i, ik_local, mo=0 )
		pm.delete( temp_constraint )
		pm.parent( ik_icon, ik_local )
		pm.makeIdentity( ik_icon, a=1, t=1, r=1, s=1)
		pm.delete(ik_icon, ch=1)

		# Parent Constrain the icons to the curveBind joints
		pm.parentConstraint( ik_icon, i, mo=1 )

		ik_icons.append( ik_icon )
		ik_locals.append( ik_local )

		# pm.setAttr(ik_local + '.visibility', 0)

		pm.setAttr( (ik_icon + '.overrideEnabled'), 1 )

		if 'lt_' in whichSide:
			pm.setAttr( (ik_icon + '.overrideColor'), 6 )

		if 'rt_' in whichSide:
			pm.setAttr( (ik_icon + '.overrideColor'), 13 )

		if 'ct_' in whichSide:
			pm.setAttr( (ik_icon + '.overrideColor'), 17 )

	# Rename the icons
	count = 1
	for each in ik_icons:
		new_name = '{0}_0{1}_ik_icon'.format( (limbName), (count) )
		# print( new_name )
		each.rename( new_name )
		count = count + 1

	# Rename the locals
	count = 1
	for each in ik_locals:
		new_name = '{0}_0{1}_ik_local'.format( (limbName), (count) )
		# print( new_name )
		each.rename( new_name )
		count = count + 1

	# Create the first set of tweak icons 
	ik_tweak_icons = []
	ik_tweak_locals = []
	ik_tweak_offsets = []

	for i in curveBindList[1::2]:
		ik_tweak_icon = pm.curve( d=1, p=[(1, 1, 1),(1, 1, -1),(-1, 1, -1),(-1, 1, 1),(1, 1, 1),(1, -1, 1),(1, -1, -1),(1, 1, -1),(-1, 1, -1),(-1, -1, -1),(1, -1, -1),(-1, -1, -1),(-1, -1, 1),(-1, 1, 1),(-1, -1, 1),(1, -1, 1)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] )
		temp_constraint = pm.parentConstraint( i, ik_tweak_icon, mo=0 )
		pm.delete( temp_constraint )
		pm.xform(ik_tweak_icon, scale=[0.5, 0.5, 0.5])
		ik_tweak_local = pm.group( empty=1 )
		temp_constraint = pm.parentConstraint( i, ik_tweak_local, mo=0 )
		pm.delete( temp_constraint )
		pm.parent( ik_tweak_icon, ik_tweak_local )
		ik_tweak_offset = pm.group( ik_tweak_local )
		pm.makeIdentity( ik_tweak_icon, a=1, t=1, r=1, s=1 )
		pm.delete(ik_tweak_icon, ch=1)

		pm.parentConstraint( ik_tweak_icon, i, mo=1 )

		ik_tweak_icons.append(ik_tweak_icon)
		ik_tweak_locals.append(ik_tweak_local)
		ik_tweak_offsets.append(ik_tweak_offset)

		pm.setAttr( (ik_tweak_icon + '.overrideEnabled'), 1 )

		if 'lt_' in whichSide:
			pm.setAttr( (ik_tweak_icon + '.overrideColor'), 18 )

		if 'rt_' in whichSide:
			pm.setAttr( (ik_tweak_icon + '.overrideColor'), 4 )

		if 'ct_' in whichSide:
			pm.setAttr( (ik_tweak_icon + '.overrideColor'), 25 )

	# Rename the icons
	count = 1
	for each in ik_tweak_icons:
		new_name = '{0}_0{1}_tweak_icon'.format( (limbName), (count) )
		# print( new_name )
		each.rename( new_name )
		count = count + 1

	# Rename the locals
	count = 1
	for each in ik_tweak_locals:
		new_name = '{0}_0{1}_tweak_local'.format( (limbName), (count) )
		# print( new_name )
		each.rename( new_name )
		count = count + 1

	# Rename the offsets
	count = 1
	for each in ik_tweak_offsets:
		new_name = '{0}_0{1}_tweak_offset'.format( (limbName), (count) )
		# print( new_name )
		each.rename( new_name )
		count = count + 1

	# Need to figure out how to get the main ik icons to point contrain to the tweak offsets
	# then the main icon after the tweak icon to aim constrain to the tweak local


	# ---------------------------------------------------------------------------------------
	# Group the icons
	# ---------------------------------------------------------------------------------------
	ik_main_icon_grp = pm.group( ik_locals, n=(limbName + '_ik_main_icon_grp') )
	ik_tweak_icon_grp = pm.group( ik_tweak_offsets, n=(limbName + '_ik_tweak_icon_grp') )
	ik_icon_grp = pm.group( empty=1, n=(limbName + '_ik_icon_grp') )
	temp_constraint = pm.parentConstraint( jointRoot, ik_icon_grp, mo=0 )
	pm.delete( temp_constraint )
	pm.parent( ik_main_icon_grp, ik_tweak_icon_grp, ik_icon_grp )

	# ---------------------------------------------------------------------------------------
	# Set the driven keys for visibility
	# ---------------------------------------------------------------------------------------
	
	# Create the attrs for ik and fk vis
	pm.addAttr( switch, ln='ikVis', at='bool' )
	pm.setAttr( (switch + '.ikVis'),  lock=0, keyable=1 )

	pm.addAttr( switch, ln='tweakVis', at='bool' )
	pm.setAttr( (switch + '.tweakVis'),  lock=0, keyable=1 )

	pm.addAttr( switch, ln='fkVis', at='bool' )
	pm.setAttr( (switch + '.fkVis'),  lock=0, keyable=1 )


	# Set the keys
	pm.setAttr( (jointHierarchy[0] + '_fk_icon.visibility'), 0 )
	pm.setDrivenKeyframe( (jointHierarchy[0] + '_fk_icon.visibility'), cd=(switch + '.fkVis') )

	pm.setAttr( (switch + '.fkVis'), 1)
	pm.setAttr( (jointHierarchy[0] + '_fk_icon.visibility'), 1 )
	pm.setDrivenKeyframe( (jointHierarchy[0] + '_fk_icon.visibility'), cd=(switch + '.fkVis') )


	pm.setAttr( (ik_icon_grp + '.visibility'), 0 )
	pm.setDrivenKeyframe( (ik_icon_grp + '.visibility'), cd=(switch + '.ikVis') )

	pm.setAttr( (switch + '.ikVis'), 1)
	pm.setAttr( (ik_icon_grp + '.visibility'), 1 )
	pm.setDrivenKeyframe( (ik_icon_grp + '.visibility'), cd=(switch + '.ikVis') )


	pm.setAttr( (ik_tweak_icon_grp + '.visibility'), 0 )
	pm.setDrivenKeyframe( (ik_tweak_icon_grp + '.visibility'), cd=(switch + '.tweakVis') )

	pm.setAttr( (switch + '.tweakVis'), 1)
	pm.setAttr( (ik_tweak_icon_grp + '.visibility'), 1 )
	pm.setDrivenKeyframe( (ik_tweak_icon_grp + '.visibility'), cd=(switch + '.tweakVis') )

	pm.setAttr( (switch + '.tweakVis'), 0)
	pm.setAttr( (switch + '.fkVis'), 0)

	# ---------------------------------------------------------------------------------------
	# Setup Dynamics
	# ---------------------------------------------------------------------------------------
	
	# Create the hair system
	pm.createNode( 'hairSystem', n=(limbName + '_hairSystemShape') )

	hairSystem = pm.ls( sl=1, dag=1 )[0]
	
	# Assign the solver
	pm.mel.assignNSolver( "" )

	# Get the nucleus and rename 
	nuc = pm.ls( sl=1 )[0]

	new_name = '{0}'.format( (limbName + '_nuc') )
	# print( new_name )

	nuc.rename( new_name )

	# Get the dyn_crv shape
	dyn_crv = pm.ls( dyn_crv, dag=1, type='shape' )
	# print( dyn_crv )

	# Assign the hair system
 	pm.select( dyn_crv )
 	pm.mel.assignHairSystem( hairSystem )

 	# Get the follicle and rename
 	foll = hairSystem.inputHair[0].connections()[0]
 	# print( foll )

 	new_name = '{0}'.format( (limbName + '_foll') )
	# print( new_name )

	foll.rename(new_name)

	# Get the output_crv and rename
 	outCurve = foll.outCurve.connections()[0]
 	# print( outCurve )

 	new_name = '{0}'.format( (limbName + '_outCrv') )
	# print( new_name )

	outCurve.rename(new_name)

	# Create the blendshape with fk crv
	pm.select( fk_crv, outCurve )
	fk_blend = pm.blendShape( n=(limbName + '_fk_bs') )[0]
	# print(fk_blend)

	fk_input = ('.' + fk_crv)
	# print( fk_input )

	# Set the bs attrs 
	pm.setAttr(fk_blend + '.envelope', 0)

	pm.setAttr( str(fk_blend + fk_input),  1 )

	# Create the blendshape with fk crv
	pm.select( ik_crv, outCurve )
	ik_blend = pm.blendShape( n=(limbName + '_ik_bs') )[0]
	# print(ik_blend)

	ik_input = ('.' + ik_crv)
	# print( ik_input )

	# Set the bs attrs
	pm.setAttr(ik_blend + '.envelope', 0)

	pm.setAttr( str(ik_blend + ik_input),  1 )

	# Create a revese node for switching
	reveseNode = pm.shadingNode( 'reverse', asUtility=1, n=(limbName + '_reverse') )

	# Connect the envelope for the ik_blend to the inputX of the reverse
	pm.connectAttr( (ik_blend + '.envelope'), (reveseNode + '.inputX'), f=1 )

	# Connect the output to the envelope of the fk_blend
	pm.connectAttr( (reveseNode + '.outputX'), (fk_blend + '.envelope'), f=1 )

	# Create a reverse node for the ik_blend
	ik_rev = pm.shadingNode( 'reverse', asUtility=1, n=(limbName + '_ik_rev') )

	# Connect the switch to the mult
	pm.connectAttr( (switch + '.IkFk'), (ik_rev + '.inputX'), f=1 )

	# Connect the rev to the envelope of the ik_blend
	pm.connectAttr( (ik_rev + '.outputX'), (ik_blend + '.envelope'), f=1 )

	# Fix the hair shape name, so there isn't an error
	new_name = '{0}'.format('hairSystemShape1')
	# print( new_name )

	hairSystem.rename(new_name)

	# Set up ability to go full dynamic 
	pm.addAttr( switch, ln='fullDynmic', at='float', min=0, max=1, dv=1)
	pm.setAttr( (switch + '.fullDynmic'), lock=0, keyable=1 )

	pm.connectAttr( (switch + '.fullDynmic'), (ik_rev + '.inputY'), f=1 )
	pm.connectAttr( (ik_rev + '.outputY'), str(ik_blend + ik_input), f=1 )
	pm.connectAttr( (ik_rev + '.outputY'), str(fk_blend + fk_input), f=1 )

	# Create the splineIK using the dyn joints and the out crv
	dyn_ik = pm.ikHandle( sol='ikSplineSolver', sj=(jointHierarchy[0] + '_dyn'), ee=(jointHierarchy[-1] + '_dyn'), c=outCurve, ccv=0, pcv=0, n=(limbName + '_dyn_ikh') )[0]


	# ---------------------------------------------------------------------------------------
	# Dynamic clean up
	# ---------------------------------------------------------------------------------------
	foll_grp = (limbName + '_hairSystemFollicles')
	# print( foll_grp )

	output_grp = (limbName + '_hairSystemOutputCurves')
	# print( output_grp )

	dyn_grp = pm.group( foll_grp, output_grp, hairSystem, dyn_ik, n=(limbName + '_dyn_grp') )

	outCurve.inheritsTransform.set(0)


	# Rename the bind joints

	for i in range(limbJoints):
		new_name = '{0}'.format( (jointHierarchy[i] + '_bind') )
		print( new_name )
		jointHierarchy[i].rename( new_name )

def windowResize( *args ):
	if pm.window( 'BR_Dynamic_IKFK_v01', q=1, exists=1 ):
		pm.window( 'BR_Dynamic_IKFK_v01', e=1, wh=(300, 80), rtf=1 )
	else:
		pm.warning( "ByrdRigs' Dynamic IK/FK Tool does not exist" )

def deleteUI( *args ):
	# print('Closing UI')
	pm.deleteUI( 'BR_Dynamic_IKFK_v01' )