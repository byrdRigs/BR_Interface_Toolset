'''
BR_handFinger_setup

How to run window:
import BR_Interface_Toolset.BR_handFinger_setup as BR_handFinger_setup
reload(BR_handFinger_setup)
BR_handFinger.gui()


How to run the fisrt step:
import BR_Interface_Toolset.BR_handFinger_setup as BR_handFinger_setup
reload(BR_handFinger_setup)
BR_handFinger_setup.hand_setup()

How to run the second step:
import BR_Interface_Toolset.BR_handFinger_setup as BR_handFinger_setup
reload(BR_handFinger_setup)
BR_handFinger_setup.fingerSelection()
'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

window_bgc = (.2,.2,.2)
color_1 = (.141,.725,.627)
color_2 = (.078, .678, .557)
color_3 = (.059, .612, .749)
color_4 = (.059, .475, .616)
color_5 = (.059, .392, .663)
color_6 = (.224, .259, .894)
color_7 = (.475, .278, .925)
color_8 = (.447, .145, .965)
color_9 = (.475, .078, .678)
color_10 = (.576, .039, .839)

def gui():
	if pm.window('ByrdRigs_Hand_Window', q=1, exists=1):
		pm.deleteUI('ByrdRigs_Hand_Window')
		#ByrdRigs_Hand_Window

	win_width = 240
	window_object = pm.window('ByrdRigs_Hand_Window', title="ByrdRigs_Hand_Window", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()

	hand_layout = pm.frameLayout(w=win_width, l='Hand Setup', bgc=color_1, cl=0, cll=1, ann='Hand Setup', cc=windowResize)
	pm.gridLayout(w=win_width, cr=1, cw=120, nr=4, nc=2)
	pm.button(l='Last arm joint', w=120, c=armJoint_selection)
	arm_joint_selection = pm.textField('arm_joint_selection', ed=0, w=120)
	pm.button(l='Arm Icon', w=120, c=armIcon_selection)
	arm_icon_selection = pm.textField('arm_icon_selection', ed=0, w=120)
	pm.button(l='Hand Joint', w=120, c=handJoint_selection)
	hand_root_joint_selection = pm.textField('hand_root_joint_selection', ed=0, w=120)
	pm.setParent(hand_layout)
	pm.columnLayout(w=win_width)
	pm.button(l='Hand Setup', w=win_width, c=hand_setup)

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_1, st='in')


	fingerSelection_layout = pm.frameLayout(w=win_width, l='Finger Selection', bgc=color_2, cl=0, cll=1, ann='Finger Selection', cc=windowResize)
	# pm.text(l='Select the fingers and thumb "01_bind" joints')
	pm.gridLayout(w=win_width, cr=1, cw=120, nr=5, nc=2)
	pm.button(l='Index Selection', w=win_width, c=index_selection)
	indexJoint_selection = pm.textField('indexJoint_selection', ed=0, w=120)
	pm.button(l='Middle Selection', w=win_width, c=middle_selection)
	middleJoint_selection = pm.textField('middleJoint_selection', ed=0, w=120)
	pm.button(l='Ring Selection', w=win_width, c=ring_selection)
	ringJoint_selection = pm.textField('ringJoint_selection', ed=0, w=120)
	pm.button(l='Pinky Selection', w=win_width, c=pinky_selection)
	pinkyJoint_selection = pm.textField('pinkyJoint_selection', ed=0, w=120)
	pm.button(l='Thumb Selection', w=win_width, c=thumb_selection)
	thumbJoint_selection = pm.textField('thumbJoint_selection', ed=0, w=120)
	pm.setParent(fingerSelection_layout)
	pm.text(l='Chose Selection amount')
	pm.rowColumnLayout(w=win_width, nc=3)
	pm.button(l='Two + Thumb', w=90, c=twoFingerSelection)
	pm.button(l='Three + Thumb', w=90, c=threeFingerSelection)
	pm.button(l='Five', w=60, c=fiveFingerSelection)


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_2, st='in')
	



	finger_layout = pm.frameLayout(w=win_width, l='Finger Setup', bgc=color_3, cl=0, cll=1, ann='Finger Setuo', cc=windowResize)
	pm.columnLayout(adjustableColumn=1)
	finger_selection_grp = pm.radioButtonGrp('fingerSelection_Grp', labelArray3=['Two Fingers and Thumb', 'Three Fingers and Thumb', 'Five Fingers'], numberOfRadioButtons=3, vr=1, sl=3, w=win_width)
	pm.setParent(finger_layout)
	pm.columnLayout()
	pm.button(l='Finger Setup', w=win_width, c=buttonSelection)

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_3, st='in')


	# pm.text(l='Create the pivot locators', w=win_width)
	# pm.button(l='Locator Creation', w=win_width, c=locator_creation)

	# pm.separator(w=win_width, bgc=color_3, st='in')
	# pm.text(l='Move inner_loc to the inner part of the palm, the outer_loc to the outer part, and the middle_loc to the middle joint', w=win_width, ww=1)



	pm.window('ByrdRigs_Hand_Window', e=1, wh=(240, 45), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)


def windowResize(*args):
	if pm.window('ByrdRigs_Hand_Window', q=1, exists=1):
		pm.window('ByrdRigs_Hand_Window', e=1, wh=(240, 45), rtf=1)
	else:
		pm.warming('ByrdRigs_Hand_Window does not exist')

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
	# print 'Parent Constraint with Maintain Offset On'
	selection = pm.ls(sl=1, dag=1)
	driver = selection[0]
	driven = selection[1]
	pm.parentConstraint(driver, driven, mo=1)

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

def armJoint_selection(*args):
	global arm_waste
	selection = pm.ls(sl=1)
	arm_waste = selection[0]
	print 'arm_12_bind selected:', arm_waste

	arm_textChange = pm.textField('arm_joint_selection', e=1, text=arm_waste)

def armIcon_selection(*args):
	global arm_icon
	selection = pm.ls(sl=1)
	arm_icon = selection[0]
	print 'arm_icon selected:', arm_icon

	armIcon_textChange = pm.textField('arm_icon_selection', e=1, text=arm_icon)

def handJoint_selection(*args):
	global hand_root_joint, hand_joint_2
	selection = pm.ls(sl=1, dag=1)
	hand_root_joint = selection[0]
	hand_joint_2 = selection[1]
	print 'hand_01_bind selected:', hand_root_joint
	print 'hand_02_waste selected:', hand_joint_2

	hand_textChange_1 = pm.textField('hand_root_joint_selection', e=1, text=hand_root_joint)

def index_selection(*args):
	global index_selection, index_root, index_joint_2, index_joint_3, index_joint_4, index_joint_5
	index_selection = pm.ls(sl=1, dag=1)
	index_root = index_selection[0]
	index_joint_2 = index_selection[1]
	index_joint_3 = index_selection[2]
	index_joint_4 = index_selection[3]
	index_joint_5 = index_selection[4]
	print 'Index Root:', index_root
	print 'Index Joint 2:', index_joint_2
	print 'Index Joint 3:',  index_joint_3
	print 'Index Joint 4:', index_joint_4
	print 'Index Joint 5:', index_joint_5 

	index_textChange = pm.textField('indexJoint_selection', e=1, text=index_root)

def middle_selection(*args):
	global middle_selection, middle_root, middle_joint_2, middle_joint_3, middle_joint_4, middle_joint_5
	middle_selection = pm.ls(sl=1, dag=1)
	middle_root = middle_selection[0]
	middle_joint_2 = middle_selection[1]
	middle_joint_3 = middle_selection[2]
	middle_joint_4 = middle_selection[3]
	middle_joint_5 = middle_selection[4]
	print 'Middle Root:', middle_root
	print 'Middle Joint 2:', middle_joint_2
	print 'Middle Joint 3:',  middle_joint_3
	print 'Middle Joint 4:', middle_joint_4
	print 'Middle Joint 5:', middle_joint_5 

	middle_textChange = pm.textField('middleJoint_selection', e=1, text=middle_root)

def ring_selection(*args):
	global ring_selection, ring_root, ring_joint_2, ring_joint_3, ring_joint_4, ring_joint_5
	ring_selection = pm.ls(sl=1, dag=1)
	ring_root = ring_selection[0]
	ring_joint_2 = ring_selection[1]
	ring_joint_3 = ring_selection[2]
	ring_joint_4 = ring_selection[3]
	ring_joint_5 = ring_selection[4]
	print 'Ring Root:', ring_root
	print 'Ring Joint 2:', ring_joint_2
	print 'Ring Joint 3:',  ring_joint_3
	print 'Ring Joint 4:', ring_joint_4
	print 'Ring Joint 5:', ring_joint_5 

	ring_textChange = pm.textField('ringJoint_selection', e=1, text=ring_root)

def pinky_selection(*args):
	global pinky_selection, pinky_root, pinky_joint_2, pinky_joint_3, pinky_joint_4, pinky_joint_5
	pinky_selection = pm.ls(sl=1, dag=1)
	pinky_root = pinky_selection[0]
	pinky_joint_2 = pinky_selection[1]
	pinky_joint_3 = pinky_selection[2]
	pinky_joint_4 = pinky_selection[3]
	pinky_joint_5 = pinky_selection[4]
	print 'Pinky Root:', pinky_root
	print 'Pinky Joint 2:', pinky_joint_2
	print 'Pinky Joint 3:',  pinky_joint_3
	print 'Pinky Joint 4:', pinky_joint_4
	print 'Pinky Joint 5:', pinky_joint_5 

	pinky_textChange = pm.textField('pinkyJoint_selection', e=1, text=pinky_root)

def thumb_selection(*args):
	global thumb_selection, thumb_pivot, thumb_joint_1, thumb_joint_2, thumb_joint_3, thumb_joint_4
	thumb_selection = pm.ls(sl=1, dag=1)
	thumb_pivot = thumb_selection[0]
	thumb_joint_1 = thumb_selection[1]
	thumb_joint_2 = thumb_selection[2]
	thumb_joint_3 = thumb_selection[3]
	thumb_joint_4 = thumb_selection[4]
	print 'Thumb Pivot:', thumb_pivot
	print 'Thumb Joint 1:', thumb_joint_1
	print 'Thumb Joint 2:',  thumb_joint_2
	print 'Thumb Joint 3:', thumb_joint_3
	print 'Thumb Joint 4:', thumb_joint_4

	thumb_textChange = pm.textField('thumbJoint_selection', e=1, text=thumb_pivot) 

def create_circle():
    global icon
    icon = pm.circle(nr=[0,1,0])[0]

def ctrlPadding(*args):
	selected = pm.ls(selection=1)
	#print 'Current Selected:' , selected 
	icon = selected[0]

	local = pm.group(empty=1)
	temp_constraint =pm.parentConstraint(icon, local)
	pm.delete(temp_constraint)
	pm.parent(icon, local)
	local_name = icon.replace('_iconShape', '_local')
	# print(local_name)
	local.rename(local_name)

def hand_setup(*args):
	# global arm_waste, arm_icon, hand_root_joint, hand_joint_2
	# selection = pm.ls(sl=1, dag=1)
	# arm_waste = selection[0]
	# hand_root_joint = selection[1]
	# hand_joint_2 = selection[2]
	# arm_icon = selection[3]
	# print 'selection:', selection
	# print 'Arm Waste:', arm_waste
	# print 'Hand Root Joint:', hand_root_joint
	# print 'Hand Joint 2:', hand_joint_2
	# print 'Arm Icon:', arm_icon

	pm.select(arm_icon)
	ctrlPadding()

	create_circle()
	print 'Hand Icon:', icon
	temp_constraint = pm.parentConstraint(hand_root_joint, icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = hand_root_joint.replace('01_bind', 'icon')
	print 'Icon name:', icon_name
	icon.rename(icon_name)

	hand_local = pm.group(empty=1)

	temp_constraint = pm.parentConstraint(hand_root_joint, hand_local, mo=0)
	pm.delete(temp_constraint)

	local_name = icon.replace('icon', 'local')
	print 'Local Name:', local_name
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

	pm.parentConstraint(icon, hand_root_joint, mo=1)

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

def twoFingerSelection(*args):
	pm.select(index_selection, pinky_selection, thumb_selection)
	twoFinger_selection = pm.ls(sl=1)

	pm.select(cl=1)
	ik_twoFinger_setup()

def threeFingerSelection(*args):
	pm.select(index_selection, middle_selection, pinky_selection, thumb_selection)
	threeFinger_selection = pm.ls(sl=1)

	pm.select(cl=1)
	ik_threeFinger_setup()

def fiveFingerSelection(*args):
	pm.select(index_selection, middle_selection, ring_selection, pinky_selection, thumb_selection)
	fiveFinger_selection = pm.ls(sl=1)

	pm.select(cl=1)
	ik_fiveFinger_setup()

def buttonSelection(*args):
	selectionType = pm.radioButtonGrp('fingerSelection_Grp', q=1, sl=1)
	print 'Finger Selection Value:', selectionType

	if selectionType == 1:
		twoFingers_and_thumb()
	if selectionType == 2:
		threeFingers_and_thumb()
	if selectionType == 3:
		five_finger_setup()

def ik_twoFinger_setup(*args):
	global hand_base
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
	pm.parent(index_root, pinky_root, thumb_joint_1, hand_base)
	
	'''
	Orient the Joints
	'''
	pm.joint(hand_base, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	
	
	'''
	Parent the thumb_01 back to the pivot
	'''
	pm.parent(thumb_joint_1, thumb_pivot)
	pm.parent(thumb_pivot, hand_base)

	pm.parent(index_root, pinky_root, thumb_pivot, w=1)		

def ik_threeFinger_setup(*args):
	global hand_base
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
	pm.parent(index_root, middle_root, pinky_root, thumb_joint_1, hand_base)
	
	'''
	Orient the Joints
	'''
	pm.joint(hand_base, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	
	
	'''
	Parent the thumb_01 back to the pivot
	'''
	pm.parent(thumb_joint_1, thumb_pivot)
	pm.parent(thumb_pivot, hand_base)

	pm.parent(index_root, middle_root, pinky_root, thumb_pivot, w=1)

def ik_fiveFinger_setup(*args):
	global hand_base
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

def indexSetup(*args):
	global index_fk_root, index_fk_joint_2, index_fk_joint_3, index_fk_joint_4, index_fk_joint_5
	global index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4, index_fkOri_joint_5
	global index_01_local
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
	# print 'Index Ori Joints:', index_ori_joints
	index_ori_root = index_ori_joints[0]
	index_ori_joint_2 = index_ori_joints[1]
	index_ori_joint_3 = index_ori_joints[2]
	index_ori_joint_4 = index_ori_joints[3]
	index_ori_joint_5 = index_ori_joints[4]

	pm.mel.searchReplaceNames('bind', 'ori', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'ori', 'hierarchy')
	joint_name = index_root.replace('bind', 'ori')
	index_ori_root.rename(joint_name)

	'''
	Parent the ori and bind
	'''

	pm.parent(index_ori_root, index_root)
	pm.parent(index_ori_joint_2, index_joint_2)
	pm.parent(index_joint_2, index_ori_root)

	pm.parent(index_ori_joint_3, index_joint_3)
	pm.parent(index_joint_3, index_ori_joint_2)

	pm.parent(index_ori_joint_4, index_joint_4)
	pm.parent(index_joint_4, index_ori_joint_3)

	pm.parent(index_ori_joint_5, index_joint_5)
	pm.parent(index_joint_5, index_ori_joint_4)

	'''
	Creat the fk joints
	'''

	index_fk_joint_system = pm.duplicate(index_root)
	pm.select(index_fk_joint_system)
	index_fk_joints = pm.ls(index_fk_joint_system, sl=1, dag=1)
	# print 'Index Fk Joints:', index_fk_joints
	index_fk_root = index_fk_joints[0]
	index_fkOri_root = index_fk_joints[1]

	index_fk_joint_2 = index_fk_joints[2]
	index_fkOri_joint_2 = index_fk_joints[3]

	index_fk_joint_3 = index_fk_joints[4]
	index_fkOri_joint_3 = index_fk_joints[5]

	index_fk_joint_4 = index_fk_joints[6]
	index_fkOri_joint_4 = index_fk_joints[7]

	index_fk_joint_5 = index_fk_joints[8]
	index_fkOri_joint_5 = index_fk_joints[9]

	pm.mel.searchReplaceNames('bind', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('ori', 'fkOri', 'hierarchy')
	joint_name = index_root.replace('bind', 'fk')
	index_fk_root.rename(joint_name)
	# print 'Fk Ori Root Joint:', index_fkOri_root

	'''
	Create the fk icons
	'''

	# Icon I
	index_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]

	temp_constraint = pm.parentConstraint(index_fk_root, index_01_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = index_fk_root.replace('fk', 'icon')
	index_01_icon.rename(icon_name)

	index_01_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(index_fk_root, index_01_local, mo=0)
	pm.delete(temp_constraint)

	local_name = index_01_icon.replace('icon', 'local')
	index_01_local.rename(local_name)

	pm.parent(index_01_icon, index_01_local)
	freezeTransform()

	pm.parent(index_fk_root, index_01_icon)

	# Icon II
	index_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(index_fk_joint_2, index_02_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = index_01_icon.replace('01', '02')
	index_02_icon.rename(icon_name)


	index_02_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(index_fk_joint_2, index_02_local, mo=0)
	pm.delete(temp_constraint)

	local_name = index_02_icon.replace('icon', 'local')
	index_02_local.rename(local_name)

	pm.parent(index_02_local, index_fkOri_root)

	pm.parent(index_02_icon, index_02_local)
	freezeTransform()

	pm.parent(index_02_local, index_fkOri_root)

	pm.parent(index_fk_joint_2, index_02_icon)

	# Icon III
	index_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(index_fk_joint_3, index_03_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = index_02_icon.replace('02', '03')
	index_03_icon.rename(icon_name)


	index_03_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(index_fk_joint_3, index_03_local, mo=0)
	pm.delete(temp_constraint)

	local_name = index_03_icon.replace('icon', 'local')
	index_03_local.rename(local_name)

	pm.parent(index_03_local, index_fkOri_joint_2)

	pm.parent(index_03_icon, index_03_local)
	freezeTransform()

	pm.parent(index_03_local, index_fkOri_joint_2)

	pm.parent(index_fk_joint_3, index_03_icon)

	# Icon IV
	index_04_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(index_fk_joint_4, index_04_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = index_03_icon.replace('03', '04')
	index_04_icon.rename(icon_name)


	index_04_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(index_fk_joint_4, index_04_local, mo=0)
	pm.delete(temp_constraint)

	local_name = index_04_icon.replace('icon', 'local')
	index_04_local.rename(local_name)

	pm.parent(index_04_local, index_fkOri_joint_2)

	pm.parent(index_04_icon, index_04_local)
	freezeTransform()

	pm.parent(index_04_local, index_fkOri_joint_3)

	pm.parent(index_fk_joint_4, index_04_icon)


	'''
	Delete History on icons
	'''
	pm.select(index_01_icon)
	deleteHistory()


	'''
	Connect the fk joints to the bind
	'''
	pm.orientConstraint(index_01_icon, index_root, mo=1)
	pm.orientConstraint(index_02_icon, index_joint_2, mo=1)
	pm.orientConstraint(index_03_icon, index_joint_3, mo=1)
	pm.orientConstraint(index_04_icon, index_joint_4, mo=1)
	pm.orientConstraint(index_04_icon, index_joint_5, mo=1)

	'''
	Connect the fkOri joints to the ori
	'''
	pm.connectAttr(index_fkOri_root + '.rotate', index_ori_root + '.rotate')
	pm.connectAttr(index_fkOri_joint_2 + '.rotate', index_ori_joint_2 + '.rotate')
	pm.connectAttr(index_fkOri_joint_3 + '.rotate', index_ori_joint_3 + '.rotate')
	pm.connectAttr(index_fkOri_joint_4 + '.rotate', index_ori_joint_4 + '.rotate')
	pm.connectAttr(index_fkOri_joint_5 + '.rotate', index_ori_joint_5 + '.rotate')

	pm.connectAttr(index_fkOri_joint_2 + '.translate', index_ori_joint_2 + '.translate')
	pm.connectAttr(index_fkOri_joint_3 + '.translate', index_ori_joint_3 + '.translate')
	pm.connectAttr(index_fkOri_joint_4 + '.translate', index_ori_joint_4 + '.translate')

def middleSetup(*args):
	global middle_fk_root, middle_fk_joint_2, middle_fk_joint_3, middle_fk_joint_4, middle_fk_joint_5
	global middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4, middle_fkOri_joint_5
	global middle_01_local
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
	middle_joint_dups = pm.duplicate(middle_root)
	pm.select(middle_joint_dups)
	middle_ori_joint_system = pm.ls(sl=1,dag=1)
	print 'Middle ori joint system:', middle_ori_joint_system
	middle_ori_joints = pm.ls(middle_ori_joint_system, sl=1, dag=1)
	print 'Middle Ori Joints:', middle_ori_joints
	middle_ori_root = middle_ori_joints[0]
	middle_ori_joint_2 = middle_ori_joints[1]
	middle_ori_joint_3 = middle_ori_joints[2]
	middle_ori_joint_4 = middle_ori_joints[3]
	middle_ori_joint_5 = middle_ori_joints[4]

	pm.mel.searchReplaceNames('bind', 'ori', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'ori', 'hierarchy')
	joint_name = middle_root.replace('bind', 'ori')
	middle_ori_root.rename(joint_name)

	'''
	Parent the ori and bind
	'''

	pm.parent(middle_ori_root, middle_root)
	pm.parent(middle_ori_joint_2, middle_joint_2)
	pm.parent(middle_joint_2, middle_ori_root)

	pm.parent(middle_ori_joint_3, middle_joint_3)
	pm.parent(middle_joint_3, middle_ori_joint_2)

	pm.parent(middle_ori_joint_4, middle_joint_4)
	pm.parent(middle_joint_4, middle_ori_joint_3)

	pm.parent(middle_ori_joint_5, middle_joint_5)
	pm.parent(middle_joint_5, middle_ori_joint_4)

	'''
	Creat the fk joints
	'''

	middle_fk_joint_system = pm.duplicate(middle_root)
	pm.select(middle_fk_joint_system)
	middle_fk_joints = pm.ls(middle_fk_joint_system, sl=1, dag=1)
	# print 'Index Fk Joints:', middle_fk_joints
	middle_fk_root = middle_fk_joints[0]
	middle_fkOri_root = middle_fk_joints[1]

	middle_fk_joint_2 = middle_fk_joints[2]
	middle_fkOri_joint_2 = middle_fk_joints[3]

	middle_fk_joint_3 = middle_fk_joints[4]
	middle_fkOri_joint_3 = middle_fk_joints[5]

	middle_fk_joint_4 = middle_fk_joints[6]
	middle_fkOri_joint_4 = middle_fk_joints[7]

	middle_fk_joint_5 = middle_fk_joints[8]
	middle_fkOri_joint_5 = middle_fk_joints[9]

	pm.mel.searchReplaceNames('bind', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('waste', 'fk', 'hierarchy')
	pm.mel.searchReplaceNames('ori', 'fkOri', 'hierarchy')
	joint_name = middle_root.replace('bind', 'fk')
	middle_fk_root.rename(joint_name)
	# print 'Fk Ori Root Joint:', middle_fkOri_root

	'''
	Create the fk icons
	'''

	# Icon I
	middle_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]

	temp_constraint = pm.parentConstraint(middle_fk_root, middle_01_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = middle_fk_root.replace('fk', 'icon')
	middle_01_icon.rename(icon_name)

	middle_01_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(middle_fk_root, middle_01_local, mo=0)
	pm.delete(temp_constraint)

	local_name = middle_01_icon.replace('icon', 'local')
	middle_01_local.rename(local_name)

	pm.parent(middle_01_icon, middle_01_local)
	freezeTransform()

	pm.parent(middle_fk_root, middle_01_icon)

	# Icon II
	middle_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(middle_fk_joint_2, middle_02_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = middle_01_icon.replace('01', '02')
	middle_02_icon.rename(icon_name)


	middle_02_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(middle_fk_joint_2, middle_02_local, mo=0)
	pm.delete(temp_constraint)

	local_name = middle_02_icon.replace('icon', 'local')
	middle_02_local.rename(local_name)

	pm.parent(middle_02_local, middle_fkOri_root)

	pm.parent(middle_02_icon, middle_02_local)
	freezeTransform()

	pm.parent(middle_02_local, middle_fkOri_root)

	pm.parent(middle_fk_joint_2, middle_02_icon)

	# Icon III
	middle_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(middle_fk_joint_3, middle_03_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = middle_02_icon.replace('02', '03')
	middle_03_icon.rename(icon_name)


	middle_03_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(middle_fk_joint_3, middle_03_local, mo=0)
	pm.delete(temp_constraint)

	local_name = middle_03_icon.replace('icon', 'local')
	middle_03_local.rename(local_name)

	pm.parent(middle_03_local, middle_fkOri_joint_2)

	pm.parent(middle_03_icon, middle_03_local)
	freezeTransform()

	pm.parent(middle_03_local, middle_fkOri_joint_2)

	pm.parent(middle_fk_joint_3, middle_03_icon)

	# Icon IV
	middle_04_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(middle_fk_joint_4, middle_04_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = middle_03_icon.replace('03', '04')
	middle_04_icon.rename(icon_name)


	middle_04_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(middle_fk_joint_4, middle_04_local, mo=0)
	pm.delete(temp_constraint)

	local_name = middle_04_icon.replace('icon', 'local')
	middle_04_local.rename(local_name)

	pm.parent(middle_04_local, middle_fkOri_joint_2)

	pm.parent(middle_04_icon, middle_04_local)
	freezeTransform()

	pm.parent(middle_04_local, middle_fkOri_joint_3)

	pm.parent(middle_fk_joint_4, middle_04_icon)


	'''
	Delete History on icons
	'''
	pm.select(middle_01_icon)
	deleteHistory()


	'''
	Connect the fk joints to the bind
	'''
	pm.orientConstraint(middle_01_icon, middle_root, mo=1)
	pm.orientConstraint(middle_02_icon, middle_joint_2, mo=1)
	pm.orientConstraint(middle_03_icon, middle_joint_3, mo=1)
	pm.orientConstraint(middle_04_icon, middle_joint_4, mo=1)
	pm.orientConstraint(middle_04_icon, middle_joint_5, mo=1)

	'''
	Connect the fkOri joints to the ori
	'''
	pm.connectAttr(middle_fkOri_root + '.rotate', middle_ori_root + '.rotate')
	pm.connectAttr(middle_fkOri_joint_2 + '.rotate', middle_ori_joint_2 + '.rotate')
	pm.connectAttr(middle_fkOri_joint_3 + '.rotate', middle_ori_joint_3 + '.rotate')
	pm.connectAttr(middle_fkOri_joint_4 + '.rotate', middle_ori_joint_4 + '.rotate')
	pm.connectAttr(middle_fkOri_joint_5 + '.rotate', middle_ori_joint_5 + '.rotate')

	pm.connectAttr(middle_fkOri_joint_2 + '.translate', middle_ori_joint_2 + '.translate')
	pm.connectAttr(middle_fkOri_joint_3 + '.translate', middle_ori_joint_3 + '.translate')
	pm.connectAttr(middle_fkOri_joint_4 + '.translate', middle_ori_joint_4 + '.translate')

def ringSetup(*args):
	global ring_fk_root, ring_fk_joint_2, ring_fk_joint_3, ring_fk_joint_4, ring_fk_joint_5
	global ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4, ring_fkOri_joint_5
	global ring_01_local
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
	ring_joint_dups = pm.duplicate(ring_root)
	pm.select(ring_joint_dups)
	ring_ori_joint_system = pm.ls(sl=1,dag=1)
	print 'Ring ori joint system:', ring_ori_joint_system
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

	'''
	Parent the ori and bind
	'''

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
	# print 'Index Fk Joints:', ring_fk_joints
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
	# print 'Fk Ori Root Joint:', ring_fkOri_root

	'''
	Create the fk icons
	'''

	# Icon I
	ring_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]

	temp_constraint = pm.parentConstraint(ring_fk_root, ring_01_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = ring_fk_root.replace('fk', 'icon')
	ring_01_icon.rename(icon_name)

	ring_01_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(ring_fk_root, ring_01_local, mo=0)
	pm.delete(temp_constraint)

	local_name = ring_01_icon.replace('icon', 'local')
	ring_01_local.rename(local_name)

	pm.parent(ring_01_icon, ring_01_local)
	freezeTransform()

	pm.parent(ring_fk_root, ring_01_icon)

	# Icon II
	ring_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(ring_fk_joint_2, ring_02_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = ring_01_icon.replace('01', '02')
	ring_02_icon.rename(icon_name)


	ring_02_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(ring_fk_joint_2, ring_02_local, mo=0)
	pm.delete(temp_constraint)

	local_name = ring_02_icon.replace('icon', 'local')
	ring_02_local.rename(local_name)

	pm.parent(ring_02_local, ring_fkOri_root)

	pm.parent(ring_02_icon, ring_02_local)
	freezeTransform()

	pm.parent(ring_02_local, ring_fkOri_root)

	pm.parent(ring_fk_joint_2, ring_02_icon)

	# Icon III
	ring_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(ring_fk_joint_3, ring_03_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = ring_02_icon.replace('02', '03')
	ring_03_icon.rename(icon_name)


	ring_03_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(ring_fk_joint_3, ring_03_local, mo=0)
	pm.delete(temp_constraint)

	local_name = ring_03_icon.replace('icon', 'local')
	ring_03_local.rename(local_name)

	pm.parent(ring_03_local, ring_fkOri_joint_2)

	pm.parent(ring_03_icon, ring_03_local)
	freezeTransform()

	pm.parent(ring_03_local, ring_fkOri_joint_2)

	pm.parent(ring_fk_joint_3, ring_03_icon)

	# Icon IV
	ring_04_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(ring_fk_joint_4, ring_04_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = ring_03_icon.replace('03', '04')
	ring_04_icon.rename(icon_name)


	ring_04_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(ring_fk_joint_4, ring_04_local, mo=0)
	pm.delete(temp_constraint)

	local_name = ring_04_icon.replace('icon', 'local')
	ring_04_local.rename(local_name)

	pm.parent(ring_04_local, ring_fkOri_joint_2)

	pm.parent(ring_04_icon, ring_04_local)
	freezeTransform()

	pm.parent(ring_04_local, ring_fkOri_joint_3)

	pm.parent(ring_fk_joint_4, ring_04_icon)


	'''
	Delete History on icons
	'''
	pm.select(ring_01_icon)
	deleteHistory()


	'''
	Connect the fk joints to the bind
	'''
	pm.orientConstraint(ring_01_icon, ring_root, mo=1)
	pm.orientConstraint(ring_02_icon, ring_joint_2, mo=1)
	pm.orientConstraint(ring_03_icon, ring_joint_3, mo=1)
	pm.orientConstraint(ring_04_icon, ring_joint_4, mo=1)
	pm.orientConstraint(ring_04_icon, ring_joint_5, mo=1)

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

def pinkySetup(*args):
	global pinky_fk_root, pinky_fk_joint_2, pinky_fk_joint_3, pinky_fk_joint_4, pinky_fk_joint_5
	global pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4, pinky_fkOri_joint_5
	global pinky_01_local
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
	pinky_joint_dups = pm.duplicate(pinky_root)
	pm.select(pinky_joint_dups)
	pinky_ori_joint_system = pm.ls(sl=1,dag=1)
	print 'Pinky ori joint system:', pinky_ori_joint_system
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

	'''
	Parent the ori and bind
	'''

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
	# print 'Index Fk Joints:', pinky_fk_joints
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
	# print 'Fk Ori Root Joint:', pinky_fkOri_root

	'''
	Create the fk icons
	'''

	# Icon I
	pinky_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]

	temp_constraint = pm.parentConstraint(pinky_fk_root, pinky_01_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = pinky_fk_root.replace('fk', 'icon')
	pinky_01_icon.rename(icon_name)

	pinky_01_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(pinky_fk_root, pinky_01_local, mo=0)
	pm.delete(temp_constraint)

	local_name = pinky_01_icon.replace('icon', 'local')
	pinky_01_local.rename(local_name)

	pm.parent(pinky_01_icon, pinky_01_local)
	freezeTransform()

	pm.parent(pinky_fk_root, pinky_01_icon)

	# Icon II
	pinky_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(pinky_fk_joint_2, pinky_02_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = pinky_01_icon.replace('01', '02')
	pinky_02_icon.rename(icon_name)


	pinky_02_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(pinky_fk_joint_2, pinky_02_local, mo=0)
	pm.delete(temp_constraint)

	local_name = pinky_02_icon.replace('icon', 'local')
	pinky_02_local.rename(local_name)

	pm.parent(pinky_02_local, pinky_fkOri_root)

	pm.parent(pinky_02_icon, pinky_02_local)
	freezeTransform()

	pm.parent(pinky_02_local, pinky_fkOri_root)

	pm.parent(pinky_fk_joint_2, pinky_02_icon)

	# Icon III
	pinky_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(pinky_fk_joint_3, pinky_03_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = pinky_02_icon.replace('02', '03')
	pinky_03_icon.rename(icon_name)


	pinky_03_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(pinky_fk_joint_3, pinky_03_local, mo=0)
	pm.delete(temp_constraint)

	local_name = pinky_03_icon.replace('icon', 'local')
	pinky_03_local.rename(local_name)

	pm.parent(pinky_03_local, pinky_fkOri_joint_2)

	pm.parent(pinky_03_icon, pinky_03_local)
	freezeTransform()

	pm.parent(pinky_03_local, pinky_fkOri_joint_2)

	pm.parent(pinky_fk_joint_3, pinky_03_icon)

	# Icon IV
	pinky_04_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(pinky_fk_joint_4, pinky_04_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = pinky_03_icon.replace('03', '04')
	pinky_04_icon.rename(icon_name)


	pinky_04_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(pinky_fk_joint_4, pinky_04_local, mo=0)
	pm.delete(temp_constraint)

	local_name = pinky_04_icon.replace('icon', 'local')
	pinky_04_local.rename(local_name)

	pm.parent(pinky_04_local, pinky_fkOri_joint_2)

	pm.parent(pinky_04_icon, pinky_04_local)
	freezeTransform()

	pm.parent(pinky_04_local, pinky_fkOri_joint_3)

	pm.parent(pinky_fk_joint_4, pinky_04_icon)


	'''
	Delete History on icons
	'''
	pm.select(pinky_01_icon)
	deleteHistory()


	'''
	Connect the fk joints to the bind
	'''
	pm.orientConstraint(pinky_01_icon, pinky_root, mo=1)
	pm.orientConstraint(pinky_02_icon, pinky_joint_2, mo=1)
	pm.orientConstraint(pinky_03_icon, pinky_joint_3, mo=1)
	pm.orientConstraint(pinky_04_icon, pinky_joint_4, mo=1)
	pm.orientConstraint(pinky_04_icon, pinky_joint_5, mo=1)

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

def thumbSetup(*args):
	global thumb_fk_pivot, thumb_fk_joint_1, thumb_fk_joint_2, thumb_fk_joint_3
	global thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3
	global thumb_01_local, thumb_02_local

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
	thumb_joint_dups = pm.duplicate(thumb_pivot)
	pm.select(thumb_joint_dups)
	thumb_ori_joint_system = pm.ls(sl=1, dag=1)
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
	Create the fk icons
	'''
	
	# Icon I
	thumb_01_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	temp_constraint = pm.parentConstraint(thumb_fk_pivot, thumb_01_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = thumb_fk_pivot.replace('fk', 'icon')
	thumb_01_icon.rename(icon_name)

	thumb_01_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(thumb_fk_pivot, thumb_01_local, mo=0)
	pm.delete(temp_constraint)

	local_name = thumb_01_icon.replace('icon', 'local')
	thumb_01_local.rename(local_name)

	pm.parent(thumb_01_icon, thumb_01_local)
	freezeTransform()

	pm.parent(thumb_fk_pivot, thumb_01_icon)


	# Icon II
	thumb_02_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(thumb_fk_joint_1, thumb_02_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = thumb_fk_joint_1.replace('fk', 'icon')
	thumb_02_icon.rename(icon_name)

	thumb_02_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(thumb_fk_joint_1, thumb_02_local, mo=0)
	pm.delete(temp_constraint)

	local_name = thumb_02_icon.replace('icon', 'local')
	thumb_02_local.rename(local_name)

	pm.parent(thumb_02_icon, thumb_02_local)
	freezeTransform()

	pm.parent(thumb_fk_joint_1, thumb_02_icon)

	pm.parent(thumb_02_local, thumb_fkOri_pivot)
	

	# Icon III
	thumb_03_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(thumb_fk_joint_2, thumb_03_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = thumb_fk_joint_2.replace('fk', 'icon')
	thumb_03_icon.rename(icon_name)

	thumb_03_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(thumb_fk_joint_2, thumb_03_local, mo=0)
	pm.delete(temp_constraint)

	local_name = thumb_03_icon.replace('icon', 'local')
	thumb_03_local.rename(local_name)

	pm.parent(thumb_03_icon, thumb_03_local)
	freezeTransform()

	pm.parent(thumb_fk_joint_2, thumb_03_icon)

	pm.parent(thumb_03_local, thumb_fkOri_joint_1)
	

	# Icon IV
	thumb_04_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 0, 1))[0]
	temp_constraint = pm.parentConstraint(thumb_fk_joint_3, thumb_04_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	icon_name = thumb_fk_joint_3.replace('fk', 'icon')
	thumb_04_icon.rename(icon_name)

	thumb_04_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(thumb_fk_joint_3, thumb_04_local, mo=0)
	pm.delete(temp_constraint)

	local_name = thumb_04_icon.replace('icon', 'local')
	thumb_04_local.rename(local_name)

	pm.parent(thumb_04_icon, thumb_04_local)
	freezeTransform()

	pm.parent(thumb_fk_joint_3, thumb_04_icon)

	pm.parent(thumb_04_local, thumb_fkOri_joint_2)
	

	'''
	Delete History on icons
	'''
	pm.select(thumb_01_icon)
	deleteHistory()

	'''
	Connect the fk joints to the bind
	'''
	pm.orientConstraint(thumb_01_icon, thumb_pivot, mo=1)
	pm.orientConstraint(thumb_02_icon, thumb_joint_1, mo=1)
	pm.orientConstraint(thumb_03_icon, thumb_joint_2, mo=1)
	pm.orientConstraint(thumb_04_icon, thumb_joint_3, mo=1)
	pm.orientConstraint(thumb_04_icon, thumb_joint_4, mo=1)

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

def five_finger_setup(*args):
	indexSetup()
	middleSetup()
	ringSetup()
	pinkySetup()
	thumbSetup()
	SDK_setup()

def threeFingers_and_thumb(*args):
	global index_joint_system, index_root, index_joint_2, index_joint_3, index_joint_4, index_joint_5
	global middle_joint_system, middle_root, middle_joint_2, middle_joint_3, middle_joint_4, middle_joint_5
	global pinky_joint_system, pinky_root, pinky_joint_2, pinky_joint_3, pinky_joint_4, pinky_joint_5
	global thumb_joint_system, thumb_pivot, thumb_joint_1, thumb_joint_2, thumb_joint_3, thumb_joint_4
	global finger_selection
	finger_selection = pm.ls(sl=1)
	index_joint_system = finger_selection[0]
	middle_joint_system = finger_selection[1]
	pinky_joint_system = finger_selection[2]
	thumb_joint_system = finger_selection[3]
	# print 'Selection:', finger_selection
	# print 'Index Joint System:', index_joint_system
	# print 'Middele Joint System:', middle_joint_system
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

	pm.select(cl=1)

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
	pm.parent(index_root, middle_root, pinky_root, thumb_joint_1, hand_base)
	
	'''
	Orient the Joints
	'''
	pm.joint(hand_base, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	
	
	'''
	Parent the thumb_01 back to the pivot
	'''
	pm.parent(thumb_joint_1, thumb_pivot)
	pm.parent(thumb_pivot, hand_base)

	pm.parent(index_root, middle_root, pinky_root, thumb_pivot, w=1)

	indexSetup()
	middleSetup()
	pinkySetup()
	thumbSetup()


	global parent_icon, index_icon, middle_icon, pinky_icon
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
	middle_icon.tz.set(-3)
	middle_icon.sy.set(.6)
	middle_icon.sz.set(.6)
	icon_name = middle_root.replace('01_bind', 'icon')
	middle_icon.rename(icon_name)
	freezeTransform()
	deleteHistory(middle_icon)

	pinky_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	pinky_icon.tz.set(-6)
	pinky_icon.sy.set(.6)
	pinky_icon.sz.set(.6)
	icon_name = pinky_root.replace('01_bind', 'icon')
	pinky_icon.rename(icon_name)
	freezeTransform()
	deleteHistory(pinky_icon)

	pm.parent(index_icon, middle_icon, pinky_icon, parent_icon)
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


	pm.select(index_icon, middle_icon, pinky_icon)
	icon_selection = pm.ls(sl=1)

	pm.addAttr(icon_selection, ln='fingerCtrl',  at='enum', en ='-------')
	index_icon.fingerCtrl.set(lock=1, e=1, keyable=1)
	middle_icon.fingerCtrl.set(lock=1, e=1, keyable=1)
	pinky_icon.fingerCtrl.set(lock=1, e=1, keyable=1)

	pm.addAttr(icon_selection, ln='curl', max=10, dv=0, at='double', min=-10)
	index_icon.curl.set(e=1, keyable=1)
	middle_icon.curl.set(e=1, keyable=1)
	pinky_icon.curl.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='relax', max=10, dv=0, at='double', min=0)
	index_icon.relax.set(e=1, keyable=1)
	middle_icon.relax.set(e=1, keyable=1)
	pinky_icon.relax.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='scrunch', max=10, dv=0, at='double', min=-10)
	index_icon.scrunch.set(e=1, keyable=1)
	middle_icon.scrunch.set(e=1, keyable=1)
	pinky_icon.scrunch.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='spread', max=10, dv=0, at='double', min=-10)
	index_icon.spread.set(e=1, keyable=1)
	middle_icon.spread.set(e=1, keyable=1)
	pinky_icon.spread.set(e=1, keyable=1)

	
	pm.select(parent_icon)
	icon_selection = pm.ls(sl=1, dag=1)
	index_icon = icon_selection[2]
	middle_icon = icon_selection[4] 
	pinky_icon = icon_selection[6]
	# print 'Index Icon:', index_icon
	# print 'Middle Icon:', middle_icon
	# print 'Pinky Icon:', pinky_icon

	lock_and_hide(index_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(middle_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(pinky_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])



	'''
	Index Curl
	'''
	index_drivenAttr_curl = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_curl = (index_icon + '.curl')
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)

	# print "Driven:", index_driven
	index_driven_curl= [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_icon.curl.set(10)
	pm.xform(index_driven_curl, ro=(0, 0, 90))
	index_fkOri_root.rz.set(15)
	index_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)
	index_icon.curl.set(-10)
	pm.xform(index_driven_curl, ro=(0, 0, -10))
	index_fkOri_joint_2.rz.set(-20)
	index_fkOri_joint_3.rz.set(-25)
	index_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)
	index_drivenKeyframes_curl = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.curl.set(0)

	'''
	Index Scrunch
	'''
	index_drivenAttr_allScrunch = [index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_allScrunch = (index_icon + '.scrunch')
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	# print "Driven:", index_driven
	index_driven_allScrunch= [index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_icon.scrunch.set(10)
	index_fkOri_joint_2.rz.set(-50)
	index_fkOri_joint_3.rz.set(110)
	index_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	index_icon.scrunch.set(-10)
	index_fkOri_joint_2.rz.set(-3)
	index_fkOri_joint_3.rz.set(-4)
	index_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	index_drivenKeyframes_allScrunch = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.scrunch.set(0)


	'''
	Index Spread
	'''
	index_drivenAttr_spread = (index_fkOri_root + '.ry', index_fkOri_joint_2 + '.ry')
	index_driven_spread= (index_fkOri_root, index_fkOri_joint_2)
	index_driver_spread = (index_icon + '.spread')
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(10)
	pm.xform(index_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(-10)
	pm.xform(index_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(0)

	index_drivenKeyframes_spread = (index_fkOri_root + '_rotateY', index_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(index_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Index Relax
	'''
	index_drivenAttr_relax = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driven_relax = [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_driver_relax = (index_icon + '.relax')
	pm.setDrivenKeyframe(index_drivenAttr_relax, currentDriver=index_driver_relax)
	index_icon.relax.set(10)
	index_fkOri_root.rz.set(12)
	index_fkOri_joint_2.rz.set(15)
	index_fkOri_joint_3.rz.set(18)
	index_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(index_drivenAttr_relax, currentDriver=index_driver_relax)
	index_icon.relax.set(0)

	pm.keyTangent(index_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Middle Curl
	'''
	middle_drivenAttr_curl = [middle_fkOri_root + '.rz', middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driver_curl = (middle_icon + '.curl')
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)

	# print "Driven:", middle_driven
	middle_driven_curl= [middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	middle_icon.curl.set(10)
	pm.xform(middle_driven_curl, ro=(0, 0, 90))
	middle_fkOri_root.rz.set(15)
	middle_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)
	middle_icon.curl.set(-10)
	pm.xform(middle_driven_curl, ro=(0, 0, -10))
	middle_fkOri_joint_2.rz.set(-20)
	middle_fkOri_joint_3.rz.set(-25)
	middle_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)
	middle_drivenKeyframes_curl = (middle_fkOri_root + '_rotateZ', middle_fkOri_joint_2 + '_rotateZ', middle_fkOri_joint_3 + '_rotateZ', middle_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	middle_icon.curl.set(0)

	'''
	Middle Scrunch
	'''
	middle_drivenAttr_allScrunch = [middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driver_allScrunch = (middle_icon + '.scrunch')
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	# print "Driven:", middle_driven
	middle_driven_allScrunch= [middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	middle_icon.scrunch.set(10)
	middle_fkOri_joint_2.rz.set(-50)
	middle_fkOri_joint_3.rz.set(110)
	middle_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	middle_icon.scrunch.set(-10)
	middle_fkOri_joint_2.rz.set(-3)
	middle_fkOri_joint_3.rz.set(-4)
	middle_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	middle_drivenKeyframes_allScrunch = (middle_fkOri_root + '_rotateZ', middle_fkOri_joint_2 + '_rotateZ', middle_fkOri_joint_3 + '_rotateZ', middle_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	middle_icon.scrunch.set(0)

	'''
	Middle Spread
	'''
	middle_drivenAttr_spread = (middle_fkOri_root + '.ry', middle_fkOri_joint_2 + '.ry')
	middle_driven_spread= (middle_fkOri_root, middle_fkOri_joint_2)
	middle_driver_spread = (middle_icon + '.spread')
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(10)
	pm.xform(middle_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(-10)
	pm.xform(middle_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(0)

	middle_drivenKeyframes_spread = (middle_fkOri_root + '_rotateY', middle_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(middle_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Middle Relax
	'''
	middle_drivenAttr_relax = [middle_fkOri_root + '.rz', middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driven_relax = [middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	middle_driver_relax = (middle_icon + '.relax')
	pm.setDrivenKeyframe(middle_drivenAttr_relax, currentDriver=middle_driver_relax)
	middle_icon.relax.set(10)
	middle_fkOri_root.rz.set(12)
	middle_fkOri_joint_2.rz.set(15)
	middle_fkOri_joint_3.rz.set(18)
	middle_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(middle_drivenAttr_relax, currentDriver=middle_driver_relax)
	middle_icon.relax.set(0)

	pm.keyTangent(middle_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Pinky Curl
	'''
	pinky_drivenAttr_curl = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_curl = (pinky_icon + '.curl')
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)

	# print "Driven:", pinky_driven
	pinky_driven_curl= [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_icon.curl.set(10)
	pm.xform(pinky_driven_curl, ro=(0, 0, 90))
	pinky_fkOri_root.rz.set(15)
	pinky_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)
	pinky_icon.curl.set(-10)
	pm.xform(pinky_driven_curl, ro=(0, 0, -10))
	pinky_fkOri_joint_2.rz.set(-20)
	pinky_fkOri_joint_3.rz.set(-25)
	pinky_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)
	pinky_drivenKeyframes_curl = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.curl.set(0)

	'''
	Pinky Scrunch
	'''
	pinky_drivenAttr_allScrunch = [pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_allScrunch = (pinky_icon + '.scrunch')
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	# print "Driven:", pinky_driven
	pinky_driven_allScrunch= [pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_icon.scrunch.set(10)
	pinky_fkOri_joint_2.rz.set(-50)
	pinky_fkOri_joint_3.rz.set(110)
	pinky_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	pinky_icon.scrunch.set(-10)
	pinky_fkOri_joint_2.rz.set(-3)
	pinky_fkOri_joint_3.rz.set(-4)
	pinky_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	pinky_drivenKeyframes_allScrunch = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.scrunch.set(0)

	'''
	Pinky Spread
	'''
	pinky_drivenAttr_spread = (pinky_fkOri_root + '.ry', pinky_fkOri_joint_2 + '.ry')
	pinky_driven_spread= (pinky_fkOri_root, pinky_fkOri_joint_2)
	pinky_driver_spread = (pinky_icon + '.spread')
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(10)
	pm.xform(pinky_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(-10)
	pm.xform(pinky_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(0)

	pinky_drivenKeyframes_spread = (pinky_fkOri_root + '_rotateY', pinky_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(pinky_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky Relax
	'''
	pinky_drivenAttr_relax = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driven_relax = [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_driver_relax = (pinky_icon + '.relax')
	pm.setDrivenKeyframe(pinky_drivenAttr_relax, currentDriver=pinky_driver_relax)
	pinky_icon.relax.set(10)
	pinky_fkOri_root.rz.set(12)
	pinky_fkOri_joint_2.rz.set(15)
	pinky_fkOri_joint_3.rz.set(18)
	pinky_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(pinky_drivenAttr_relax, currentDriver=pinky_driver_relax)
	pinky_icon.relax.set(0)

	pm.keyTangent(pinky_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pm.select(index_icon, middle_icon, pinky_icon)
	icon_selection = pm.ls(sl=1)

	color_index = 28

	for each in icon_selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideColor', color_index)
		color_index = color_index + 1


	'''
	Parent Icon Things
	'''

	lock_and_hide(parent_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])

	pm.addAttr(parent_icon, ln='fingerCtrls',  at='enum', en ='-------')
	parent_icon.fingerCtrls.set(lock=1, e=1, keyable=1)

	lockAttrs(parent_icon, ['fingerCtrls'])

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


	'''
	Index Fist
	'''
	index_drivenAttr_fist = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_fist = (parent_icon + '.fist')
	index_driven_fist= [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	pm.setDrivenKeyframe(index_drivenAttr_fist, currentDriver=index_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(index_driven_fist, ro=(0, 0, 90))
	index_fkOri_root.rz.set(15)
	index_fkOri_joint_3.rz.set(75)
	index_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(index_drivenAttr_fist, currentDriver=index_driver_fist)
	parent_icon.fist.set(0)


	'''
	Middle Fist
	'''
	middle_drivenAttr_fist = [middle_fkOri_root + '.rz', middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driver_fist = (parent_icon + '.fist')
	middle_driven_fist= [middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	pm.setDrivenKeyframe(middle_drivenAttr_fist, currentDriver=middle_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(middle_driven_fist, ro=(0, 0, 90))
	middle_fkOri_root.rz.set(15)
	middle_fkOri_joint_3.rz.set(75)
	middle_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(middle_drivenAttr_fist, currentDriver=middle_driver_fist)
	parent_icon.fist.set(0)

	'''
	Pinky Fist
	'''
	pinky_drivenAttr_fist = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_fist = (parent_icon + '.fist')
	pinky_driven_fist= [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pm.setDrivenKeyframe(pinky_drivenAttr_fist, currentDriver=pinky_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(pinky_driven_fist, ro=(0, 0, 90))
	pinky_fkOri_root.rz.set(15)
	pinky_fkOri_joint_3.rz.set(75)
	pinky_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(pinky_drivenAttr_fist, currentDriver=pinky_driver_fist)
	parent_icon.fist.set(0)

	'''
	Thumb fist
	'''
	thumb_drivenAttr_fist = [thumb_fkOri_pivot + '.rx', thumb_fkOri_pivot + '.ry', thumb_fkOri_pivot + '.rz', thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry']
	thumb_driver_fist  = (parent_icon + '.fist')
	thumb_driven_fist = [thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(thumb_fkOri_pivot, ro=(-32, -12, 7))
	thumb_fkOri_joint_1.ry.set(-16)
	thumb_fkOri_joint_2.ry.set(-25)
	thumb_fkOri_joint_3.ry.set(-8)
	pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
	parent_icon.fist.set(0)

	thumb_drivenKeyframes_allSpread = (thumb_fkOri_pivot + '_rotateX', thumb_fkOri_pivot + '_rotateY', thumb_fkOri_pivot + '_rotateZ', thumb_fkOri_joint_1 + '_rotateY', thumb_fkOri_joint_2 + '_rotateY', thumb_fkOri_joint_3 + '_rotateY')
	pm.keyTangent(thumb_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Index allScrunch
	'''
	index_drivenAttr_allScrunch = [index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	# print "Driven:", index_driven
	index_driven_allScrunch= [index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	index_fkOri_joint_2.rz.set(-50)
	index_fkOri_joint_3.rz.set(110)
	index_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	index_fkOri_joint_2.rz.set(-3)
	index_fkOri_joint_3.rz.set(-4)
	index_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	index_drivenKeyframes_allScrunch = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	'''
	Middle allScrunch
	'''
	middle_drivenAttr_allScrunch = [middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	# print "Driven:", middle_driven
	middle_driven_allScrunch= [middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	middle_fkOri_joint_2.rz.set(-50)
	middle_fkOri_joint_3.rz.set(110)
	middle_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	middle_fkOri_joint_2.rz.set(-3)
	middle_fkOri_joint_3.rz.set(-4)
	middle_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	middle_drivenKeyframes_allScrunch = (middle_fkOri_root + '_rotateZ', middle_fkOri_joint_2 + '_rotateZ', middle_fkOri_joint_3 + '_rotateZ', middle_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	'''
	Pinky allScrunch
	'''
	pinky_drivenAttr_allScrunch = [pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	# print "Driven:", pinky_driven
	pinky_driven_allScrunch= [pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	pinky_fkOri_joint_2.rz.set(-50)
	pinky_fkOri_joint_3.rz.set(110)
	pinky_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	pinky_fkOri_joint_2.rz.set(-3)
	pinky_fkOri_joint_3.rz.set(-4)
	pinky_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	pinky_drivenKeyframes_allScrunch = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)


	'''
	Index allSpread
	'''
	index_drivenAttr_allSpread = (index_fkOri_root + '.ry', index_fkOri_joint_2 + '.ry')
	index_driven_allSpread= (index_fkOri_root, index_fkOri_joint_2)
	index_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(index_driven_allSpread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(index_driven_allSpread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(0)

	index_drivenKeyframes_allSpread = (index_fkOri_root + '_rotateY', index_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(index_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Middle allSpread
	'''
	middle_drivenAttr_allSpread = (middle_fkOri_root + '.ry', middle_fkOri_joint_2 + '.ry')
	middle_driven_allSpread= (middle_fkOri_root, middle_fkOri_joint_2)
	middle_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(middle_driven_allSpread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(middle_driven_allSpread, ro=(0, 0, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(0)

	middle_drivenKeyframes_allSpread = (middle_fkOri_root + '_rotateY', middle_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(middle_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky allSpread
	'''
	pinky_drivenAttr_allSpread = (pinky_fkOri_root + '.ry', pinky_fkOri_joint_2 + '.ry')
	pinky_driven_allSpread= (pinky_fkOri_root, pinky_fkOri_joint_2)
	pinky_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(pinky_driven_allSpread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(pinky_driven_allSpread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(0)

	pinky_drivenKeyframes_allSpread = (pinky_fkOri_root + '_rotateY', pinky_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(pinky_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb allSpread
	'''
	thumb_drivenAttr_allSpread = [thumb_fkOri_joint_1 + '.ry']
	thumb_driver_allSpread  = (parent_icon + '.spread')
	thumb_driven_allSpread = [thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(10)
	thumb_fkOri_joint_1.ry.set(30)
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(-10)
	thumb_fkOri_joint_1.ry.set(-50)
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(0)

	thumb_drivenKeyframes_allSpread = (thumb_fkOri_joint_1 + '_rotateY')
	pm.keyTangent(thumb_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)



	'''
	Index allRelax
	'''
	index_drivenAttr_allRelax = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driven_allRelax = [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(10)
	index_fkOri_root.rz.set(3)
	index_fkOri_joint_2.rz.set(3.75)
	index_fkOri_joint_3.rz.set(4.5)
	index_fkOri_joint_4.rz.set(8.4)
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(-10)
	index_fkOri_root.rz.set(12)
	index_fkOri_joint_2.rz.set(15)
	index_fkOri_joint_3.rz.set(18)
	index_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(index_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Middle allRelax
	'''
	middle_drivenAttr_allRelax = [middle_fkOri_root + '.rz', middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driven_allRelax = [middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	middle_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(10)
	middle_fkOri_root.rz.set(6)
	middle_fkOri_joint_2.rz.set(7.5)
	middle_fkOri_joint_3.rz.set(9)
	middle_fkOri_joint_4.rz.set(12.6)
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(-10)
	middle_fkOri_root.rz.set(9)
	middle_fkOri_joint_2.rz.set(11.25)
	middle_fkOri_joint_3.rz.set(13.5)
	middle_fkOri_joint_4.rz.set(16.8)
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(middle_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky allRelax
	'''
	pinky_drivenAttr_allRelax = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driven_allRelax = [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(10)
	pinky_fkOri_root.rz.set(12)
	pinky_fkOri_joint_2.rz.set(15)
	pinky_fkOri_joint_3.rz.set(18)
	pinky_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(-10)
	pinky_fkOri_root.rz.set(3)
	pinky_fkOri_joint_2.rz.set(3.75)
	pinky_fkOri_joint_3.rz.set(4.5)
	pinky_fkOri_joint_4.rz.set(8.4)
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(pinky_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Curl
	'''
	thumb_drivenAttr_curl = [thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry']
	thumb_driven_curl = [thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	thumb_driver_curl = (parent_icon + '.curl')
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(10)
	thumb_fkOri_joint_1.ry.set(-25)
	thumb_fkOri_joint_2.ry.set(-30)
	thumb_fkOri_joint_3.ry.set(-32)
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(-10)
	thumb_fkOri_joint_1.ry.set(40)
	thumb_fkOri_joint_2.ry.set(30)
	thumb_fkOri_joint_3.ry.set(32)
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(0)

	pm.keyTangent(thumb_driven_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Drop
	'''
	thumb_drivenAttr_drop = [thumb_fkOri_pivot + '.rx']
	thumb_driven_drop = [thumb_fkOri_pivot]
	thumb_driver_drop = (parent_icon + '.drop')
	pm.setDrivenKeyframe(thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
	parent_icon.drop.set(10)
	thumb_fkOri_pivot.rx.set(-64)
	pm.setDrivenKeyframe(thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
	parent_icon.drop.set(0)

	pm.keyTangent(thumb_driven_drop, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Relax
	'''
	thumb_drivenAttr_relax = [thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry', thumb_fkOri_joint_1 + '.rz', thumb_fkOri_joint_2 + '.rz', thumb_fkOri_joint_3 + '.rz']
	thumb_driven_relax = [thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	thumb_driver_relax = (parent_icon + '.thumbRelax')
	pm.setDrivenKeyframe(thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
	parent_icon.thumbRelax.set(10)
	thumb_fkOri_joint_1.ry.set(-9)
	thumb_fkOri_joint_2.ry.set(-6)
	thumb_fkOri_joint_3.ry.set(-12)
	thumb_fkOri_joint_1.rz.set(4)
	thumb_fkOri_joint_2.rz.set(7)
	thumb_fkOri_joint_3.rz.set(12)
	pm.setDrivenKeyframe(thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
	parent_icon.thumbRelax.set(0)

	pm.keyTangent(thumb_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Spread
	'''
	thumb_drivenAttr_spread = [thumb_fkOri_joint_1 + '.ry']
	thumb_driven_spread = [thumb_fkOri_joint_1]
	thumb_driver_spread = (parent_icon + '.thumbSpread')
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(10)
	thumb_fkOri_joint_1.ry.set(-45)
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(-10)
	thumb_fkOri_joint_1.ry.set(40)
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(0)

	pm.keyTangent(thumb_driven_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

def twoFingers_and_thumb(*args):
	global index_joint_system, index_root, index_joint_2, index_joint_3, index_joint_4, index_joint_5
	global pinky_joint_system, pinky_root, pinky_joint_2, pinky_joint_3, pinky_joint_4, pinky_joint_5
	global thumb_joint_system, thumb_pivot, thumb_joint_1, thumb_joint_2, thumb_joint_3, thumb_joint_4
	global finger_selection
	finger_selection = pm.ls(sl=1)
	index_joint_system = finger_selection[0]
	pinky_joint_system = finger_selection[1]
	thumb_joint_system = finger_selection[2]
	# print 'Selection:', finger_selection
	# print 'Index Joint System:', index_joint_system
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

	pm.select(cl=1)

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
	pm.parent(index_root, pinky_root, thumb_joint_1, hand_base)
	
	'''
	Orient the Joints
	'''
	pm.joint(hand_base, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	
	
	'''
	Parent the thumb_01 back to the pivot
	'''
	pm.parent(thumb_joint_1, thumb_pivot)
	pm.parent(thumb_pivot, hand_base)

	pm.parent(index_root, pinky_root, thumb_pivot, w=1)

	indexSetup()
	pinkySetup()
	thumbSetup()

	global parent_icon, index_icon, pinky_icon
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

	pinky_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	pinky_icon.tz.set(-6)
	pinky_icon.sy.set(.6)
	pinky_icon.sz.set(.6)
	icon_name = pinky_root.replace('01_bind', 'icon')
	pinky_icon.rename(icon_name)
	freezeTransform()
	deleteHistory(pinky_icon)

	pm.parent(index_icon, pinky_icon, parent_icon)
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
	pm.select(index_icon, pinky_icon)
	icon_selection = pm.ls(sl=1)

	pm.addAttr(icon_selection, ln='fingerCtrl',  at='enum', en ='-------')
	index_icon.fingerCtrl.set(lock=1, e=1, keyable=1)
	pinky_icon.fingerCtrl.set(lock=1, e=1, keyable=1)

	pm.addAttr(icon_selection, ln='curl', max=10, dv=0, at='double', min=-10)
	index_icon.curl.set(e=1, keyable=1)
	pinky_icon.curl.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='relax', max=10, dv=0, at='double', min=0)
	index_icon.relax.set(e=1, keyable=1)
	pinky_icon.relax.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='scrunch', max=10, dv=0, at='double', min=-10)
	index_icon.scrunch.set(e=1, keyable=1)
	pinky_icon.scrunch.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='spread', max=10, dv=0, at='double', min=-10)
	index_icon.spread.set(e=1, keyable=1)
	pinky_icon.spread.set(e=1, keyable=1)

	
	pm.select(parent_icon)
	icon_selection = pm.ls(sl=1, dag=1)
	index_icon = icon_selection[2]
	pinky_icon = icon_selection[4]
	# print 'Index Icon:', index_icon
	# print 'Pinky Icon:', pinky_icon

	lock_and_hide(index_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(pinky_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])



	'''
	Index Curl
	'''
	index_drivenAttr_curl = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_curl = (index_icon + '.curl')
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)

	# print "Driven:", index_driven
	index_driven_curl= [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_icon.curl.set(10)
	pm.xform(index_driven_curl, ro=(0, 0, 90))
	index_fkOri_root.rz.set(15)
	index_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)
	index_icon.curl.set(-10)
	pm.xform(index_driven_curl, ro=(0, 0, -10))
	index_fkOri_joint_2.rz.set(-20)
	index_fkOri_joint_3.rz.set(-25)
	index_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)
	index_drivenKeyframes_curl = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.curl.set(0)

	'''
	Index Scrunch
	'''
	index_drivenAttr_allScrunch = [index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_allScrunch = (index_icon + '.scrunch')
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	# print "Driven:", index_driven
	index_driven_allScrunch= [index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_icon.scrunch.set(10)
	index_fkOri_joint_2.rz.set(-50)
	index_fkOri_joint_3.rz.set(110)
	index_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	index_icon.scrunch.set(-10)
	index_fkOri_joint_2.rz.set(-3)
	index_fkOri_joint_3.rz.set(-4)
	index_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	index_drivenKeyframes_allScrunch = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.scrunch.set(0)

	'''
	Index Spread
	'''
	index_drivenAttr_spread = (index_fkOri_root + '.ry', index_fkOri_joint_2 + '.ry')
	index_driven_spread= (index_fkOri_root, index_fkOri_joint_2)
	index_driver_spread = (index_icon + '.spread')
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(10)
	pm.xform(index_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(-10)
	pm.xform(index_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(0)

	index_drivenKeyframes_spread = (index_fkOri_root + '_rotateY', index_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(index_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Index Relax
	'''
	index_drivenAttr_relax = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driven_relax = [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_driver_relax = (index_icon + '.relax')
	pm.setDrivenKeyframe(index_drivenAttr_relax, currentDriver=index_driver_relax)
	index_icon.relax.set(10)
	index_fkOri_root.rz.set(12)
	index_fkOri_joint_2.rz.set(15)
	index_fkOri_joint_3.rz.set(18)
	index_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(index_drivenAttr_relax, currentDriver=index_driver_relax)
	index_icon.relax.set(0)

	pm.keyTangent(index_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Pinky Curl
	'''
	pinky_drivenAttr_curl = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_curl = (pinky_icon + '.curl')
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)

	# print "Driven:", pinky_driven
	pinky_driven_curl= [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_icon.curl.set(10)
	pm.xform(pinky_driven_curl, ro=(0, 0, 90))
	pinky_fkOri_root.rz.set(15)
	pinky_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)
	pinky_icon.curl.set(-10)
	pm.xform(pinky_driven_curl, ro=(0, 0, -10))
	pinky_fkOri_joint_2.rz.set(-20)
	pinky_fkOri_joint_3.rz.set(-25)
	pinky_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)
	pinky_drivenKeyframes_curl = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.curl.set(0)

	'''
	Pinky Scrunch
	'''
	pinky_drivenAttr_allScrunch = [pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_allScrunch = (pinky_icon + '.scrunch')
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	# print "Driven:", pinky_driven
	pinky_driven_allScrunch= [pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_icon.scrunch.set(10)
	pinky_fkOri_joint_2.rz.set(-50)
	pinky_fkOri_joint_3.rz.set(110)
	pinky_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	pinky_icon.scrunch.set(-10)
	pinky_fkOri_joint_2.rz.set(-3)
	pinky_fkOri_joint_3.rz.set(-4)
	pinky_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	pinky_drivenKeyframes_allScrunch = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.scrunch.set(0)

	'''
	Pinky Spread
	'''
	pinky_drivenAttr_spread = (pinky_fkOri_root + '.ry', pinky_fkOri_joint_2 + '.ry')
	pinky_driven_spread= (pinky_fkOri_root, pinky_fkOri_joint_2)
	pinky_driver_spread = (pinky_icon + '.spread')
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(10)
	pm.xform(pinky_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(-10)
	pm.xform(pinky_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(0)

	pinky_drivenKeyframes_spread = (pinky_fkOri_root + '_rotateY', pinky_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(pinky_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky Relax
	'''
	pinky_drivenAttr_relax = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driven_relax = [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_driver_relax = (pinky_icon + '.relax')
	pm.setDrivenKeyframe(pinky_drivenAttr_relax, currentDriver=pinky_driver_relax)
	pinky_icon.relax.set(10)
	pinky_fkOri_root.rz.set(12)
	pinky_fkOri_joint_2.rz.set(15)
	pinky_fkOri_joint_3.rz.set(18)
	pinky_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(pinky_drivenAttr_relax, currentDriver=pinky_driver_relax)
	pinky_icon.relax.set(0)

	pm.keyTangent(pinky_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pm.select(index_icon, pinky_icon)
	icon_selection = pm.ls(sl=1)

	color_index = 27

	for each in icon_selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideColor', color_index)
		color_index = color_index + 1


	'''
	Parent Icon Things
	'''

	lock_and_hide(parent_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])

	pm.addAttr(parent_icon, ln='fingerCtrls',  at='enum', en ='-------')
	parent_icon.fingerCtrls.set(lock=1, e=1, keyable=1)

	lockAttrs(parent_icon, ['fingerCtrls'])

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


	'''
	Index Fist
	'''
	index_drivenAttr_fist = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_fist = (parent_icon + '.fist')
	index_driven_fist= [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	pm.setDrivenKeyframe(index_drivenAttr_fist, currentDriver=index_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(index_driven_fist, ro=(0, 0, 90))
	index_fkOri_root.rz.set(15)
	index_fkOri_joint_3.rz.set(75)
	index_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(index_drivenAttr_fist, currentDriver=index_driver_fist)
	parent_icon.fist.set(0)


	'''
	Pinky Fist
	'''
	pinky_drivenAttr_fist = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_fist = (parent_icon + '.fist')
	pinky_driven_fist= [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pm.setDrivenKeyframe(pinky_drivenAttr_fist, currentDriver=pinky_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(pinky_driven_fist, ro=(0, 0, 90))
	pinky_fkOri_root.rz.set(15)
	pinky_fkOri_joint_3.rz.set(75)
	pinky_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(pinky_drivenAttr_fist, currentDriver=pinky_driver_fist)
	parent_icon.fist.set(0)

	'''
	Thumb fist
	'''
	thumb_drivenAttr_fist = [thumb_fkOri_pivot + '.rx', thumb_fkOri_pivot + '.ry', thumb_fkOri_pivot + '.rz', thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry']
	thumb_driver_fist  = (parent_icon + '.fist')
	thumb_driven_fist = [thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(thumb_fkOri_pivot, ro=(-32, -12, 7))
	thumb_fkOri_joint_1.ry.set(-16)
	thumb_fkOri_joint_2.ry.set(-25)
	thumb_fkOri_joint_3.ry.set(-8)
	pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
	parent_icon.fist.set(0)

	thumb_drivenKeyframes_allSpread = (thumb_fkOri_pivot + '_rotateX', thumb_fkOri_pivot + '_rotateY', thumb_fkOri_pivot + '_rotateZ', thumb_fkOri_joint_1 + '_rotateY', thumb_fkOri_joint_2 + '_rotateY', thumb_fkOri_joint_3 + '_rotateY')
	pm.keyTangent(thumb_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Index allScrunch
	'''
	index_drivenAttr_allScrunch = [index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	# print "Driven:", index_driven
	index_driven_allScrunch= [index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	index_fkOri_joint_2.rz.set(-50)
	index_fkOri_joint_3.rz.set(110)
	index_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	index_fkOri_joint_2.rz.set(-3)
	index_fkOri_joint_3.rz.set(-4)
	index_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	index_drivenKeyframes_allScrunch = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	'''
	Pinky allScrunch
	'''
	pinky_drivenAttr_allScrunch = [pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	# print "Driven:", pinky_driven
	pinky_driven_allScrunch= [pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	pinky_fkOri_joint_2.rz.set(-50)
	pinky_fkOri_joint_3.rz.set(110)
	pinky_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	pinky_fkOri_joint_2.rz.set(-3)
	pinky_fkOri_joint_3.rz.set(-4)
	pinky_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	pinky_drivenKeyframes_allScrunch = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	'''
	Index allSpread
	'''
	index_drivenAttr_allSpread = (index_fkOri_root + '.ry', index_fkOri_joint_2 + '.ry')
	index_driven_allSpread= (index_fkOri_root, index_fkOri_joint_2)
	index_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(index_driven_allSpread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(index_driven_allSpread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(0)

	index_drivenKeyframes_allSpread = (index_fkOri_root + '_rotateY', index_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(index_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Pinky allSpread
	'''
	pinky_drivenAttr_allSpread = (pinky_fkOri_root + '.ry', pinky_fkOri_joint_2 + '.ry')
	pinky_driven_allSpread= (pinky_fkOri_root, pinky_fkOri_joint_2)
	pinky_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(pinky_driven_allSpread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(pinky_driven_allSpread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(0)

	pinky_drivenKeyframes_allSpread = (pinky_fkOri_root + '_rotateY', pinky_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(pinky_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb allSpread
	'''
	thumb_drivenAttr_allSpread = [thumb_fkOri_joint_1 + '.ry']
	thumb_driver_allSpread  = (parent_icon + '.spread')
	thumb_driven_allSpread = [thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(10)
	thumb_fkOri_joint_1.ry.set(30)
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(-10)
	thumb_fkOri_joint_1.ry.set(-50)
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(0)

	thumb_drivenKeyframes_allSpread = (thumb_fkOri_joint_1 + '_rotateY')
	pm.keyTangent(thumb_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)



	'''
	Index allRelax
	'''
	index_drivenAttr_allRelax = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driven_allRelax = [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(10)
	index_fkOri_root.rz.set(3)
	index_fkOri_joint_2.rz.set(3.75)
	index_fkOri_joint_3.rz.set(4.5)
	index_fkOri_joint_4.rz.set(8.4)
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(-10)
	index_fkOri_root.rz.set(12)
	index_fkOri_joint_2.rz.set(15)
	index_fkOri_joint_3.rz.set(18)
	index_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(index_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	'''
	Pinky allRelax
	'''
	pinky_drivenAttr_allRelax = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driven_allRelax = [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(10)
	pinky_fkOri_root.rz.set(12)
	pinky_fkOri_joint_2.rz.set(15)
	pinky_fkOri_joint_3.rz.set(18)
	pinky_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(-10)
	pinky_fkOri_root.rz.set(3)
	pinky_fkOri_joint_2.rz.set(3.75)
	pinky_fkOri_joint_3.rz.set(4.5)
	pinky_fkOri_joint_4.rz.set(8.4)
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(pinky_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Curl
	'''
	thumb_drivenAttr_curl = [thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry']
	thumb_driven_curl = [thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	thumb_driver_curl = (parent_icon + '.curl')
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(10)
	thumb_fkOri_joint_1.ry.set(-25)
	thumb_fkOri_joint_2.ry.set(-30)
	thumb_fkOri_joint_3.ry.set(-32)
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(-10)
	thumb_fkOri_joint_1.ry.set(40)
	thumb_fkOri_joint_2.ry.set(30)
	thumb_fkOri_joint_3.ry.set(32)
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(0)

	pm.keyTangent(thumb_driven_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Drop
	'''
	thumb_drivenAttr_drop = [thumb_fkOri_pivot + '.rx']
	thumb_driven_drop = [thumb_fkOri_pivot]
	thumb_driver_drop = (parent_icon + '.drop')
	pm.setDrivenKeyframe(thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
	parent_icon.drop.set(10)
	thumb_fkOri_pivot.rx.set(-64)
	pm.setDrivenKeyframe(thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
	parent_icon.drop.set(0)

	pm.keyTangent(thumb_driven_drop, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Relax
	'''
	thumb_drivenAttr_relax = [thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry', thumb_fkOri_joint_1 + '.rz', thumb_fkOri_joint_2 + '.rz', thumb_fkOri_joint_3 + '.rz']
	thumb_driven_relax = [thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	thumb_driver_relax = (parent_icon + '.thumbRelax')
	pm.setDrivenKeyframe(thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
	parent_icon.thumbRelax.set(10)
	thumb_fkOri_joint_1.ry.set(-9)
	thumb_fkOri_joint_2.ry.set(-6)
	thumb_fkOri_joint_3.ry.set(-12)
	thumb_fkOri_joint_1.rz.set(4)
	thumb_fkOri_joint_2.rz.set(7)
	thumb_fkOri_joint_3.rz.set(12)
	pm.setDrivenKeyframe(thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
	parent_icon.thumbRelax.set(0)

	pm.keyTangent(thumb_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Spread
	'''
	thumb_drivenAttr_spread = [thumb_fkOri_joint_1 + '.ry']
	thumb_driven_spread = [thumb_fkOri_joint_1]
	thumb_driver_spread = (parent_icon + '.thumbSpread')
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(10)
	thumb_fkOri_joint_1.ry.set(-45)
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(-10)
	thumb_fkOri_joint_1.ry.set(40)
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(0)

	pm.keyTangent(thumb_driven_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

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

def jointPadding(*args):
	'''
	This creates a world orientated pad on the root joint.

	import byrdCheyenne_riggingTools
	reload(byrdCheyenne_riggingTools)
	byrdCheyenne_riggingTools.padding_tool()
	'''

	selected = pm.ls(selection=1)
	# print 'Current Selected:' , selected 
	root_joint = selected[0]

	# Create empty group
	# empty=1 will create an empty group 
	# 
	pad = pm.group(empty=1)

	# Move group to joint.
	# 	and delete constraint
	temp_constraint = pm.pointConstraint(root_joint, pad)
	pm.delete(temp_constraint)

	# Freeze Transformation on the group.
	pm.makeIdentity(pad, apply=1, t=1, r=1, s=1, n=0)
	# Parent joint to group
	pm.parent(root_joint, pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	print 'Padding group created.'

def SDK_setup(*args):
	global parent_icon, index_icon, middle_icon, ring_icon, pinky_icon
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

	pm.addAttr(icon_selection, ln='relax', max=10, dv=0, at='double', min=0)
	index_icon.relax.set(e=1, keyable=1)
	middle_icon.relax.set(e=1, keyable=1)
	ring_icon.relax.set(e=1, keyable=1)
	pinky_icon.relax.set(e=1, keyable=1)

	pm.addAttr(icon_selection, ln='scrunch', max=10, dv=0, at='double', min=-10)
	index_icon.scrunch.set(e=1, keyable=1)
	middle_icon.scrunch.set(e=1, keyable=1)
	ring_icon.scrunch.set(e=1, keyable=1)
	pinky_icon.scrunch.set(e=1, keyable=1)


	pm.addAttr(icon_selection, ln='spread', max=10, dv=0, at='double', min=-10)
	index_icon.spread.set(e=1, keyable=1)
	middle_icon.spread.set(e=1, keyable=1)
	ring_icon.spread.set(e=1, keyable=1)
	pinky_icon.spread.set(e=1, keyable=1)

	
	pm.select(parent_icon)
	icon_selection = pm.ls(sl=1, dag=1)
	index_icon = icon_selection[2]
	middle_icon = icon_selection[4] 
	ring_icon = icon_selection[6]
	pinky_icon = icon_selection[8]
	# print 'Index Icon:', index_icon
	# print 'Middle Icon:', middle_icon
	# print 'Ring Icon:', ring_icon
	# print 'Pinky Icon:', pinky_icon

	lock_and_hide(index_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(middle_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(ring_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])
	lock_and_hide(pinky_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])

	'''
	Index Curl
	'''
	index_drivenAttr_curl = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_curl = (index_icon + '.curl')
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)

	# print "Driven:", index_driven
	index_driven_curl= [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_icon.curl.set(10)
	pm.xform(index_driven_curl, ro=(0, 0, 90))
	index_fkOri_root.rz.set(15)
	index_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)
	index_icon.curl.set(-10)
	pm.xform(index_driven_curl, ro=(0, 0, -10))
	index_fkOri_joint_2.rz.set(-20)
	index_fkOri_joint_3.rz.set(-25)
	index_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(index_drivenAttr_curl, currentDriver=index_driver_curl)
	index_drivenKeyframes_curl = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.curl.set(0)

	'''
	Middle Curl
	'''
	middle_drivenAttr_curl = [middle_fkOri_root + '.rz', middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driver_curl = (middle_icon + '.curl')
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)

	# print "Driven:", middle_driven
	middle_driven_curl= [middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	middle_icon.curl.set(10)
	pm.xform(middle_driven_curl, ro=(0, 0, 90))
	middle_fkOri_root.rz.set(15)
	middle_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)
	middle_icon.curl.set(-10)
	pm.xform(middle_driven_curl, ro=(0, 0, -10))
	middle_fkOri_joint_2.rz.set(-20)
	middle_fkOri_joint_3.rz.set(-25)
	middle_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(middle_drivenAttr_curl, currentDriver=middle_driver_curl)
	middle_drivenKeyframes_curl = (middle_fkOri_root + '_rotateZ', middle_fkOri_joint_2 + '_rotateZ', middle_fkOri_joint_3 + '_rotateZ', middle_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	middle_icon.curl.set(0)

	'''
	Ring Curl
	'''
	ring_drivenAttr_curl = [ring_fkOri_root + '.rz', ring_fkOri_joint_2 + '.rz', ring_fkOri_joint_3 + '.rz', ring_fkOri_joint_4 + '.rz']
	ring_driver_curl = (ring_icon + '.curl')
	pm.setDrivenKeyframe(ring_drivenAttr_curl, currentDriver=ring_driver_curl)

	# print "Driven:", ring_driven
	ring_driven_curl= [ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4]
	ring_icon.curl.set(10)
	pm.xform(ring_driven_curl, ro=(0, 0, 90))
	ring_fkOri_root.rz.set(15)
	ring_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(ring_drivenAttr_curl, currentDriver=ring_driver_curl)
	ring_icon.curl.set(-10)
	pm.xform(ring_driven_curl, ro=(0, 0, -10))
	ring_fkOri_joint_2.rz.set(-20)
	ring_fkOri_joint_3.rz.set(-25)
	ring_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(ring_drivenAttr_curl, currentDriver=ring_driver_curl)
	ring_drivenKeyframes_curl = (ring_fkOri_root + '_rotateZ', ring_fkOri_joint_2 + '_rotateZ', ring_fkOri_joint_3 + '_rotateZ', ring_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(ring_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	ring_icon.curl.set(0)

	'''
	Pinky Curl
	'''
	pinky_drivenAttr_curl = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_curl = (pinky_icon + '.curl')
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)

	# print "Driven:", pinky_driven
	pinky_driven_curl= [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_icon.curl.set(10)
	pm.xform(pinky_driven_curl, ro=(0, 0, 90))
	pinky_fkOri_root.rz.set(15)
	pinky_fkOri_joint_3.rz.set(75)
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)
	pinky_icon.curl.set(-10)
	pm.xform(pinky_driven_curl, ro=(0, 0, -10))
	pinky_fkOri_joint_2.rz.set(-20)
	pinky_fkOri_joint_3.rz.set(-25)
	pinky_fkOri_joint_4.rz.set(-30)
	pm.setDrivenKeyframe(pinky_drivenAttr_curl, currentDriver=pinky_driver_curl)
	pinky_drivenKeyframes_curl = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.curl.set(0)

	'''
	Index Scrunch
	'''
	index_drivenAttr_scrunch = [index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_scrunch = (index_icon + '.scrunch')
	pm.setDrivenKeyframe(index_drivenAttr_scrunch, currentDriver=index_driver_scrunch)
	# print "Driven:", index_driven
	index_driven_scrunch= [index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_icon.scrunch.set(10)
	index_fkOri_joint_2.rz.set(-50)
	index_fkOri_joint_3.rz.set(110)
	index_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(index_drivenAttr_scrunch, currentDriver=index_driver_scrunch)
	index_icon.scrunch.set(-10)
	index_fkOri_joint_2.rz.set(-3)
	index_fkOri_joint_3.rz.set(-4)
	index_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(index_drivenAttr_scrunch, currentDriver=index_driver_scrunch)
	index_drivenKeyframes_scrunch = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_scrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	index_icon.scrunch.set(0)

	'''
	Middle Scrunch
	'''
	middle_drivenAttr_scrunch = [middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driver_scrunch = (middle_icon + '.scrunch')
	pm.setDrivenKeyframe(middle_drivenAttr_scrunch, currentDriver=middle_driver_scrunch)
	# print "Driven:", middle_driven
	middle_driven_scrunch= [middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	middle_icon.scrunch.set(10)
	middle_fkOri_joint_2.rz.set(-50)
	middle_fkOri_joint_3.rz.set(110)
	middle_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(middle_drivenAttr_scrunch, currentDriver=middle_driver_scrunch)
	middle_icon.scrunch.set(-10)
	middle_fkOri_joint_2.rz.set(-3)
	middle_fkOri_joint_3.rz.set(-4)
	middle_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(middle_drivenAttr_scrunch, currentDriver=middle_driver_scrunch)
	middle_drivenKeyframes_scrunch = (middle_fkOri_root + '_rotateZ', middle_fkOri_joint_2 + '_rotateZ', middle_fkOri_joint_3 + '_rotateZ', middle_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_scrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	middle_icon.scrunch.set(0)

	'''
	Ring Scrunch
	'''
	ring_drivenAttr_scrunch = [ring_fkOri_joint_2 + '.rz', ring_fkOri_joint_3 + '.rz', ring_fkOri_joint_4 + '.rz']
	ring_driver_scrunch = (ring_icon + '.scrunch')
	pm.setDrivenKeyframe(ring_drivenAttr_scrunch, currentDriver=ring_driver_scrunch)
	# print "Driven:", ring_driven
	ring_driven_scrunch= [ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4]
	ring_icon.scrunch.set(10)
	ring_fkOri_joint_2.rz.set(-50)
	ring_fkOri_joint_3.rz.set(110)
	ring_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(ring_drivenAttr_scrunch, currentDriver=ring_driver_scrunch)
	ring_icon.scrunch.set(-10)
	ring_fkOri_joint_2.rz.set(-3)
	ring_fkOri_joint_3.rz.set(-4)
	ring_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(ring_drivenAttr_scrunch, currentDriver=ring_driver_scrunch)
	ring_drivenKeyframes_scrunch = (ring_fkOri_root + '_rotateZ', ring_fkOri_joint_2 + '_rotateZ', ring_fkOri_joint_3 + '_rotateZ', ring_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(ring_drivenKeyframes_scrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	ring_icon.scrunch.set(0)

	'''
	Pinky Scrunch
	'''
	pinky_drivenAttr_scrunch = [pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_scrunch = (pinky_icon + '.scrunch')
	pm.setDrivenKeyframe(pinky_drivenAttr_scrunch, currentDriver=pinky_driver_scrunch)
	# print "Driven:", pinky_driven
	pinky_driven_scrunch= [pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_icon.scrunch.set(10)
	pinky_fkOri_joint_2.rz.set(-50)
	pinky_fkOri_joint_3.rz.set(110)
	pinky_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(pinky_drivenAttr_scrunch, currentDriver=pinky_driver_scrunch)
	pinky_icon.scrunch.set(-10)
	pinky_fkOri_joint_2.rz.set(-3)
	pinky_fkOri_joint_3.rz.set(-4)
	pinky_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(pinky_drivenAttr_scrunch, currentDriver=pinky_driver_scrunch)
	pinky_drivenKeyframes_scrunch = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_scrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pinky_icon.scrunch.set(0)

	'''
	Index Spread
	'''
	index_drivenAttr_spread = (index_fkOri_root + '.ry', index_fkOri_joint_2 + '.ry')
	index_driven_spread= (index_fkOri_root, index_fkOri_joint_2)
	index_driver_spread = (index_icon + '.spread')
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(10)
	pm.xform(index_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(-10)
	pm.xform(index_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(index_drivenAttr_spread, currentDriver=index_driver_spread)
	index_icon.spread.set(0)

	index_drivenKeyframes_spread = (index_fkOri_root + '_rotateY', index_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(index_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Middle Spread
	'''
	middle_drivenAttr_spread = (middle_fkOri_root + '.ry', middle_fkOri_joint_2 + '.ry')
	middle_driven_spread= (middle_fkOri_root, middle_fkOri_joint_2)
	middle_driver_spread = (middle_icon + '.spread')
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(10)
	pm.xform(middle_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(-10)
	pm.xform(middle_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_spread, currentDriver=middle_driver_spread)
	middle_icon.spread.set(0)

	middle_drivenKeyframes_spread = (middle_fkOri_root + '_rotateY', middle_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(middle_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Ring Spread
	'''
	ring_drivenAttr_spread = (ring_fkOri_root + '.ry', ring_fkOri_joint_2 + '.ry')
	ring_driven_spread= (ring_fkOri_root, ring_fkOri_joint_2)
	ring_driver_spread = (ring_icon + '.spread')
	pm.setDrivenKeyframe(ring_drivenAttr_spread, currentDriver=ring_driver_spread)
	ring_icon.spread.set(10)
	pm.xform(ring_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(ring_drivenAttr_spread, currentDriver=ring_driver_spread)
	ring_icon.spread.set(-10)
	pm.xform(ring_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(ring_drivenAttr_spread, currentDriver=ring_driver_spread)
	ring_icon.spread.set(0)

	ring_drivenKeyframes_spread = (ring_fkOri_root + '_rotateY', ring_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(ring_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky Spread
	'''
	pinky_drivenAttr_spread = (pinky_fkOri_root + '.ry', pinky_fkOri_joint_2 + '.ry')
	pinky_driven_spread= (pinky_fkOri_root, pinky_fkOri_joint_2)
	pinky_driver_spread = (pinky_icon + '.spread')
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(10)
	pm.xform(pinky_driven_spread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(-10)
	pm.xform(pinky_driven_spread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_spread, currentDriver=pinky_driver_spread)
	pinky_icon.spread.set(0)

	pinky_drivenKeyframes_spread = (pinky_fkOri_root + '_rotateY', pinky_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(pinky_drivenKeyframes_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)



	'''
	Index Relax
	'''
	index_drivenAttr_relax = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driven_relax = [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_driver_relax = (index_icon + '.relax')
	pm.setDrivenKeyframe(index_drivenAttr_relax, currentDriver=index_driver_relax)
	index_icon.relax.set(10)
	index_fkOri_root.rz.set(12)
	index_fkOri_joint_2.rz.set(15)
	index_fkOri_joint_3.rz.set(18)
	index_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(index_drivenAttr_relax, currentDriver=index_driver_relax)
	index_icon.relax.set(0)

	pm.keyTangent(index_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Middle Relax
	'''
	middle_drivenAttr_relax = [middle_fkOri_root + '.rz', middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driven_relax = [middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	middle_driver_relax = (middle_icon + '.relax')
	pm.setDrivenKeyframe(middle_drivenAttr_relax, currentDriver=middle_driver_relax)
	middle_icon.relax.set(10)
	middle_fkOri_root.rz.set(12)
	middle_fkOri_joint_2.rz.set(15)
	middle_fkOri_joint_3.rz.set(18)
	middle_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(middle_drivenAttr_relax, currentDriver=middle_driver_relax)
	middle_icon.relax.set(0)

	pm.keyTangent(middle_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Ring Relax
	'''
	ring_drivenAttr_relax = [ring_fkOri_root + '.rz', ring_fkOri_joint_2 + '.rz', ring_fkOri_joint_3 + '.rz', ring_fkOri_joint_4 + '.rz']
	ring_driven_relax = [ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4]
	ring_driver_relax = (ring_icon + '.relax')
	pm.setDrivenKeyframe(ring_drivenAttr_relax, currentDriver=ring_driver_relax)
	ring_icon.relax.set(10)
	ring_fkOri_root.rz.set(12)
	ring_fkOri_joint_2.rz.set(15)
	ring_fkOri_joint_3.rz.set(18)
	ring_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(ring_drivenAttr_relax, currentDriver=ring_driver_relax)
	ring_icon.relax.set(0)

	pm.keyTangent(ring_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky Relax
	'''
	pinky_drivenAttr_relax = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driven_relax = [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_driver_relax = (pinky_icon + '.relax')
	pm.setDrivenKeyframe(pinky_drivenAttr_relax, currentDriver=pinky_driver_relax)
	pinky_icon.relax.set(10)
	pinky_fkOri_root.rz.set(12)
	pinky_fkOri_joint_2.rz.set(15)
	pinky_fkOri_joint_3.rz.set(18)
	pinky_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(pinky_drivenAttr_relax, currentDriver=pinky_driver_relax)
	pinky_icon.relax.set(0)

	pm.keyTangent(pinky_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	pm.select(index_icon, middle_icon, ring_icon, pinky_icon)
	icon_selection = pm.ls(sl=1)

	color_index = 27

	for each in icon_selection:
		pm.setAttr(each + '.overrideEnabled', 1)
		pm.setAttr(each + '.overrideColor', color_index)
		color_index = color_index + 1

	'''
	Parent Icon Things
	'''

	lock_and_hide(parent_icon, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])

	pm.addAttr(parent_icon, ln='fingerCtrls',  at='enum', en ='-------')
	parent_icon.fingerCtrls.set(lock=1, e=1, keyable=1)

	lockAttrs(parent_icon, ['fingerCtrls'])

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


	'''
	Index Fist
	'''
	index_drivenAttr_fist = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_fist = (parent_icon + '.fist')
	index_driven_fist= [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	pm.setDrivenKeyframe(index_drivenAttr_fist, currentDriver=index_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(index_driven_fist, ro=(0, 0, 90))
	index_fkOri_root.rz.set(15)
	index_fkOri_joint_3.rz.set(75)
	index_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(index_drivenAttr_fist, currentDriver=index_driver_fist)
	parent_icon.fist.set(0)


	'''
	Middle Fist
	'''
	middle_drivenAttr_fist = [middle_fkOri_root + '.rz', middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driver_fist = (parent_icon + '.fist')
	middle_driven_fist= [middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	pm.setDrivenKeyframe(middle_drivenAttr_fist, currentDriver=middle_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(middle_driven_fist, ro=(0, 0, 90))
	middle_fkOri_root.rz.set(15)
	middle_fkOri_joint_3.rz.set(75)
	middle_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(middle_drivenAttr_fist, currentDriver=middle_driver_fist)
	parent_icon.fist.set(0)


	'''
	Ring Fist
	'''
	ring_drivenAttr_fist = [ring_fkOri_root + '.rz', ring_fkOri_joint_2 + '.rz', ring_fkOri_joint_3 + '.rz', ring_fkOri_joint_4 + '.rz']
	ring_driver_fist = (parent_icon + '.fist')
	ring_driven_fist= [ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4]
	pm.setDrivenKeyframe(ring_drivenAttr_fist, currentDriver=ring_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(ring_driven_fist, ro=(0, 0, 90))
	ring_fkOri_root.rz.set(15)
	ring_fkOri_joint_3.rz.set(75)
	ring_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(ring_drivenAttr_fist, currentDriver=ring_driver_fist)
	parent_icon.fist.set(0)

	'''
	Pinky Fist
	'''
	pinky_drivenAttr_fist = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_fist = (parent_icon + '.fist')
	pinky_driven_fist= [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pm.setDrivenKeyframe(pinky_drivenAttr_fist, currentDriver=pinky_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(pinky_driven_fist, ro=(0, 0, 90))
	pinky_fkOri_root.rz.set(15)
	pinky_fkOri_joint_3.rz.set(75)
	pinky_fkOri_joint_4.rz.set(25)
	pm.setDrivenKeyframe(pinky_drivenAttr_fist, currentDriver=pinky_driver_fist)
	parent_icon.fist.set(0)

	'''
	Thumb fist
	'''
	thumb_drivenAttr_fist = [thumb_fkOri_pivot + '.rx', thumb_fkOri_pivot + '.ry', thumb_fkOri_pivot + '.rz', thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry']
	thumb_driver_fist  = (parent_icon + '.fist')
	thumb_driven_fist = [thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
	parent_icon.fist.set(10)
	pm.xform(thumb_fkOri_pivot, ro=(-32, -12, 7))
	thumb_fkOri_joint_1.ry.set(-16)
	thumb_fkOri_joint_2.ry.set(-25)
	thumb_fkOri_joint_3.ry.set(-8)
	pm.setDrivenKeyframe(thumb_drivenAttr_fist, currentDriver=thumb_driver_fist)
	parent_icon.fist.set(0)

	thumb_drivenKeyframes_allSpread = (thumb_fkOri_pivot + '_rotateX', thumb_fkOri_pivot + '_rotateY', thumb_fkOri_pivot + '_rotateZ', thumb_fkOri_joint_1 + '_rotateY', thumb_fkOri_joint_2 + '_rotateY', thumb_fkOri_joint_3 + '_rotateY')
	pm.keyTangent(thumb_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Index Scrunch
	'''
	index_drivenAttr_allScrunch = [index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	# print "Driven:", index_driven
	index_driven_allScrunch= [index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	index_fkOri_joint_2.rz.set(-50)
	index_fkOri_joint_3.rz.set(110)
	index_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	index_fkOri_joint_2.rz.set(-3)
	index_fkOri_joint_3.rz.set(-4)
	index_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(index_drivenAttr_allScrunch, currentDriver=index_driver_allScrunch)
	index_drivenKeyframes_allScrunch = (index_fkOri_root + '_rotateZ', index_fkOri_joint_2 + '_rotateZ', index_fkOri_joint_3 + '_rotateZ', index_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(index_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	'''
	Middle Scrunch
	'''
	middle_drivenAttr_allScrunch = [middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	# print "Driven:", middle_driven
	middle_driven_allScrunch= [middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	middle_fkOri_joint_2.rz.set(-50)
	middle_fkOri_joint_3.rz.set(110)
	middle_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	middle_fkOri_joint_2.rz.set(-3)
	middle_fkOri_joint_3.rz.set(-4)
	middle_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(middle_drivenAttr_allScrunch, currentDriver=middle_driver_allScrunch)
	middle_drivenKeyframes_allScrunch = (middle_fkOri_root + '_rotateZ', middle_fkOri_joint_2 + '_rotateZ', middle_fkOri_joint_3 + '_rotateZ', middle_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(middle_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	'''
	Ring Scrunch
	'''
	ring_drivenAttr_allScrunch = [ring_fkOri_joint_2 + '.rz', ring_fkOri_joint_3 + '.rz', ring_fkOri_joint_4 + '.rz']
	ring_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(ring_drivenAttr_allScrunch, currentDriver=ring_driver_allScrunch)
	# print "Driven:", ring_driven
	ring_driven_allScrunch= [ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	ring_fkOri_joint_2.rz.set(-50)
	ring_fkOri_joint_3.rz.set(110)
	ring_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(ring_drivenAttr_allScrunch, currentDriver=ring_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	ring_fkOri_joint_2.rz.set(-3)
	ring_fkOri_joint_3.rz.set(-4)
	ring_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(ring_drivenAttr_allScrunch, currentDriver=ring_driver_allScrunch)
	ring_drivenKeyframes_allScrunch = (ring_fkOri_root + '_rotateZ', ring_fkOri_joint_2 + '_rotateZ', ring_fkOri_joint_3 + '_rotateZ', ring_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(ring_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	'''
	Pinky Scrunch
	'''
	pinky_drivenAttr_allScrunch = [pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driver_allScrunch = (parent_icon + '.scrunch')
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	# print "Driven:", pinky_driven
	pinky_driven_allScrunch= [pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	parent_icon.scrunch.set(10)
	pinky_fkOri_joint_2.rz.set(-50)
	pinky_fkOri_joint_3.rz.set(110)
	pinky_fkOri_joint_4.rz.set(30)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	parent_icon.scrunch.set(-10)
	pinky_fkOri_joint_2.rz.set(-3)
	pinky_fkOri_joint_3.rz.set(-4)
	pinky_fkOri_joint_4.rz.set(-10)
	pm.setDrivenKeyframe(pinky_drivenAttr_allScrunch, currentDriver=pinky_driver_allScrunch)
	pinky_drivenKeyframes_allScrunch = (pinky_fkOri_root + '_rotateZ', pinky_fkOri_joint_2 + '_rotateZ', pinky_fkOri_joint_3 + '_rotateZ', pinky_fkOri_joint_4 + '_rotateZ')
	pm.keyTangent(pinky_drivenKeyframes_allScrunch, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

	parent_icon.scrunch.set(0)

	'''
	Index allSpread
	'''
	index_drivenAttr_allSpread = (index_fkOri_root + '.ry', index_fkOri_joint_2 + '.ry')
	index_driven_allSpread= (index_fkOri_root, index_fkOri_joint_2)
	index_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(index_driven_allSpread, ro=(0, 6, 0))
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(index_driven_allSpread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(index_drivenAttr_allSpread, currentDriver=index_driver_allSpread)
	parent_icon.spread.set(0)

	index_drivenKeyframes_allSpread = (index_fkOri_root + '_rotateY', index_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(index_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Middle allSpread
	'''
	middle_drivenAttr_allSpread = (middle_fkOri_root + '.ry', middle_fkOri_joint_2 + '.ry')
	middle_driven_allSpread= (middle_fkOri_root, middle_fkOri_joint_2)
	middle_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(middle_driven_allSpread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(middle_driven_allSpread, ro=(0, 0, 0))
	pm.setDrivenKeyframe(middle_drivenAttr_allSpread, currentDriver=middle_driver_allSpread)
	parent_icon.spread.set(0)

	middle_drivenKeyframes_allSpread = (middle_fkOri_root + '_rotateY', middle_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(middle_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Ring allSpread
	'''
	ring_drivenAttr_allSpread = (ring_fkOri_root + '.ry', ring_fkOri_joint_2 + '.ry')
	ring_driven_allSpread= (ring_fkOri_root, ring_fkOri_joint_2)
	ring_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(ring_drivenAttr_allSpread, currentDriver=ring_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(ring_driven_allSpread, ro=(0, -3, 0))
	pm.setDrivenKeyframe(ring_drivenAttr_allSpread, currentDriver=ring_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(ring_driven_allSpread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(ring_drivenAttr_allSpread, currentDriver=ring_driver_allSpread)
	parent_icon.spread.set(0)

	ring_drivenKeyframes_allSpread = (ring_fkOri_root + '_rotateY', ring_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(ring_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky allSpread
	'''
	pinky_drivenAttr_allSpread = (pinky_fkOri_root + '.ry', pinky_fkOri_joint_2 + '.ry')
	pinky_driven_allSpread= (pinky_fkOri_root, pinky_fkOri_joint_2)
	pinky_driver_allSpread = (parent_icon + '.spread')
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(10)
	pm.xform(pinky_driven_allSpread, ro=(0, -6, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(-10)
	pm.xform(pinky_driven_allSpread, ro=(0, 3, 0))
	pm.setDrivenKeyframe(pinky_drivenAttr_allSpread, currentDriver=pinky_driver_allSpread)
	parent_icon.spread.set(0)

	pinky_drivenKeyframes_allSpread = (pinky_fkOri_root + '_rotateY', pinky_fkOri_joint_2 + '_rotateY')
	pm.keyTangent(pinky_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb allSpread
	'''
	thumb_drivenAttr_allSpread = [thumb_fkOri_joint_1 + '.ry']
	thumb_driver_allSpread  = (parent_icon + '.spread')
	thumb_driven_allSpread = [thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_pivot, thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(10)
	thumb_fkOri_joint_1.ry.set(30)
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(-10)
	thumb_fkOri_joint_1.ry.set(-50)
	pm.setDrivenKeyframe(thumb_drivenAttr_allSpread, currentDriver=thumb_driver_allSpread)
	parent_icon.spread.set(0)

	thumb_drivenKeyframes_allSpread = (thumb_fkOri_joint_1 + '_rotateY')
	pm.keyTangent(thumb_drivenKeyframes_allSpread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)



	'''
	Index allRelax
	'''
	index_drivenAttr_allRelax = [index_fkOri_root + '.rz', index_fkOri_joint_2 + '.rz', index_fkOri_joint_3 + '.rz', index_fkOri_joint_4 + '.rz']
	index_driven_allRelax = [index_fkOri_root, index_fkOri_joint_2, index_fkOri_joint_3, index_fkOri_joint_4]
	index_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(10)
	index_fkOri_root.rz.set(3)
	index_fkOri_joint_2.rz.set(3.75)
	index_fkOri_joint_3.rz.set(4.5)
	index_fkOri_joint_4.rz.set(8.4)
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(-10)
	index_fkOri_root.rz.set(12)
	index_fkOri_joint_2.rz.set(15)
	index_fkOri_joint_3.rz.set(18)
	index_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(index_drivenAttr_allRelax, currentDriver=index_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(index_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Middle allRelax
	'''
	middle_drivenAttr_allRelax = [middle_fkOri_root + '.rz', middle_fkOri_joint_2 + '.rz', middle_fkOri_joint_3 + '.rz', middle_fkOri_joint_4 + '.rz']
	middle_driven_allRelax = [middle_fkOri_root, middle_fkOri_joint_2, middle_fkOri_joint_3, middle_fkOri_joint_4]
	middle_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(10)
	middle_fkOri_root.rz.set(6)
	middle_fkOri_joint_2.rz.set(7.5)
	middle_fkOri_joint_3.rz.set(9)
	middle_fkOri_joint_4.rz.set(12.6)
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(-10)
	middle_fkOri_root.rz.set(9)
	middle_fkOri_joint_2.rz.set(11.25)
	middle_fkOri_joint_3.rz.set(13.5)
	middle_fkOri_joint_4.rz.set(16.8)
	pm.setDrivenKeyframe(middle_drivenAttr_allRelax, currentDriver=middle_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(middle_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Ring allRelax
	'''
	ring_drivenAttr_allRelax = [ring_fkOri_root + '.rz', ring_fkOri_joint_2 + '.rz', ring_fkOri_joint_3 + '.rz', ring_fkOri_joint_4 + '.rz']
	ring_driven_allRelax = [ring_fkOri_root, ring_fkOri_joint_2, ring_fkOri_joint_3, ring_fkOri_joint_4]
	ring_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(ring_drivenAttr_allRelax, currentDriver=ring_driver_allRelax)
	parent_icon.relax.set(10)
	ring_fkOri_root.rz.set(9)
	ring_fkOri_joint_2.rz.set(11.25)
	ring_fkOri_joint_3.rz.set(13.5)
	ring_fkOri_joint_4.rz.set(16.8)
	pm.setDrivenKeyframe(ring_drivenAttr_allRelax, currentDriver=ring_driver_allRelax)
	parent_icon.relax.set(-10)
	ring_fkOri_root.rz.set(6)
	ring_fkOri_joint_2.rz.set(7.5)
	ring_fkOri_joint_3.rz.set(9)
	ring_fkOri_joint_4.rz.set(12.6)
	pm.setDrivenKeyframe(ring_drivenAttr_allRelax, currentDriver=ring_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(ring_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Pinky allRelax
	'''
	pinky_drivenAttr_allRelax = [pinky_fkOri_root + '.rz', pinky_fkOri_joint_2 + '.rz', pinky_fkOri_joint_3 + '.rz', pinky_fkOri_joint_4 + '.rz']
	pinky_driven_allRelax = [pinky_fkOri_root, pinky_fkOri_joint_2, pinky_fkOri_joint_3, pinky_fkOri_joint_4]
	pinky_driver_allRelax = (parent_icon + '.relax')
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(10)
	pinky_fkOri_root.rz.set(12)
	pinky_fkOri_joint_2.rz.set(15)
	pinky_fkOri_joint_3.rz.set(18)
	pinky_fkOri_joint_4.rz.set(21)
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(-10)
	pinky_fkOri_root.rz.set(3)
	pinky_fkOri_joint_2.rz.set(3.75)
	pinky_fkOri_joint_3.rz.set(4.5)
	pinky_fkOri_joint_4.rz.set(8.4)
	pm.setDrivenKeyframe(pinky_drivenAttr_allRelax, currentDriver=pinky_driver_allRelax)
	parent_icon.relax.set(0)

	pm.keyTangent(pinky_driven_allRelax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Curl
	'''
	thumb_drivenAttr_curl = [thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry']
	thumb_driven_curl = [thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	thumb_driver_curl = (parent_icon + '.curl')
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(10)
	thumb_fkOri_joint_1.ry.set(-25)
	thumb_fkOri_joint_2.ry.set(-30)
	thumb_fkOri_joint_3.ry.set(-32)
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(-10)
	thumb_fkOri_joint_1.ry.set(40)
	thumb_fkOri_joint_2.ry.set(30)
	thumb_fkOri_joint_3.ry.set(32)
	pm.setDrivenKeyframe(thumb_drivenAttr_curl, currentDriver=thumb_driver_curl)
	parent_icon.curl.set(0)

	pm.keyTangent(thumb_driven_curl, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Drop
	'''
	thumb_drivenAttr_drop = [thumb_fkOri_pivot + '.rx']
	thumb_driven_drop = [thumb_fkOri_pivot]
	thumb_driver_drop = (parent_icon + '.drop')
	pm.setDrivenKeyframe(thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
	parent_icon.drop.set(10)
	thumb_fkOri_pivot.rx.set(-64)
	pm.setDrivenKeyframe(thumb_drivenAttr_drop, currentDriver=thumb_driver_drop)
	parent_icon.drop.set(0)

	pm.keyTangent(thumb_driven_drop, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Relax
	'''
	thumb_drivenAttr_relax = [thumb_fkOri_joint_1 + '.ry', thumb_fkOri_joint_2 + '.ry', thumb_fkOri_joint_3 + '.ry', thumb_fkOri_joint_1 + '.rz', thumb_fkOri_joint_2 + '.rz', thumb_fkOri_joint_3 + '.rz']
	thumb_driven_relax = [thumb_fkOri_joint_1, thumb_fkOri_joint_2, thumb_fkOri_joint_3]
	thumb_driver_relax = (parent_icon + '.thumbRelax')
	pm.setDrivenKeyframe(thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
	parent_icon.thumbRelax.set(10)
	thumb_fkOri_joint_1.ry.set(-9)
	thumb_fkOri_joint_2.ry.set(-6)
	thumb_fkOri_joint_3.ry.set(-12)
	thumb_fkOri_joint_1.rz.set(4)
	thumb_fkOri_joint_2.rz.set(7)
	thumb_fkOri_joint_3.rz.set(12)
	pm.setDrivenKeyframe(thumb_drivenAttr_relax, currentDriver=thumb_driver_relax)
	parent_icon.thumbRelax.set(0)

	pm.keyTangent(thumb_driven_relax, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)


	'''
	Thumb Spread
	'''
	thumb_drivenAttr_spread = [thumb_fkOri_joint_1 + '.ry']
	thumb_driven_spread = [thumb_fkOri_joint_1]
	thumb_driver_spread = (parent_icon + '.thumbSpread')
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(10)
	thumb_fkOri_joint_1.ry.set(-45)
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(-10)
	thumb_fkOri_joint_1.ry.set(40)
	pm.setDrivenKeyframe(thumb_drivenAttr_spread, currentDriver=thumb_driver_spread)
	parent_icon.thumbSpread.set(0)

	pm.keyTangent(thumb_driven_spread, 'graphEditor1FromOutliner', ott='auto', itt='auto', animation='objects', e=1)

def locator_creation(*args):
	global inner_loc, outer_loc, middle_loc

	inner_loc = pm.spaceLocator(p=(0, 0, 0))

	outer_loc = pm.spaceLocator(p=(0, 0, 0))

	middle_loc = pm.spaceLocator(p=(0, 0, 0))

	loc_name = hand_root_joint.replace('hand_01_bind', 'inner_loc')
	inner_loc.rename(loc_name)

	loc_name = inner_loc.replace('inner', 'outer')
	outer_loc.rename(loc_name)

	loc_name = outer_loc.replace('outer', 'middle')
	middle_loc.rename(loc_name)

def palmSetup_part_1(*args):
	'''
	Create the locators
	'''
	pm.parent(middle_loc, outer_loc)
	pm.parent(outer_loc, inner_loc)

	joint_name = hand_base.replace('temp', 'const_pivot')
	hand_base.rename(joint_name)

	loc_name = hand_root_joint.replace('hand_01_bind', 'inner_loc')
	inner_loc.rename(loc_name)

	loc_name = inner_loc.replace('inner', 'outer')
	outer_loc.rename(loc_name)

	loc_name = outer_loc.replace('outer', 'middle')
	middle_loc.rename(loc_name)

	pm.parent(hand_base, middle_loc)

	'''
	Pad the joints
	'''
	index_pad = pm.group(empty=1)

	middle_pad = pm.group(empty=1)

	ring_pad = pm.group(empty=1)

	pinky_pad = pm.group(empty=1)

	thumb_pad = pm.group(empty=1)

	temp_constraint = pm.parentConstraint(index_root, index_pad, mo=0)
	pm.delete(temp_constraint)
	pm.select(index_pad)
	freezeTransform()

	pad_name = index_root.replace('01_bind', '00_pad')
	index_pad.rename(pad_name)

	pm.parent(index_root, index_pad)	


	temp_constraint = pm.parentConstraint(middle_root, middle_pad, mo=0)
	pm.delete(temp_constraint)
	pm.select(middle_pad)
	freezeTransform()

	pad_name = middle_root.replace('01_bind', '00_pad')
	middle_pad.rename(pad_name)

	pm.parent(middle_root, middle_pad)	

	temp_constraint = pm.parentConstraint(ring_root, ring_pad, mo=0)
	pm.delete(temp_constraint)
	pm.select(ring_pad)
	freezeTransform()

	pad_name = ring_root.replace('01_bind', '00_pad')
	ring_pad.rename(pad_name)

	pm.parent(ring_root, ring_pad)	

	temp_constraint = pm.parentConstraint(pinky_root, pinky_pad, mo=0)
	pm.delete(temp_constraint)
	pm.select(pinky_pad)
	freezeTransform()

	pad_name = pinky_root.replace('01_bind', '00_pad')
	pinky_pad.rename(pad_name)

	pm.parent(pinky_root, pinky_pad)	

	temp_constraint = pm.parentConstraint(thumb_pivot, thumb_pad, mo=0)
	pm.delete(temp_constraint)
	pm.select(thumb_pad)
	freezeTransform()

	pad_name = thumb_joint_1.replace('02_bind', '00_pad')
	thumb_pad.rename(pad_name)

	pm.parent(thumb_pivot, thumb_pad)

	# '''
	# Parent Constrain the const pivot to the pads and locals
	# '''
	# pm.select(hand_base, index_01_local)
	# parentConstraint_on()

	# pm.select(hand_base, middle_01_local)
	# parentConstraint_on()

	# pm.select(hand_base, ring_01_local)
	# parentConstraint_on()

	# pm.select(hand_base, pinky_01_local)
	# parentConstraint_on()

	# pm.select(hand_base, thumb_01_local)
	# parentConstraint_on()

	'''
	Create the ik joints
	'''
	index_01_ik = pm.joint(index_root)
	index_02_ik = pm.joint(index_joint_5)

	pm.parent(index_02_ik, index_01_ik)
	pm.parent(index_01_ik, w=1)

	middle_01_ik = pm.joint(middle_root)
	middle_02_ik = pm.joint(middle_joint_5)

	pm.parent(middle_02_ik, middle_01_ik)
	pm.parent(middle_01_ik, w=1)

	ring_01_ik = pm.joint(ring_root)
	ring_02_ik = pm.joint(ring_joint_5)

	pm.parent(ring_02_ik, ring_01_ik)
	pm.parent(ring_01_ik, w=1)

	pinky_01_ik = pm.joint(pinky_root)
	pinky_02_ik = pm.joint(pinky_joint_5)

	pm.parent(pinky_02_ik, pinky_01_ik)
	pm.parent(pinky_01_ik, w=1)

	thumb_01_ik = pm.joint(thumb_joint_1)
	thumb_02_ik = pm.joint(thumb_joint_4)

	pm.parent(thumb_02_ik, thumb_01_ik)
	pm.parent(thumb_01_ik, w=1)

	'''
	Create the ik handles
	'''
	index_ikh = pm.ikHandle(sj=index_01_ik, ee=index_02_ik, sol='ikSCsolver')[0]
	print 'Index ikh:', index_ikh

	middle_ikh = pm.ikHandle(sj=middle_01_ik, ee=middle_02_ik, sol='ikSCsolver')[0]
	print 'Middle ikh:', middle_ikh

	ring_ikh = pm.ikHandle(sj=ring_01_ik, ee=ring_02_ik, sol='ikSCsolver')[0]
	print 'Ring ikh:', ring_ikh

	pinky_ikh = pm.ikHandle(sj=pinky_01_ik, ee=pinky_02_ik, sol='ikSCsolver')[0]
	print 'Pinky ikh:', pinky_ikh

	thumb_ikh = pm.ikHandle(sj=thumb_01_ik, ee=thumb_02_ik, sol='ikSCsolver')[0]
	print 'Thumb ikh:', thumb_ikh

	straight_const_grp = pm.group(index_ikh, middle_ikh, ring_ikh, pinky_ikh, thumb_ikh)
	centerPivot(straight_const_grp)


	# index_const = pm.parentConstraint(mo=False)
	# index_const_targets = index_const.getWeightAliasList()









