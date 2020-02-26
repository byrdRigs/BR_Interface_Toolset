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
	reload (beJointSplit)
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
	reload (beJointSplit)
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

