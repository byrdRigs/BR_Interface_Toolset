'''
BR_handFinger_setup

How to run:
import BR_Interface_Toolset.BR_handFinger_setup as BR_handFinger_setup
reload(BR_handFinger_setup)
BR_handFinger_setup()
'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel


def deleteHistory(*args):
	pm.delete(ch=1)
	# print 'History Deleted'

def centerPivot(*args):
	pm.xform(cpc=1)
	# print 'Selected pivot centered.'

def freezeTransform(*agrs):
	pm.makeIdentity(apply=1, t=1, r=1, s=1, n=0, pn=1)
	# print 'Transform Frozen'

def parentConstraint_on(*args):
	print 'Parent Constraint with Maintain Offset On'
	selection = pm.ls(sl=1)
	pm.parentConstraint(selection, mo=1)

def parentConstraint_off(*args):
	print 'Parent Constraint with Maintain Offset Off'
	selection = pm.ls(sl=1)
	pm.parentConstraint(selection, mo=0)

def pointConstraint_on(*args):
	print 'Point Constraint with Maintain Offset On'
	selection = pm.ls(sl=1)
	pm.pointConstraint(selection, mo=1)

def pointConstraint_off(*args):
	print 'Point Constraint with Maintain Offset Off'
	selection = pm.ls(sl=1)
	pm.pointConstraint(selection, mo=0)

def orientConstraint_on(*args):
	print 'Orient Constraint with Maintain Offset On'
	selection = pm.ls(sl=1)
	pm.orientConstraint(selection, mo=1)

def orientConstraint_off(*args):
	print 'Orient Constraint with Maintain Offset Off'
	selection = pm.ls(sl=1)
	pm.orientConstraint(selection, mo=0)

def create_circle():
    global icon
    icon = pm.circle( nr=[0,1,0])[0]

def hand_setup():
	global arm_waste, hand_root_joint, hand_joint_2
	selection = pm.ls(sl=1, dag=1)
	arm_waste = selection[0]
	hand_root_joint = selection[1]
	hand_joint_2 = selection[2]
	print 'selection:', selection
	print 'Arm Waste:', arm_waste
	print 'Hand Root Joint:', hand_root_joint
	print 'Hand Joint 2:', hand_joint_2

	create_circle()
	# print 'Hand Icon:', icon
	temp_constraint = pm.parentConstraint(hand_root_joint, icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = hand_root_joint.replace('01_bind', 'icon')
	icon.rename(icon_name)

	hand_local = pm.group(empty=1)

	temp_constraint = pm.parentConstraint(hand_root_joint, hand_local, mo=0)
	pm.delete(temp_constraint)

	local_name = icon.replace('icon', 'local')
	hand_local.rename(local_name)

	pm.parent(icon, hand_local)
	freezeTransform(icon)
	deleteHistory(icon)

	local_const = pm.pointConstraint(arm_waste, hand_local)


	world_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(hand_root_joint, world_pad, mo=0)
	pm.delete(temp_constraint)

	world_name = hand_local.replace('local', 'world')
	world_pad.rename(world_name)

	pm.select(icon, hand_root_joint)
	parentConstraint_on()

	pm.select(arm_waste, world_pad, hand_local)
	const = pm.orientConstraint(arm_waste, world_pad, hand_local, mo=0)
	local_const = const.getWeightAliasList()[0]
	world_const = const.getWeightAliasList()[1]

	print 'Local Const:', local_const
	print 'World Const:', world_const

	pm.addAttr(icon, ln="localWorld", max=10, dv=0, at='double', min=0)
	icon.localWorld.set(e=1, keyable=True)

	world_const.set(0)
	pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')
	icon.localWorld.set(10)
	world_const.set(1)
	local_const.set(0)
	pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')

	pm.addAttr(icon, ln="fkVis", at='bool')
	icon.fkVis.set(e=1, keyable=True)

def fingerSelection():
	global index_joint_system, index_root, index_joint_2, index_joint_3, index_joint_4, index_joint_5
	global middle_joint_system, middle_root, middle_joint_2, middle_joint_3, middle_joint_4, middle_joint_5
	global ring_joint_system, ring_root, ring_joint_2, ring_joint_3, ring_joint_4, ring_joint_5
	global pinky_joint_system, pinky_root, pinky_joint_2, pinky_joint_3, pinky_joint_4, pinky_joint_5
	global thumb_joint_system, thumb_pivot, thumb_joint_1, thumb_joint_2, thumb_joint_3, thumb_joint_4
	global finger_selection
	finger_selection = pm.ls(sl=1)
	index_joint_system = finger_selection[0]
	middle_joint_system = finger_selection[1]
	ring_joint_system = finger_selection[2]
	pinky_joint_system = finger_selection[3]
	thumb_joint_system = finger_selection[4]
	# print 'Selection:', finger_selection
	# print 'Index Joint System:', index_joint_system
	# print 'Middele Joint System:', middle_joint_system
	# print 'Ring Joint System:', ring_joint_system
	# print 'Pinky Joint System:', pinky_joint_system
	# print 'Thumb Joint System:', thumb_joint_system

	index_joints = pm.ls(index_joint_system, dag=1)
	index_root = index_joints[0]
	index_joint_2 = index_joints[1]
	index_joint_3 = index_joints[2]
	index_joint_4 = index_joints[3]
	index_joint_5 = index_joints[4]
	# print 'Index Root:', index_root
	# print 'Index Joint 2:', index_joint_2
	# print 'Index Joint 3:',  index_joint_3
	# print 'Index Joint 4:', index_joint_4
	# print 'Index Joint 5:', index_joint_5 

	middle_joints = pm.ls(middle_joint_system, dag=1)
	middle_root = middle_joints[0]
	middle_joint_2 = middle_joints[1]
	middle_joint_3 = middle_joints[2]
	middle_joint_4 = middle_joints[3]
	middle_joint_5 = middle_joints[4]
	# print 'Index Root:', middle_root
	# print 'Index Joint 2:', middle_joint_2
	# print 'Index Joint 3:',  middle_joint_3
	# print 'Index Joint 4:', middle_joint_4
	# print 'Index Joint 5:', middle_joint_5 

	ring_joints = pm.ls(ring_joint_system, dag=1)
	ring_root = ring_joints[0]
	ring_joint_2 = ring_joints[1]
	ring_joint_3 = ring_joints[2]
	ring_joint_4 = ring_joints[3]
	ring_joint_5 = ring_joints[4]
	# print 'Index Root:', ring_root
	# print 'Index Joint 2:', ring_joint_2
	# print 'Index Joint 3:',  ring_joint_3
	# print 'Index Joint 4:', ring_joint_4
	# print 'Index Joint 5:', ring_joint_5

	pinky_joints = pm.ls(pinky_joint_system, dag=1)
	pinky_root = pinky_joints[0]
	pinky_joint_2 = pinky_joints[1]
	pinky_joint_3 = pinky_joints[2]
	pinky_joint_4 = pinky_joints[3]
	pinky_joint_5 = pinky_joints[4]
	# print 'Index Root:', pinky_root
	# print 'Index Joint 2:', pinky_joint_2
	# print 'Index Joint 3:',  pinky_joint_3
	# print 'Index Joint 4:', pinky_joint_4
	# print 'Index Joint 5:', pinky_joint_5

	thumb_joints = pm.ls(thumb_joint_system, dag=1)
	thumb_pivot = thumb_joints[0]
	thumb_joint_1 = thumb_joints[1]
	thumb_joint_2 = thumb_joints[2]
	thumb_joint_3 = thumb_joints[3]
	thumb_joint_4 = thumb_joints[4]
	# print 'Index Root:', thumb_pivot
	# print 'Index Joint 2:', thumb_joint_1
	# print 'Index Joint 3:',  thumb_joint_2
	# print 'Index Joint 4:', thumb_joint_3
	# print 'Index Joint 5:', thumb_joint_4

def ik_finger_setup():
	'''
	Create the finger parent joint
	'''
	hand_base = pm.joint()

	temp_constraint = pm.parentConstraint(hand_root_joint, hand_base, mo=0)
	pm.delete(temp_constraint)

	joint_name = hand_root_joint.replace('01_bind', 'temp')
	hand_base.rename(joint_name)

	pm.parent(hand_base, w=1)

	'''
	Un=parent the thumb_01 from the pivot
	'''
	pm.parent(thumb_joint_1, w=1)
	pm.select(hand_base)
	freezeTransform()
	'''
	Parent the finger joints under the base joint
	'''
	pm.parent(index_root, middle_root, ring_root, pinky_root, thumb_joint_1, hand_base)
	
	'''
	Orient the Joints
	'''
	pm.joint(hand_base, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	
	
	'''
	Parent the thumb_01 back to the pivot
	'''
	pm.parent(thumb_joint_1, thumb_pivot)
	pm.parent(thumb_pivot, hand_base)

	pm.parent(index_root, middle_root, ring_root, pinky_root, thumb_pivot, w=1)

def indexSetup():
	global ind_fk_root, ind_fk_joint_2, ind_fk_joint_3, ind_fk_joint_4, ind_fk_joint_5
	global ind_fkOri_root, ind_fkOri_joint_2, ind_fkOri_joint_3, ind_fkOri_joint_4, ind_fkOri_joint_5
	global ind_fk_01_shape, ind_fk_02_shape, ind_fk_03_shape
	'''
	Index
	'''

	index_joint_5.jointOrientX.set(0)
	index_root.rotateOrder.set(5)
	index_joint_2.rotateOrder.set(5)
	index_joint_3.rotateOrder.set(5)
	index_joint_4.rotateOrder.set(5)
	index_joint_5.rotateOrder.set(5)
	'''
	Duplicate the bind for the "Ori" joints
	'''
	index_ori_joint_system = pm.duplicate(index_root)
	index_ori_joints = pm.ls(index_ori_joint_system, sl=1, dag=1)
	print 'Index Ori Joints:', index_ori_joints
	ind_ori_root = index_ori_joints[0]
	ind_ori_joint_2 = index_ori_joints[1]
	ind_ori_joint_3 = index_ori_joints[2]
	ind_ori_joint_4 = index_ori_joints[3]
	ind_ori_joint_5 = index_ori_joints[4]

	pm.mel.searchReplaceNames('bind', 'ori', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'ori', 'hierarchy')
	joint_name = index_root.replace('bind', 'ori')
	ind_ori_root.rename(joint_name)

	'''
	Parent the ori and bind
	'''

	pm.parent(ind_ori_root, index_root)
	pm.parent(ind_ori_joint_2, index_joint_2)
	pm.parent(index_joint_2, ind_ori_root)

	pm.parent(ind_ori_joint_3, index_joint_3)
	pm.parent(index_joint_3, ind_ori_joint_2)

	pm.parent(ind_ori_joint_4, index_joint_4)
	pm.parent(index_joint_4, ind_ori_joint_3)

	pm.parent(ind_ori_joint_5, index_joint_5)
	pm.parent(index_joint_5, ind_ori_joint_4)

	'''
	Creat the fk joints
	'''

	index_fk_joint_system = pm.duplicate(index_root)
	pm.select(index_fk_joint_system)
	index_fk_joints = pm.ls(index_fk_joint_system, sl=1, dag=1)
	print 'Index Fk Joints:', index_fk_joints
	ind_fk_root = index_fk_joints[0]
	ind_fkOri_root = index_fk_joints[1]

	ind_fk_joint_2 = index_fk_joints[2]
	ind_fkOri_joint_2 = index_fk_joints[3]

	ind_fk_joint_3 = index_fk_joints[4]
	ind_fkOri_joint_3 = index_fk_joints[5]

	ind_fk_joint_4 = index_fk_joints[6]
	ind_fkOri_joint_4 = index_fk_joints[7]

	ind_fk_joint_5 = index_fk_joints[8]
	ind_fkOri_joint_5 = index_fk_joints[9]

	pm.mel.searchReplaceNames('bind', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('ori', 'fkOri', 'hierarchy')
	joint_name = index_root.replace('bind', 'fk')
	ind_fk_root.rename(joint_name)
	print 'Fk Ori Root Joint:', ind_fkOri_root

	'''
	Connect the fk joints to the bind
	'''
	pm.connectAttr(ind_fk_root + '.rotate', index_root + '.rotate')
	pm.connectAttr(ind_fk_joint_2 + '.rotate', index_joint_2 + '.rotate')
	pm.connectAttr(ind_fk_joint_3 + '.rotate', index_joint_3 + '.rotate')
	pm.connectAttr(ind_fk_joint_4 + '.rotate', index_joint_4 + '.rotate')
	pm.connectAttr(ind_fk_joint_5 + '.rotate', index_joint_5 + '.rotate')

	'''
	Connect the fkOri joints to the ori
	'''
	pm.connectAttr(ind_fkOri_root + '.rotate', ind_ori_root + '.rotate')
	pm.connectAttr(ind_fkOri_joint_2 + '.rotate', ind_ori_joint_2 + '.rotate')
	pm.connectAttr(ind_fkOri_joint_3 + '.rotate', ind_ori_joint_3 + '.rotate')
	pm.connectAttr(ind_fkOri_joint_4 + '.rotate', ind_ori_joint_4 + '.rotate')
	pm.connectAttr(ind_fkOri_joint_5 + '.rotate', ind_ori_joint_5 + '.rotate')

	pm.connectAttr(ind_fkOri_joint_2 + '.translate', ind_ori_joint_2 + '.translate')
	pm.connectAttr(ind_fkOri_joint_3 + '.translate', ind_ori_joint_3 + '.translate')
	pm.connectAttr(ind_fkOri_joint_4 + '.translate', ind_ori_joint_4 + '.translate')

	'''
	Create the fk icons
	'''
	
	ind_fk_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	ind_fk_01_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	ind_fk_01_shape = selection[1]
	print 'Icon Shape:', ind_fk_01_shape

	pm.parent(ind_fk_01_shape, ind_fk_joint_2, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = ind_fk_joint_2.replace('fk', 'fk_icon')
	ind_fk_01_shape.rename(icon_name)

	ind_fk_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	ind_fk_02_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	ind_fk_02_shape = selection[1]
	print 'Icon Shape:', ind_fk_02_shape

	pm.parent(ind_fk_02_shape, ind_fk_joint_3, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = ind_fk_joint_3.replace('fk', 'fk_icon')
	ind_fk_02_shape.rename(icon_name)


	ind_fk_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	ind_fk_03_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	ind_fk_03_shape = selection[1]
	print 'Icon Shape:', ind_fk_03_shape

	pm.parent(ind_fk_03_shape, ind_fk_joint_4, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = ind_fk_joint_4.replace('fk', 'fk_icon')
	ind_fk_03_shape.rename(icon_name)

	pm.delete(ind_fk_01_icon, ind_fk_02_icon, ind_fk_03_icon)

	'''
	Setting the overrides
	'''
	pm.select(ind_fk_root, ind_fk_joint_2, ind_fk_joint_3, ind_fk_joint_4, ind_fk_joint_5, ind_fkOri_root, ind_fkOri_joint_2, ind_fkOri_joint_3, ind_fkOri_joint_4, ind_fkOri_joint_5)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 1)
		pm.setAttr(each + '.overrideLevelOfDetail', 1)

	pm.select(ind_fk_01_shape, ind_fk_02_shape, ind_fk_03_shape)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 0)
		pm.setAttr(each + '.overrideLevelOfDetail', 0)


def middleSetup():
	global mid_fk_root, mid_fk_joint_2, mid_fk_joint_3, mid_fk_joint_4, mid_fk_joint_5
	global mid_fkOri_root, mid_fkOri_joint_2, mid_fkOri_joint_3, mid_fkOri_joint_4, mid_fkOri_joint_5
	global mid_fk_01_shape, mid_fk_02_shape, mid_fk_03_shape

	'''
	Middle
	'''
	middle_joint_5.jointOrientX.set(0)

	middle_root.rotateOrder.set(5)
	middle_joint_2.rotateOrder.set(5)
	middle_joint_3.rotateOrder.set(5)
	middle_joint_4.rotateOrder.set(5)
	middle_joint_5.rotateOrder.set(5)

	'''
	Duplicate the bind for the "Ori" joints
	'''
	middle_ori_joint_system = pm.duplicate(middle_root)
	pm.select(middle_ori_joint_system)
	middle_ori_joints = pm.ls(middle_ori_joint_system, sl=1, dag=1)
	print 'Middle Ori Joints:', middle_ori_joints
	mid_ori_root = middle_ori_joints[0]
	mid_ori_joint_2 = middle_ori_joints[1]
	mid_ori_joint_3 = middle_ori_joints[2]
	mid_ori_joint_4 = middle_ori_joints[3]
	mid_ori_joint_5 = middle_ori_joints[4]

	pm.mel.searchReplaceNames('bind', 'ori', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'ori', 'hierarchy')
	joint_name = middle_root.replace('bind', 'ori')
	mid_ori_root.rename(joint_name)
	
	pm.parent(mid_ori_root, middle_root)
	pm.parent(mid_ori_joint_2, middle_joint_2)
	pm.parent(middle_joint_2, mid_ori_root)

	pm.parent(mid_ori_joint_3, middle_joint_3)
	pm.parent(middle_joint_3, mid_ori_joint_2)

	pm.parent(mid_ori_joint_4, middle_joint_4)
	pm.parent(middle_joint_4, mid_ori_joint_3)

	pm.parent(mid_ori_joint_5, middle_joint_5)
	pm.parent(middle_joint_5, mid_ori_joint_4)


	'''
	Creat the fk joints
	'''

	middle_fk_joint_system = pm.duplicate(middle_root)
	pm.select(middle_fk_joint_system)
	middle_fk_joints = pm.ls(middle_fk_joint_system, sl=1, dag=1)
	print 'Index Fk Joints:', middle_fk_joints
	mid_fk_root = middle_fk_joints[0]
	mid_fkOri_root = middle_fk_joints[1]

	mid_fk_joint_2 = middle_fk_joints[2]
	mid_fkOri_joint_2 = middle_fk_joints[3]

	mid_fk_joint_3 = middle_fk_joints[4]
	mid_fkOri_joint_3 = middle_fk_joints[5]

	mid_fk_joint_4 = middle_fk_joints[6]
	mid_fkOri_joint_4 = middle_fk_joints[7]

	mid_fk_joint_5 = middle_fk_joints[8]
	mid_fkOri_joint_5 = middle_fk_joints[9]

	pm.mel.searchReplaceNames('bind', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('ori', 'fkOri', 'hierarchy')
	joint_name = middle_root.replace('bind', 'fk')
	mid_fk_root.rename(joint_name)

	'''
	Connect the fk joints to the bind
	'''
	pm.connectAttr(mid_fk_root + '.rotate', middle_root + '.rotate')
	pm.connectAttr(mid_fk_joint_2 + '.rotate', middle_joint_2 + '.rotate')
	pm.connectAttr(mid_fk_joint_3 + '.rotate', middle_joint_3 + '.rotate')
	pm.connectAttr(mid_fk_joint_4 + '.rotate', middle_joint_4 + '.rotate')
	pm.connectAttr(mid_fk_joint_5 + '.rotate', middle_joint_5 + '.rotate')

	'''
	Connect the fkOri joints to the ori
	'''
	pm.connectAttr(mid_fkOri_root + '.rotate', mid_ori_root + '.rotate')
	pm.connectAttr(mid_fkOri_joint_2 + '.rotate', mid_ori_joint_2 + '.rotate')
	pm.connectAttr(mid_fkOri_joint_3 + '.rotate', mid_ori_joint_3 + '.rotate')
	pm.connectAttr(mid_fkOri_joint_4 + '.rotate', mid_ori_joint_4 + '.rotate')
	pm.connectAttr(mid_fkOri_joint_5 + '.rotate', mid_ori_joint_5 + '.rotate')

	pm.connectAttr(mid_fkOri_joint_2 + '.translate', mid_ori_joint_2 + '.translate')
	pm.connectAttr(mid_fkOri_joint_3 + '.translate', mid_ori_joint_3 + '.translate')
	pm.connectAttr(mid_fkOri_joint_4 + '.translate', mid_ori_joint_4 + '.translate')

	'''
	Create the fk icons
	'''
	mid_fk_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	mid_fk_01_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	mid_fk_01_shape = selection[1]
	print 'Icon Shape:', mid_fk_01_shape

	pm.parent(mid_fk_01_shape, mid_fk_joint_2, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = mid_fk_joint_2.replace('fk', 'fk_icon')
	mid_fk_01_shape.rename(icon_name)

	mid_fk_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	mid_fk_02_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	mid_fk_02_shape = selection[1]
	print 'Icon Shape:', mid_fk_02_shape

	pm.parent(mid_fk_02_shape, mid_fk_joint_3, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = mid_fk_joint_3.replace('fk', 'fk_icon')
	mid_fk_02_shape.rename(icon_name)


	mid_fk_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	mid_fk_03_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	mid_fk_03_shape = selection[1]
	print 'Icon Shape:', mid_fk_03_shape

	pm.parent(mid_fk_03_shape, mid_fk_joint_4, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = mid_fk_joint_4.replace('fk', 'fk_icon')
	mid_fk_03_shape.rename(icon_name)

	pm.delete(mid_fk_01_icon, mid_fk_02_icon, mid_fk_03_icon)

	'''
	Setting the overrides
	'''
	pm.select(mid_fk_root, mid_fk_joint_2, mid_fk_joint_3, mid_fk_joint_4, mid_fk_joint_5, mid_fkOri_root, mid_fkOri_joint_2, mid_fkOri_joint_3, mid_fkOri_joint_4, mid_fkOri_joint_5)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 1)
		pm.setAttr(each + '.overrideLevelOfDetail', 1)

	pm.select(mid_fk_01_shape, mid_fk_02_shape, mid_fk_03_shape)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 0)
		pm.setAttr(each + '.overrideLevelOfDetail', 0)


def ringSetup():
	global ring_fk_root, ring_fk_joint_2, ring_fk_joint_3, ring_fk_joint_4, ring_fk_joint_5
	global ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4, ring_fkOri_joint_5
	global ring_fk_01_shape, ring_fk_02_shape, ring_fk_03_shape

	'''
	Ring
	'''
	ring_joint_5.jointOrientX.set(0)

	ring_root.rotateOrder.set(5)
	ring_joint_2.rotateOrder.set(5)
	ring_joint_3.rotateOrder.set(5)
	ring_joint_4.rotateOrder.set(5)
	ring_joint_5.rotateOrder.set(5)

	'''
	Duplicate the bind for the "Ori" joints
	'''
	ring_ori_joint_system = pm.duplicate(ring_root)
	pm.select(ring_ori_joint_system)
	ring_ori_joints = pm.ls(ring_ori_joint_system, sl=1, dag=1)
	print 'Ring Ori Joints:', ring_ori_joints
	ring_ori_root = ring_ori_joints[0]
	ring_ori_joint_2 = ring_ori_joints[1]
	ring_ori_joint_3 = ring_ori_joints[2]
	ring_ori_joint_4 = ring_ori_joints[3]
	ring_ori_joint_5 = ring_ori_joints[4]

	pm.mel.searchReplaceNames('bind', 'ori', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'ori', 'hierarchy')
	joint_name = ring_root.replace('bind', 'ori')
	ring_ori_root.rename(joint_name)

	pm.parent(ring_ori_root, ring_root)
	pm.parent(ring_ori_joint_2, ring_joint_2)
	pm.parent(ring_joint_2, ring_ori_root)

	pm.parent(ring_ori_joint_3, ring_joint_3)
	pm.parent(ring_joint_3, ring_ori_joint_2)

	pm.parent(ring_ori_joint_4, ring_joint_4)
	pm.parent(ring_joint_4, ring_ori_joint_3)

	pm.parent(ring_ori_joint_5, ring_joint_5)
	pm.parent(ring_joint_5, ring_ori_joint_4)

	'''
	Creat the fk joints
	'''

	ring_fk_joint_system = pm.duplicate(ring_root)
	pm.select(ring_fk_joint_system)
	ring_fk_joints = pm.ls(ring_fk_joint_system, sl=1, dag=1)
	print 'Index Fk Joints:', ring_fk_joints
	ring_fk_root = ring_fk_joints[0]
	ring_fkOri_root = ring_fk_joints[1]

	ring_fk_joint_2 = ring_fk_joints[2]
	ring_fkOri_joint_2 = ring_fk_joints[3]

	ring_fk_joint_3 = ring_fk_joints[4]
	ring_fkOri_joint_3 = ring_fk_joints[5]

	ring_fk_joint_4 = ring_fk_joints[6]
	ring_fkOri_joint_4 = ring_fk_joints[7]

	ring_fk_joint_5 = ring_fk_joints[8]
	ring_fkOri_joint_5 = ring_fk_joints[9]

	pm.mel.searchReplaceNames('bind', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('ori', 'fkOri', 'hierarchy')
	joint_name = ring_root.replace('bind', 'fk')
	ring_fk_root.rename(joint_name)

	'''
	Connect the fk joints to the bind
	'''
	pm.connectAttr(ring_fk_root + '.rotate', ring_root + '.rotate')
	pm.connectAttr(ring_fk_joint_2 + '.rotate', ring_joint_2 + '.rotate')
	pm.connectAttr(ring_fk_joint_3 + '.rotate', ring_joint_3 + '.rotate')
	pm.connectAttr(ring_fk_joint_4 + '.rotate', ring_joint_4 + '.rotate')
	pm.connectAttr(ring_fk_joint_5 + '.rotate', ring_joint_5 + '.rotate')

	'''
	Connect the fkOri joints to the ori
	'''
	pm.connectAttr(ring_fkOri_root + '.rotate', ring_ori_root + '.rotate')
	pm.connectAttr(ring_fkOri_joint_2 + '.rotate', ring_ori_joint_2 + '.rotate')
	pm.connectAttr(ring_fkOri_joint_3 + '.rotate', ring_ori_joint_3 + '.rotate')
	pm.connectAttr(ring_fkOri_joint_4 + '.rotate', ring_ori_joint_4 + '.rotate')
	pm.connectAttr(ring_fkOri_joint_5 + '.rotate', ring_ori_joint_5 + '.rotate')

	pm.connectAttr(ring_fkOri_joint_2 + '.translate', ring_ori_joint_2 + '.translate')
	pm.connectAttr(ring_fkOri_joint_3 + '.translate', ring_ori_joint_3 + '.translate')
	pm.connectAttr(ring_fkOri_joint_4 + '.translate', ring_ori_joint_4 + '.translate')

	'''
	Create the fk icons
	'''
	ring_fk_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	ring_fk_01_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	ring_fk_01_shape = selection[1]
	print 'Icon Shape:', ring_fk_01_shape

	pm.parent(ring_fk_01_shape, ring_fk_joint_2, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = ring_fk_joint_2.replace('fk', 'fk_icon')
	ring_fk_01_shape.rename(icon_name)

	ring_fk_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	ring_fk_02_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	ring_fk_02_shape = selection[1]
	print 'Icon Shape:', ring_fk_02_shape

	pm.parent(ring_fk_02_shape, ring_fk_joint_3, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = ring_fk_joint_3.replace('fk', 'fk_icon')
	ring_fk_02_shape.rename(icon_name)


	ring_fk_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	ring_fk_03_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	ring_fk_03_shape = selection[1]
	print 'Icon Shape:', ring_fk_03_shape

	pm.parent(ring_fk_03_shape, ring_fk_joint_4, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = ring_fk_joint_4.replace('fk', 'fk_icon')
	ring_fk_03_shape.rename(icon_name)

	pm.delete(ring_fk_01_icon, ring_fk_02_icon, ring_fk_03_icon)

	'''
	Setting the overrides
	'''
	pm.select(ring_fk_root, ring_fk_joint_2, ring_fk_joint_3, ring_fk_joint_4, ring_fk_joint_5, ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4, ring_fkOri_joint_5)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 1)
		pm.setAttr(each + '.overrideLevelOfDetail', 1)

	pm.select(ring_fk_01_shape, ring_fk_02_shape, ring_fk_03_shape)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 0)
		pm.setAttr(each + '.overrideLevelOfDetail', 0)


def pinkySetup():
	global pinky_fk_root, pinky_fk_joint_2, pinky_fk_joint_3, pinky_fk_joint_4, pinky_fk_joint_5
	global pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4, pinky_fkOri_joint_5
	global pinky_fk_01_shape, pinky_fk_02_shape, pinky_fk_03_shape

	'''
	Pinky
	'''
	pinky_joint_5.jointOrientX.set(0)

	pinky_root.rotateOrder.set(5)
	pinky_joint_2.rotateOrder.set(5)
	pinky_joint_3.rotateOrder.set(5)
	pinky_joint_4.rotateOrder.set(5)
	pinky_joint_5.rotateOrder.set(5)

	'''
	Duplicate the bind for the "Ori" joints
	'''
	pinky_ori_joint_system = pm.duplicate(pinky_root)
	pm.select(pinky_ori_joint_system)
	pinky_ori_joints = pm.ls(pinky_ori_joint_system, sl=1, dag=1)
	print 'Pinky Ori Joints:', pinky_ori_joints
	pinky_ori_root = pinky_ori_joints[0]
	pinky_ori_joint_2 = pinky_ori_joints[1]
	pinky_ori_joint_3 = pinky_ori_joints[2]
	pinky_ori_joint_4 = pinky_ori_joints[3]
	pinky_ori_joint_5 = pinky_ori_joints[4]

	pm.mel.searchReplaceNames('bind', 'ori', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'ori', 'hierarchy')
	joint_name = pinky_root.replace('bind', 'ori')
	pinky_ori_root.rename(joint_name)

	pm.parent(pinky_ori_root, pinky_root)
	pm.parent(pinky_ori_joint_2, pinky_joint_2)
	pm.parent(pinky_joint_2, pinky_ori_root)

	pm.parent(pinky_ori_joint_3, pinky_joint_3)
	pm.parent(pinky_joint_3, pinky_ori_joint_2)

	pm.parent(pinky_ori_joint_4, pinky_joint_4)
	pm.parent(pinky_joint_4, pinky_ori_joint_3)

	pm.parent(pinky_ori_joint_5, pinky_joint_5)
	pm.parent(pinky_joint_5, pinky_ori_joint_4)

	'''
	Creat the fk joints
	'''

	pinky_fk_joint_system = pm.duplicate(pinky_root)
	pm.select(pinky_fk_joint_system)
	pinky_fk_joints = pm.ls(pinky_fk_joint_system, sl=1, dag=1)
	print 'Index Fk Joints:', pinky_fk_joints
	pinky_fk_root = pinky_fk_joints[0]
	pinky_fkOri_root = pinky_fk_joints[1]

	pinky_fk_joint_2 = pinky_fk_joints[2]
	pinky_fkOri_joint_2 = pinky_fk_joints[3]

	pinky_fk_joint_3 = pinky_fk_joints[4]
	pinky_fkOri_joint_3 = pinky_fk_joints[5]

	pinky_fk_joint_4 = pinky_fk_joints[6]
	pinky_fkOri_joint_4 = pinky_fk_joints[7]

	pinky_fk_joint_5 = pinky_fk_joints[8]
	pinky_fkOri_joint_5 = pinky_fk_joints[9]

	pm.mel.searchReplaceNames('bind', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('ori', 'fkOri', 'hierarchy')
	joint_name = pinky_root.replace('bind', 'fk')
	pinky_fk_root.rename(joint_name)

	'''
	Connect the fk joints to the bind
	'''
	pm.connectAttr(pinky_fk_root + '.rotate', pinky_root + '.rotate')
	pm.connectAttr(pinky_fk_joint_2 + '.rotate', pinky_joint_2 + '.rotate')
	pm.connectAttr(pinky_fk_joint_3 + '.rotate', pinky_joint_3 + '.rotate')
	pm.connectAttr(pinky_fk_joint_4 + '.rotate', pinky_joint_4 + '.rotate')
	pm.connectAttr(pinky_fk_joint_5 + '.rotate', pinky_joint_5 + '.rotate')

	'''
	Connect the fkOri joints to the ori
	'''
	pm.connectAttr(pinky_fkOri_root + '.rotate', pinky_ori_root + '.rotate')
	pm.connectAttr(pinky_fkOri_joint_2 + '.rotate', pinky_ori_joint_2 + '.rotate')
	pm.connectAttr(pinky_fkOri_joint_3 + '.rotate', pinky_ori_joint_3 + '.rotate')
	pm.connectAttr(pinky_fkOri_joint_4 + '.rotate', pinky_ori_joint_4 + '.rotate')
	pm.connectAttr(pinky_fkOri_joint_5 + '.rotate', pinky_ori_joint_5 + '.rotate')

	pm.connectAttr(pinky_fkOri_joint_2 + '.translate', pinky_ori_joint_2 + '.translate')
	pm.connectAttr(pinky_fkOri_joint_3 + '.translate', pinky_ori_joint_3 + '.translate')
	pm.connectAttr(pinky_fkOri_joint_4 + '.translate', pinky_ori_joint_4 + '.translate')

	'''
	Create the fk icons
	'''
	pinky_fk_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	pinky_fk_01_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	pinky_fk_01_shape = selection[1]
	print 'Icon Shape:', pinky_fk_01_shape

	pm.parent(pinky_fk_01_shape, pinky_fk_joint_2, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = pinky_fk_joint_2.replace('fk', 'fk_icon')
	pinky_fk_01_shape.rename(icon_name)

	pinky_fk_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	pinky_fk_02_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	pinky_fk_02_shape = selection[1]
	print 'Icon Shape:', pinky_fk_02_shape

	pm.parent(pinky_fk_02_shape, pinky_fk_joint_3, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = pinky_fk_joint_3.replace('fk', 'fk_icon')
	pinky_fk_02_shape.rename(icon_name)


	pinky_fk_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	pinky_fk_03_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	pinky_fk_03_shape = selection[1]
	print 'Icon Shape:', pinky_fk_03_shape

	pm.parent(pinky_fk_03_shape, pinky_fk_joint_4, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = pinky_fk_joint_4.replace('fk', 'fk_icon')
	pinky_fk_03_shape.rename(icon_name)

	pm.delete(pinky_fk_01_icon, pinky_fk_02_icon, pinky_fk_03_icon)

	'''
	Setting the overrides
	'''
	pm.select(pinky_fk_root, pinky_fk_joint_2, pinky_fk_joint_3, pinky_fk_joint_4, pinky_fk_joint_5, pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4, pinky_fkOri_joint_5)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 1)
		pm.setAttr(each + '.overrideLevelOfDetail', 1)

	pm.select(pinky_fk_01_shape, pinky_fk_02_shape, pinky_fk_03_shape)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 0)
		pm.setAttr(each + '.overrideLevelOfDetail', 0)



def thumbSetup():
	global thumb_fk_pivot, thumb_fk_joint_1, thumb_fk_joint_2, thumb_fk_joint_3
	global thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3
	global thumb_fk_piv_shape, thumb_fk_01_shape, thumb_fk_02_shape, thumb_fk_03_shape

	'''
	Thumb
	'''
	thumb_joint_4.jointOrientX.set(0)

	thumb_joint_1.rotateOrder.set(5)
	thumb_joint_2.rotateOrder.set(5)
	thumb_joint_3.rotateOrder.set(5)
	thumb_joint_4.rotateOrder.set(5)

	'''
	Duplicate the bind for the "Ori" joints
	'''
	thumb_ori_joint_system = pm.duplicate(thumb_pivot)
	pm.select(thumb_ori_joint_system)
	thumb_ori_joints = pm.ls(thumb_ori_joint_system, sl=1, dag=1)
	print 'Thumb Ori Joints:', thumb_ori_joints
	thumb_ori_pivot = thumb_ori_joints[0]
	thumb_ori_joint_1 = thumb_ori_joints[1]
	thumb_ori_joint_2 = thumb_ori_joints[2]
	thumb_ori_joint_3 = thumb_ori_joints[3]
	thumb_ori_joint_4 = thumb_ori_joints[4]

	pm.mel.searchReplaceNames('pivot', 'ori', 'hierarchy')
	pm.mel.searchReplaceNames('bind', 'ori', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'ori', 'hierarchy')
	joint_name = thumb_pivot.replace('pivot', 'ori')
	thumb_ori_pivot.rename(joint_name)

	pm.parent(thumb_ori_pivot, thumb_pivot)
	pm.parent(thumb_joint_1, thumb_ori_pivot)

	pm.parent(thumb_ori_joint_1, thumb_joint_1)
	pm.parent(thumb_joint_2, thumb_ori_joint_1)

	pm.parent(thumb_ori_joint_2, thumb_joint_2)
	pm.parent(thumb_joint_3, thumb_ori_joint_2)

	pm.parent(thumb_ori_joint_3, thumb_joint_3)
	pm.parent(thumb_joint_4, thumb_ori_joint_3)


	pm.parent(thumb_ori_joint_4, thumb_joint_4)
	

	'''
	Creat the fk joints
	'''

	thumb_fk_joint_system = pm.duplicate(thumb_pivot)
	pm.select(thumb_fk_joint_system)
	thumb_fk_joints = pm.ls(thumb_fk_joint_system, sl=1, dag=1)
	print 'Index Fk Joints:', thumb_fk_joints
	thumb_fk_pivot = thumb_fk_joints[0]
	thumb_fkOri_pivot = thumb_fk_joints[1]

	thumb_fk_joint_1 = thumb_fk_joints[2]
	thumb_fkOri_joint_1 = thumb_fk_joints[3]

	thumb_fk_joint_2 = thumb_fk_joints[4]
	thumb_fkOri_joint_2 = thumb_fk_joints[5]

	thumb_fk_joint_3 = thumb_fk_joints[6]
	thumb_fkOri_joint_3 = thumb_fk_joints[7]

	thumb_fk_joint_4 = thumb_fk_joints[8]
	thumb_fkOri_joint_4 = thumb_fk_joints[9]

	pm.mel.searchReplaceNames('bind', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('ori', 'fkOri', 'hierarchy')
	joint_name = thumb_pivot.replace('pivot', 'fk')
	thumb_fk_pivot.rename(joint_name)

	'''
	Connect the fk joints to the bind
	'''
	pm.connectAttr(thumb_fk_pivot + '.rotate', thumb_pivot + '.rotate')
	pm.connectAttr(thumb_fk_joint_1 + '.rotate', thumb_joint_1 + '.rotate')
	pm.connectAttr(thumb_fk_joint_2 + '.rotate', thumb_joint_2 + '.rotate')
	pm.connectAttr(thumb_fk_joint_3 + '.rotate', thumb_joint_3 + '.rotate')
	pm.connectAttr(thumb_fk_joint_4 + '.rotate', thumb_joint_4 + '.rotate')

	'''
	Connect the fkOri joints to the ori
	'''
	pm.connectAttr(thumb_fkOri_pivot + '.rotate', thumb_ori_pivot + '.rotate')
	pm.connectAttr(thumb_fkOri_joint_1 + '.rotate', thumb_ori_joint_1 + '.rotate')
	pm.connectAttr(thumb_fkOri_joint_2 + '.rotate', thumb_ori_joint_2 + '.rotate')
	pm.connectAttr(thumb_fkOri_joint_3 + '.rotate', thumb_ori_joint_3 + '.rotate')
	pm.connectAttr(thumb_fkOri_joint_4 + '.rotate', thumb_ori_joint_4 + '.rotate')

	pm.connectAttr(thumb_fkOri_joint_1 + '.translate', thumb_ori_joint_1 + '.translate')
	pm.connectAttr(thumb_fkOri_joint_2 + '.translate', thumb_ori_joint_2 + '.translate')
	pm.connectAttr(thumb_fkOri_joint_3 + '.translate', thumb_ori_joint_3 + '.translate')

	'''
	Create the fk icons
	'''
	thumb_fk_piv_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	thumb_fk_piv_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	thumb_fk_piv_shape = selection[1]
	print 'Icon Shape:', thumb_fk_piv_shape

	pm.parent(thumb_fk_piv_shape, thumb_fk_pivot, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = thumb_fk_pivot.replace('pivot', 'fk_icon')
	thumb_fk_piv_shape.rename(icon_name)


	thumb_fk_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	thumb_fk_01_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	thumb_fk_01_shape = selection[1]
	print 'Icon Shape:', thumb_fk_01_shape

	pm.parent(thumb_fk_01_shape, thumb_fk_joint_1, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = thumb_fk_joint_1.replace('fk', 'fk_icon')
	thumb_fk_01_shape.rename(icon_name)

	thumb_fk_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	thumb_fk_02_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	thumb_fk_02_shape = selection[1]
	print 'Icon Shape:', thumb_fk_02_shape

	pm.parent(thumb_fk_02_shape, thumb_fk_joint_2, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = thumb_fk_joint_2.replace('fk', 'fk_icon')
	thumb_fk_02_shape.rename(icon_name)

	thumb_fk_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]	
	thumb_fk_03_icon.ry.set(90)
	freezeTransform()
	selection =pm.ls(sl=1, dag=1)
	thumb_fk_03_shape = selection[1]
	print 'Icon Shape:', thumb_fk_03_shape

	pm.parent(thumb_fk_03_shape, thumb_fk_joint_3, r=1, s=1)
	freezeTransform()
	deleteHistory()

	icon_name = thumb_fk_joint_3.replace('fk', 'fk_icon')
	thumb_fk_02_shape.rename(icon_name)

	pm.delete(thumb_fk_piv_icon, thumb_fk_01_icon, thumb_fk_02_icon, thumb_fk_03_icon)

	'''
	Setting the overrides
	'''
	pm.select(thumb_fk_pivot, thumb_fk_joint_1, thumb_fk_joint_2, thumb_fk_joint_3, thumb_fk_joint_4, thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3, thumb_fkOri_joint_4)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 1)
		pm.setAttr(each + '.overrideLevelOfDetail', 1)

	pm.select(thumb_fk_piv_shape, thumb_fk_01_shape, thumb_fk_02_shape, thumb_fk_03_shape)
	selection = pm.ls(sl=True)

	for each in selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideDisplayType', 0)
		pm.setAttr(each + '.overrideLevelOfDetail', 0)



def five_finger_setup():
	indexSetup()
	middleSetup()
	ringSetup()
	pinkySetup()
	thumbSetup()


def lock_and_hide(icon, attrs):
	for current_attr in attrs:
		attr = icon.attr(current_attr)
		attr.set(lock=1, keyable=0)


def SDK_icon():
	parent_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=16, r=1, tol=0.01, nr=(1, 0, 0))[0]

	pm.select(parent_icon + '.cv[0]', parent_icon + '.cv[1]', parent_icon + '.cv[9]', parent_icon + '.cv[10]', parent_icon + '.cv[11]', parent_icon + '.cv[12]', parent_icon + '.cv[13]', parent_icon + '.cv[14]', parent_icon + '.cv[15]')            
	first_cv_set = pm.ls(sl=1)
	cmds.move(0, 0, -2, r=1, os=1, wd=1)

	pm.select(parent_icon + '.cv[0]', parent_icon + '.cv[10]', parent_icon + '.cv[11]', parent_icon + '.cv[12]', parent_icon + '.cv[13]', parent_icon + '.cv[14]', parent_icon + '.cv[15]')            
	second_cv_set = pm.ls(sl=1)
	cmds.move(0, 0, -4, r=1, os=1, wd=1)

	index_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	index_icon.sy.set(.6)
	index_icon.sz.set(.6)

	icon_name = index_root.replace('01_bind', 'icon')
	index_icon.rename(icon_name)

	icon_name = index_icon.replace('index', 'fingers')
	parent_icon.rename(icon_name)

	freezeTransform()
	deleteHistory(index_icon)

	middle_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	middle_icon.tz.set(-2)
	middle_icon.sy.set(.6)
	middle_icon.sz.set(.6)
	icon_name = middle_root.replace('01_bind', 'icon')
	middle_icon.rename(icon_name)
	freezeTransform()
	deleteHistory(middle_icon)

	ring_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	ring_icon.tz.set(-4)
	ring_icon.sy.set(.6)
	ring_icon.sz.set(.6)
	icon_name = ring_root.replace('01_bind', 'icon')
	ring_icon.rename(icon_name)
	freezeTransform()
	deleteHistory(ring_icon)

	pinky_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	pinky_icon.tz.set(-6)
	pinky_icon.sy.set(.6)
	pinky_icon.sz.set(.6)
	icon_name = pinky_root.replace('01_bind', 'icon')
	pinky_icon.rename(icon_name)
	freezeTransform()
	deleteHistory(pinky_icon)

	pm.parent(index_icon, middle_icon, ring_icon, pinky_icon, parent_icon)
	pm.select(parent_icon)
	centerPivot()

	temp_constraint = pm.pointConstraint(hand_joint_2, parent_icon, mo=0)
	pm.delete(temp_constraint)
	pm.select(parent_icon)
	freezeTransform()
	deleteHistory()

	parent_icon.ty.set(4)
	pm.select(parent_icon)
	freezeTransform()

	pm.parent(parent_icon, icon)
	freezeTransform()

	pm.select(index_icon, middle_icon, ring_icon, pinky_icon)
	icon_selection = pm.ls(sl=1)

	pm.addAttr(icon_selection, ln='fingerCtrl',  at='enum', en ='-------')
	index_icon.fingerCtrl.set(lock=1, e=1, keyable=1)
	middle_icon.fingerCtrl.set(lock=1, e=1, keyable=1)
	ring_icon.fingerCtrl.set(lock=1, e=1, keyable=1)
	pinky_icon.fingerCtrl.set(lock=1, e=1, keyable=1)

	pm.addAttr(icon_selection, ln='curl', max=10, dv=0, at='double', min=-10)
	
	index_icon.curl.set(e=1, keyable=1)
	middle_icon.curl.set(e=1, keyable=1)
	ring_icon.curl.set(e=1, keyable=1)
	pinky_icon.curl.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='spread', max=10, dv=0, at='double', min=-10)
	index_icon.spread.set(e=1, keyable=1)
	middle_icon.spread.set(e=1, keyable=1)
	ring_icon.spread.set(e=1, keyable=1)
	pinky_icon.spread.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='relax', max=10, dv=0, at='double', min=0)
	index_icon.relax.set(e=1, keyable=1)
	middle_icon.relax.set(e=1, keyable=1)
	ring_icon.relax.set(e=1, keyable=1)
	pinky_icon.relax.set(e=1, keyable=1)

	pm.select(parent_icon)
	icon_selection = pm.ls(sl=1, dag=1)
	index_icon = icon_selection[2]
	middle_icon = icon_selection[4] 
	ring_icon = icon_selection[6]
	pinky_icon = icon_selection[8]
	print 'Index Icon:', index_icon
	print 'Middle Icon:', middle_icon
	print 'Ring Icon:', ring_icon
	print 'Pinky Icon:', pinky_icon

	lock_and_hide(index_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(middle_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(ring_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(pinky_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])

	'''
	Index Curl
	'''
	drivenAttr_curl = [ind_fkOri_root + '.rz', ind_fkOri_joint_2 + '.rz', ind_fkOri_joint_3 + '.rz', ind_fkOri_joint_4 + '.rz']
	driver_curl = (index_icon + '.curl')
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)

	# print "Driven:", driven
	driven_curl= [ind_fkOri_root, ind_fkOri_joint_2, ind_fkOri_joint_3, ind_fkOri_joint_4]
	index_icon.curl.set(10)
	pm.xform(driven_curl, ro=(0, 0, 90))
	ind_fkOri_root.rz.set(15)
	ind_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)
	index_icon.curl.set(-10)
	pm.xform(driven_curl, ro=(0, 0, -10))
	ind_fkOri_joint_2.rz.set(-20)
	ind_fkOri_joint_3.rz.set(-25)
	ind_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)
	drivenKeyframes_curl = (ind_fkOri_root + '_rotateZ', ind_fkOri_joint_2 + '_rotateZ', ind_fkOri_joint_3 + '_rotateZ', ind_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.curl.set(0)

	'''
	Middle Curl
	'''
	drivenAttr_curl = [mid_fkOri_root + '.rz', mid_fkOri_joint_2 + '.rz', mid_fkOri_joint_3 + '.rz', mid_fkOri_joint_4 + '.rz']
	driver_curl = (middle_icon + '.curl')
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)

	# print "Driven:", driven
	driven_curl= [mid_fkOri_root, mid_fkOri_joint_2, mid_fkOri_joint_3, mid_fkOri_joint_4]
	middle_icon.curl.set(10)
	pm.xform(driven_curl, ro=(0, 0, 90))
	mid_fkOri_root.rz.set(15)
	mid_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)
	middle_icon.curl.set(-10)
	pm.xform(driven_curl, ro=(0, 0, -10))
	mid_fkOri_joint_2.rz.set(-20)
	mid_fkOri_joint_3.rz.set(-25)
	mid_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)
	drivenKeyframes_curl = (mid_fkOri_root + '_rotateZ', mid_fkOri_joint_2 + '_rotateZ', mid_fkOri_joint_3 + '_rotateZ', mid_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	middle_icon.curl.set(0)

	'''
	Ring Curl
	'''
	drivenAttr_curl = [ring_fkOri_root + '.rz', ring_fkOri_joint_2 + '.rz', ring_fkOri_joint_3 + '.rz', ring_fkOri_joint_4 + '.rz']
	driver_curl = (ring_icon + '.curl')
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)

	# print "Driven:", driven
	driven_curl= [ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4]
	ring_icon.curl.set(10)
	pm.xform(driven_curl, ro=(0, 0, 90))
	ring_fkOri_root.rz.set(15)
	ring_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)
	ring_icon.curl.set(-10)
	pm.xform(driven_curl, ro=(0, 0, -10))
	ring_fkOri_joint_2.rz.set(-20)
	ring_fkOri_joint_3.rz.set(-25)
	ring_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)
	drivenKeyframes_curl = (ring_fkOri_root + '_rotateZ', ring_fkOri_joint_2 + '_rotateZ', ring_fkOri_joint_3 + '_rotateZ', ring_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	ring_icon.curl.set(0)

	'''
	Pinky Curl
	'''
	drivenAttr_curl = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	driver_curl = (pinky_icon + '.curl')
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)

	# print "Driven:", driven
	driven_curl= [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_icon.curl.set(10)
	pm.xform(driven_curl, ro=(0, 0, 90))
	pinky_fkOri_root.rz.set(15)
	pinky_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)
	pinky_icon.curl.set(-10)
	pm.xform(driven_curl, ro=(0, 0, -10))
	pinky_fkOri_joint_2.rz.set(-20)
	pinky_fkOri_joint_3.rz.set(-25)
	pinky_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(drivenAttr_curl, currentDriver=driver_curl)
	drivenKeyframes_curl = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.curl.set(0)



	'''
	Index Spread
	'''
	drivenAttr_spread = (ind_fkOri_root + '.ry', ind_fkOri_joint_2 + '.ry')
	driven_spread= (ind_fkOri_root, ind_fkOri_joint_2)
	driver_spread = (index_icon + '.spread')
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	index_icon.spread.set(10)
	pm.xform(driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	index_icon.spread.set(-10)
	pm.xform(driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	index_icon.spread.set(0)

	drivenKeyframes_spread = (ind_fkOri_root + '_rotateY', ind_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Middle Spread
	'''
	drivenAttr_spread = (mid_fkOri_root + '.ry', mid_fkOri_joint_2 + '.ry')
	driven_spread= (mid_fkOri_root, mid_fkOri_joint_2)
	driver_spread = (middle_icon + '.spread')
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	middle_icon.spread.set(10)
	pm.xform(driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	middle_icon.spread.set(-10)
	pm.xform(driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	middle_icon.spread.set(0)

	drivenKeyframes_spread = (mid_fkOri_root + '_rotateY', mid_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Ring Spread
	'''
	drivenAttr_spread = (ring_fkOri_root + '.ry', ring_fkOri_joint_2 + '.ry')
	driven_spread= (ring_fkOri_root, ring_fkOri_joint_2)
	driver_spread = (ring_icon + '.spread')
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	ring_icon.spread.set(10)
	pm.xform(driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	ring_icon.spread.set(-10)
	pm.xform(driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	ring_icon.spread.set(0)

	drivenKeyframes_spread = (ring_fkOri_root + '_rotateY', ring_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky Spread
	'''
	drivenAttr_spread = (pinky_fkOri_root + '.ry', pinky_fkOri_joint_2 + '.ry')
	driven_spread= (pinky_fkOri_root, pinky_fkOri_joint_2)
	driver_spread = (pinky_icon + '.spread')
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	pinky_icon.spread.set(10)
	pm.xform(driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	pinky_icon.spread.set(-10)
	pm.xform(driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(drivenAttr_spread, currentDriver=driver_spread)
	pinky_icon.spread.set(0)

	drivenKeyframes_spread = (pinky_fkOri_root + '_rotateY', pinky_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)



	'''
	Index Relax
	'''
	drivenAttr_relax = [ind_fkOri_root + '.rz', ind_fkOri_joint_2 + '.rz', ind_fkOri_joint_3 + '.rz', ind_fkOri_joint_4 + '.rz']
	driven_relax = [ind_fkOri_root, ind_fkOri_joint_2, ind_fkOri_joint_3, ind_fkOri_joint_4]
	driver_relax = (index_icon + '.relax')
	pm.setDrivenKeyframe(drivenAttr_relax, currentDriver=driver_relax)
	index_icon.relax.set(10)
	ind_fkOri_root.rz.set(12)
	ind_fkOri_joint_2.rz.set(15)
	ind_fkOri_joint_3.rz.set(18)
	ind_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(drivenAttr_relax, currentDriver=driver_relax)
	index_icon.relax.set(0)

	pm.keyTangent(driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Middle Relax
	'''
	drivenAttr_relax = [mid_fkOri_root + '.rz', mid_fkOri_joint_2 + '.rz', mid_fkOri_joint_3 + '.rz', mid_fkOri_joint_4 + '.rz']
	driven_relax = [mid_fkOri_root, mid_fkOri_joint_2, mid_fkOri_joint_3, mid_fkOri_joint_4]
	driver_relax = (middle_icon + '.relax')
	pm.setDrivenKeyframe(drivenAttr_relax, currentDriver=driver_relax)
	middle_icon.relax.set(10)
	mid_fkOri_root.rz.set(12)
	mid_fkOri_joint_2.rz.set(15)
	mid_fkOri_joint_3.rz.set(18)
	mid_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(drivenAttr_relax, currentDriver=driver_relax)
	middle_icon.relax.set(0)

	pm.keyTangent(driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Ring Relax
	'''
	drivenAttr_relax = [ring_fkOri_root + '.rz', ring_fkOri_joint_2 + '.rz', ring_fkOri_joint_3 + '.rz', ring_fkOri_joint_4 + '.rz']
	driven_relax = [ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4]
	driver_relax = (ring_icon + '.relax')
	pm.setDrivenKeyframe(drivenAttr_relax, currentDriver=driver_relax)
	ring_icon.relax.set(10)
	ring_fkOri_root.rz.set(12)
	ring_fkOri_joint_2.rz.set(15)
	ring_fkOri_joint_3.rz.set(18)
	ring_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(drivenAttr_relax, currentDriver=driver_relax)
	ring_icon.relax.set(0)

	pm.keyTangent(driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky Relax
	'''
	drivenAttr_relax = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	driven_relax = [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	driver_relax = (pinky_icon + '.relax')
	pm.setDrivenKeyframe(drivenAttr_relax, currentDriver=driver_relax)
	pinky_icon.relax.set(10)
	pinky_fkOri_root.rz.set(12)
	pinky_fkOri_joint_2.rz.set(15)
	pinky_fkOri_joint_3.rz.set(18)
	pinky_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(drivenAttr_relax, currentDriver=driver_relax)
	pinky_icon.relax.set(0)

	pm.keyTangent(driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pm.select(index_icon, middle_icon, ring_icon, pinky_icon)
	icon_selection = pm.ls(sl=1)

	color_index = 27

	for each in icon_selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideColor', color_index)
		color_index = color_index + 1

		


'''
Global names
'''
global index_joint_system, index_root, index_joint_2, index_joint_3, index_joint_4, index_joint_5
global middle_joint_system, middle_root, middle_joint_2, middle_joint_3, middle_joint_4, middle_joint_5
global ring_joint_system, ring_root, ring_joint_2, ring_joint_3, ring_joint_4, ring_joint_5
global pinky_joint_system, pinky_root, pinky_joint_2, pinky_joint_3, pinky_joint_4, pinky_joint_5
global thumb_joint_system, thumb_pivot, thumb_joint_1, thumb_joint_2, thumb_joint_3, thumb_joint_4

global ind_ori_root, ind_ori_joint_2, ind_ori_joint_3, ind_ori_joint_4, ind_ori_joint_5
global mid_ori_root, mid_ori_joint_2, mid_ori_joint_3, mid_ori_joint_4, mid_ori_joint_5
global ring_ori_root, ring_ori_joint_2, ring_ori_joint_3, ring_ori_joint_4, ring_ori_joint_5
global pinky_ori_root, pinky_ori_joint_2, pinky_ori_joint_3, pinky_ori_joint_4, pinky_ori_joint_5
global thumb_ori_pivot, thumb_ori_joint_1, thumb_ori_joint_2, thumb_ori_joint_3, thumb_ori_joint_4

global ind_fk_root, ind_fk_joint_2, ind_fk_joint_3, ind_fk_joint_4, ind_fk_joint_5
global ind_fkOri_root, ind_fkOri_joint_2, ind_fkOri_joint_3, ind_fkOri_joint_4, ind_fkOri_joint_5

global mid_fk_root, mid_fk_joint_2, mid_fk_joint_3, mid_fk_joint_4, mid_fk_joint_5
global mid_fkOri_root, mid_fkOri_joint_2, mid_fkOri_joint_3, mid_fkOri_joint_4, mid_fkOri_joint_5

global ring_fk_root, ring_fk_joint_2, ring_fk_joint_3, ring_fk_joint_4, ring_fk_joint_5
global ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4, ring_fkOri_joint_5

global pinky_fk_root, pinky_fk_joint_2, pinky_fk_joint_3, pinky_fk_joint_4, pinky_fk_joint_5
global pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4, pinky_fkOri_joint_5

global thumb_fk_pivot, thumb_fk_joint_1, thumb_fk_joint_2, thumb_fk_joint_3
global thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3

global parent_icon, index_icon, middle_icon, ring_icon, pinky_icon
global ind_fk_01_shape, ind_fk_02_shape, ind_fk_03_shape
global mid_fk_01_shape, mid_fk_02_shape, mid_fk_03_shape
global ring_fk_01_shape, ring_fk_02_shape, ring_fk_03_shape
global pinky_fk_01_shape, pinky_fk_02_shape, pinky_fk_03_shape
global thumb_fk_piv_shape, thumb_fk_01_shape, thumb_fk_02_shape, thumb_fk_03_shape






