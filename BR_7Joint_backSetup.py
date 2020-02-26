import pymel.core as pm
def back():

	joint_system = pm.ls(sl=True)
	bind_joint_system = joint_system[0]
	curve_bind = joint_system[1]
	fk_joint_system = joint_system[2]

	bind_joints = pm.ls(bind_joint_system, dag=True)
	curve_joints = pm.ls(curve_bind, dag=True)
	fk_joints = pm.ls(fk_joint_system, dag=True)

	b_joint_pad = bind_joints[0]
	b_joint_1 = bind_joints[1]
	b_joint_2 = bind_joints[2]
	b_joint_3 = bind_joints[3]
	b_joint_4 = bind_joints[4]
	b_joint_5 = bind_joints[5]
	b_joint_6 = bind_joints[6]
	b_joint_7 = bind_joints[7]
	ik_curve = bind_joints[8]
	print ik_curve
	ik_curve_shape = bind_joints[9]

	cB_joint_1 = curve_joints[0]
	cB_joint_2 = curve_joints[1]
	cB_joint_3 = curve_joints[2]
	cB_joint_4 = curve_joints[3]
	cB_joint_5 = curve_joints[4]
	cB_joint_6 = curve_joints[5]
	cB_joint_7 = curve_joints[6]

	fk_joint_1 = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	fk_joint_4 = fk_joints[3]
	fk_joint_5 = fk_joints[4]
	fk_joint_6 = fk_joints[5]
	fk_joint_7 = fk_joints[6]

	'''
	Step one
	'''
	pm.select(b_joint_1, b_joint_7, ik_curve)
	back_ik = pm.ikHandle(sol='ikSplineSolver', pcv=False, ccv=False)[0]
	ik_name = b_joint_1.replace('01_bind', 'ikh')
	back_ik.rename(ik_name)
	curve_name = back_ik.replace('ikh', 'crv')
	ik_curve.rename(curve_name)
	back_ik.twist.set(-90)
	ik_curve.inheritsTransform.set(0)

	'''
	Step two
	'''
	pm.parent(cB_joint_7, b_joint_pad)
	back_7_name = bind_joint_system.replace('00_pad', '02_curveBind')
	cB_joint_7.rename(back_7_name)

	pm.delete(cB_joint_2)

	back_1_name = cB_joint_7.replace('02', '01')
	cB_joint_1.rename(back_1_name)

	pm.select(cB_joint_1, cB_joint_7, ik_curve)
	pm.mel.SmoothBindSkin()

	'''
	Step Three
	'''
	hip_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	deleteHistory(hip_icon)
	icon_naame = b_joint_1.replace('back_01_bind', 'hip_icon')
	hip_icon.rename(icon_naame)

	chest_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	deleteHistory(chest_icon)
	icon_naame = hip_icon.replace('hip', 'chest')
	chest_icon.rename(icon_naame)

	temp_constraint = pm.pointConstraint(b_joint_7, chest_icon)
	pm.delete(temp_constraint)
	freezeTransform()

	hip_icon.rotateOrder.set(2)
	chest_icon.rotateOrder.set(2)
	cB_joint_1.rotateOrder.set(2)
	cB_joint_7.rotateOrder.set(2)

	pm.parentConstraint(chest_icon, cB_joint_7, mo=1)
	pm.parentConstraint(hip_icon, cB_joint_1, mo=1)


	back_ik.dTwistControlEnable.set(1)
	back_ik.dWorldUpType.set(4)

	back_ik.dWorldUpAxis.set(1)
	back_ik.dWorldUpVectorY.set(-1)
	back_ik.dWorldUpVectorEndY.set(0)
	back_ik.dWorldUpVectorEndZ.set(-1)

	'''
	Step Four
	'''
	pm.parent(fk_joint_3, fk_joint_1)
	pm.delete(fk_joint_2)
	pm.parent(fk_joint_5, fk_joint_3)
	pm.delete(fk_joint_4)
	pm.parent(fk_joint_7, fk_joint_5)
	pm.delete(fk_joint_6)

	joint_name = fk_joint_1.replace('bind2', 'fk')
	fk_joint_1.rename(joint_name)

	joint_name = fk_joint_1.replace('01', '02')
	fk_joint_3.rename(joint_name)

	joint_name = fk_joint_3.replace('02', '03')
	fk_joint_5.rename(joint_name)

	joint_name = fk_joint_7.replace('07_waste', '04_fk')
	fk_joint_7.rename(joint_name)

	fk_joint_1.rotateOrder.set(1)
	fk_joint_3.rotateOrder.set(1)
	fk_joint_5.rotateOrder.set(1)
	fk_joint_7.rotateOrder.set(1)

	hip_local = pm.group(hip_icon)

	chest_local = pm.group(chest_icon)

	local_name = hip_icon.replace('icon', 'local')
	hip_local.rename(local_name)

	local_name = chest_icon.replace('icon', 'local')
	chest_local.rename(local_name)

	pm.parentConstraint(fk_joint_1, hip_local, mo=1)
	pm.parentConstraint(fk_joint_7, chest_local, mo=1)

	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	deleteHistory(fk_icon_1)
	fk_icon_2 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	deleteHistory(fk_icon_2)

	temp_constraint = pm.parentConstraint(fk_joint_3, fk_icon_1, mo=0)
	pm.delete(temp_constraint)
	temp_constraint = pm.parentConstraint(fk_joint_5, fk_icon_2, mo=0)
	pm.delete(temp_constraint)
	pm.orientConstraint(fk_icon_1, fk_joint_3, mo=1)
	pm.orientConstraint(fk_icon_2, fk_joint_5, mo=1)

	fk_local_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_joint_3, fk_local_1)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_1, fk_local_1)	

	fk_local_2 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_joint_5, fk_local_2)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_2, fk_local_2)
	pm.select(fk_icon_1, fk_icon_2)
	freezeTransform()

	pm.parent(fk_local_2, fk_icon_1)

	icon_naame = hip_icon.replace('hip', 'back_01_fk')
	fk_icon_1.rename(icon_naame)

	icon_naame = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(icon_naame)

	local_name = fk_icon_1.replace('icon', 'local')
	fk_local_1.rename(local_name)

	local_name =fk_icon_2.replace('icon', 'local')
	fk_local_2.rename(local_name)

	'''
	Step five
	'''
	curve_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = ik_curve.replace('crv', 'info')
	curve_info.rename(node_name)

	pm.connectAttr(ik_curve + '.worldSpace', curve_info + '.inputCurve')

	stretch_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = curve_info.replace('info', 'mult')
	stretch_mult.rename(node_name)
	stretch_mult.operation.set(2)

	pm.connectAttr(curve_info + '.arcLength', stretch_mult + '.input1X')
	arcLen = pm.promptDialog(title='arcLength #', 
							 m='Enter arcLength #', 
							 b=['Enter', 'Cancel'],
							 db='Enter',
							 cb='Cancel',
							 ds='Cancel'
							 )
	if arcLen == 'Enter':
		text = pm.promptDialog(q=True, tx=True)
		stretch_mult.input2X.set(int(text))
		pm.connectAttr(stretch_mult + '.outputX', b_joint_1 + '.sx')
		pm.connectAttr(stretch_mult + '.outputX', b_joint_2 + '.sx')
		pm.connectAttr(stretch_mult + '.outputX', b_joint_3 + '.sx')
		pm.connectAttr(stretch_mult + '.outputX', b_joint_4 + '.sx')
		pm.connectAttr(stretch_mult + '.outputX', b_joint_5 + '.sx')
		pm.connectAttr(stretch_mult + '.outputX', b_joint_6 + '.sx')

		stretch_squareRoot = pm.shadingNode('multiplyDivide', asUtility=1)
		node_name = stretch_mult.replace('mult', 'squareRoot')
		stretch_squareRoot.rename(node_name)

		pm.connectAttr(stretch_mult + '.outputX', stretch_squareRoot + '.input1X')
		stretch_squareRoot.operation.set(3)
		stretch_squareRoot.input2X.set(.5)

		stretch_invert = pm.shadingNode('multiplyDivide', asUtility=1)
		node_name = stretch_mult.replace('mult', 'invert')
		stretch_invert.rename(node_name)

		pm.connectAttr(stretch_squareRoot + '.outputX', stretch_invert + '.input2X')
		stretch_invert.operation.set(2)
		stretch_invert.input1X.set(1)


		pm.connectAttr(stretch_invert + '.outputX', b_joint_1 + '.sy')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_2 + '.sy')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_3 + '.sy')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_4 + '.sy')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_5 + '.sy')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_6 + '.sy')

		pm.connectAttr(stretch_invert + '.outputX', b_joint_1 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_2 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_3 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_4 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_5 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', b_joint_6 + '.sz')

		'''
		Step six
		'''

		back_global = pm.curve(p=[(0.5, 0, 0.5), (-0.5, 0, 0.5), (-0.5, 0, -0.5), (0.5, 0, -0.5), (0.5, 0, 0.5)], k=[0, 1, 2, 3, 4], d=1)
		icon_naame = hip_icon.replace('hip', 'body')
		back_global.rename(icon_naame)

		temp_constraint = pm.pointConstraint(b_joint_1, back_global, mo=0)
		pm.delete(temp_constraint)
		pm.select(back_global)
		deleteHistory()
		freezeTransform()
		back_global.rotateOrder.set(2)

		pm.parent(fk_local_1, chest_local, hip_local, back_ik, b_joint_pad)

		pm.parentConstraint(back_global, b_joint_pad, mo=1)

		'''
		Step eight 
		'''
		dnt = pm.group(ik_curve, cB_joint_1, cB_joint_7, fk_joint_1)
		grp_name = b_joint_pad.replace('00_pad', 'DO____NOT____TOUCH')
		dnt.rename(grp_name)
		dnt.overrideEnabled.set(1)
		dnt.overrideDisplayType.set(2)
		dnt.v.set(0)

		pm.setAttr(fk_icon_1 + '.tx', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_1 + '.ty', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_1 + '.tz', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_1 + '.sx', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_1 + '.sy', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_1 + '.sz', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_1 + '.v', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_2 + '.tx', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_2 + '.ty', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_2 + '.tz', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_2 + '.sx', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_2 + '.sy', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_2 + '.sz', lock=True, channelBox=False, keyable=False)
		pm.setAttr(fk_icon_2 + '.v', lock=True, channelBox=False, keyable=False)
		pm.setAttr(back_global + '.sx', lock=True, channelBox=False, keyable=False)
		pm.setAttr(back_global +'.sy', lock=True, channelBox=False, keyable=False)
		pm.setAttr(back_global + '.sz', lock=True, channelBox=False, keyable=False)
	if arcLen == 'Cancel':
		pm.warning('Must enter arcLength - Select the back_info node, find the arcLength, undo the back setup, then do step 5 again')

	


def freezeTransform(*args):
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
	print 'Transform Frozen'

def deleteHistory(*args):
	pm.delete(ch=True)
	print 'History Deleted'









