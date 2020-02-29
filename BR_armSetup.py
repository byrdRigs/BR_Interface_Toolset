'''
Advanced Arm Set up
'''

import pymel.core as pm 
import maya.cmds as cmds


def twistStartCreation():
	joint_system = pm.ls(sl=True, dag=True)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	print 'Root joint:', root_joint
	print 'Joint 2:', joint_2
	print 'Joint 3:', joint_3

	pm.joint(root_joint, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	joint_3.jointOrientX.set(0)
	joint_3.jointOrientY.set(0)
	root_joint.rotateOrder.set(3)

	twist_chain = pm.duplicate(root_joint)

	twist_chain = pm.ls(sl=True, dag=True)
	tRoot_joint = twist_chain[0]
	tJoint_2 = twist_chain[1]
	tJoint_3 = twist_chain[2]
	print 'Twist Root:', tRoot_joint
	print 'Twist Joint 2:', tJoint_2
	print 'Twist Joint 3:', tJoint_3

	joint_name = root_joint.replace('bind', 'twist')
	tRoot_joint.rename(joint_name)

	joint_name = tRoot_joint.replace('01', '02')
	tJoint_2.rename(joint_name)

	joint_name = tJoint_2.replace('02', '03')
	tJoint_3.rename(joint_name)

	import beJointSplit
	beJointSplit.split()

def twistMidCreation():
	twist_chain = pm.ls(sl=True, dag=True)
	tRoot_joint = twist_chain[0]
	tJoint_2 = twist_chain[1]
	tJoint_3 = twist_chain[2]
	tJoint_4 = twist_chain[3]
	tJoint_5 = twist_chain[4]
	tJoint_6 = twist_chain[5]
	tJoint_7 = twist_chain[6]
	print 'Twist Root Joint:', tRoot_joint
	print 'Twist Joint 2:', tJoint_2
	print 'Twist Joint 3:', tJoint_3
	print 'Twist Joint 4:', tJoint_4
	print 'Twist Joint 5:', tJoint_5
	print 'Twist Joint 6:', tJoint_6
	print 'Twist Joint 7:', tJoint_7

	joint_name = tRoot_joint.replace('1', '2')
	tJoint_2.rename(joint_name)

	joint_name = tJoint_2.replace('2', '3')
	tJoint_3.rename(joint_name)

	joint_name = tJoint_3.replace('3', '4')
	tJoint_4.rename(joint_name)

	joint_name = tJoint_4.replace('4', '5')
	tJoint_5.rename(joint_name)

	joint_name = tJoint_5.replace('5', '6')
	tJoint_6.rename(joint_name)

	joint_name = tJoint_6.replace('6', '7')
	tJoint_7.rename(joint_name)

	pm.parent(tJoint_6, w=1)

def twistEndCreation():
	twist_chain = pm.ls(sl=True, dag=True)
	tJoint_6 = twist_chain[0]
	tJoint_7 = twist_chain[1]
	print 'Twist Joint 6:', tJoint_6
	print 'Twist Joint 6:', tJoint_7

	import beJointSplit
	beJointSplit.split()

def twistResult():
	twist_chain = pm.ls(sl=True, dag=True)
	tJoint_6 = twist_chain[0]
	tJoint_7 = twist_chain[1]
	tJoint_8 = twist_chain[2]
	tJoint_9 = twist_chain[3]
	tJoint_10 = twist_chain[4]
	tJoint_11 = twist_chain[5]
	
	print 'Twist Joint 6:', tJoint_6
	print 'Twist Joint 7:', tJoint_7
	print 'Twist Joint 8:', tJoint_8
	print 'Twist Joint 9:', tJoint_9
	print 'Twist Joint 10:', tJoint_10
	print 'Twist Joint 11:', tJoint_11
	

	joint_name = tJoint_6.replace('6', '7')
	tJoint_7.rename(joint_name)

	joint_name = tJoint_7.replace('7', '8')
	tJoint_8.rename(joint_name)

	joint_name = tJoint_8.replace('8', '9')
	tJoint_9.rename(joint_name)

	joint_name = tJoint_9.replace('09', '10')
	tJoint_10.rename(joint_name)

	joint_name = tJoint_10.replace('10', '11')
	tJoint_11.rename(joint_name)

def firstSplineIk():
	twist_chain_1 = pm.ls(sl=True, dag=True)
	root_joint = twist_chain_1[0]
	joint_2 = twist_chain_1[1]
	joint_3 = twist_chain_1[2]
	joint_4 = twist_chain_1[3]
	joint_5 = twist_chain_1[4]

	temp_joints = pm.duplicate(root_joint)

	twist_chain_2 = pm.ls(sl=True, dag=True)
	tRoot_joint = twist_chain_2[0]
	tJoint_2 = twist_chain_2[1]
	tJoint_3 = twist_chain_2[2]
	tJoint_4 = twist_chain_2[3]
	tJoint_5 = twist_chain_2[4]
	print 'Twist Dup:', tRoot_joint

	joint_name = tRoot_joint.replace('twist1', 'temp')
	tRoot_joint.rename(joint_name)

	joint_name = tRoot_joint.replace('1', '2')
	tJoint_5.rename(joint_name)

	pm.parent(tJoint_5, tRoot_joint)
	pm.delete(tJoint_2)

	pm.select(tRoot_joint)
	joint_positions()
	joints = joint_positions(tRoot_joint) 
	arm_curve_1 = pm.curve(d = 1, p=joints)

	crv_name = root_joint.replace('twist', 'twistCrv')
	arm_curve_1.rename(crv_name)

	cB_joints = pm.duplicate(temp_joints)

	pm.select(cB_joints)
	cB_joints = pm.ls(sl=True, dag=True)
	cB_joint_1 = cB_joints[0]
	cB_joint_2 = cB_joints[1]

	joint_name = root_joint.replace('twist', 'twistBind')
	cB_joint_1.rename(joint_name)

	joint_name = cB_joint_1.replace('1', '2')
	cB_joint_2.rename(joint_name)

	pm.parent(cB_joint_2, w=1)
 
	pm.delete(temp_joints)

	pm.select(root_joint, joint_5, arm_curve_1)
	arm_ik_1 = pm.ikHandle(sol='ikSplineSolver', ccv=False, pcv=False)[0]

	ik_name = arm_curve_1.replace('Crv', '_ikh')
	arm_ik_1.rename(ik_name)

	pm.select(cB_joint_1, cB_joint_2, arm_curve_1)
	pm.mel.SmoothBindSkin()

	arm_ik_1.dTwistControlEnable.set(1)
	arm_ik_1.dWorldUpType.set(4)

	arm_ik_1.dForwardAxis.set(0)
	arm_ik_1.dWorldUpAxis.set(0)

	arm_ik_1.dWorldUpVectorY.set(1)
	arm_ik_1.dWorldUpVectorEndY.set(-1)

	arm_curve_1.inheritsTransform.set(0)

def secondSplineIk():
	twist_chain_1 = pm.ls(sl=True, dag=True)
	root_joint = twist_chain_1[0]
	joint_2 = twist_chain_1[1]
	joint_3 = twist_chain_1[2]
	joint_4 = twist_chain_1[3]
	joint_5 = twist_chain_1[4]
	joint_6 = twist_chain_1[5]

	temp_joints = pm.duplicate(root_joint)

	twist_chain_2 = pm.ls(sl=True, dag=True)
	tRoot_joint = twist_chain_2[0]
	tJoint_2 = twist_chain_2[1]
	tJoint_3 = twist_chain_2[2]
	tJoint_4 = twist_chain_2[3]
	tJoint_5 = twist_chain_2[4]
	tJoint_6 = twist_chain_2[5]
	print 'Twist Dup:', tRoot_joint

	joint_name = tRoot_joint.replace('twist1', 'temp')
	tRoot_joint.rename(joint_name)

	joint_name = tRoot_joint.replace('06', '11')
	tJoint_6.rename(joint_name)

	pm.parent(tJoint_6, tRoot_joint)
	pm.delete(tJoint_2)

	pm.select(tRoot_joint)
	joint_positions()
	joints = joint_positions(tRoot_joint) 
	arm_curve_2 = pm.curve(d = 1, p=joints)

	crv_name = root_joint.replace('06_twist', '02_twistCrv')
	arm_curve_2.rename(crv_name)


	cB_joint_3 = pm.duplicate(tJoint_6)[0]

	pm.parent(cB_joint_3, w=1)

	joint_name = root_joint.replace('06_twist', '03_twistBind')
	cB_joint_3.rename(joint_name)
 
	pm.delete(temp_joints)

	pm.select(root_joint, joint_5, arm_curve_2)
	arm_ik_2 = pm.ikHandle(sol='ikSplineSolver', ccv=False, pcv=False)[0]

	ik_name = arm_curve_2.replace('Crv', '_ikh')
	arm_ik_2.rename(ik_name)

	arm_ik_2.dTwistControlEnable.set(1)
	arm_ik_2.dWorldUpType.set(4)

	arm_ik_2.dForwardAxis.set(0)
	arm_ik_2.dWorldUpAxis.set(0)

	arm_ik_2.dWorldUpVectorY.set(1)
	arm_ik_2.dWorldUpVectorEndY.set(-1)

	arm_curve_2.inheritsTransform.set(0)

def joint_positions(*j):
	pm.joint(zso=1, ch=1, e=1, oj='xzy', secondaryAxisOrient='zup')
	pos = [pm.xform(j,q=True, t=True, ws=True)]
	print pos
   	children = cmds.listRelatives(j, c=True) or []
   	for child in children:
 		pos.extend(joint_positions(child))
	return pos


def bind():
	cB_joints = pm.ls(sl=True)
	cB_joint_2 = cB_joints[0]
	cB_joint_3 = cB_joints[1]
	arm_curve_2 = cB_joints[2]

	pm.mel.SmoothBindSkin()



def freezeTransform(*args):
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
	print 'Transform Frozen'

def deleteHistory(*args):
	pm.delete(ch=True)
	print 'History Deleted'

def centerPivot(*args):
	pm.xform(cpc=True)
	print 'Selected pivot centered.'

def ikfk(*args):
	arm_joints = pm.ls(sl=True, dag=True)
	root_joint = arm_joints[0]
	joint_2 = arm_joints[1]
	joint_3 = arm_joints[2]

	pm.joint(root_joint, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	joint_3.jointOrientX.set(0)
	joint_3.jointOrientY.set(0)
	root_joint.rotateOrder.set(3)

	ik_joints = pm.duplicate(arm_joints)
	ik_joints = pm.ls(sl=True, dag=True)
	ik_root = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]

	joint_name = root_joint.replace('bind', 'ik')
	ik_root.rename(joint_name)

	joint_name = ik_root.replace('1', '2')
	ik_joint_2.rename(joint_name)

	joint_name = root_joint.replace('1_bind', '3_ik')
	ik_joint_3.rename(joint_name)

	fk_joints = pm.duplicate(arm_joints)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=True, dag=True)
	fk_root = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]

	joint_name = ik_root.replace('ik', 'fk')
	fk_root.rename(joint_name)

	joint_name = ik_joint_2.replace('ik', 'fk')
	fk_joint_2.rename(joint_name)

	joint_name = ik_joint_3.replace('ik', 'fk')
	fk_joint_3.rename(joint_name)

	root_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_joint.replace('bind', 'rot_ikfk_blend')
	root_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_root + '.rotate', root_rot_ikfk + '.color2')
	pm.connectAttr(fk_root + '.rotate', root_rot_ikfk + '.color1')
	pm.connectAttr(root_rot_ikfk + '.output', root_joint + '.rotate')

	joint_2_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_rot_ikfk.replace('1', '2')
	joint_2_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_2 + '.rotate', joint_2_rot_ikfk + '.color2')
	pm.connectAttr(fk_joint_2 + '.rotate', joint_2_rot_ikfk + '.color1')
	pm.connectAttr(joint_2_rot_ikfk + '.output', joint_2 + '.rotate')

	joint_3_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_rot_ikfk.replace('1', '3')
	joint_3_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_3 + '.rotate', joint_3_rot_ikfk + '.color2')
	pm.connectAttr(fk_joint_3 + '.rotate', joint_3_rot_ikfk + '.color1')
	pm.connectAttr(joint_3_rot_ikfk + '.output', joint_3 + '.rotate')

	root_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_joint.replace('bind', 'trans_ikfk_blend')
	root_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_root + '.translate', root_trans_ikfk + '.color2')
	pm.connectAttr(fk_root + '.translate', root_trans_ikfk + '.color1')
	pm.connectAttr(root_trans_ikfk + '.output', root_joint + '.translate')

	joint_2_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_trans_ikfk.replace('1', '2')
	joint_2_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_2 + '.translate', joint_2_trans_ikfk + '.color2')
	pm.connectAttr(fk_joint_2 + '.translate', joint_2_trans_ikfk + '.color1')
	pm.connectAttr(joint_2_trans_ikfk + '.output', joint_2 + '.translate')

	joint_3_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_trans_ikfk.replace('1', '3')
	joint_3_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_3 + '.translate', joint_3_trans_ikfk + '.color2')
	pm.connectAttr(fk_joint_3 + '.translate', joint_3_trans_ikfk + '.color1')
	pm.connectAttr(joint_3_trans_ikfk + '.output', joint_3 + '.translate')



	'''
	Create the arm icon
	'''
	arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	temp_constraint = pm.pointConstraint(joint_3, arm_icon)
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()

	'''
	Rename arm icon
	'''
	arm_icon_name = root_joint.replace('01_bind', 'icon')
	arm_icon.rename(arm_icon_name)



	'''
	Create the IK/FK switch
	'''
	ikfk_shape_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	ikfk_shape_2 = pm.curve(p=[(0, 0, -1), (0, 0, 1)], k=[0, 1], d=1)
	ikfk_shape_3 = pm.curve(p=[(-1, 0, 0), (1, 0, 0)], k=[0, 1], d=1)
	ikfk_shape_4 = pm.curve(p=[(0, 0, 1), (0, 0, 3)], k=[0, 1], d=1)

	shape_name_1 = root_joint.replace('arm_01_bind', 'ikfk_curve1') 
	# print 'Shape 1 Name:', shape_name_1
	ikfk_shape_1.rename(shape_name_1)

	shape_name_2 = root_joint.replace('arm_01_bind', 'ikfk_curve2') 
	# print 'Shape 2 Name:', shape_name_2
	ikfk_shape_2.rename(shape_name_2)

	shape_name_3 = root_joint.replace('arm_01_bind', 'ikfk_curve3') 
	# print 'Shape 3 Name:', shape_name_3
	ikfk_shape_3.rename(shape_name_3)

	shape_name_4 = root_joint.replace('arm_01_bind', 'ikfk_curve4') 
	# print 'Shape 4 Name:', shape_name_4
	ikfk_shape_4.rename(shape_name_4)

	switch = pm.group(empty=True)
	pm.select(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4, switch)
	shapes = pm.ls(selection=True, dag=True)
	curveShape_1 = shapes[1]
	curveShape_2 = shapes[3]
	curveShape_3 = shapes[5]
	curveShape_4 = shapes[7]
	switch_grp = shapes[8]
	# print 'Curve Shape 1:', curveShape_1
	# print 'Curve Shape 2:', curveShape_2
	# print 'Curve Shape 3:', curveShape_3
	# print 'Curve Shape 4:', curveShape_4
	# print 'Switch:', switch_grp
	pm.select(ikfk_shape_2, ikfk_shape_3)

	pm.cmds.scale(0.768, 0.768, 0.768)
	freezeTransform()

	pm.parent(curveShape_1, curveShape_2, curveShape_3, curveShape_4, switch, s=1, r=1)
	pm.delete(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4)
	pm.cmds.move(0, 0, 3, switch + '.scalePivot', switch + '.rotatePivot', rpr=1)

	pm.xform(switch, ro=[0,0,90], scale=[1.5,1.5,1.5])
	freezeTransform(switch)
	temp_constraint = pm.pointConstraint(joint_3, switch, mo=0, w=1)
	pm.delete(temp_constraint)
	freezeTransform()
	switch_name = root_joint.replace('01_bind', 'IkFk_switch')
	switch.rename(switch_name)
	pm.parentConstraint(joint_3, switch, mo=1, w=1)
	deleteHistory()

	'''
	Add IkFk attribute
	'''
	pm.addAttr(switch, ln="IkFk", nn='Ik/Fk', max=1, dv=0, at='double', min=0)
	switch.IkFk.set(e=1, keyable=True)

	'''
	Lock and hide attrs
	'''
	switch.tx.set(lock=True, channelBox=False, keyable=False)
	switch.ty.set(lock=True, channelBox=False, keyable=False)
	switch.tz.set(lock=True, channelBox=False, keyable=False)
	switch.rx.set(lock=True, channelBox=False, keyable=False)
	switch.ry.set(lock=True, channelBox=False, keyable=False)
	switch.rz.set(lock=True, channelBox=False, keyable=False)
	switch.sx.set(lock=True, channelBox=False, keyable=False)
	switch.sy.set(lock=True, channelBox=False, keyable=False)
	switch.sz.set(lock=True, channelBox=False, keyable=False)
	switch.v.set(lock=True, channelBox=False, keyable=False)


	'''
	Connect the blend attrs the the switch
	'''
	pm.connectAttr(switch + '.IkFk', root_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', joint_2_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', joint_3_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', root_trans_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', joint_2_trans_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', joint_3_trans_ikfk + '.blender')


	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(fk_root, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_root, fk_pad_1)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_1, fk_pad_1)
	pm.select(fk_icon_1)
	freezeTransform()


	fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	print 'Fk icon 2:', fk_icon_2
	temp_constraint = pm.parentConstraint(fk_joint_2, fk_icon_2)
	pm.delete(temp_constraint)
	fk_pad_2 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_joint_2, fk_pad_2)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_2, fk_pad_2)
	pm.select(fk_icon_2)
	freezeTransform()
	pm.parent(fk_pad_2, fk_icon_1)

	'''
	Rename the icons and the pads
	'''
	fk_icon1_name = fk_root.replace('fk', 'fk_icon')
	fk_icon_1.rename(fk_icon1_name)

	fk_icon2_name = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(fk_icon2_name)

	fk_pad1_name = fk_icon_1.replace('icon', 'local')
	fk_pad_1.rename(fk_pad1_name)

	fk_pad2_name = fk_icon_2.replace('icon', 'local')
	fk_pad_2.rename(fk_pad2_name) 



	pm.parentConstraint(fk_icon_1, fk_root)
	pm.parentConstraint(fk_icon_2, fk_joint_2)

	'''
	Create length attr
	'''
	pm.addAttr(fk_icon_1, ln='length', at='double', min=0, dv=1)
	fk_icon_1.length.set(e=1, keyable=True)
	pm.setDrivenKeyframe(fk_pad_2 + '.tx', currentDriver=fk_icon_1 + '.length')
	fk_icon_1.length.set(0)
	fk_pad_2.tx.set(0)
	pm.setDrivenKeyframe(fk_pad_2 + '.tx', currentDriver=fk_icon_1 + '.length')
	fk_icon_1.length.set(1)
	pm.keyTangent(fk_pad_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(fk_pad_2 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	pm.addAttr(fk_icon_2, ln='length', at='double', min=0, dv=1)
	fk_icon_2.length.set(e=1, keyable=True)
	pm.setDrivenKeyframe(fk_joint_3 + '.tx', currentDriver=fk_icon_2 + '.length')
	fk_icon_2.length.set(0)
	fk_joint_3.tx.set(0)
	pm.setDrivenKeyframe(fk_joint_3 + '.tx', currentDriver=fk_icon_2 + '.length')
	fk_icon_2.length.set(1)
	pm.keyTangent(fk_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(fk_joint_3 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	'''
	Create the ik
	'''
	pm.select(ik_root, ik_joint_3)
	ikh = pm.ikHandle()[0]

	ikh_name = root_joint.replace('bind', 'ikh')
	ikh.rename(ikh_name)


	'''
	Create the elbow icon.
	'''

	elbow_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
	pm.select('curve1.cv[0]', 'curve1.cv[6]', 'curve1.cv[12]', 'curve1.cv[18]', 'curve1.cv[24]', r=1)
	pm.cmds.move(0, -0.982783, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[22]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[23]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[19]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[20]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[16]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[17]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[13]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[14]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[10]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[11]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[7]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[8]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[4]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[5]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[1]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)
	pm.select('curve1.cv[2]', r=1)
	pm.cmds.move(0, -0.483525, 0, r=1, os=1, wd=1)

	pm.select(elbow_icon)
	centerPivot(elbow_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the elbow icon.
	'''
	temp_constraint = pm.pointConstraint(joint_2, elbow_icon)
	pm.delete(temp_constraint)
	freezeTransform(elbow_icon)
	pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
	freezeTransform(elbow_icon)

	'''
	Rename elbow icon
	'''
	elbow_icon_name = root_joint.replace('arm_01_bind', 'elbow_icon')
	elbow_icon.rename(elbow_icon_name)

	'''
	Create the pole vector for the elbow
	'''
	pm.poleVectorConstraint(elbow_icon, ikh)

	'''
	Parent the ikh under the arm_icon
	'''
	pm.parent(ikh, arm_icon)


	'''
	Icon visibility SDKs
	'''
	fk_pad_1.v.set(0)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(1)
	fk_pad_1.v.set(1)
	arm_icon.v.set(0)
	elbow_icon.v.set(0)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0)
