'''
4 Joint neck Ik spline setup

How to run:
import BR_Interface_Toolset.BR_4Joint_neckSetup as BR_4Joint_neckSetup
reload(BR_4Joint_neckSetup)
BR_4Joint_neckSetup.setup()
'''

import pymel.core as pm 
import maya.cmds as cmds

def joint_positions(*j):
	pm.joint(zso=1, ch=1, e=1, oj='xzy', secondaryAxisOrient='zup')
	pos = [pm.xform(j,q=True, t=True, ws=True)]
	print pos
   	children = cmds.listRelatives(j, c=True) or []
   	for child in children:
 		pos.extend(joint_positions(child))
	return pos


def freezeTransform(*args):
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
	print 'Transform Frozen'

def deleteHistory(*args):
	pm.delete(ch=True)
	print 'History Deleted'

def setup(*args):
	joint_system = pm.ls(sl=True, dag=True)
	root_joint  = joint_system[0]
	joint_2 = joint_system[1]
	joint_3= joint_system[2]
	joint_4 = joint_system[3]
	print 'Root joint:', root_joint
	print 'Joint 2:', joint_2
	print 'Joint 3', joint_3
	print 'Joint 4:', joint_4	
	joints = joint_positions(root_joint) 
	neck_curve = pm.curve(d = 1, p=joints)

	joint_4.jointOrientX.set(0)

	pad = pm.group(empty=True)

	# Move group to joint.
	# 	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transformation on the group.
	pm.makeIdentity(pad, apply=True, t=1, r=1, s=1, n=0)
	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

	curve_name = root_joint.replace('01_bind', 'crv')
	neck_curve.rename(curve_name)

	ik_jointChain = pm.duplicate(root_joint)
	pm.select(ik_jointChain)

	ik_joints = pm.ls(sl=True, dag=True)

	ik_root = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	ik_joint_4 = ik_joints[3]

	joint_name = ik_root.replace('bind1', 'ik')
	ik_root.rename(joint_name)

	joint_name = ik_root.replace('01', '02')
	ik_joint_2.rename(joint_name)

	joint_name = ik_root.replace('01', '03')
	ik_joint_3.rename(joint_name)

	joint_name = ik_joint_4.replace('waste', 'ik')
	ik_joint_4.rename(joint_name)


	fk_jointChain = pm.duplicate(root_joint)
	pm.select(fk_jointChain)

	fk_joints = pm.ls(sl=True, dag=True)

	fk_root_joint = fk_joints[0]
	fk_joint_2 = fk_joints[3]
	fk_joint_3 = fk_joints[1]


	pm.parent(fk_joint_2, fk_root_joint)
	pm.delete(fk_joint_3)

	joint_name = ik_root.replace('ik', 'fk')
	fk_root_joint.rename(joint_name)

	joint_name = ik_joint_2.replace('ik', 'fk')
	fk_joint_2.rename(joint_name)

	fk_root_joint.rotateOrder.set(1)



	'''
	Create the ikSpline
	'''

	pm.select(ik_root, ik_joint_4, neck_curve)
	neck_ik = pm.ikHandle(sol='ikSplineSolver', ccv=False, pcv=False)[0]

	ik_name = neck_curve.replace('crv', 'ikh')
	neck_ik.rename(ik_name)

	'''
	Create the curveBind joints
	'''

	bind_dup = pm.duplicate(root_joint)

	pm.select(bind_dup)

	curveBind = pm.ls(sl=True, dag=True)
	cb_joint_1 = curveBind[0]
	cb_joint_2 = curveBind[3]
	cb_joint_3 = curveBind[1]


	pm.parent(cb_joint_2, w=1)
	pm.delete(cb_joint_3)

	joint_name = root_joint.replace('b', 'curveB')
	cb_joint_1.rename(joint_name)

	joint_name = cb_joint_1.replace('01', '02')
	cb_joint_2.rename(joint_name)

	pm.select(cb_joint_1, cb_joint_2,neck_curve)
	pm.mel.SmoothBindSkin()

	neck_ik.dTwistControlEnable.set(1)
	neck_ik.dWorldUpType.set(4)

	neck_ik.dForwardAxis.set(0)
	neck_ik.dWorldUpAxis.set(1)


	'''
	Create the ik and fk curve
	'''

	ik_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]

	temp_constraint = pm.parentConstraint(ik_joint_4, ik_icon)
	pm.delete(temp_constraint)
	freezeTransform(ik_icon)
	deleteHistory(ik_icon)

	curve_name = neck_ik.replace('h', '_icon')
	ik_icon.rename(curve_name)

	pm.parentConstraint(ik_icon, cb_joint_2, mo=1)



	fk_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_icon)
	pm.delete(temp_constraint)
	freezeTransform(fk_icon)
	deleteHistory(fk_icon)

	curve_name = ik_icon.replace('ik', 'fk')
	fk_icon.rename(curve_name)

	pm.parentConstraint(fk_icon, fk_root_joint, mo=1)

	attrs = ['tx', 'ty','tz', 'sx', 'sy', 'sz']

	for current_attr in attrs:
		attr = fk_icon.attr(current_attr)
		attr.set(lock=1, keyable=0, channelBox=0)


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




	ik_local = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(ik_icon, ik_local)
	pm.delete(temp_constraint)

	pm.parent(ik_icon, ik_local)
	freezeTransform(ik_icon)
	local_name = ik_icon.replace('icon', 'local')
	ik_local.rename(local_name)


	pm.parentConstraint(fk_icon, ik_local, mo=1)


	curve_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = neck_curve.replace('crv', 'info')
	curve_info.rename(node_name)

	pm.connectAttr(neck_curve + '.worldSpace', curve_info + '.inputCurve')

	stretch_percent_div = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = curve_info.replace('info', 'percent_div')
	stretch_percent_div.rename(node_name)
	stretch_percent_div.operation.set(2)

	arcLen = pm.getAttr(curve_info + '.arcLength')
	stretch_percent_div.input2X.set(arcLen)

	global_scale = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = stretch_percent_div.replace('div', 'global_scale_neck_div')
	global_scale.rename(node_name)
	pm.connectAttr(curve_info + '.arcLength', global_scale + '.input1X')
	pm.connectAttr(moveAll + '.scaleY', global_scale + '.input2X')
	global_scale.operation.set(2)

	pm.connectAttr(stretch_percent_div + '.outputX', ik_root + '.scaleX')
	pm.connectAttr(stretch_percent_div + '.outputX', ik_joint_2 + '.scaleX')
	pm.connectAttr(stretch_percent_div + '.outputX', ik_joint_3 + '.scaleX')

	pm.connectAttr(global_scale + '.outputX', stretch_percent_div + '.input1X')


	pm.parentConstraint(ik_root, root_joint)
	pm.parentConstraint(ik_joint_2, joint_2)
	pm.parentConstraint(ik_joint_3, joint_3)

	global_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(root_joint, global_grp)
	pm.delete(temp_constraint)
	freezeTransform(global_grp)

	pm.parent(neck_curve, neck_ik, cb_joint_1, cb_joint_2, fk_icon, ik_local, global_grp)

	group_name = root_joint.replace('01_bind', 'global_grp')
	global_grp.rename(group_name)

	pm.parent(global_grp, moveAll)

	neck_curve.inheritsTransform.set(0)

	pm.parentConstraint(moveAll, pad, mo=1)


	attrs = ['sx', 'sy', 'sz']

	for current_attr in attrs:
		attr = ik_icon.attr(current_attr)
		attr.set(lock=1, keyable=0, channelBox=0)


	'''
	Space Switch
	'''

	'''
	Head
	'''

	head_loc = pm.spaceLocator(p=(0, 0, 0))

	loc_name = joint_4.replace('neck_04_waste', 'headNeck_space_loc')
	head_loc.rename(loc_name)

	temp_constraint = pm.parentConstraint(joint_4, head_loc, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(head_loc)
