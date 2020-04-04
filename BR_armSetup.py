import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel


def armSetup(*args):
	arm_system = pm.ls(sl=True, dag=True)
	main_root = arm_system[0]
	mJ_2 = arm_system[1]
	mJ_3 = arm_system[2]
	# print 'Main Root:', main_root
	# print 'Main Joint 2:', mJ_2
	# print 'Main Joint 3:', mJ_3

	pm.joint(main_root, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	mJ_3.jointOrientX.set(0)
	mJ_3.jointOrientY.set(0)
	main_root.rotateOrder.set(3)


	ik_joints = pm.duplicate(main_root)
	ik_joints = pm.ls(sl=True, dag=True)
	ik_root = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	# print 'Ik Root:', ik_root
	# print 'Ik Joint 2:', ik_joint_2
	# print 'Ik Joint 3:', ik_joint_3

	
	for each in ik_joints:
		joint_name = main_root.replace('bind', 'ik')
		ik_root.rename(joint_name)

	joint_name = ik_root.replace('1', '2')
	ik_joint_2.rename(joint_name)

	joint_name = ik_joint_2.replace('2', '3')
	ik_joint_3.rename(joint_name)

	fk_joints = pm.duplicate(main_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=True, dag=True)
	fk_root = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	# print 'Fk Root:', fk_root
	# print 'Fk Joint 2:', fk_joint_2
	# print 'Fk Joint 3:', fk_joint_3

	
	joint_name = ik_root.replace('ik', 'fk')
	fk_root.rename(joint_name)

	joint_name = ik_joint_2.replace('ik', 'fk')
	fk_joint_2.rename(joint_name)

	joint_name = ik_joint_3.replace('ik', 'fk')
	fk_joint_3.rename(joint_name)

	hybrid_fk_joints = pm.duplicate(fk_joint_2)
	pm.parent(hybrid_fk_joints, w=1)

	pm.select(hybrid_fk_joints)
	hJoints = pm.ls(sl=True,  dag=True)
	hJ_1 = hJoints[0]
	hJ_2 = hJoints[1]
	# print hJ_1
	# print hJ_2

	jnt_name = fk_joint_2.replace('fk', 'hybridFk')
	hJ_1.rename(jnt_name)

	jnt_name = hJ_1.replace('02', '03')
	hJ_2.rename(jnt_name)
	


	twist_joints = pm.duplicate(main_root)
	pm.select(twist_joints)
	joint_system = pm.ls(sl=True, dag=True)
	root_joint = joint_system[0]
	mid_joint = joint_system[1]
	end_joint = joint_system[2]
	# print 'Root joint:', root_joint
	# print 'Mid joint:', mid_joint
	# print 'End joint:', end_joint

	new_name = root_joint.replace('bind1', 'twist')
	root_joint.rename(new_name)
	jnt_name_1 = root_joint.replace('01', '05')
	jnt_name_2 = root_joint.replace('01', '04')
	jnt_name_3 = root_joint.replace('01', '03')
	jnt_name_4 = root_joint.replace('01', '02')
	
	jnt_name_6 = mid_joint.replace('02_bind', '06_twist')


	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.orientConstraint(root_joint, loc_1, mo=0)
	point_constraint_1 = pm.pointConstraint(root_joint, loc_1, mo=0, w=0)
	point_constraint_2 = pm.pointConstraint(mid_joint, loc_1, mo=0, w=1)
	splitJnt_1 = pm.joint(loc_1, name=jnt_name_1)

	loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_2 = pm.orientConstraint(root_joint, loc_2, mo=0)
	point_constraint_3 = pm.pointConstraint(root_joint, loc_2, mo=0, w=.25)
	point_constraint_4 = pm.pointConstraint(mid_joint, loc_2, mo=0, w=.75)
	splitJnt_2 = pm.joint(loc_2, name=jnt_name_2)

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_3 = pm.orientConstraint(root_joint, loc_3, mo=0)
	point_constraint_5 = pm.pointConstraint(root_joint, loc_3, mo=0, w=.5)
	point_constraint_6 = pm.pointConstraint(mid_joint, loc_3, mo=0, w=.5)
	splitJnt_3 = pm.joint(loc_3, name=jnt_name_3)

	loc_4 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_4 = pm.orientConstraint(root_joint, loc_4, mo=0)
	point_constraint_7 = pm.pointConstraint(root_joint, loc_4, mo=0, w=.75)
	point_constraint_8 = pm.pointConstraint(mid_joint, loc_4, mo=0, w=.25)
	splitJnt_4 = pm.joint(loc_4, name=jnt_name_4)

	pm.parent(splitJnt_4, root_joint)
	pm.parent(splitJnt_3, splitJnt_4)
	pm.parent(splitJnt_2, splitJnt_3)
	pm.parent(splitJnt_1, splitJnt_2)
	pm.parent(mid_joint, splitJnt_1)

	pm.delete(loc_1, loc_2, loc_3, loc_4)

	mid_joint.rename(jnt_name_6)

	jnt_name_7 = mid_joint.replace('06', '07')

	end_joint.rename(jnt_name_7)

	twist_joints = pm.duplicate(mid_joint)

	pm.parent(twist_joints, w=1)

	twist_joints = pm.ls(sl=True, dag=True)
	joint_7 = twist_joints[0]
	joint_12 = twist_joints[1]

	pm.delete(end_joint)

	jnt_name_12 = joint_12.replace('07', '12')
	joint_12.rename(jnt_name_12)
	jnt_name_7 = joint_7.replace('06_twist1', '07_twist')
	joint_7.rename(jnt_name_7)

	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_1 = pm.pointConstraint(joint_7, loc_1, mo=0, w=0)
	point_constraint_2 = pm.pointConstraint(joint_12, loc_1, mo=0, w=1)
	jnt_name_11 = joint_12.replace('12', '11')
	joint_11 = pm.joint(loc_1, name=jnt_name_11)

	loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_1 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_3 = pm.pointConstraint(joint_7 , loc_2, mo=0, w=.25)
	point_constraint_4 = pm.pointConstraint(joint_12 , loc_2, mo=0, w=.75)
	jnt_name_10 = joint_11.replace('11', '10')
	joint_10 = pm.joint(loc_2, n=jnt_name_10)

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_2 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_5 = pm.pointConstraint(joint_7 ,loc_3, mo=0, w=.5)
	point_constraint_6 = pm.pointConstraint(joint_12 ,loc_3, mo=0, w=.5)
	jnt_name_9 = joint_10.replace('10', '09')
	joint_9 = pm.joint(loc_3, n=jnt_name_9)

	loc_4 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_3 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_7 = pm.pointConstraint(joint_7 ,loc_4, mo=0, w=.75)
	point_constraint_8 = pm.pointConstraint(joint_12 ,loc_4, mo=0, w=.25)
	jnt_name_8 = joint_9.replace('9', '8')
	joint_8 = pm.joint(loc_4, n=jnt_name_8)

	pm.parent(joint_11, joint_10)
	pm.parent(joint_10, joint_9)
	pm.parent(joint_9, joint_8)
	pm.parent(joint_8, joint_7)

	pm.delete(loc_1, loc_2, loc_3, loc_4)

	pm.parent(joint_12, joint_11)


	temp_joints = pm.duplicate(root_joint)

	pm.select(temp_joints)


	temp_joints = pm.ls(sl=True, dag=True)

	cb_joint_1 = temp_joints[0]
	cb_joint_2 = temp_joints[5]
	cb_joint_3 = temp_joints[1]
	# print 'cb joint 1:', cb_joint_1	
	# print 'cb joint 2:', cb_joint_2	
	# print 'cb joint 3:', cb_joint_3	

	pm.parent(cb_joint_2, cb_joint_1)
	pm.delete(cb_joint_3)

	bind_name = cb_joint_1.replace('twist1', 'curveTwist')
	cb_joint_1.rename(bind_name)

	bind_name = cb_joint_1.replace('01', '02')
	cb_joint_2.rename(bind_name)

	pm.parent(cb_joint_2, w=1)

	cb_joint_3 = pm.duplicate(joint_12)[0]

	bind_name = cb_joint_2.replace('2', '3')
	cb_joint_3.rename(bind_name)

	pm.parent(cb_joint_3, w=1)

	tempBind = pm.duplicate(main_root)

	pm.select(tempBind)
	temp_joints = pm.ls(sl=True, dag=True)
	temp_1 = temp_joints[0]
	temp_2 = temp_joints[1]
	temp_3 = temp_joints[2]

	temp_name = main_root.replace('bind', 'temp')
	temp_1.rename(temp_name)

	temp_name = temp_1.replace('1', '2')
	temp_2.rename(temp_name)

	temp_name = temp_2.replace('2', '3')
	temp_3.rename(temp_name)

	pm.parent(temp_3, w=1)


	joint_positions(temp_1)
	joints = joint_positions(temp_1) 
	arm_curve_1 = pm.curve(d = 1, p=joints)


	crv_name = root_joint.replace('twist', 'crv')
	arm_curve_1.rename(crv_name)

	pm.select(cb_joint_1, cb_joint_2, arm_curve_1)
	pm.mel.SmoothBindSkin()


	pm.select(root_joint, mid_joint, arm_curve_1)
	arm_ik_1 = pm.ikHandle(sol='ikSplineSolver', ccv=False, pcv=False)[0]

	ik_name = arm_curve_1.replace('crv', 'twistIkh')
	arm_ik_1.rename(ik_name)

	arm_ik_1.dTwistControlEnable.set(1)
	arm_ik_1.dWorldUpType.set(4)

	arm_ik_1.dForwardAxis.set(0)
	arm_ik_1.dWorldUpAxis.set(3)

	arm_ik_1.dWorldUpVectorY.set(0)
	arm_ik_1.dWorldUpVectorEndY.set(0)

	arm_ik_1.dWorldUpVectorZ.set(1)
	arm_ik_1.dWorldUpVectorEndZ.set(1)

	arm_curve_1.inheritsTransform.set(0)

	pm.connectAttr(cb_joint_1 + '.xformMatrix', arm_ik_1 + '.dWorldUpMatrix')
	pm.connectAttr(cb_joint_2 + '.xformMatrix', arm_ik_1 + '.dWorldUpMatrixEnd')

	pm.parent(temp_3, temp_2)

	joint_positions(temp_2)
	joints = joint_positions(temp_2) 
	arm_curve_2 = pm.curve(d = 1, p=joints)

	crv_name = arm_curve_1.replace('1', '2')
	arm_curve_2.rename(crv_name)

	pm.delete(temp_1, temp_2)


	pm.select(mid_joint, arm_curve_2)
	selection = pm.ls(sl=True)
	driver = selection[0]
	driven = selection[1]

	driver_translate =	driver.getTranslation(ws=True)
	driven.setPivots(driver_translate, ws=True)

	pm.select(cb_joint_2, cb_joint_3, arm_curve_2)
	pm.mel.SmoothBindSkin()

	pm.select(end_joint, joint_12, arm_curve_2)
	arm_ik_2 = pm.ikHandle(sol='ikSplineSolver', ccv=False, pcv=False)[0]

	ik_name = arm_ik_1.replace('1', '2')
	arm_ik_2.rename(ik_name)

	arm_ik_2.dTwistControlEnable.set(1)
	arm_ik_2.dWorldUpType.set(4)

	arm_ik_2.dForwardAxis.set(0)
	arm_ik_2.dWorldUpAxis.set(3)

	arm_ik_2.dWorldUpVectorY.set(0)
	arm_ik_2.dWorldUpVectorEndY.set(0)

	arm_ik_2.dWorldUpVectorZ.set(1)
	arm_ik_2.dWorldUpVectorEndZ.set(1)

	arm_curve_2.inheritsTransform.set(0)

	pm.connectAttr(cb_joint_2 + '.xformMatrix', arm_ik_2 + '.dWorldUpMatrix')
	pm.connectAttr(cb_joint_3 + '.xformMatrix', arm_ik_2 + '.dWorldUpMatrixEnd')

	twist_grp = pm.group(arm_curve_1, arm_curve_2, arm_ik_1, arm_ik_2, cb_joint_1, cb_joint_2, cb_joint_3 )
	grp_name = root_joint.replace('01_twist', 'twist_grp')
	twist_grp.rename(grp_name)

	pm.select(root_joint, twist_grp)
	selection = pm.ls(sl=True)
	driver = selection[0]
	driven = selection[1]

	driver_translate = driver.getTranslation(ws=True)
	driven.setPivots(driver_translate, ws=True)

	pm.parentConstraint(mJ_3, cb_joint_3, mo=1)
	pm.parentConstraint(mJ_2, cb_joint_2, mo=1)
	pm.pointConstraint(main_root, cb_joint_1, mo=1)


	'''================================================================================================================'''
	root_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = main_root.replace('bind', 'rot_ikfk_blend')
	root_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_root + '.rotate', root_rot_ikfk + '.color2')
	pm.connectAttr(fk_root + '.rotate', root_rot_ikfk + '.color1')
	pm.connectAttr(root_rot_ikfk + '.output', main_root + '.rotate')

	mJ_2_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_rot_ikfk.replace('1', '2')
	mJ_2_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_2 + '.rotate', mJ_2_rot_ikfk + '.color2')
	pm.connectAttr(fk_joint_2 + '.rotate', mJ_2_rot_ikfk + '.color1')
	pm.connectAttr(mJ_2_rot_ikfk + '.output', mJ_2 + '.rotate')

	mJ_3_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_rot_ikfk.replace('1', '3')
	mJ_3_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_3 + '.rotate', mJ_3_rot_ikfk + '.color2')
	pm.connectAttr(fk_joint_3 + '.rotate', mJ_3_rot_ikfk + '.color1')
	pm.connectAttr(mJ_3_rot_ikfk + '.output', mJ_3 + '.rotate')

	root_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = main_root.replace('bind', 'trans_ikfk_blend')
	root_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_root + '.translate', root_trans_ikfk + '.color2')
	pm.connectAttr(fk_root + '.translate', root_trans_ikfk + '.color1')
	pm.connectAttr(root_trans_ikfk + '.output', main_root + '.translate')

	mJ_2_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_trans_ikfk.replace('1', '2')
	mJ_2_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_2 + '.translate', mJ_2_trans_ikfk + '.color2')
	pm.connectAttr(fk_joint_2 + '.translate', mJ_2_trans_ikfk + '.color1')
	pm.connectAttr(mJ_2_trans_ikfk + '.output', mJ_2 + '.translate')

	mJ_3_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_trans_ikfk.replace('1', '3')
	mJ_3_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_3 + '.translate', mJ_3_trans_ikfk + '.color2')
	pm.connectAttr(fk_joint_3 + '.translate', mJ_3_trans_ikfk + '.color1')
	pm.connectAttr(mJ_3_trans_ikfk + '.output', mJ_3 + '.translate')

	'''
	Create the arm icon
	'''
	arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	temp_constraint = pm.pointConstraint(mJ_3, arm_icon)
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()

	'''
	Rename arm icon
	'''
	arm_icon_name = main_root.replace('01_bind', 'icon')
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
	deleteHistory()
	temp_constraint = pm.pointConstraint(mJ_3, switch, mo=0, w=1)
	pm.delete(temp_constraint)
	pm.select(switch)
	freezeTransform()
	switch_name = main_root.replace('01_bind', 'IkFk_switch')
	switch.rename(switch_name)
	pm.parentConstraint(mJ_3, switch, mo=1)



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
	pm.connectAttr(switch + '.IkFk', mJ_2_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', mJ_3_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', root_trans_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', mJ_2_trans_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', mJ_3_trans_ikfk + '.blender')

	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(fk_root, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_root, fk_pad_1)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_1, fk_pad_1)
	pm.select(fk_icon_1)
	freezeTransform()

	fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 2:', fk_icon_2
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

	ikh_name = main_root.replace('bind', 'ikh')
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
	temp_constraint = pm.pointConstraint(mJ_2, elbow_icon)
	pm.delete(temp_constraint)
	freezeTransform(elbow_icon)
	pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
	freezeTransform(elbow_icon)

	'''
	Rename elbow icon
	'''
	elbow_icon_name = main_root.replace('arm_01_bind', 'elbow_icon')
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
	switch.IkFk.set(0.1)
	fk_pad_1.v.set(1)
	arm_icon.v.set(1)
	elbow_icon.v.set(1)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0.99)
	fk_pad_1.v.set(1)
	arm_icon.v.set(1)
	elbow_icon.v.set(1)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0)

	upperArm_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = main_root.replace('01_bind', 'info')
	upperArm_info.rename(node_name)

	upperArm_div = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = upperArm_info.replace('info', 'div')
	upperArm_div.rename(node_name)

	pm.connectAttr(arm_curve_1 + '.worldSpace[0]', upperArm_info + '.inputCurve')

	pm.connectAttr(upperArm_info + '.arcLength', upperArm_div + '.input1X')

	upperArm_div.operation.set(2)

	arcLen = upperArm_info.arcLength.get()
	upperArm_div.input2X.set(arcLen)

	pm.connectAttr(upperArm_div + '.outputX', root_joint + '.sx')
	pm.connectAttr(upperArm_div + '.outputX', splitJnt_4 + '.sx')
	pm.connectAttr(upperArm_div + '.outputX', splitJnt_3 + '.sx')
	pm.connectAttr(upperArm_div + '.outputX', splitJnt_2 + '.sx')
	pm.connectAttr(upperArm_div + '.outputX', splitJnt_1 + '.sx')
	pm.connectAttr(upperArm_div + '.outputX', mid_joint + '.sx')

	'''==========================================================================================================================='''

	jnt_name = main_root.replace('bind', 'twist')
	main_root.rename(jnt_name)

	jnt_name = root_joint.replace('twist', 'bind')
	root_joint.rename(jnt_name)

	jnt_name = main_root.replace('t1', 't')
	main_root.rename(jnt_name)

	jnt_name = main_root.replace('01', '02')
	mJ_2.rename(jnt_name)

	jnt_name = main_root.replace('01', '03')
	mJ_3.rename(jnt_name)

	jnt_name = root_joint.replace('01', '02')
	splitJnt_4.rename(jnt_name)

	jnt_name = root_joint.replace('01', '03')
	splitJnt_3.rename(jnt_name)

	jnt_name = root_joint.replace('01', '04')
	splitJnt_2.rename(jnt_name)

	jnt_name = root_joint.replace('01', '05')
	splitJnt_1.rename(jnt_name)

	jnt_name = root_joint.replace('01', '06')
	mid_joint.rename(jnt_name)

	jnt_name = mid_joint.replace('06', '07')
	joint_7.rename(jnt_name)

	jnt_name = mid_joint.replace('06', '08')
	joint_8.rename(jnt_name)

	jnt_name = mid_joint.replace('06', '09')
	joint_9.rename(jnt_name)

	jnt_name = mid_joint.replace('06', '10')
	joint_10.rename(jnt_name)

	jnt_name = mid_joint.replace('06', '11')
	joint_11.rename(jnt_name)

	jnt_name = mid_joint.replace('06', '12')
	joint_12.rename(jnt_name)

	'''==========================================================================================================================='''

	foreArm_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = upperArm_info.replace('01', '02')
	foreArm_info.rename(node_name)

	foreArm_div = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = upperArm_div.replace('01', '02')
	foreArm_div.rename(node_name)

	pm.connectAttr(arm_curve_2 + '.worldSpace[0]', foreArm_info + '.inputCurve')

	pm.connectAttr(foreArm_info + '.arcLength', foreArm_div + '.input1X')

	foreArm_div.operation.set(2)

	arcLen = foreArm_info.arcLength.get()
	foreArm_div.input2X.set(arcLen)

	pm.connectAttr(foreArm_div + '.outputX', joint_7 + '.sx')
	pm.connectAttr(foreArm_div + '.outputX', joint_8 + '.sx')
	pm.connectAttr(foreArm_div + '.outputX', joint_9 + '.sx')
	pm.connectAttr(foreArm_div + '.outputX', joint_10 + '.sx')
	pm.connectAttr(foreArm_div + '.outputX', joint_11 + '.sx')
	
	'''==========================================================================================================================='''
	loc_1 = pm.spaceLocator(p=(0, 0, 0))

	loc_2 = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.parentConstraint(main_root, loc_1, mo=0)
	pm.delete(temp_constraint)
	pm.select(loc_1)
	freezeTransform(loc_1)

	loc_name = root_joint.replace('01_bind', 'start_loc')
	loc_1.rename(loc_name)

	temp_constraint = pm.parentConstraint(mJ_3, loc_2, mo=0)
	pm.delete(temp_constraint)
	pm.select(loc_2)
	freezeTransform(loc_2)

	loc_name = loc_1.replace('start', 'end')
	loc_2.rename(loc_name)

	arm_dist = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.select(arm_dist)
	selection = pm.ls(sl=True, s=False)
	shape = selection[0]
	pm.pickWalk(d='up')
	transform = pm.ls(sl=True)[0]

	node_name = loc_2.replace('end_loc', 'dist')
	# print node_name
	transform.rename(node_name)

	pm.connectAttr(loc_1 + '.worldPosition', arm_dist + '.startPoint')
	pm.connectAttr(loc_2 + '.worldPosition', arm_dist + '.endPoint')

	pm.parentConstraint(arm_icon, loc_2)

	upperArm_len = pm.getAttr(ik_joint_2 + '.tx')

	foreArm_len = pm.getAttr(ik_joint_3 + '.tx')

	sumLen = upperArm_len + foreArm_len

	pm.setDrivenKeyframe(ik_joint_2 + '.tx', currentDriver=arm_dist + '.distance', value=upperArm_len, driverValue=sumLen)

	pm.setDrivenKeyframe(ik_joint_2 + '.tx',  currentDriver=arm_dist + '.distance', value=(upperArm_len*2), driverValue=(sumLen*2))

	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=arm_dist + '.distance', value=foreArm_len, driverValue=sumLen)

	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=arm_dist + '.distance', value=(foreArm_len*2), driverValue=(sumLen*2))

	pm.keyTangent(ik_joint_2, ik_joint_3,'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.setInfinity(ik_joint_2, ik_joint_3, poi='linear')

	'''	This is to fix preserve the volumn, but it doesn't work at the moment
	stretch_squareRoot = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = arm_dist.replace('dist', '01_squareRoot')
	stretch_squareRoot.rename(node_name)

	pm.connectAttr(arm_dist + '.distance', stretch_squareRoot + '.input1X')
	stretch_squareRoot.operation.set(3)
	stretch_squareRoot.input2X.set(.5)

	stretch_invert = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = arm_dist.replace('dist', '01_invert')
	stretch_invert.rename(node_name)

	pm.connectAttr(stretch_squareRoot + '.outputX', stretch_invert + '.input2X')
	stretch_invert.operation.set(2)
	stretch_invert.input1X.set(1)


	pm.connectAttr(stretch_invert + '.outputX', root_joint + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', splitJnt_1 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', splitJnt_2 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', splitJnt_3 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', splitJnt_4 + '.sy')

	pm.connectAttr(stretch_invert + '.outputX', root_joint + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', splitJnt_1 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', splitJnt_2 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', splitJnt_3 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', splitJnt_4 + '.sz')

	stretch_squareRoot = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = arm_dist.replace('dist', '02_squareRoot')
	stretch_squareRoot.rename(node_name)

	pm.connectAttr(arm_dist + '.distance', stretch_squareRoot + '.input1X')
	stretch_squareRoot.operation.set(3)
	stretch_squareRoot.input2X.set(.5)

	stretch_invert = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = arm_dist.replace('dist', '02_invert')
	stretch_invert.rename(node_name)

	pm.connectAttr(stretch_squareRoot + '.outputX', stretch_invert + '.input2X')
	stretch_invert.operation.set(2)
	stretch_invert.input1X.set(1)

	pm.connectAttr(stretch_invert + '.outputX', joint_7 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', joint_8 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', joint_9 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', joint_10 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', joint_11 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', joint_12 + '.sy')

	pm.connectAttr(stretch_invert + '.outputX', joint_7 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_8 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_9 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_10 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_11 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_12 + '.sz')
	'''
	'''==========================================================================================================================='''

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(root_joint, loc_3, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_3)

	node_name = loc_1.replace('start_loc', '01_snap_loc')
	loc_3.rename(node_name)

	loc_4 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(elbow_icon, loc_4, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_4)

	node_name = loc_3.replace('01', '02')
	loc_4.rename(node_name)


	loc_5 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(mJ_3, loc_5, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_5)

	node_name = loc_4.replace('02', '03')
	loc_5.rename(node_name)

	snap_dist_1 = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.select(snap_dist_1)
	selection = pm.ls(sl=True, s=False)
	shape_1 = selection[0]
	pm.pickWalk(d='up')
	transform_1 = pm.ls(sl=True)[0]
	temp_constraint = pm.pointConstraint(main_root, transform_1, mo=0)
	pm.delete(temp_constraint)


	node_name = loc_2.replace('end_loc', '01_snap_dist')
	transform_1.rename(node_name)

	pm.connectAttr(loc_3 + '.worldPosition', snap_dist_1 + '.startPoint')

	pm.connectAttr(loc_4 + '.worldPosition', snap_dist_1 + '.endPoint')


	snap_dist_2 = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.select(snap_dist_2)
	selection = pm.ls(sl=True, s=False)
	shape_2 = selection[0]
	pm.pickWalk(d='up')
	transform_2 = pm.ls(sl=True)[0]
	temp_constraint = pm.pointConstraint(mJ_3, transform_2, mo=0)
	pm.delete(temp_constraint)

	node_name = transform_1.replace('01','02')
	transform_2.rename(node_name)

	pm.connectAttr(loc_4 + '.worldPosition', snap_dist_2 + '.startPoint')

	pm.connectAttr(loc_5 + '.worldPosition', snap_dist_2 + '.endPoint')

	pm.parent(loc_4, elbow_icon)

	pm.parent(loc_5, arm_icon)

	pm.addAttr(elbow_icon, ln='elbowSnap', at='double', min=0, max=1, dv=0)
	elbow_icon.elbowSnap.set(e=1, keyable=True)

	upperArm_stretch = pm.shadingNode('blendColors', asUtility=1)
	node_name = upperArm_info.replace('info', 'stretch_blend')
	upperArm_stretch.rename(node_name)

	pm.connectAttr(elbow_icon + '.elbowSnap', upperArm_stretch + '.blender')
	pm.connectAttr(snap_dist_1 + '.distance', upperArm_stretch + '.color1R')
	pm.connectAttr(ik_joint_2 + '_translateX.output', upperArm_stretch + '.color2R')
	pm.disconnectAttr(ik_joint_2 + '_translateX.output', ik_joint_2 + '.tx')
	pm.connectAttr(upperArm_stretch + '.outputR', ik_joint_2 + '.tx')

	foreArm_stretch = pm.shadingNode('blendColors', asUtility=1)
	node_name = foreArm_info.replace('info', 'stretch_blend')
	foreArm_stretch.rename(node_name)

	pm.connectAttr(elbow_icon + '.elbowSnap', foreArm_stretch + '.blender')
	pm.connectAttr(snap_dist_2 + '.distance', foreArm_stretch + '.color1R')
	pm.connectAttr(ik_joint_3 + '_translateX.output', foreArm_stretch + '.color2R')
	pm.disconnectAttr(ik_joint_3 + '_translateX.output', ik_joint_3 + '.tx')
	pm.connectAttr(foreArm_stretch + '.outputR', ik_joint_3 + '.tx')

	hybrid_fk_icons = pm.duplicate(fk_pad_2)
	pm.parent(hybrid_fk_icons, w=1)

	pm.select(hybrid_fk_icons)
	hIcons = pm.ls(sl=True, dag=True)
	hPad = hIcons[0]
	hIcon = hIcons[1]
	# print hPad
	# print hIcon

	pad_name = hJ_1.replace('hybridFk', 'hybridFk_local')
	hPad.rename(pad_name)

	icon_name = hPad.replace('local', 'icon')
	hIcon.rename(icon_name)

	temp_constraint = pm.pointConstraint(elbow_icon, hJ_1, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(hJ_1)

	temp_constraint = pm.pointConstraint(elbow_icon, hPad, mo=0)
	pm.delete(temp_constraint)

	pm.orientConstraint(hIcon, hJ_1)

	ik_cons_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(mJ_3, ik_cons_grp)
	pm.delete(temp_constraint)
	freezeTransform(ik_cons_grp)
	pm.parent(ikh, loc_5, ik_cons_grp)
	grp_name = twist_grp.replace('twist', 'cons')
	ik_cons_grp.rename(grp_name)
	constraint_1 = pm.parentConstraint(arm_icon, ik_cons_grp, mo=0)
	const_1_targets = constraint_1.getWeightAliasList()[0]
	print const_1_targets
	constraint_2 = pm.parentConstraint(hJ_2, ik_cons_grp, mo=0)
	const_2_targets = constraint_2.getWeightAliasList()[1]
	print const_2_targets
	pm.parent(hPad, elbow_icon)

	hJpad = pm.group(empty=True)
	pad_name = hJ_1.replace('02_hybridFk', '00_hybrdFk_pad')
	hJpad.rename(pad_name)

	temp_constraint = pm.parentConstraint(hJ_1, hJpad)
	pm.delete(temp_constraint)
	freezeTransform(hJpad)

	pm.parent(hJ_1, hJpad)

	pm.parentConstraint(hIcon, hJpad, mo=1)

	pm.addAttr(elbow_icon, ln='FK_foreArmBlend', at='double', min=0, max=1, dv=0)
	elbow_icon.FK_foreArmBlend.set(e=1, keyable=True)

	elbow_icon.FK_foreArmBlend.set(1)
	const_1_targets.set(0)
	pm.setDrivenKeyframe(const_1_targets, const_2_targets, currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hIcon + '.v',  currentDriver=elbow_icon + '.FK_foreArmBlend')
	elbow_icon.FK_foreArmBlend.set(0)
	const_1_targets.set(1)
	const_2_targets.set(0)
	hIcon.v.set(0)
	pm.setDrivenKeyframe(const_1_targets, const_2_targets, currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hIcon + '.v',  currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hJ_2 + '.tx', currentDriver=hIcon + '.length')
	hIcon.length.set(0)
	hJ_2.tx.set(0)
	length_sdk = pm.setDrivenKeyframe(hJ_2 + '.tx', currentDriver=hIcon + '.length')
	pm.keyTangent(hJ_2, itt='clamped', ott='clamped')
	pm.setInfinity(hJ_2, poi='linear')
	hIcon.length.set(1)

	'''==========================================================================================================================='''
	transform.v.set(0)
	transform_1.v.set(0)
	transform_2.v.set(0)

	dnt_grp = pm.group(loc_1,loc_2, loc_3, arm_dist, twist_grp, main_root, ik_root, fk_root, snap_dist_1, snap_dist_2, ik_cons_grp, hJpad)
	grp_name = twist_grp.replace('twist_grp', 'DO____NOT____TOUCH')
	dnt_grp.rename(grp_name)

	pad = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(main_root, pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(pad)

	pm.parent(root_joint, joint_7, pad)
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	ik_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(main_root, ik_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(ik_grp)
	pm.parent(ik_grp, dnt_grp)
	pm.parent(ik_root, loc_1, loc_2, ik_grp)

	grp_name = ik_root.replace('01_ik', '00_ik_cons_grp')
	ik_grp.rename(grp_name)

	twist_jnt_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(main_root, twist_jnt_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(twist_jnt_grp)
	pm.parent(twist_jnt_grp, dnt_grp)
	pm.parent(main_root, twist_jnt_grp)	

	grp_name = ik_grp.replace('ik', 'twist')
	twist_jnt_grp.rename(grp_name)


	arm_global = pm.group(empty=True)

	temp_constraint = pm.parentConstraint(main_root, arm_global)
	pm.delete(temp_constraint)
	freezeTransform(arm_global)
	pm.parent(arm_icon, elbow_icon, pad, switch, fk_pad_1, dnt_grp, arm_global)
	grp_name = pad.replace('00_pad', 'global_grp')
	arm_global.rename(grp_name)

	if pm.objExists('*moveAll'):
		pm.select('*moveAll')
		moveAll = '*moveAll'


	else:
		'''
		Create the global icon
		'''

		moveAll_circle = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
		moveAll_circle.sx.set(3)
		moveAll_circle.sy.set(3)
		moveAll_circle.sz.set(3)
		freezeTransform(moveAll_circle)


		xAxis = pm.curve(p=[(3.324583, 0, -0.594445), (5, 0, -0.594444), (5.000001, 0, -1.008806), (6, 0, 0), (5.000001, 0, 1.008806), (5, 0, 0.594444), (3.324583, 0, 0.594445), (3.324583, 0, -0.594445)], k=[0, 1, 2, 3, 4, 5, 6, 7], d=1)


		zAxis = pm.curve(p=[(0.594444, 0, 3.324583), (0.594444, 0, 5), (1.008806, 0, 5.000001), (0, 0, 6), (-1.008806, 0, 5.000001), (-0.594444, 0, 5), (-0.594444, 0, 3.324583), (0.594444, 0, 3.324583)], k=[0, 1, 2, 3, 4, 5, 6, 7], d=1)


		pm.select(moveAll_circle, xAxis, zAxis)

		shapes = pm.ls(sl=True, dag=True)
		cShape_1 = shapes[1]
		cShape_2 = shapes[3]
		cShape_3 = shapes[5]
		print 'shape 1:', cShape_1
		print 'shape 2:', cShape_2
		print 'shape 3:', cShape_3

		cShape_2.overrideEnabled.set(1)
		cShape_2.overrideColor.set(12)
		cShape_3.overrideEnabled.set(1)
		cShape_3.overrideColor.set(6)
		pm.rename(cShape_1, 'moveAll_shape')
		pm.rename(cShape_2, 'xAxis_shape')
		pm.rename(cShape_3, 'zAxis_shape')


		moveAll = pm.group(empty=True, n='ct_moveAll')

		pm.parent(cShape_1, cShape_2, cShape_3, moveAll, s=1, r=1)

		pm.delete(moveAll_circle, xAxis, zAxis)

	if pm.objExists('*joint_grp'):
		pm.select('*joint_grp')
		jnt_grp = pm.ls(sl=True)[0]
		# print jnt_grp
		# pm.parent(pad, jnt_grp)
		pm.scaleConstraint(moveAll, jnt_grp)

	else:
		jnt_grp = pm.group(empty=True)
		grp_name = main_root.replace('lt_arm_01_twist', 'joint_grp')
		jnt_grp.rename(grp_name)
		# print jnt_grp
		# pm.parent(pad, jnt_grp)
		pm.scaleConstraint(moveAll, jnt_grp)

	if pm.objExists('*icon_grp'):
		pm.select('*icon_grp')
		icon_grp = pm.ls(sl=True)[0] 
		pm.parent(moveAll, '*icon_grp')
		# pm.parent(arm_icon, fk_pad_1, elbow_icon, moveAll)

	else:
		icon_grp = pm.group(empty=True)
		pm.parent(moveAll, icon_grp)
		group_name = jnt_grp.replace('joint', 'icon')
		icon_grp.rename(group_name)
		# pm.parent(arm_icon, fk_pad_1, elbow_icon, moveAll)
	'''
	Create the Gimbal icon
	'''
	gimbal_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))

	gimbal_icon_2 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=0.2, tol=0.01, nr=(1, 0, 0))[0]

	gimbal_icon_2.ty.set(1)
	freezeTransform(gimbal_icon_2)

	pm.select(gimbal_icon, gimbal_icon_2)

	selection = pm.ls(sl=True, dag=True, s=True)
	shape_1 = selection[0]
	shape_2 = selection[1]
	# print shape_1
	# print shape_2

	core_icon = pm.group(empty=True)

	pm.parent(shape_1, shape_2, core_icon, r=True, s=True)

	pm.delete(gimbal_icon, gimbal_icon_2)

	icon_name = arm_icon.replace('arm', 'arm_gimbal_core')
	core_icon.rename(icon_name)

	shape_name = core_icon.replace('_icon', 'Shape1')
	shape_1.rename(shape_name)

	shape_name = shape_1.replace('1', '2')
	shape_2.rename(shape_name)

	temp_constraint = pm.pointConstraint(main_root, core_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(core_icon)

	pm.parent(core_icon, arm_global)
	pm.orientConstraint(core_icon, fk_pad_1, mo=1)


	twist_gimbal_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(main_root, twist_gimbal_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(twist_gimbal_grp)

	pm.parent(twist_gimbal_grp, twist_jnt_grp)

	pm.parent(main_root, twist_gimbal_grp)


	grp_name = core_icon.replace('arm_gimbal_core_icon', 'twist_gimbal_core_grp')
	twist_gimbal_grp.rename(grp_name)

	gimbal_core_tog = pm.shadingNode('blendColors', asUtility=1)

	node_name = arm_icon.replace('icon', 'gimbal_core_tog_blendColors')
	gimbal_core_tog.rename(node_name)

	pm.connectAttr(core_icon + '.r', gimbal_core_tog + '.color2')
	gimbal_core_tog.color1R.set(0)
	gimbal_core_tog.color1G.set(0)
	gimbal_core_tog.color1B.set(0)
	pm.connectAttr(gimbal_core_tog + '.output', twist_jnt_grp + '.r')
	pm.connectAttr(switch + '.IkFk', gimbal_core_tog + '.blender')
	pm.connectAttr(switch + '.IkFk', core_icon + '.v')




def joint_positions(*j):
	pm.joint(zso=1, ch=1, e=1, oj='xzy', secondaryAxisOrient='zup')
	pos = [pm.xform(j,q=True, t=True, ws=True)]
	# print pos
   	children = cmds.listRelatives(j, c=True) or []
   	for child in children:
 		pos.extend(joint_positions(child))
	return pos

def freezeTransform(*args):
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
	# print 'Transform Frozen'

def deleteHistory(*args):
	pm.delete(ch=True)
	# print 'History Deleted'

def centerPivot(*args):
	pm.xform(cpc=True)
	# print 'Selected pivot centered.'

