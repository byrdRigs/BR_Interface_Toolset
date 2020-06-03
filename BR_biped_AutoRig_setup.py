'''
Biped Complete Auto-rig Setup
Description
	This file contains:
		Biped Window
		Joint Location Locators 
		Locator conversion
		Head Setup
		Eye Setup
		Jaw Setup
		Neck Setup
		Shoulder Setup
		Arm Setup
		Hand Fetup
		Finger Setup
		Back Setup
		Root Setup 
		Hip Setup
		Leg Setup
		Extra Limbs
How to run:
	import BR_Interface_Toolset.BR_biped_AutoRig_setup as BR_biped_setup
	reload (BR_biped_setup)
	BR_biped_setup.gui()
'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os






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
	if pm.window('ByrdRigs_Biped_Body_Auto_Rigger', q=1, exists=1):
		pm.deleteUI('ByrdRigs_Biped_Body_Auto_Rigger')
		#ByrdRigs_Biped_Body_Auto_Rigger

	win_width = 280
	window_object = pm.window('ByrdRigs_Biped_Body_Auto_Rigger', title="ByrdRigs' Biped Body Auto Rigger", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()


	pm.button(l='Locator Creation', w=win_width, bgc=color_1, c=biped_locImport)
	pm.separator('locatorSep', w=win_width, bgc=color_1, st='in')
	pm.text('locatorMoveStatement', l="Move the locators where you want the joints to be placed, this can be changed until you are ready to build the rig.", w=win_width, ww=1, bgc=color_15)
	pm.text(l="***Please keep all locators even if you aren't using the joints***", w=win_width, ww=1, bgc=color_16)
	pm.text(l="You can delete the ones you don't want after converting them", w=win_width, ww=1, bgc=color_17)
	pm.separator(w=win_width, bgc=color_1, st='in')
	pm.button('locConvert', l='Convert Locators to Joints.', w=win_width, bgc=color_2, c=jointConvert)
	pm.separator('locConvert_sep', w=win_width, bgc=color_2, st='in')


	'''
	Maunal Rig
	'''

	manual_layout = pm.frameLayout(w=win_width, l='Manual Build', bgc=color_3, cl=1, cll=1, cc=windowResize)
	manual_sub_layout = pm.columnLayout()

	'''
	Head
	'''

	pm.setParent(manual_sub_layout)
	head_layout = pm.frameLayout(w=win_width, l='Head/Eyes/Jaw', bgc=color_4, cl=1, cll=1, cc=windowResize)
	pm.columnLayout()
	pm.button('headSetup_button', l='Head Space locator and icon', w=win_width, bgc=color_5, c=headSetup)

	pm.separator(w=win_width, bgc=color_5, st='in')

	'''
	Eye
	'''
	
	pm.button('eyeSetup_button', l='Eye Setup', w=win_width, bgc=color_6, c=eyeSetup)
	pm.separator(w=win_width, bgc=color_6, st='in')

	'''
	Jaw
	'''
	pm.button('jawSetup_buuton', l='Jaw Setup', w=win_width, bgc=color_7, c= jawSetup)
	pm.separator(w=win_width, bgc=color_7, st='in')


	pm.setParent(manual_sub_layout)
	pm.separator('headFrame_sep', w=win_width, bgc=color_4, st='in')

	'''
	Neck
	'''
	pm.setParent(manual_sub_layout)
	neck_layout = pm.frameLayout(w=win_width, l='Neck (Based on 4 joints)', bgc=color_5, cl=1, cll=1, cc=windowResize)
	pm.columnLayout()
	pm.button('neckSetup_button', l='Ik/Fk System', w=win_width, bgc=color_6, c=neckSetup)
	pm.separator(w=win_width, bgc=color_6, st='in')


	pm.setParent(manual_sub_layout)
	pm.separator('neckFrame_sep', w=win_width, bgc=color_5, st='in')

	'''
	Shoulder
	'''
	pm.setParent(manual_sub_layout)
	shoulder_layout = pm.frameLayout(w=win_width, l='Shoulder/Arms/Hand/Fingers', bgc=color_6, cl=1, cll=1, cc=windowResize)
	pm.text(l='Please go in order from top to bottom', w=win_width, ww=1)
	pm.rowColumnLayout(nc=4, cw=([1,65], [2, 65], [3, 65], [4, 65]))
	pm.text('shoulder_orientationText', l='Ori:')
	pm.radioButtonGrp('shoulder_orientationOption', w=win_width, cw=([1, 65], [2, 65], [3, 65]), labelArray3=['Lt', 'Rt', 'Both'], numberOfRadioButtons=3, sl=3)
	pm.setParent(shoulder_layout)
	pm.columnLayout(w=win_width)
	pm.button(l='Shoulder Setup', w=win_width, bgc=color_7, c= shoulderSystem)

	pm.separator('shoulderSetup_sep', w=win_width, bgc=color_7, st='in')

	'''
	Arm
	'''
	pm.rowColumnLayout(nc=4, cw=([1,65], [2, 65], [3, 65], [4, 65]))
	pm.text('arm_orientationText', l='Ori:')
	pm.radioButtonGrp('arm_orientationOption', labelArray3=['Lt', 'Rt', 'Both'], numberOfRadioButtons=3, vr=1, sl=3)
	pm.text('armSystem_text', l='System')
	pm.radioButtonGrp('arm_systemOption', labelArray3=['Fk', 'Ik', 'Ik/Fk'], numberOfRadioButtons=3, vr=1, sl=3)
	pm.columnLayout(w=win_width)
	pm.button('armSetup_button', l='Arm Setup', w=win_width, bgc=color_8, c=armSystem)

	pm.separator('armSetup_sep', w=win_width, bgc=color_8, st='in')

	'''
	Hand
	'''
	pm.rowColumnLayout(nc=4, cw=([1,65], [2, 65], [3, 65], [4, 65]))
	pm.text('hand_orientationText', l='Ori:')
	pm.radioButtonGrp('hand_orientationOption', w=win_width, cw=([1, 65], [2, 65], [3, 65]), labelArray3=['Lt', 'Rt', 'Both'], numberOfRadioButtons=3, sl=3)
	pm.setParent(shoulder_layout)
	pm.columnLayout(w=win_width)
	pm.button(l='Hand Setup', w=win_width, bgc=color_9, c= handSystem)

	pm.separator('handSetup_sep', w=win_width, bgc=color_9, st='in')

	pm.setParent(manual_sub_layout)
	pm.separator('sh_a_hFrame_sep', w=win_width, bgc=color_6, st='in')

	'''
	Back
	'''
	back_layout = pm.frameLayout(w=win_width, l='Back', bgc=color_7, cl=1, cll=1, cc=windowResize)
	pm.columnLayout()
	pm.button('back_button', l='Back Setup', w=win_width, bgc=color_8, c=backSetup)


	pm.setParent(manual_sub_layout)
	pm.separator('backFrame_sep', w=win_width, bgc=color_7, st='in')

	'''
	Hip
	'''
	hip_layout = pm.frameLayout(w=win_width, l='Hip', bgc=color_8, cl=1, cll=1, cc=windowResize)
	pm.columnLayout()
	pm.button('hip_button', l='Hip Setup', w=win_width, bgc=color_9, c=hipSetup)


	pm.setParent(manual_sub_layout)
	pm.separator('hipFrame_sep', w=win_width, bgc=color_8, st='in')

	'''
	Leg
	'''
	leg_layout = pm.frameLayout(w=win_width, l='Legs/Feet', bgc=color_9, cl=1, cll=1, cc=windowResize)
	pm.rowColumnLayout(nc=4, cw=([1,65], [2, 65], [3, 65], [4, 65]))
	pm.text('leg_orientationText', l='Ori:')
	pm.radioButtonGrp('leg_orientationOption', labelArray3=['Lt', 'Rt', 'Both'], numberOfRadioButtons=3, vr=1, sl=3)
	pm.text('legSystem_text', l='System')
	pm.radioButtonGrp('leg_systemOption', labelArray3=['Fk', 'Ik', 'Ik/Fk'], numberOfRadioButtons=3, vr=1, sl=3)
	pm.columnLayout(w=win_width)

	pm.button('legSetup_button', l='Leg Setup', w=win_width, bgc=color_10, c=legSystem)
	pm.separator('legSetup_sep', w=win_width, bgc=color_9, st='in')

	'''
	RFL
	'''
	rfl_layout = pm.rowColumnLayout('rfl_layout', nc=4, cw=([1,65], [2, 65], [3, 65], [4, 65]))
	pm.text('rfl_orientationText', l='Ori:')
	pm.radioButtonGrp('rfl_orientationOption', w=win_width, cw=([1, 65], [2, 65], [3, 65]), labelArray3=['Lt', 'Rt', 'Both'], numberOfRadioButtons=3, sl=3)
	pm.setParent(leg_layout)
	pm.columnLayout(w=win_width)
	pm.text(l='Create and move rfl locators', ww=1, w=win_width)
	pm.button(l='RFL Prep', w=win_width, bgc=color_11, c=rflPrepSystem)
	pm.separator('rflPrep_sep', w=win_width, bgc=color_11, st='in')
	pm.button('rflSetup_button', l='RFL Setup', w=win_width, bgc=color_12, c=rflSystem)
	pm.separator('rflSetup_sep', w=win_width, bgc=color_12, st='in')

	'''
	Bind
	'''
	pm.setParent(manual_sub_layout)
	weight_layout = pm.frameLayout(l='Bind', bgc=color_10, w=win_width, cl=1, cll=1, cc=windowResize)
	pm.gridLayout(w=win_width, cr=1, cw=130, nr=3, nc=2)
	pm.button(l='Body Geo', w=120, c=bodyGeo_selection)
	body_geo_selection = pm.textField('body_geo_selection', ed=0, w=130)
	pm.button(l='Lt Eye Geo', w=120, c=lt_eyeGeo_selection)
	lt_eye_geo_selection = pm.textField('lt_eye_geo_selection', ed=0, w=130)
	pm.button(l='Rt Eye Geo', w=120, c=rt_eyeGeo_selection)
	rt_eye_geo_selection = pm.textField('rt_eye_geo_selection', ed=0, w=130)
	pm.setParent(weight_layout)
	pm.columnLayout(w=win_width)
	pm.button(l='Bind Body', w=win_width, bgc=color_11, c=bodyBind)
	pm.separator(w=win_width, bgc=color_11, st='in')
	pm.button(l='Bind Eyes', w=win_width, bgc=color_12, c=eyeBind)
	pm.separator(w=win_width, bgc=color_12, st='in')


	pm.setParent(main_layout)
	pm.separator('manualBuild_sep', w=win_width, bgc=color_4, st='in')



	'''
	Auto-Rig
	'''
	pm.frameLayout(w=win_width, l='Auto Build-Best to manually build first', bgc=color_4, cl=1, cll=1, cc=windowResize)
	pm.columnLayout(w=win_width)
	pm.text(l='Create and move rfl locators', ww=1, w=win_width)
	pm.button(l='RFL Prep', bgc=color_4, w=win_width, c=rflPrep)
	pm.button('autoBuild_button', l='Build Rig', w=win_width, bgc=color_5, c=autoBuild)


	pm.setParent(main_layout)
	pm.separator('autoBuild_sep', w=win_width, bgc=color_4, st='in')
	pm.columnLayout()

	'''
	'''

	pm.setParent(main_layout)
	pm.button('closeButton', l='Close', w=win_width, c=deleteUI)

	pm.window('ByrdRigs_Biped_Body_Auto_Rigger', e=1, wh=(260, 80), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)

def getDir():
	global file_name
	file_name = os.path.dirname(fileName)
	extension = os.path.splitext(file_name)
	# print file_name
	# print raw_name

	listOfFiles = getListOfFiles(file_name)
	print listOfFiles[9]
	cmds.file(listOfFiles[9], pr=1, rpr="biped", ignoreVersion=1, i=1, type="mayaAscii", importFrameRate=True, importTimeRange="override", ra=True, mergeNamespacesOnClash=False, options="v=0;")

def getListOfFiles(file_name):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(file_name)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(file_name, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def deleteHistory(*args):
	pm.delete(ch=1)
	# print 'History Deleted'

def centerPivot(*args):
	pm.xform(cpc=1)
	# print 'Selected pivot centered.'

def freezeTransform(*agrs):
	pm.makeIdentity(apply=1, t=1, r=1, s=1, n=0, pn=1)
	# print 'Transform Frozen'

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

def mirrorToolO(*args):
	print 'Mirroring Joints'
	selection = pm.ls(sl=1) 
	for each in selection:
		pm.mirrorJoint(each, searchReplace=("lt", "rt"), mirrorYZ=1)

def mirrorToolB(*args):
	print 'Mirroring Joints'
	selection = pm.ls(sl=1) 
	for each in selection:
		pm.mirrorJoint(each, mirrorBehavior=1,searchReplace=("lt", "rt"), mirrorYZ=1)

def RP_IkHandle(*args):
	print 'RP IK Handle Tool.'
	pm.ikHandle()

def SC_IkHandle(*args):
	print 'SC IK Handle Tool.'
	pm.ikHandle(sol='ikSCsolver')

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

def ctrlPadding(*args):
	selected = pm.ls(selection=1)
	#print 'Current Selected:' , selected 
	root_joint = selected[0]

	local = pm.group(empty=1)
	temp_constraint =pm.parentConstraint(root_joint, local)
	pm.delete(temp_constraint)
	pm.parent(root_joint, local)
	local_name = root_joint.replace('_icon', '_local')
	# print(local_name)
	local.rename(local_name)

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

def poleVector(*args):
	print 'Pole Vector Constraint'
	selection = pm.ls(sl=1)
	driver = selection[0]
	driven = selection[1]
	pm.poleVectorConstraint(driver, driven)

def joint_positions(*j):
	pm.joint(zso=1, ch=1, e=1, oj='xzy', secondaryAxisOrient='zup')
	pos = [pm.xform(j,q=True, t=True, ws=True)]
	print pos
   	children = cmds.listRelatives(j, c=True) or []
   	for child in children:
 		pos.extend(joint_positions(child))
	return pos

def create_circle():
    global icon
    icon = pm.circle(nr=[0,1,0])[0]

def biped_locImport(*args):
	global root_loc, hip_loc, lt_leg_01_loc, lt_toeA_01_loc, lt_toeB_01_loc, lt_toeC_01_loc, lt_toeD_01_loc
	global lt_toeE_01_loc, back_01_loc, neck_01_loc, head_01_loc, lt_eye_01_loc, jaw_01_loc, lt_clav_01_loc
	global lt_arm_01_loc, lt_hand_01_loc, lt_index_01_loc, lt_middle_01_loc, lt_pinky_01_loc, lt_ring_01_loc 
	global lt_thumb_01_loc, icon

	import BR_Interface_Toolset
	getDir()
	loc_grp = 'biped_fitSkeleton_crv'
	# print 'Loc Group:', loc_grp

	pm.select(loc_grp)
	loc_grp = pm.ls(sl=1, dag=1, transforms=1)
	# print 'Locators:', loc_grp
	icon = loc_grp[0]
	root_loc = loc_grp[1]
	hip_loc = loc_grp[2]
	lt_leg_01_loc = loc_grp[3]
	lt_toeA_01_loc = loc_grp[8]
	lt_toeB_01_loc = loc_grp[11] 
	lt_toeC_01_loc = loc_grp[14] 
	lt_toeD_01_loc = loc_grp[17] 
	lt_toeE_01_loc = loc_grp[20] 
	back_01_loc = loc_grp[23]
	neck_01_loc = loc_grp[30]
	head_01_loc = loc_grp[34]
	lt_eye_01_loc = loc_grp[36]
	jaw_01_loc = loc_grp[38]
	lt_clav_01_loc = loc_grp[40]
	lt_arm_01_loc = loc_grp[42]
	lt_hand_01_loc = loc_grp[45]
	lt_index_01_loc = loc_grp[47]
	lt_middle_01_loc = loc_grp[52]
	lt_pinky_01_loc = loc_grp[57]
	lt_ring_01_loc = loc_grp[62]
	lt_thumb_01_loc = loc_grp[67]
	# print 'Grp:', grp
	# print 'Icon:', icon
	# print 'Root Loc:', root_loc
	# print 'Hip Loc:', hip_loc
	# print 'Toe A:', lt_toeA_01_loc
	# print 'Toe B:', lt_toeB_01_loc
	# print 'Toe C:', lt_toeC_01_loc
	# print 'Toe D:', lt_toeD_01_loc
	# print 'Toe E:', lt_toeE_01_loc
	# print 'Back Loc:', back_01_loc
	# print 'Neck Loc:', neck_01_loc
	# print 'Eye Loc:', lt_eye_01_loc
	# print 'Jaw Loc:', jaw_01_loc
	# print 'Clav Loc:', lt_clav_01_loc
	# print 'Arm Loc:', lt_arm_01_loc
	# print 'Hand Loc:', lt_hand_01_loc
	# print 'Index Loc:', lt_index_01_loc
	# print 'Middle Loc:', lt_middle_01_loc
	# print 'Pinky Loc:', lt_pinky_01_loc
	# print 'Ring Loc:', lt_ring_01_loc
	# print 'Thumb Loc:', lt_thumb_01_loc

def jointConvert(*args):
	global ct_root_waste, ct_hip_bind, lt_leg_01_bind, lt_toeA_01_bind, lt_toeB_01_bind, lt_toeC_01_bind, lt_toeD_01_bind
	global lt_toeE_01_bind, back_01_bind, lt_eye_01_bind, jaw_01_bind, lt_clav_01_bind
	global lt_arm_01_bind, lt_hand_01_bind, lt_index_01_bind, lt_middle_01_bind, lt_pinky_01_bind, lt_ring_01_bind 
	global lt_thumb_01_bind, rt_leg_01_bind, rt_toeA_01_bind, rt_toeB_01_bind, rt_toeC_01_bind, rt_toeD_01_bind
	global rt_toeE_01_bind, rt_eye_01_bind, jaw_01_bind, rt_clav_01_bind
	global rt_arm_01_bind, rt_hand_01_bind, rt_index_01_bind, rt_middle_01_bind, rt_pinky_01_bind, rt_ring_01_bind 
	global rt_thumb_01_bind, ct_head_01_bind, ct_neck_01_bind, ct_jaw_01_bind, ct_back_01_bind
	pm.parent('*_01_loc', icon)
	
	pm.select(back_01_loc)
	selection = pm.ls(sl=1, dag=1, type='transform')
	for each in selection:
		joints = pm.joint()
		temp_constraint = pm.parentConstraint(each, joints, mo=0)
		pm.delete(temp_constraint)
		freezeTransform()


	pm.select('joint1')
	joint_chain = pm.ls(sl=1, dag=1, type='transform')
	# print 'Joint chain', joint_chain
	ori = 'ct'
	system_name = 'back'
	count = 0
	suffix = 'bind'

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		current_joint.rename(new_name)
		
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)

	pm.select(joint_chain)
	joint_chain = pm.ls(sl=1)[0]
	# print joint_chain
	pm.parent(joint_chain, w=1)

	

	pm.select(head_01_loc)
	selection = pm.ls(sl=1, dag=1, type='transform')
	for each in selection:
		joints = pm.joint()
		temp_constraint = pm.parentConstraint(each, joints, mo=0)
		pm.delete(temp_constraint)
		freezeTransform()


	pm.select('joint1')
	joint_chain = pm.ls(sl=1, dag=1, type='transform')
	# print 'Joint chain', joint_chain
	ori = 'ct'
	system_name = 'head'
	count = 0
	suffix = 'bind'

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		current_joint.rename(new_name)
		
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)

	pm.select(joint_chain)
	joint_chain = pm.ls(sl=1)[0]
	# print joint_chain
	pm.parent(joint_chain, w=1)



	pm.select(hip_loc)
	selection = pm.ls(sl=1, dag=1, type='transform')
	joints = pm.joint()
	temp_constraint = pm.parentConstraint(selection, joints, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()


	pm.select('joint1')
	joint_chain = pm.ls(sl=1, dag=1, type='transform')
	# print 'Joint chain', joint_chain
	ori = 'ct'
	system_name = 'hip'
	count = 0
	suffix = 'bind'

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		current_joint.rename(new_name)
		
	pm.select(joint_chain)
	joint_chain = pm.ls(sl=1)[0]
	# print joint_chain
	pm.parent(joint_chain, w=1)


	pm.select(jaw_01_loc)
	selection = pm.ls(sl=1, dag=1, type='transform')
	for each in selection:
		joints = pm.joint()
		temp_constraint = pm.parentConstraint(each, joints, mo=0)
		pm.delete(temp_constraint)
		freezeTransform()


	pm.select('joint1')
	joint_chain = pm.ls(sl=1, dag=1, type='transform')
	# print 'Joint chain', joint_chain
	ori = 'ct'
	system_name = 'jaw'
	count = 0
	suffix = 'bind'

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		current_joint.rename(new_name)
		
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)

	pm.select(joint_chain)
	joint_chain = pm.ls(sl=1)[0]
	# print joint_chain
	pm.parent(joint_chain, w=1)


	pm.select(neck_01_loc)
	selection = pm.ls(sl=1, dag=1, type='transform')
	for each in selection:
		joints = pm.joint()
		temp_constraint = pm.parentConstraint(each, joints, mo=0)
		pm.delete(temp_constraint)
		freezeTransform()


	pm.select('joint1')
	joint_chain = pm.ls(sl=1, dag=1, type='transform')
	# print 'Joint chain', joint_chain
	ori = 'ct'
	system_name = 'neck'
	count = 0
	suffix = 'bind'

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		current_joint.rename(new_name)
		
	new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
	current_joint.rename(new_name)

	pm.select(joint_chain)
	joint_chain = pm.ls(sl=1)[0]
	# print joint_chain
	pm.parent(joint_chain, w=1)


	pm.select(root_loc)
	selection = pm.ls(sl=1, dag=1, type='transform')
	joints = pm.joint()


	pm.select('joint1')
	joint_chain = pm.ls(sl=1, dag=1, type='transform')
	# print 'Joint chain', joint_chain
	ori = 'ct'
	system_name = 'root'
	count = 0
	suffix = 'waste'

	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0}_{1}_{2}'.format(ori, system_name, suffix)
		current_joint.rename(new_name)
		

	pm.select(joint_chain)
	joint_chain = pm.ls(sl=1)[0]
	# print joint_chain
	pm.parent(joint_chain, w=1)

	if pm.objExists(lt_arm_01_loc):
		pm.select(lt_arm_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'arm'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Arm doesn't exist")

	if pm.objExists(lt_clav_01_loc):
		pm.select(lt_clav_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'clav'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Clav doesn't exist")

	if pm.objExists(lt_eye_01_loc):
		pm.select(lt_eye_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'eye'
		count = 0
		suffix = 'Bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Eye doesn't exist")


	if pm.objExists(lt_hand_01_loc):
		pm.select(lt_hand_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'hand'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Hand doesn't exist")

	if pm.objExists(lt_index_01_loc):
		pm.select(lt_index_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'index'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Index Finger doesn't exist")

	if pm.objExists(lt_leg_01_loc):
		pm.select(lt_leg_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'leg'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
	else:
		pm.warning("Leg doesn't exist")
	

	if pm.objExists(lt_middle_01_loc):
		pm.select(lt_middle_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'middle'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Middle Finger doesn't exist")

	if pm.objExists(lt_pinky_01_loc):
		pm.select(lt_pinky_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'pinky'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Pinky Finger doesn't exist")

	if pm.objExists(lt_ring_01_loc):
		pm.select(lt_ring_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'ring'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Ring Finger doesn't exist")

	if pm.objExists(lt_thumb_01_loc):
		pm.select(lt_thumb_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		pivot_joint = joint_chain[0]
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'thumb'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		new_name = pivot_joint.replace('bind', 'pivot')
		pivot_joint.rename(new_name)



		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Thumb doesn't exist")

	if pm.objExists(lt_toeA_01_loc):
		pm.select(lt_toeA_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'toeA'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Toe A doesn't exist")

	if pm.objExists(lt_toeB_01_loc):
		pm.select(lt_toeB_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'toeB'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Toe B doesn't exist")
		

	if pm.objExists(lt_toeC_01_loc):
		pm.select(lt_toeC_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'toeC'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Toe C doesn't exist")


	if pm.objExists(lt_toeD_01_loc):
		pm.select(lt_toeD_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'toeD'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Toe D doesn't exist")


	if pm.objExists(lt_toeE_01_loc):
		pm.select(lt_toeE_01_loc)
		selection = pm.ls(sl=1, dag=1, type='transform')
		for each in selection:
			joints = pm.joint()
			temp_constraint = pm.parentConstraint(each, joints, mo=0)
			pm.delete(temp_constraint)
			freezeTransform()


		pm.select('joint1')
		joint_chain = pm.ls(sl=1, dag=1, type='transform')
		# print 'Joint chain', joint_chain
		ori = 'lt'
		system_name = 'toeE'
		count = 0
		suffix = 'bind'

		for current_joint in joint_chain:
			count = count + 1
			new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
			current_joint.rename(new_name)
			
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, 'waste')
		current_joint.rename(new_name)

		pm.select(joint_chain)
		joint_chain = pm.ls(sl=1)[0]
		# print joint_chain
		pm.parent(joint_chain, w=1)
	else:
		pm.warning("Toe E doesn't exist")
	
	pm.select('*01_bind')
	pm.joint(zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='yup')


	if pm.objExists(lt_hand_01_loc):
		pm.parent('lt_hand_01_bind', 'lt_arm_03_waste')
	if pm.objExists(lt_index_01_loc):
		pm.parent('lt_index_01_bind','lt_hand_02_waste')
		if pm.objExists(lt_middle_01_loc):
			pm.parent('lt_middle_01_bind','lt_hand_02_waste')
			if pm.objExists(lt_ring_01_loc):
				pm.parent('lt_ring_01_bind','lt_hand_02_waste')
				if pm.objExists(lt_pinky_01_loc):
					pm.parent('lt_pinky_01_bind','lt_hand_02_waste')
					if pm.objExists(lt_thumb_01_loc):
						pm.parent('lt_thumb_01_pivot','lt_hand_02_waste')

	if pm.objExists(lt_arm_01_loc):
		pm.parent('lt_arm_01_bind', 'lt_clav_02_waste')

	if pm.objExists(lt_toeA_01_loc):
		pm.parent('lt_toeA_01_bind','lt_leg_04_bind')
		if pm.objExists(lt_toeB_01_loc):
			pm.parent('lt_toeB_01_bind','lt_leg_04_bind')
			if pm.objExists(lt_toeC_01_loc):
				pm.parent('lt_toeC_01_bind', 'lt_leg_04_bind')
				if pm.objExists(lt_toeD_01_loc):
					pm.parent('lt_toeD_01_bind', 'lt_leg_04_bind')
					if pm.objExists(lt_toeE_01_loc):
						pm.parent('lt_toeE_01_bind', 'lt_leg_04_bind')

	if pm.objExists(lt_leg_01_loc):
		pm.parent('lt_leg_01_bind', 'ct_hip_01_bind')

	if pm.objExists(lt_clav_01_loc):
		pm.parent('lt_clav_01_bind', 'ct_back_06_bind')

	pm.parent('ct_back_01_bind', 'ct_hip_01_bind')
	pm.parent('ct_neck_01_bind', 'ct_back_07_waste')
	pm.parent('ct_head_01_bind', 'ct_neck_04_waste')
	pm.parent('lt_eye_01_Bind', 'ct_head_01_bind')
	pm.parent('ct_jaw_01_bind', 'ct_head_01_bind')
	pm.parent('ct_hip_01_bind', 'ct_root_waste')

	if pm.objExists(lt_clav_01_loc):	
		pm.select('lt_clav_01_bind')
		mirrorToolB()
		if pm.objExists(lt_leg_01_loc):	
			pm.select('lt_leg_01_bind')
			mirrorToolB()
			if pm.objExists(lt_eye_01_loc):
				pm.select('lt_eye_01_Bind')
				mirrorToolO()

	pm.select('ct_root_waste')
	joint_chain = pm.ls(sl=1, dag=1)
	print 'Joints:', joint_chain
	ct_root_waste = joint_chain[0]
	ct_hip_bind = joint_chain[1]
	lt_leg_01_bind = joint_chain[2]
	lt_toeA_01_bind = joint_chain[7]
	lt_toeB_01_bind = joint_chain[10] 
	lt_toeC_01_bind = joint_chain[13] 
	lt_toeD_01_bind = joint_chain[16] 
	lt_toeE_01_bind = joint_chain[19] 
	ct_back_01_bind = joint_chain[22]
	ct_neck_01_bind = joint_chain[29]
	ct_head_01_bind = joint_chain[33]
	lt_eye_01_bind = joint_chain[35]
	ct_jaw_01_bind = joint_chain[37]
	rt_eye_01_bind = joint_chain[39]
	lt_clav_01_bind = joint_chain[41]
	lt_arm_01_bind = joint_chain[43]
	lt_hand_01_bind = joint_chain[46]
	lt_index_01_bind = joint_chain[48]
	lt_middle_01_bind = joint_chain[53]
	lt_ring_01_bind = joint_chain[58]
	lt_pinky_01_bind = joint_chain[63]
	lt_thumb_01_pivot = joint_chain[68]
	rt_clav_01_bind = joint_chain[73]
	rt_arm_01_bind = joint_chain[75]
	rt_hand_01_bind = joint_chain[78]
	rt_index_01_bind = joint_chain[80]
	rt_middle_01_bind = joint_chain[85]
	rt_ring_01_bind = joint_chain[90]
	rt_pinky_01_bind = joint_chain[95]
	rt_thumb_01_pivot = joint_chain[100]
	rt_leg_01_bind = joint_chain[105]
	rt_toeA_01_bind = joint_chain[110]
	rt_toeB_01_bind = joint_chain[113] 
	rt_toeC_01_bind = joint_chain[116] 
	rt_toeD_01_bind = joint_chain[119] 
	rt_toeE_01_bind = joint_chain[122] 
	print 'Root Waste:', ct_root_waste
	print 'Hip Bind:', ct_hip_bind
	print 'Lt Leg Bind:', lt_leg_01_bind
	print 'Lt Toe A:', lt_toeA_01_bind
	print 'Lt Toe B:', lt_toeB_01_bind
	print 'Lt Toe C:', lt_toeC_01_bind
	print 'Lt Toe D:', lt_toeD_01_bind
	print 'Lt Toe E:', lt_toeE_01_bind
	print 'Back Bind:', ct_back_01_bind
	print 'Neck Bind:', ct_neck_01_bind
	print 'Head Bind:', ct_head_01_bind
	print 'Lt Eye Bind:', lt_eye_01_bind
	print 'Jaw Bind:', ct_jaw_01_bind
	print 'Rt Eye Bind:', rt_eye_01_bind
	print 'Lt Clav Bind:', lt_clav_01_bind
	print 'Lt Arm Bind:', lt_arm_01_bind
	print 'Lt Hand Bind:', lt_hand_01_bind
	print 'Lt Index Bind:', lt_index_01_bind
	print 'Lt Middle Bind:', lt_middle_01_bind
	print 'Lt Pinky Bind:', lt_pinky_01_bind
	print 'Lt Ring Bind:', lt_ring_01_bind
	print 'Lt Thumb Pivot:', lt_thumb_01_pivot
	print 'Rt Clav Bind:', rt_clav_01_bind
	print 'Rt Arm Bind:', rt_arm_01_bind
	print 'Rt Hand Bind:', rt_hand_01_bind
	print 'Rt Index Bind:', rt_index_01_bind
	print 'Rt Middle Bind:', rt_middle_01_bind
	print 'Rt Ring Bind:', rt_ring_01_bind
	print 'Rt Pinky Bind:', rt_pinky_01_bind
	print 'Rt Thumb Pivot:', rt_thumb_01_pivot
	print 'Rt Leg Bind:', rt_leg_01_bind
	print 'Rt Toe A:', rt_toeA_01_bind
	print 'Rt Toe B:', rt_toeB_01_bind
	print 'Rt Toe C:', rt_toeC_01_bind
	print 'Rt Toe D:', rt_toeD_01_bind
	print 'Rt Toe E:', rt_toeE_01_bind




	if pm.objExists(lt_clav_01_bind):
		pm.parent(lt_index_01_bind, lt_middle_01_bind, lt_ring_01_bind, lt_pinky_01_bind, lt_thumb_01_pivot,
			  	  rt_index_01_bind, rt_middle_01_bind, rt_ring_01_bind, rt_pinky_01_bind, rt_thumb_01_pivot, 
			 	  lt_arm_01_bind, rt_arm_01_bind, lt_clav_01_bind, lt_hand_01_bind, rt_clav_01_bind, rt_hand_01_bind,
			 	  ct_head_01_bind, ct_neck_01_bind, ct_hip_bind, ct_back_01_bind, w=1)
		if pm.objExists(lt_leg_01_bind):
			pm.parent(lt_toeA_01_bind, lt_toeB_01_bind, lt_toeC_01_bind, lt_toeD_01_bind, lt_toeE_01_bind,
					  rt_toeA_01_bind, rt_toeB_01_bind, rt_toeC_01_bind, rt_toeD_01_bind, rt_toeE_01_bind,
						  lt_leg_01_bind, rt_leg_01_bind, w=1)


	pm.delete('biped_fitSkeleton_crv')

def autoBuild(*args):
	headSetup()
	eyeSetup()
	jawSetup()
	neckSetup()
	shoulderSystem()
	armSystem()
	handSystem()
	backSetup()
	hipSetup()
	legSetup()
	rflPrep()
	rflSetup()
	pm.select(cl=1)

	print 'Biped Auto-Rig Finished'

def headSetup(*args):
	global head_root, head_joint_2, head_icon, head_pad
	pm.select(ct_head_01_bind)
	selection = pm.ls(sl=1, dag=1)
	head_root = selection[0]
	head_joint_2 = selection[1]


	head_pad = pm.group(empty=1)
	temp_comnstraint = pm.parentConstraint(head_root, head_pad, mo=0)
	pm.delete(temp_comnstraint)
	freezeTransform(head_pad)

	pad_name = head_root.replace('01_bind', '00_pad')
	head_pad.rename(pad_name)
	pm.parent(head_root, head_pad)

	head_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=16, r=8, tol=0.01, nr=(1, 0, 0))[0]

	pm.select('nurbsCircle1.cv[10]',
		  'nurbsCircle1.cv[12]',
		  'nurbsCircle1.cv[14]',
		  'nurbsCircle1.cv[0]',
		  'nurbsCircle1.cv[2]', 
		  'nurbsCircle1.cv[4]', 
		  'nurbsCircle1.cv[6]', 
		  'nurbsCircle1.cv[8]')
	cmds.move(-4, 0, 0, r=1, os=1, wd=1)

	pm.select(head_icon)
	centerPivot()

	temp_constraint = pm.parentConstraint(head_root, head_icon, mo=0)
	pm.delete(temp_constraint)
	temp_constraint = pm.pointConstraint(head_joint_2, head_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()
	bind_pivots = head_root.getTranslation(ws=1)
	# print bind_pivots
	head_icon.setPivots(bind_pivots)

	icon_name = head_root.replace('01_bind', 'icon')
	head_icon.rename(icon_name)

	pm.parentConstraint(head_icon, head_pad, mo=0)

	head_icon.overrideEnabled.set(1)
	head_icon.overrideColor.set(yellow)

	pm.select(head_icon)
	freezeTransform()

def eyeSetup(*args):
	global lt_eye_root, lt_eye_joint_2, rt_eye_root, rt_eye_joint_2, ct_eye_icon, lt_eye_icon, rt_eye_icon, eye_local
	pm.select(lt_eye_01_bind, rt_leg_01_bind)
	selection = pm.ls(sl=1)
	lt_eye_joints = selection[0]
	rt_eye_joints = selection[1]
	

	lt_eye = pm.ls(lt_eye_joints, sl=1, dag=1)
	lt_eye_root = lt_eye[0]
	lt_eye_joint_2 = lt_eye[1]


	rt_eye = pm.ls(rt_eye_joints, sl=1, dag=1)
	rt_eye_root = rt_eye[0]
	rt_eye_joint_2  = rt_eye[1]

	ct_eye_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]

	rt_eye_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]

	lt_eye_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]

	icon_name = lt_eye_root.replace('01_bind', 'icon')
	lt_eye_icon.rename(icon_name)
	icon_name = rt_eye_root.replace('01_bind', 'icon')
	rt_eye_icon.rename(icon_name)
	icon_name = lt_eye_icon.replace('lt', 'ct')
	ct_eye_icon.rename(icon_name)

	pm.xform(ct_eye_icon, s=[5.8, 5.8, 5.8])
	pm.select(ct_eye_icon)
	freezeTransform()


	pm.select(ct_eye_icon + '.cv[5]',
			  ct_eye_icon + '.cv[1]')
	pm.cmds.scale(1, 1, 0.05, p=(0, 0, 0), r=1)

	pm.select(ct_eye_icon, lt_eye_icon, rt_eye_icon)
	icon_selection = pm.ls(sl=1)
	for each in icon_selection:
		pm.setAttr(each + '.overrideEnabled', 1)
	
	ct_eye_icon.overrideColor.set(yellow)

	rt_eye_icon.overrideColor.set(red)

	lt_eye_icon.overrideColor.set(blue)

	pm.xform(lt_eye_icon, t=[3.5, 0 , 0], s=[2.03, 2.03, 2.03])

	pm.xform(rt_eye_icon, t=[-3.5, 0 , 0], s=[2.03, 2.03, 2.03])

	pm.select(lt_eye_icon, rt_eye_icon)
	freezeTransform()

	pm.parent(lt_eye_icon, rt_eye_icon, ct_eye_icon)

	ct_eye_icon.rx.set(90)
	pm.select(ct_eye_icon)
	freezeTransform()
	pm.addAttr(ct_eye_icon, ln="followHead", at='bool')
	ct_eye_icon.followHead.set(e=1, keyable=1)

	ct_eye_icon.tz.set(20)
	freezeTransform()

	temp_constraint = pm.pointConstraint(lt_eye_01_bind, rt_eye_01_bind, ct_eye_icon, skip=['z'], w=1, mo=0)
	pm.delete(temp_constraint)
	pm.select(ct_eye_icon)
	freezeTransform()

	pm.aimConstraint(lt_eye_icon, lt_eye_01_bind, mo=0)

	pm.aimConstraint(rt_eye_icon, rt_eye_01_bind, mo=0)


	eye_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(ct_eye_icon, eye_local, mo=0)
	pm.delete(temp_constraint)
	pm.select(eye_local)
	freezeTransform()

	local_name = ct_eye_icon.replace('icon', 'eye_local')
	eye_local.rename(local_name)

	pm.parent(ct_eye_icon, eye_local)

	follow_const = pm.parentConstraint(ct_head_01_bind, eye_local, mo=1, w=0)
	print 'Follow constraint:', follow_const
	const_targets = follow_const.getWeightAliasList()[0]

	pm.setDrivenKeyframe(const_targets, currentDriver=ct_eye_icon + '.followHead')
	ct_eye_icon.followHead.set(1)
	const_targets.set(1)
	pm.setDrivenKeyframe(const_targets, currentDriver=ct_eye_icon + '.followHead')
	ct_eye_icon.followHead.set(0)
	
	pm.select(eye_local)
	deleteHistory()
	
def jawSetup(*args):
	global jaw_root, jaw_icon, jaw_local
	pm.select(ct_jaw_01_bind)
	selection = pm.ls(sl=1)
	jaw_root = selection[0]
	

	jaw_icon = pm.curve(p=[(-3, 0, -2), (-1, 0, -2), (-1, 0, -2), (-1, 0, -2), (0, 0, -1), (1, 0, -2), (1, 0, -2), (1, 0, -2), (3, 0, -2), (3, 0, -2), (3, 0, -2), (3, 0, -2), (1, 0, 0), (0, 0, 2), (0, 0, 2), (0, 0, 2), (0, 0, 2), (-1, 0, 0), (-3, 0, -2)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 16], d=3)
	pm.select('curve1.cv[1]',
			  'curve1.cv[2]', 
			  'curve1.cv[3]', 
			  'curve1.cv[5]',
			  'curve1.cv[6]', 
			  'curve1.cv[7]')
	pm.cmds.scale(2, 1, 1, p=(0, 0, -2), r=1)


	pm.xform(jaw_icon + '.cv[4]', t=(0, .5, .5))

	pm.xform(jaw_icon + '.cv[12]', t=(.5, .5, 0))

	pm.xform(jaw_icon + '.cv[17]', t=(-.5, .5, 0))

	pm.select(jaw_icon)
	centerPivot()
	deleteHistory()


	jaw_icon.ry.set(90)
	freezeTransform()
	temp_constraint = pm.parentConstraint(jaw_root, jaw_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()
	jaw_icon.rx.set(90)
	freezeTransform()
	jaw_icon.tz.set(20)
	freezeTransform()

	jaw_local = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(jaw_root, jaw_local, mo=0)
	pm.delete(temp_constraint)

	jaw_icon.ty.set(-2)
	pm.select(jaw_icon)
	freezeTransform()

	pm.parent(jaw_icon, jaw_local)
	
	bind_pivots = jaw_root.getTranslation(ws=1)
	# print bind_pivots
	jaw_icon.setPivots(bind_pivots)

	pm.select(jaw_icon)
	freezeTransform()

	icon_name = jaw_root.replace('01_bind', 'icon')
	jaw_icon.rename(icon_name)

	pad_name = jaw_icon.replace('icon', 'local')
	jaw_local.rename(pad_name)

	pm.parentConstraint(jaw_icon, jaw_root, mo=1)

	pm.parent(jaw_local, head_icon)

	jaw_icon.overrideEnabled.set(1)
	jaw_icon.overrideColor.set(cyan)

def neckSetup(*args):
	global neck_root, neck_joint_1, neck_joint_3, neck_joint_4, neck_pad, head_loc, neck_ik_icon, neck_fk_icon
	pm.select(ct_neck_01_bind)
	joint_system = pm.ls(sl=True, dag=True)
	neck_root  = joint_system[0]
	neck_joint_2 = joint_system[1]
	neck_joint_3= joint_system[2]
	neck_joint_4 = joint_system[3]
	# print 'Root joint:', neck_root
	# print 'Joint 2:', neck_joint_2
	# print 'Joint 3', neck_joint_3
	# print 'Joint 4:', neck_joint_4
	neck_joint_4.jointOrientX.set(0)
	neck_joint_4.jointOrientY.set(0)	
	joints = joint_positions(neck_root) 
	neck_curve = pm.curve(d = 1, p=joints)

	neck_joint_4.jointOrientX.set(0)

	neck_pad = pm.group(empty=True)

	# Move group to joint.
	# 	and delete constraint
	temp_constraint = pm.pointConstraint(neck_root, neck_pad)
	pm.delete(temp_constraint)

	# Freeze Transformation on the group.
	pm.makeIdentity(neck_pad, apply=True, t=1, r=1, s=1, n=0)
	# Parent joint to group
	pm.parent(neck_root, neck_pad)

	# renaming
	# ct_tail_01_bind
	# ct_tail_00_pad
	pad_name = neck_root.replace('01_bind', '00_pad')
	neck_pad.rename(pad_name)

	print 'Padding group created.'

	curve_name = neck_root.replace('01_bind', 'crv')
	neck_curve.rename(curve_name)

	ik_jointChain = pm.duplicate(neck_root)
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


	fk_jointChain = pm.duplicate(neck_root)
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
	neck_ikh= pm.ikHandle(sol='ikSplineSolver', ccv=False, pcv=False)[0]

	ik_name = neck_curve.replace('crv', 'ikh')
	neck_ikh.rename(ik_name)

	'''
	Create the curveBind joints
	'''

	bind_dup = pm.duplicate(neck_root)

	pm.select(bind_dup)

	curveBind = pm.ls(sl=True, dag=True)
	cb_joint_1 = curveBind[0]
	cb_joint_2 = curveBind[3]
	cb_joint_3 = curveBind[1]


	pm.parent(cb_joint_2, w=1)
	pm.delete(cb_joint_3)

	joint_name = neck_root.replace('b', 'curveB')
	cb_joint_1.rename(joint_name)

	joint_name = cb_joint_1.replace('01', '02')
	cb_joint_2.rename(joint_name)

	pm.select(cb_joint_1, cb_joint_2,neck_curve)
	pm.mel.SmoothBindSkin()

	neck_ikh.dTwistControlEnable.set(1)
	neck_ikh.dWorldUpType.set(4)

	neck_ikh.dForwardAxis.set(0)
	neck_ikh.dWorldUpAxis.set(1)


	'''
	Create the ik and fk curve
	'''

	neck_ik_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]

	temp_constraint = pm.parentConstraint(ik_joint_4, neck_ik_icon)
	pm.delete(temp_constraint)
	freezeTransform(neck_ik_icon)
	deleteHistory(neck_ik_icon)

	curve_name = neck_ikh.replace('h', '_icon')
	neck_ik_icon.rename(curve_name)

	pm.parentConstraint(neck_ik_icon, cb_joint_2, mo=1)



	neck_fk_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	temp_constraint = pm.parentConstraint(fk_root_joint, neck_fk_icon)
	pm.delete(temp_constraint)
	freezeTransform(neck_fk_icon)
	deleteHistory(neck_fk_icon)

	curve_name = neck_ik_icon.replace('ik', 'fk')
	neck_fk_icon.rename(curve_name)

	pm.parentConstraint(neck_fk_icon, fk_root_joint, mo=1)

	attrs = ['tx', 'ty','tz', 'sx', 'sy', 'sz']

	for current_attr in attrs:
		attr = neck_fk_icon.attr(current_attr)
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
		# print 'shape 1:', cShape_1
		# print 'shape 2:', cShape_2
		# print 'shape 3:', cShape_3

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
	temp_constraint = pm.parentConstraint(neck_ik_icon, ik_local)
	pm.delete(temp_constraint)

	pm.parent(neck_ik_icon, ik_local)
	freezeTransform(neck_ik_icon)
	local_name = neck_ik_icon.replace('icon', 'local')
	ik_local.rename(local_name)


	pm.parentConstraint(neck_fk_icon, ik_local, mo=1)


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


	pm.parentConstraint(ik_root, neck_root)
	pm.parentConstraint(ik_joint_2, neck_joint_2)
	pm.parentConstraint(ik_joint_3, neck_joint_3)

	global_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(neck_root, global_grp)
	pm.delete(temp_constraint)
	freezeTransform(global_grp)

	pm.parent(neck_curve, neck_ikh, cb_joint_1, cb_joint_2, neck_fk_icon, ik_local, global_grp)

	group_name = neck_root.replace('01_bind', 'global_grp')
	global_grp.rename(group_name)

	pm.parent(global_grp, moveAll)

	neck_curve.inheritsTransform.set(0)

	pm.parentConstraint(moveAll, neck_pad, mo=1)


	attrs = ['sx', 'sy', 'sz']

	for current_attr in attrs:
		attr = neck_ik_icon.attr(current_attr)
		attr.set(lock=1, keyable=0, channelBox=0)


	'''
	Space Switch
	'''

	'''
	Head
	'''

	head_loc = pm.spaceLocator(p=(0, 0, 0))

	loc_name = neck_joint_4.replace('neck_04_waste', 'headNeck_space_loc')
	head_loc.rename(loc_name)

	temp_constraint = pm.parentConstraint(neck_joint_4, head_loc, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(head_loc)

	pm.select(neck_ikh, fk_root_joint, ik_root, head_loc, neck_curve)
	selection = pm.ls(sl=1)

	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	pm.parent(head_icon, neck_ik_icon)

def lt_shoulderSetup(*args):
	global clav_root, clav_joint_2, arm_root, arm_joint_2, arm_joint_3, shoulder_icon, clav_space_loc
	pm.select(lt_clav_01_bind, lt_arm_01_bind)
	joint_system = pm.ls(sl=1)
	clav_system = joint_system[0]
	arm_system = joint_system[1] 

	clav_joints = pm.ls(clav_system, sl=1, dag=1)
	clav_root = clav_joints[0]
	clav_joint_2 = clav_joints[1]
	print 'Clav root joint:', clav_root
	print 'Clav waste joint:', clav_joint_2

	armJoints = pm.ls(arm_system, sl=1, dag=1)
	arm_root = armJoints[0]
	arm_joint_2 = armJoints[1]
	arm_joint_3 = armJoints[2]
	print 'Arm root joint:', arm_root
	print 'Arm joint 2:', arm_joint_2
	print 'Arm joint 3:', arm_joint_3

	pm.select(clav_root, clav_joint_2)
	ikh = pm.ikHandle(sol='ikSCsolver')[0]

	ik_name = clav_root.replace('bind', 'ikh')
	ikh.rename(ik_name)

	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(arm_root, loc_1, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_1)

	loc_name = ikh.replace('ikh', 'loc')
	loc_1.rename(loc_name)
	pm.parent(ikh, loc_1)

	loc_2 =	pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(clav_root, loc_2, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_2)
	loc_name = loc_1.replace('loc', 'startLoc')
	loc_2.rename(loc_name)

	loc_3 =	pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(clav_joint_2, loc_3, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_3)
	loc_name = loc_2.replace('start', 'end')
	loc_3.rename(loc_name)

	clav_dist = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.select(clav_dist)
	selection = pm.ls(sl=1, s=0)
	shape = selection[0]
	pm.pickWalk(d='up')
	transform = pm.ls(sl=1)[0]

	node_name = loc_1.replace('loc', 'dist')
	transform.rename(node_name)
	temp_constraint = pm.parentConstraint(clav_root, transform, mo=0)
	pm.delete(temp_constraint)

	pm.connectAttr(loc_2 + '.worldPosition', clav_dist + '.startPoint')
	pm.connectAttr(loc_3 + '.worldPosition', clav_dist + '.endPoint')

	pm.parent(loc_3, loc_1)

	driver = clav_dist + '.distance'
	length = pm.getAttr(clav_joint_2 + '.tx')


	pm.setDrivenKeyframe(clav_joint_2 + '.tx', currentDriver=driver, driverValue=length, value=length)

	pm.setDrivenKeyframe(clav_joint_2 + '.tx', currentDriver=driver, driverValue=(2 * length), value=(2 * length))
	pm.keyTangent(clav_joint_2, itt='clamped', ott='clamped')
	pm.setInfinity(clav_joint_2, poi='linear')

	shoulder_icon = pm.curve(d=1, p=[(0, 1.003235, 0),(0.668823, 0, 0),(0.334412, 0, 0),(0.334412, -0.167206, 0),(0.334412, -0.501617, 0),(0.334412, -1.003235, 0),(-0.334412, -1.003235, 0),(-0.334412, -0.501617, 0),(-0.334412, -0.167206, 0),(-0.334412, 0, 0),(-0.668823, 0, 0),(0, 1.003235, 0),(0, 0, -0.668823),(0, 0, -0.334412),(0, -0.167206, -0.334412),(0, -0.501617, -0.334412),(0, -1.003235, -0.334412),(0, -1.003235, 0.334412),(0, -0.501617, 0.334412),(0, -0.167206, 0.334412),(0, 0, 0.334412),(0, 0, 0.668823),(0, 1.003235, 0)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
	shoulder_icon.rx.set(180)
	temp_constraint = pm.pointConstraint(clav_joint_2, shoulder_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(shoulder_icon)
	shoulder_icon.ty.set(3)
	freezeTransform(shoulder_icon)

	icon_name = clav_root.replace('clav_01_bind', 'shoulder_icon')
	shoulder_icon.rename(icon_name)
	pm.parent(loc_1, shoulder_icon)

	dnt_grp = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(clav_root, dnt_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(dnt_grp)

	grp_name = clav_root.replace('01_bind', 'DO____NOT____TOUCH_grp')
	dnt_grp.rename(grp_name)

	pm.parent(transform, loc_2, dnt_grp)

	global_grp = pm.group(empty=1)
	temp_constraint = pm.pointConstraint(clav_root, global_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(global_grp)

	grp_name = clav_root.replace('01_bind', 'global_grp')
	global_grp.rename(grp_name)

	pad = pm.group(empty=1)
	temp_constraint= pm.pointConstraint(clav_root, pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(pad)

	pad_name = clav_root.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	pm.parent(clav_root, pad)

	pm.parent(pad, dnt_grp, shoulder_icon, global_grp)


	dnt_grp.overrideEnabled.set(1)
	dnt_grp.overrideDisplayType.set(2)
	dnt_grp.v.set(0)
	loc_1.v.set(0)
	loc_2.v.set(0)
	loc_3.v.set(0)

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

		shapes = pm.ls(sl=1, dag=1)
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


		moveAll = pm.group(empty=1, n='ct_moveAll')

		pm.parent(cShape_1, cShape_2, cShape_3, moveAll, s=1, r=1)

		pm.delete(moveAll_circle, xAxis, zAxis)

	if pm.objExists('*joint_grp'):
		pm.select('*joint_grp')
		jnt_grp = pm.ls(sl=1)[0]
		print jnt_grp
		# pm.parent(pad, jnt_grp)
		pm.scaleConstraint(moveAll, jnt_grp)

	else:
		jnt_grp = pm.group(empty=1)
		grp_name = clav_root.replace('lt_clav_01_bind', 'joint_grp')
		jnt_grp.rename(grp_name)
		print jnt_grp
		# pm.parent(pad, jnt_grp)
		pm.scaleConstraint(moveAll, jnt_grp)

	if pm.objExists('*icon_grp'):
		pm.select('*icon_grp')
		icon_grp = pm.ls(sl=1)[0] 
		pm.parent(moveAll, icon_grp)
		# pm.parent(shoulder_icon, moveAll)

	else:
		icon_grp = pm.group(empty=1)
		pm.parent(moveAll, icon_grp)
		group_name = jnt_grp.replace('joint', 'icon')
		icon_grp.rename(group_name)
		# pm.parent(shoulder_icon, moveAll)

	clav_space_loc = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(clav_joint_2, clav_space_loc)
	pm.delete(temp_constraint)
	freezeTransform(clav_space_loc)

	loc_name = shoulder_icon.replace('_icon', '_space_loc')
	clav_space_loc.rename(loc_name)

	pm.parent(clav_space_loc, clav_joint_2)
	freezeTransform(clav_space_loc)

def rt_shoulderSetup(*args):
	global clav_root, clav_joint_2, arm_root, arm_joint_2, arm_joint_3, shoulder_icon, clav_space_loc
	pm.select(rt_clav_01_bind, rt_arm_01_bind)
	joint_system = pm.ls(sl=1)
	clav_system = joint_system[0]
	arm_system = joint_system[1] 

	clav_joints = pm.ls(clav_system, sl=1, dag=1)
	clav_root = clav_joints[0]
	clav_joint_2 = clav_joints[1]
	print 'Clav root joint:', clav_root
	print 'Clav waste joint:', clav_joint_2

	armJoints = pm.ls(arm_system, sl=1, dag=1)
	arm_root = armJoints[0]
	arm_joint_2 = armJoints[1]
	arm_joint_3 = armJoints[2]
	print 'Arm root joint:', arm_root
	print 'Arm joint 2:', arm_joint_2
	print 'Arm joint 3:', arm_joint_3

	pm.select(clav_root, clav_joint_2)
	ikh = pm.ikHandle(sol='ikSCsolver')[0]

	ik_name = clav_root.replace('bind', 'ikh')
	ikh.rename(ik_name)

	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(arm_root, loc_1, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_1)

	loc_name = ikh.replace('ikh', 'loc')
	loc_1.rename(loc_name)
	pm.parent(ikh, loc_1)

	loc_2 =	pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(clav_root, loc_2, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_2)
	loc_name = loc_1.replace('loc', 'startLoc')
	loc_2.rename(loc_name)

	loc_3 =	pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(clav_joint_2, loc_3, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_3)
	loc_name = loc_2.replace('start', 'end')
	loc_3.rename(loc_name)

	clav_dist = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.select(clav_dist)
	selection = pm.ls(sl=1, s=0)
	shape = selection[0]
	pm.pickWalk(d='up')
	transform = pm.ls(sl=1)[0]

	node_name = loc_1.replace('loc', 'dist')
	transform.rename(node_name)
	temp_constraint = pm.parentConstraint(clav_root, transform, mo=0)
	pm.delete(temp_constraint)

	pm.connectAttr(loc_2 + '.worldPosition', clav_dist + '.startPoint')
	pm.connectAttr(loc_3 + '.worldPosition', clav_dist + '.endPoint')

	pm.parent(loc_3, loc_1)

	driver = clav_dist + '.distance'
	length = pm.getAttr(clav_joint_2 + '.tx')


	pm.setDrivenKeyframe(clav_joint_2 + '.tx', currentDriver=driver, driverValue=length, value=length)

	pm.setDrivenKeyframe(clav_joint_2 + '.tx', currentDriver=driver, driverValue=(2 * length), value=(2 * length))
	pm.keyTangent(clav_joint_2, itt='clamped', ott='clamped')
	pm.setInfinity(clav_joint_2, poi='linear')

	shoulder_icon = pm.curve(d=1, p=[(0, 1.003235, 0),(0.668823, 0, 0),(0.334412, 0, 0),(0.334412, -0.167206, 0),(0.334412, -0.501617, 0),(0.334412, -1.003235, 0),(-0.334412, -1.003235, 0),(-0.334412, -0.501617, 0),(-0.334412, -0.167206, 0),(-0.334412, 0, 0),(-0.668823, 0, 0),(0, 1.003235, 0),(0, 0, -0.668823),(0, 0, -0.334412),(0, -0.167206, -0.334412),(0, -0.501617, -0.334412),(0, -1.003235, -0.334412),(0, -1.003235, 0.334412),(0, -0.501617, 0.334412),(0, -0.167206, 0.334412),(0, 0, 0.334412),(0, 0, 0.668823),(0, 1.003235, 0)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
	shoulder_icon.rx.set(180)
	temp_constraint = pm.pointConstraint(clav_joint_2, shoulder_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(shoulder_icon)
	shoulder_icon.ty.set(3)
	freezeTransform(shoulder_icon)

	icon_name = clav_root.replace('clav_01_bind', 'shoulder_icon')
	shoulder_icon.rename(icon_name)
	pm.parent(loc_1, shoulder_icon)

	dnt_grp = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(clav_root, dnt_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(dnt_grp)

	grp_name = clav_root.replace('01_bind', 'DO____NOT____TOUCH_grp')
	dnt_grp.rename(grp_name)

	pm.parent(transform, loc_2, dnt_grp)

	global_grp = pm.group(empty=1)
	temp_constraint = pm.pointConstraint(clav_root, global_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(global_grp)

	grp_name = clav_root.replace('01_bind', 'global_grp')
	global_grp.rename(grp_name)

	pad = pm.group(empty=1)
	temp_constraint= pm.pointConstraint(clav_root, pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(pad)

	pad_name = clav_root.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	pm.parent(clav_root, pad)

	pm.parent(pad, dnt_grp, shoulder_icon, global_grp)


	dnt_grp.overrideEnabled.set(1)
	dnt_grp.overrideDisplayType.set(2)
	dnt_grp.v.set(0)
	loc_1.v.set(0)
	loc_2.v.set(0)
	loc_3.v.set(0)

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

		shapes = pm.ls(sl=1, dag=1)
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


		moveAll = pm.group(empty=1, n='ct_moveAll')

		pm.parent(cShape_1, cShape_2, cShape_3, moveAll, s=1, r=1)

		pm.delete(moveAll_circle, xAxis, zAxis)

	if pm.objExists('*joint_grp'):
		pm.select('*joint_grp')
		jnt_grp = pm.ls(sl=1)[0]
		print jnt_grp
		# pm.parent(pad, jnt_grp)
		pm.scaleConstraint(moveAll, jnt_grp)

	else:
		jnt_grp = pm.group(empty=1)
		grp_name = clav_root.replace('rt_clav_01_bind', 'joint_grp')
		jnt_grp.rename(grp_name)
		print jnt_grp
		# pm.parent(pad, jnt_grp)
		pm.scaleConstraint(moveAll, jnt_grp)

	if pm.objExists('*icon_grp'):
		pm.select('*icon_grp')
		icon_grp = pm.ls(sl=1)[0] 
		pm.parent(moveAll, icon_grp)
		# pm.parent(shoulder_icon, moveAll)

	else:
		icon_grp = pm.group(empty=1)
		pm.parent(moveAll, icon_grp)
		group_name = jnt_grp.replace('joint', 'icon')
		icon_grp.rename(group_name)
		# pm.parent(shoulder_icon, moveAll)

	clav_space_loc = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(clav_joint_2, clav_space_loc)
	pm.delete(temp_constraint)
	freezeTransform(clav_space_loc)

	loc_name = shoulder_icon.replace('_icon', '_space_loc')
	clav_space_loc.rename(loc_name)

	pm.parent(clav_space_loc, clav_joint_2)
	freezeTransform(clav_space_loc)

def shoulderSetup(*args):
	lt_shoulderSetup()
	rt_shoulderSetup()

def shoulderSystem(*args):
	ori_selection_type = pm.radioButtonGrp('shoulder_orientationOption', q=1, sl=1) 
	# print 'Orientation Selection:', ori_selection_type

	if ori_selection_type == 1:
		lt_shoulderSetup()
	if ori_selection_type == 2:
		rt_shoulderSetup()
	if ori_selection_type == 3:
		shoulderSetup()

def lt_armSetup(*args):
	global lt_arm_root, lt_fk_root, lt_ik_root, lt_joint_12, lt_arm_icon
	pm.select(lt_arm_01_bind)
	arm_system = pm.ls(sl=True, dag=True)
	lt_arm_root = arm_system[0]
	arm_joint_2 = arm_system[1]
	arm_joint_3 = arm_system[2]
	# print 'Main Root:', lt_arm_root
	# print 'Main Joint 2:', arm_joint_2
	# print 'Main Joint 3:', arm_joint_3

	pm.joint(lt_arm_root, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	arm_joint_3.jointOrientX.set(0)
	arm_joint_3.jointOrientY.set(0)
	lt_arm_root.rotateOrder.set(3)


	ik_joints = pm.duplicate(lt_arm_root)
	ik_joints = pm.ls(sl=True, dag=True)
	lt_ik_root = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	# print 'Ik Root:', lt_ik_root
	# print 'Ik Joint 2:', ik_joint_2
	# print 'Ik Joint 3:', ik_joint_3

	
	for each in ik_joints:
		joint_name = lt_arm_root.replace('bind', 'ik')
		lt_ik_root.rename(joint_name)

	joint_name = lt_ik_root.replace('1', '2')
	ik_joint_2.rename(joint_name)

	joint_name = ik_joint_2.replace('2', '3')
	ik_joint_3.rename(joint_name)

	fk_joints = pm.duplicate(lt_arm_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=True, dag=True)
	lt_fk_root = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	# print 'Fk Root:', lt_fk_root
	# print 'Fk Joint 2:', fk_joint_2
	# print 'Fk Joint 3:', fk_joint_3

	
	joint_name = lt_ik_root.replace('ik', 'fk')
	lt_fk_root.rename(joint_name)

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
	


	twist_joints = pm.duplicate(lt_arm_root)
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
	lt_joint_12 = twist_joints[1]

	pm.delete(end_joint)

	jnt_name_12 = lt_joint_12.replace('07', '12')
	lt_joint_12.rename(jnt_name_12)
	jnt_name_7 = joint_7.replace('06_twist1', '07_twist')
	joint_7.rename(jnt_name_7)

	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_1 = pm.pointConstraint(joint_7, loc_1, mo=0, w=0)
	point_constraint_2 = pm.pointConstraint(lt_joint_12, loc_1, mo=0, w=1)
	jnt_name_11 = lt_joint_12.replace('12', '11')
	joint_11 = pm.joint(loc_1, name=jnt_name_11)

	loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_1 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_3 = pm.pointConstraint(joint_7 , loc_2, mo=0, w=.25)
	point_constraint_4 = pm.pointConstraint(lt_joint_12 , loc_2, mo=0, w=.75)
	jnt_name_10 = joint_11.replace('11', '10')
	joint_10 = pm.joint(loc_2, n=jnt_name_10)

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_2 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_5 = pm.pointConstraint(joint_7 ,loc_3, mo=0, w=.5)
	point_constraint_6 = pm.pointConstraint(lt_joint_12 ,loc_3, mo=0, w=.5)
	jnt_name_9 = joint_10.replace('10', '09')
	joint_9 = pm.joint(loc_3, n=jnt_name_9)

	loc_4 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_3 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_7 = pm.pointConstraint(joint_7 ,loc_4, mo=0, w=.75)
	point_constraint_8 = pm.pointConstraint(lt_joint_12 ,loc_4, mo=0, w=.25)
	jnt_name_8 = joint_9.replace('9', '8')
	joint_8 = pm.joint(loc_4, n=jnt_name_8)

	pm.parent(joint_11, joint_10)
	pm.parent(joint_10, joint_9)
	pm.parent(joint_9, joint_8)
	pm.parent(joint_8, joint_7)

	pm.delete(loc_1, loc_2, loc_3, loc_4)

	pm.parent(lt_joint_12, joint_11)


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

	cb_joint_3 = pm.duplicate(lt_joint_12)[0]

	bind_name = cb_joint_2.replace('2', '3')
	cb_joint_3.rename(bind_name)

	pm.parent(cb_joint_3, w=1)

	tempBind = pm.duplicate(lt_arm_root)

	pm.select(tempBind)
	temp_joints = pm.ls(sl=True, dag=True)
	temp_1 = temp_joints[0]
	temp_2 = temp_joints[1]
	temp_3 = temp_joints[2]

	temp_name = lt_arm_root.replace('bind', 'temp')
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

	pm.select(end_joint, lt_joint_12, arm_curve_2)
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

	pm.parentConstraint(arm_joint_3, cb_joint_3, mo=1)
	pm.parentConstraint(arm_joint_2, cb_joint_2, mo=1)
	pm.pointConstraint(lt_arm_root, cb_joint_1, mo=1)


	'''================================================================================================================'''
	root_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = lt_arm_root.replace('bind', 'rot_ikfk_blend')
	root_rot_ikfk.rename(node_name)

	pm.connectAttr(lt_ik_root + '.rotate', root_rot_ikfk + '.color2')
	pm.connectAttr(lt_fk_root + '.rotate', root_rot_ikfk + '.color1')
	pm.connectAttr(root_rot_ikfk + '.output', lt_arm_root + '.rotate')

	arm_joint_2_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_rot_ikfk.replace('1', '2')
	arm_joint_2_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_2 + '.rotate', arm_joint_2_rot_ikfk + '.color2')
	pm.connectAttr(fk_joint_2 + '.rotate', arm_joint_2_rot_ikfk + '.color1')
	pm.connectAttr(arm_joint_2_rot_ikfk + '.output', arm_joint_2 + '.rotate')

	arm_joint_3_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_rot_ikfk.replace('1', '3')
	arm_joint_3_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_3 + '.rotate', arm_joint_3_rot_ikfk + '.color2')
	pm.connectAttr(fk_joint_3 + '.rotate', arm_joint_3_rot_ikfk + '.color1')
	pm.connectAttr(arm_joint_3_rot_ikfk + '.output', arm_joint_3 + '.rotate')

	root_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = lt_arm_root.replace('bind', 'trans_ikfk_blend')
	root_trans_ikfk.rename(node_name)

	pm.connectAttr(lt_ik_root + '.translate', root_trans_ikfk + '.color2')
	pm.connectAttr(lt_fk_root + '.translate', root_trans_ikfk + '.color1')
	pm.connectAttr(root_trans_ikfk + '.output', lt_arm_root + '.translate')

	arm_joint_2_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_trans_ikfk.replace('1', '2')
	arm_joint_2_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_2 + '.translate', arm_joint_2_trans_ikfk + '.color2')
	pm.connectAttr(fk_joint_2 + '.translate', arm_joint_2_trans_ikfk + '.color1')
	pm.connectAttr(arm_joint_2_trans_ikfk + '.output', arm_joint_2 + '.translate')

	arm_joint_3_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_trans_ikfk.replace('1', '3')
	arm_joint_3_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_3 + '.translate', arm_joint_3_trans_ikfk + '.color2')
	pm.connectAttr(fk_joint_3 + '.translate', arm_joint_3_trans_ikfk + '.color1')
	pm.connectAttr(arm_joint_3_trans_ikfk + '.output', arm_joint_3 + '.translate')

	if pm.objExists('lt_lt_arm_icon'):
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
		temp_constraint = pm.pointConstraint(arm_joint_3, switch, mo=0, w=1)
		pm.delete(temp_constraint)
		pm.select(switch)
		freezeTransform()
		switch_name = lt_arm_root.replace('01_bind', 'IkFk_switch')
		switch.rename(switch_name)
		pm.parentConstraint(arm_joint_3, switch, mo=1)



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
		pm.connectAttr(switch + '.IkFk', arm_joint_2_rot_ikfk + '.blender')
		pm.connectAttr(switch + '.IkFk', arm_joint_3_rot_ikfk + '.blender')
		pm.connectAttr(switch + '.IkFk', root_trans_ikfk + '.blender')
		pm.connectAttr(switch + '.IkFk', arm_joint_2_trans_ikfk + '.blender')
		pm.connectAttr(switch + '.IkFk', arm_joint_3_trans_ikfk + '.blender')

		'''
		Create fk icons
		'''
		fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
		# print 'Fk icon 1:', fk_icon_1
		temp_constraint = pm.parentConstraint(lt_fk_root, fk_icon_1)
		pm.delete(temp_constraint)
		fk_pad_1 = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(lt_fk_root, fk_pad_1)
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
		fk_icon1_name = lt_fk_root.replace('fk', 'fk_icon')
		fk_icon_1.rename(fk_icon1_name)

		fk_icon2_name = fk_icon_1.replace('01', '02')
		fk_icon_2.rename(fk_icon2_name)

		fk_pad1_name = fk_icon_1.replace('icon', 'local')
		fk_pad_1.rename(fk_pad1_name)

		fk_pad2_name = fk_icon_2.replace('icon', 'local')
		fk_pad_2.rename(fk_pad2_name) 



		pm.parentConstraint(fk_icon_1, lt_fk_root)
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
		pm.select(lt_ik_root, ik_joint_3)
		arm_ikh = pm.ikHandle()[0]

		ikh_name = lt_arm_root.replace('bind', 'ikh')
		arm_ikh.rename(ikh_name)


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
		temp_constraint = pm.pointConstraint(arm_joint_2, elbow_icon)
		pm.delete(temp_constraint)
		freezeTransform(elbow_icon)
		pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
		freezeTransform(elbow_icon)

		'''
		Rename elbow icon
		'''
		elbow_icon_name = lt_arm_root.replace('arm_01_bind', 'elbow_icon')
		elbow_icon.rename(elbow_icon_name)

		'''
		Create the pole vector for the elbow
		'''
		pm.poleVectorConstraint(elbow_icon, arm_ikh)

		'''
		Parent the arm_ikh under the lt_arm_icon
		'''
		pm.parent(arm_ikh, lt_arm_icon)

		'''
		Icon visibility SDKs
		'''
		fk_pad_1.v.set(0)
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(lt_arm_icon + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
		switch.IkFk.set(1)
		fk_pad_1.v.set(1)
		lt_arm_icon.v.set(0)
		elbow_icon.v.set(0)
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(lt_arm_icon + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
		switch.IkFk.set(0.1)
		fk_pad_1.v.set(1)
		lt_arm_icon.v.set(1)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(lt_arm_icon + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
		switch.IkFk.set(0.99)
		fk_pad_1.v.set(1)
		lt_arm_icon.v.set(1)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(lt_arm_icon + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
		switch.IkFk.set(0)

		upperArm_info = pm.shadingNode('curveInfo', asUtility=1)
		node_name = lt_arm_root.replace('01_bind', 'info')
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

		jnt_name = lt_arm_root.replace('bind', 'twist')
		lt_arm_root.rename(jnt_name)

		jnt_name = root_joint.replace('twist', 'bind')
		root_joint.rename(jnt_name)

		jnt_name = lt_arm_root.replace('t1', 't')
		lt_arm_root.rename(jnt_name)

		jnt_name = lt_arm_root.replace('01', '02')
		arm_joint_2.rename(jnt_name)

		jnt_name = lt_arm_root.replace('01', '03')
		arm_joint_3.rename(jnt_name)

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
		lt_joint_12.rename(jnt_name)

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

		temp_constraint = pm.parentConstraint(lt_arm_root, loc_1, mo=0)
		pm.delete(temp_constraint)
		pm.select(loc_1)
		freezeTransform(loc_1)

		loc_name = root_joint.replace('01_bind', 'start_loc')
		loc_1.rename(loc_name)

		temp_constraint = pm.parentConstraint(arm_joint_3, loc_2, mo=0)
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

		pm.parentConstraint(lt_arm_icon, loc_2)

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
		pm.connectAttr(stretch_invert + '.outputX', lt_joint_12 + '.sy')

		pm.connectAttr(stretch_invert + '.outputX', joint_7 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', joint_8 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', joint_9 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', joint_10 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', joint_11 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', lt_joint_12 + '.sz')
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
		temp_constraint = pm.parentConstraint(arm_joint_3, loc_5, mo=0)
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
		temp_constraint = pm.pointConstraint(lt_arm_root, transform_1, mo=0)
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
		temp_constraint = pm.pointConstraint(arm_joint_3, transform_2, mo=0)
		pm.delete(temp_constraint)

		node_name = transform_1.replace('01','02')
		transform_2.rename(node_name)

		pm.connectAttr(loc_4 + '.worldPosition', snap_dist_2 + '.startPoint')

		pm.connectAttr(loc_5 + '.worldPosition', snap_dist_2 + '.endPoint')

		pm.parent(loc_4, elbow_icon)

		pm.parent(loc_5, lt_arm_icon)

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
		temp_constraint = pm.parentConstraint(arm_joint_3, ik_cons_grp)
		pm.delete(temp_constraint)
		freezeTransform(ik_cons_grp)
		pm.parent(arm_ikh, loc_5, ik_cons_grp)
		grp_name = twist_grp.replace('twist', 'cons')
		ik_cons_grp.rename(grp_name)
		constraint_1 = pm.parentConstraint(lt_arm_icon, ik_cons_grp, mo=0)
		const_1_targets = constraint_1.getWeightAliasList()[0]
		# print const_1_targets
		constraint_2 = pm.parentConstraint(hJ_2, ik_cons_grp, mo=0)
		const_2_targets = constraint_2.getWeightAliasList()[1]
		# print const_2_targets
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

		dnt_grp = pm.group(loc_1,loc_2, loc_3, arm_dist, twist_grp, lt_arm_root, lt_ik_root, lt_fk_root, snap_dist_1, snap_dist_2, ik_cons_grp, hJpad)
		grp_name = twist_grp.replace('twist_grp', 'DO____NOT____TOUCH')
		dnt_grp.rename(grp_name)

		pad = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(lt_arm_root, pad, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(pad)

		pm.parent(root_joint, joint_7, pad)
		pad_name = root_joint.replace('01_bind', '00_pad')
		pad.rename(pad_name)

		ik_grp = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(lt_arm_root, ik_grp, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(ik_grp)
		pm.parent(ik_grp, dnt_grp)
		pm.parent(lt_ik_root, loc_1, loc_2, ik_grp)

		grp_name = lt_ik_root.replace('01_ik', '00_ik_cons_grp')
		ik_grp.rename(grp_name)

		twist_jnt_grp = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(lt_arm_root, twist_jnt_grp, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(twist_jnt_grp)
		pm.parent(twist_jnt_grp, dnt_grp)
		pm.parent(lt_arm_root, twist_jnt_grp)	

		grp_name = ik_grp.replace('ik', 'twist')
		twist_jnt_grp.rename(grp_name)


		arm_global = pm.group(empty=True)

		temp_constraint = pm.parentConstraint(lt_arm_root, arm_global)
		pm.delete(temp_constraint)
		freezeTransform(arm_global)
		pm.parent(lt_arm_icon, elbow_icon, pad, switch, fk_pad_1, dnt_grp, arm_global)
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
			# print 'shape 1:', cShape_1
			# print 'shape 2:', cShape_2
			# print 'shape 3:', cShape_3

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
			grp_name = lt_arm_root.replace('lt_arm_01_twist', 'joint_grp')
			jnt_grp.rename(grp_name)
			# print jnt_grp
			# pm.parent(pad, jnt_grp)
			pm.scaleConstraint(moveAll, jnt_grp)

		if pm.objExists('*icon_grp'):
			pm.select('*icon_grp')
			icon_grp = pm.ls(sl=True)[0] 
			pm.parent(moveAll, '*icon_grp')
			# pm.parent(lt_arm_icon, fk_pad_1, elbow_icon, moveAll)

		else:
			icon_grp = pm.group(empty=True)
			pm.parent(moveAll, icon_grp)
			group_name = jnt_grp.replace('joint', 'icon')
			icon_grp.rename(group_name)
			# pm.parent(lt_arm_icon, fk_pad_1, elbow_icon, moveAll)
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

		icon_name = lt_arm_icon.replace('arm', 'arm_gimbal_core')
		core_icon.rename(icon_name)

		shape_name = core_icon.replace('_icon', 'Shape1')
		shape_1.rename(shape_name)

		shape_name = shape_1.replace('1', '2')
		shape_2.rename(shape_name)

		temp_constraint = pm.pointConstraint(lt_arm_root, core_icon, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(core_icon)

		pm.parent(core_icon, arm_global)
		pm.orientConstraint(core_icon, fk_pad_1, mo=1)


		twist_gimbal_grp = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(lt_arm_root, twist_gimbal_grp, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(twist_gimbal_grp)

		pm.parent(twist_gimbal_grp, twist_jnt_grp)

		pm.parent(lt_arm_root, twist_gimbal_grp)


		grp_name = core_icon.replace('arm_gimbal_core_icon', 'twist_gimbal_core_grp')
		twist_gimbal_grp.rename(grp_name)

		gimbal_core_tog = pm.shadingNode('blendColors', asUtility=1)

		node_name = lt_arm_icon.replace('icon', 'gimbal_core_tog_blendColors')
		gimbal_core_tog.rename(node_name)

		pm.connectAttr(core_icon + '.r', gimbal_core_tog + '.color2')
		gimbal_core_tog.color1R.set(0)
		gimbal_core_tog.color1G.set(0)
		gimbal_core_tog.color1B.set(0)
		pm.connectAttr(gimbal_core_tog + '.output', twist_jnt_grp + '.r')
		pm.connectAttr(switch + '.IkFk', gimbal_core_tog + '.blender')
		pm.connectAttr(switch + '.IkFk', core_icon + '.v')


		pm.select(loc_1, loc_2, loc_3, loc_4, loc_5, snap_dist_1, snap_dist_2, lt_ik_root, arm_dist, arm_ikh, arm_ik_1, arm_ik_2, lt_arm_root, arm_curve_1, arm_curve_2, hJ_1, lt_fk_root)
		selection = pm.ls(sl=1)
		for each in selection:
			pm.setAttr(each + '.visibility', 0)
	else:
		'''
		Create the arm icon
		'''
		lt_arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
		temp_constraint = pm.pointConstraint(arm_joint_3, lt_arm_icon)
		pm.delete(temp_constraint)
		freezeTransform()
		deleteHistory()

		'''
		Rename arm icon
		'''
		lt_arm_icon_name = lt_arm_root.replace('01_bind', 'icon')
		lt_arm_icon.rename(lt_arm_icon_name)


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
	temp_constraint = pm.pointConstraint(arm_joint_3, switch, mo=0, w=1)
	pm.delete(temp_constraint)
	pm.select(switch)
	freezeTransform()
	switch_name = lt_arm_root.replace('01_bind', 'IkFk_switch')
	switch.rename(switch_name)
	pm.parentConstraint(arm_joint_3, switch, mo=1)



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
	pm.connectAttr(switch + '.IkFk', arm_joint_2_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', arm_joint_3_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', root_trans_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', arm_joint_2_trans_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', arm_joint_3_trans_ikfk + '.blender')

	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(lt_fk_root, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(lt_fk_root, fk_pad_1)
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
	fk_icon1_name = lt_fk_root.replace('fk', 'fk_icon')
	fk_icon_1.rename(fk_icon1_name)

	fk_icon2_name = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(fk_icon2_name)

	fk_pad1_name = fk_icon_1.replace('icon', 'local')
	fk_pad_1.rename(fk_pad1_name)

	fk_pad2_name = fk_icon_2.replace('icon', 'local')
	fk_pad_2.rename(fk_pad2_name) 



	pm.parentConstraint(fk_icon_1, lt_fk_root)
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
	pm.select(lt_ik_root, ik_joint_3)
	arm_ikh = pm.ikHandle()[0]

	ikh_name = lt_arm_root.replace('bind', 'ikh')
	arm_ikh.rename(ikh_name)


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
	temp_constraint = pm.pointConstraint(arm_joint_2, elbow_icon)
	pm.delete(temp_constraint)
	freezeTransform(elbow_icon)
	pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
	freezeTransform(elbow_icon)

	'''
	Rename elbow icon
	'''
	elbow_icon_name = lt_arm_root.replace('arm_01_bind', 'elbow_icon')
	elbow_icon.rename(elbow_icon_name)

	'''
	Create the pole vector for the elbow
	'''
	pm.poleVectorConstraint(elbow_icon, arm_ikh)

	'''
	Parent the arm_ikh under the lt_arm_icon
	'''
	pm.parent(arm_ikh, lt_arm_icon)

	'''
	Icon visibility SDKs
	'''
	fk_pad_1.v.set(0)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(lt_arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(1)
	fk_pad_1.v.set(1)
	lt_arm_icon.v.set(0)
	elbow_icon.v.set(0)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(lt_arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0.1)
	fk_pad_1.v.set(1)
	lt_arm_icon.v.set(1)
	elbow_icon.v.set(1)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(lt_arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0.99)
	fk_pad_1.v.set(1)
	lt_arm_icon.v.set(1)
	elbow_icon.v.set(1)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(lt_arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0)

	upperArm_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = lt_arm_root.replace('01_bind', 'info')
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

	jnt_name = lt_arm_root.replace('bind', 'twist')
	lt_arm_root.rename(jnt_name)

	jnt_name = root_joint.replace('twist', 'bind')
	root_joint.rename(jnt_name)

	jnt_name = lt_arm_root.replace('t1', 't')
	lt_arm_root.rename(jnt_name)

	jnt_name = lt_arm_root.replace('01', '02')
	arm_joint_2.rename(jnt_name)

	jnt_name = lt_arm_root.replace('01', '03')
	arm_joint_3.rename(jnt_name)

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
	lt_joint_12.rename(jnt_name)

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

	temp_constraint = pm.parentConstraint(lt_arm_root, loc_1, mo=0)
	pm.delete(temp_constraint)
	pm.select(loc_1)
	freezeTransform(loc_1)

	loc_name = root_joint.replace('01_bind', 'start_loc')
	loc_1.rename(loc_name)

	temp_constraint = pm.parentConstraint(arm_joint_3, loc_2, mo=0)
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

	pm.parentConstraint(lt_arm_icon, loc_2)

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
	pm.connectAttr(stretch_invert + '.outputX', lt_joint_12 + '.sy')

	pm.connectAttr(stretch_invert + '.outputX', joint_7 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_8 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_9 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_10 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_11 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', lt_joint_12 + '.sz')
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
	temp_constraint = pm.parentConstraint(arm_joint_3, loc_5, mo=0)
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
	temp_constraint = pm.pointConstraint(lt_arm_root, transform_1, mo=0)
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
	temp_constraint = pm.pointConstraint(arm_joint_3, transform_2, mo=0)
	pm.delete(temp_constraint)

	node_name = transform_1.replace('01','02')
	transform_2.rename(node_name)

	pm.connectAttr(loc_4 + '.worldPosition', snap_dist_2 + '.startPoint')

	pm.connectAttr(loc_5 + '.worldPosition', snap_dist_2 + '.endPoint')

	pm.parent(loc_4, elbow_icon)

	pm.parent(loc_5, lt_arm_icon)

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
	temp_constraint = pm.parentConstraint(arm_joint_3, ik_cons_grp)
	pm.delete(temp_constraint)
	freezeTransform(ik_cons_grp)
	pm.parent(arm_ikh, loc_5, ik_cons_grp)
	grp_name = twist_grp.replace('twist', 'cons')
	ik_cons_grp.rename(grp_name)
	constraint_1 = pm.parentConstraint(lt_arm_icon, ik_cons_grp, mo=0)
	const_1_targets = constraint_1.getWeightAliasList()[0]
	# print const_1_targets
	constraint_2 = pm.parentConstraint(hJ_2, ik_cons_grp, mo=0)
	const_2_targets = constraint_2.getWeightAliasList()[1]
	# print const_2_targets
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

	dnt_grp = pm.group(loc_1,loc_2, loc_3, arm_dist, twist_grp, lt_arm_root, lt_ik_root, lt_fk_root, snap_dist_1, snap_dist_2, ik_cons_grp, hJpad)
	grp_name = twist_grp.replace('twist_grp', 'DO____NOT____TOUCH')
	dnt_grp.rename(grp_name)

	pad = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(lt_arm_root, pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(pad)

	pm.parent(root_joint, joint_7, pad)
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	ik_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(lt_arm_root, ik_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(ik_grp)
	pm.parent(ik_grp, dnt_grp)
	pm.parent(lt_ik_root, loc_1, loc_2, ik_grp)

	grp_name = lt_ik_root.replace('01_ik', '00_ik_cons_grp')
	ik_grp.rename(grp_name)

	twist_jnt_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(lt_arm_root, twist_jnt_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(twist_jnt_grp)
	pm.parent(twist_jnt_grp, dnt_grp)
	pm.parent(lt_arm_root, twist_jnt_grp)	

	grp_name = ik_grp.replace('ik', 'twist')
	twist_jnt_grp.rename(grp_name)


	arm_global = pm.group(empty=True)

	temp_constraint = pm.parentConstraint(lt_arm_root, arm_global)
	pm.delete(temp_constraint)
	freezeTransform(arm_global)
	pm.parent(lt_arm_icon, elbow_icon, pad, switch, fk_pad_1, dnt_grp, arm_global)
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
		# print 'shape 1:', cShape_1
		# print 'shape 2:', cShape_2
		# print 'shape 3:', cShape_3

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
		grp_name = lt_arm_root.replace('lt_arm_01_twist', 'joint_grp')
		jnt_grp.rename(grp_name)
		# print jnt_grp
		# pm.parent(pad, jnt_grp)
		pm.scaleConstraint(moveAll, jnt_grp)

	if pm.objExists('*icon_grp'):
		pm.select('*icon_grp')
		icon_grp = pm.ls(sl=True)[0] 
		pm.parent(moveAll, '*icon_grp')
		# pm.parent(lt_arm_icon, fk_pad_1, elbow_icon, moveAll)

	else:
		icon_grp = pm.group(empty=True)
		pm.parent(moveAll, icon_grp)
		group_name = jnt_grp.replace('joint', 'icon')
		icon_grp.rename(group_name)
		# pm.parent(lt_arm_icon, fk_pad_1, elbow_icon, moveAll)
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

	icon_name = lt_arm_icon.replace('arm', 'arm_gimbal_core')
	core_icon.rename(icon_name)

	shape_name = core_icon.replace('_icon', 'Shape1')
	shape_1.rename(shape_name)

	shape_name = shape_1.replace('1', '2')
	shape_2.rename(shape_name)

	temp_constraint = pm.pointConstraint(lt_arm_root, core_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(core_icon)

	pm.parent(core_icon, arm_global)
	pm.orientConstraint(core_icon, fk_pad_1, mo=1)


	twist_gimbal_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(lt_arm_root, twist_gimbal_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(twist_gimbal_grp)

	pm.parent(twist_gimbal_grp, twist_jnt_grp)

	pm.parent(lt_arm_root, twist_gimbal_grp)


	grp_name = core_icon.replace('arm_gimbal_core_icon', 'twist_gimbal_core_grp')
	twist_gimbal_grp.rename(grp_name)

	gimbal_core_tog = pm.shadingNode('blendColors', asUtility=1)

	node_name = lt_arm_icon.replace('icon', 'gimbal_core_tog_blendColors')
	gimbal_core_tog.rename(node_name)

	pm.connectAttr(core_icon + '.r', gimbal_core_tog + '.color2')
	gimbal_core_tog.color1R.set(0)
	gimbal_core_tog.color1G.set(0)
	gimbal_core_tog.color1B.set(0)
	pm.connectAttr(gimbal_core_tog + '.output', twist_jnt_grp + '.r')
	pm.connectAttr(switch + '.IkFk', gimbal_core_tog + '.blender')
	pm.connectAttr(switch + '.IkFk', core_icon + '.v')


	pm.select(loc_1, loc_2, loc_3, loc_4, loc_5, snap_dist_1, snap_dist_2, lt_ik_root, arm_dist, arm_ikh, arm_ik_1, arm_ik_2, lt_arm_root, arm_curve_1, arm_curve_2, hJ_1, lt_fk_root)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

def lt_fkArmSetup(*args):
	pm.select(lt_arm_01_bind)
	arm_system = pm.ls(sl=True, dag=True)
	lt_arm_root = arm_system[0]
	arm_joint_2 = arm_system[1]
	arm_joint_3 = arm_system[2]
	# print 'Main Root:', lt_arm_root
	# print 'Main Joint 2:', arm_joint_2
	# print 'Main Joint 3:', arm_joint_3

	pm.joint(lt_arm_root, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	arm_joint_3.jointOrientX.set(0)
	arm_joint_3.jointOrientY.set(0)
	lt_arm_root.rotateOrder.set(3)

	fk_joints = pm.duplicate(lt_arm_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=True, dag=True)
	lt_fk_root = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	# print 'Fk Root:', lt_fk_root
	# print 'Fk Joint 2:', fk_joint_2
	# print 'Fk Joint 3:', fk_joint_3

	joint_name = lt_arm_root.replace('bind', 'fk')
	lt_fk_root.rename(joint_name)

	joint_name = fk_joint_2.replace('01', '02')
	fk_joint_2.rename(joint_name)

	joint_name = fk_joint_3.replace('02', '03')
	fk_joint_3.rename(joint_name)


	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(lt_fk_root, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(lt_fk_root, fk_pad_1)
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
	fk_icon1_name = lt_fk_root.replace('fk', 'fk_icon')
	fk_icon_1.rename(fk_icon1_name)

	fk_icon2_name = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(fk_icon2_name)

	fk_pad1_name = fk_icon_1.replace('icon', 'local')
	fk_pad_1.rename(fk_pad1_name)

	fk_pad2_name = fk_icon_2.replace('icon', 'local')
	fk_pad_2.rename(fk_pad2_name) 



	pm.parentConstraint(fk_icon_1, lt_fk_root)
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

	pm.connectAttr(lt_fk_root + '.rotate', lt_arm_root + '.rotate')
	pm.connectAttr(fk_joint_2 + '.rotate', arm_joint_2 + '.rotate')
	pm.connectAttr(fk_joint_3 + '.rotate', arm_joint_3 + '.rotate')

	pm.connectAttr(lt_fk_root + '.translate', lt_arm_root + '.translate')
	pm.connectAttr(fk_joint_2 + '.translate', arm_joint_2 + '.translate')
	pm.connectAttr(fk_joint_3 + '.translate', arm_joint_3 + '.translate')

	lt_fk_root.v.set(0)

def lt_ikArmSetup(*args):
	pm.select(lt_arm_01_bind)
	arm_system = pm.ls(sl=True, dag=True)
	lt_arm_root = arm_system[0]
	arm_joint_2 = arm_system[1]
	arm_joint_3 = arm_system[2]
	# print 'Main Root:', lt_arm_root
	# print 'Main Joint 2:', arm_joint_2
	# print 'Main Joint 3:', arm_joint_3

	pm.joint(lt_arm_root, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	arm_joint_3.jointOrientX.set(0)
	arm_joint_3.jointOrientY.set(0)
	lt_arm_root.rotateOrder.set(3)


	ik_joints = pm.duplicate(lt_arm_root)
	ik_joints = pm.ls(sl=True, dag=True)
	lt_ik_root = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	# print 'Ik Root:', lt_ik_root
	# print 'Ik Joint 2:', ik_joint_2
	# print 'Ik Joint 3:', ik_joint_3

	
	for each in ik_joints:
		joint_name = lt_arm_root.replace('bind', 'ik')
		lt_ik_root.rename(joint_name)

	joint_name = lt_ik_root.replace('1', '2')
	ik_joint_2.rename(joint_name)

	joint_name = ik_joint_2.replace('2', '3')
	ik_joint_3.rename(joint_name)

	twist_joints = pm.duplicate(lt_arm_root)
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
	lt_joint_12 = twist_joints[1]

	pm.delete(end_joint)

	jnt_name_12 = lt_joint_12.replace('07', '12')
	lt_joint_12.rename(jnt_name_12)
	jnt_name_7 = joint_7.replace('06_twist1', '07_twist')
	joint_7.rename(jnt_name_7)

	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_1 = pm.pointConstraint(joint_7, loc_1, mo=0, w=0)
	point_constraint_2 = pm.pointConstraint(lt_joint_12, loc_1, mo=0, w=1)
	jnt_name_11 = lt_joint_12.replace('12', '11')
	joint_11 = pm.joint(loc_1, name=jnt_name_11)

	loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_1 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_3 = pm.pointConstraint(joint_7 , loc_2, mo=0, w=.25)
	point_constraint_4 = pm.pointConstraint(lt_joint_12 , loc_2, mo=0, w=.75)
	jnt_name_10 = joint_11.replace('11', '10')
	joint_10 = pm.joint(loc_2, n=jnt_name_10)

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_2 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_5 = pm.pointConstraint(joint_7 ,loc_3, mo=0, w=.5)
	point_constraint_6 = pm.pointConstraint(lt_joint_12 ,loc_3, mo=0, w=.5)
	jnt_name_9 = joint_10.replace('10', '09')
	joint_9 = pm.joint(loc_3, n=jnt_name_9)

	loc_4 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_3 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_7 = pm.pointConstraint(joint_7 ,loc_4, mo=0, w=.75)
	point_constraint_8 = pm.pointConstraint(lt_joint_12 ,loc_4, mo=0, w=.25)
	jnt_name_8 = joint_9.replace('9', '8')
	joint_8 = pm.joint(loc_4, n=jnt_name_8)

	pm.parent(joint_11, joint_10)
	pm.parent(joint_10, joint_9)
	pm.parent(joint_9, joint_8)
	pm.parent(joint_8, joint_7)

	pm.delete(loc_1, loc_2, loc_3, loc_4)

	pm.parent(lt_joint_12, joint_11)


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

	cb_joint_3 = pm.duplicate(lt_joint_12)[0]

	bind_name = cb_joint_2.replace('2', '3')
	cb_joint_3.rename(bind_name)

	pm.parent(cb_joint_3, w=1)

	tempBind = pm.duplicate(lt_arm_root)

	pm.select(tempBind)
	temp_joints = pm.ls(sl=True, dag=True)
	temp_1 = temp_joints[0]
	temp_2 = temp_joints[1]
	temp_3 = temp_joints[2]

	temp_name = lt_arm_root.replace('bind', 'temp')
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

	ik_name = arm_curve_1.replace('crv', 'twist_ikh')
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

	pm.select(end_joint, lt_joint_12, arm_curve_2)
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

	pm.parentConstraint(arm_joint_3, cb_joint_3, mo=1)
	pm.parentConstraint(arm_joint_2, cb_joint_2, mo=1)
	pm.pointConstraint(lt_arm_root, cb_joint_1, mo=1)


	'''================================================================================================================'''
	pm.connectAttr(lt_ik_root + '.rotate', lt_arm_root + '.rotate')
	pm.connectAttr(ik_joint_2 + '.rotate', arm_joint_2 + '.rotate')
	pm.connectAttr(ik_joint_3 + '.rotate', arm_joint_3 + '.rotate')

	pm.connectAttr(lt_ik_root + '.translate', lt_arm_root + '.translate')
	pm.connectAttr(ik_joint_2 + '.translate', arm_joint_2 + '.translate')
	pm.connectAttr(ik_joint_3 + '.translate', arm_joint_3 + '.translate')

	'''
	Create the arm icon
	'''
	lt_arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	temp_constraint = pm.pointConstraint(arm_joint_3, lt_arm_icon)
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()

	'''
	Rename arm icon
	'''
	lt_arm_icon_name = lt_arm_root.replace('01_bind', 'icon')
	lt_arm_icon.rename(lt_arm_icon_name)


	'''
	Create the ik
	'''
	pm.select(lt_ik_root, ik_joint_3)
	arm_ikh = pm.ikHandle()[0]

	ikh_name = lt_arm_root.replace('bind', 'ikh')
	arm_ikh.rename(ikh_name)


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
	temp_constraint = pm.pointConstraint(arm_joint_2, elbow_icon)
	pm.delete(temp_constraint)
	freezeTransform(elbow_icon)
	pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
	freezeTransform(elbow_icon)

	'''
	Rename elbow icon
	'''
	elbow_icon_name = lt_arm_root.replace('arm_01_bind', 'elbow_icon')
	elbow_icon.rename(elbow_icon_name)

	'''
	Create the pole vector for the elbow
	'''
	pm.poleVectorConstraint(elbow_icon, arm_ikh)

	'''
	Parent the arm_ikh under the lt_arm_icon
	'''
	pm.parent(arm_ikh, lt_arm_icon)

	'''==========================================================================================================================='''

	upperArm_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = lt_arm_root.replace('01_bind', 'info')
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

	jnt_name = lt_arm_root.replace('bind', 'twist')
	lt_arm_root.rename(jnt_name)

	jnt_name = root_joint.replace('twist', 'bind')
	root_joint.rename(jnt_name)

	jnt_name = lt_arm_root.replace('t1', 't')
	lt_arm_root.rename(jnt_name)

	jnt_name = lt_arm_root.replace('01', '02')
	arm_joint_2.rename(jnt_name)

	jnt_name = lt_arm_root.replace('01', '03')
	arm_joint_3.rename(jnt_name)

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
	lt_joint_12.rename(jnt_name)

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

	temp_constraint = pm.parentConstraint(lt_arm_root, loc_1, mo=0)
	pm.delete(temp_constraint)
	pm.select(loc_1)
	freezeTransform(loc_1)

	loc_name = lt_arm_root.replace('01_twist', 'start_loc')
	loc_1.rename(loc_name)

	temp_constraint = pm.parentConstraint(arm_joint_3, loc_2, mo=0)
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

	pm.parentConstraint(lt_arm_icon, loc_2)

	upperArm_len = pm.getAttr(ik_joint_2 + '.tx')

	foreArm_len = pm.getAttr(ik_joint_3 + '.tx')

	sumLen = upperArm_len + foreArm_len

	pm.setDrivenKeyframe(ik_joint_2 + '.tx', currentDriver=arm_dist + '.distance', value=upperArm_len, driverValue=sumLen)

	pm.setDrivenKeyframe(ik_joint_2 + '.tx',  currentDriver=arm_dist + '.distance', value=(upperArm_len*2), driverValue=(sumLen*2))

	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=arm_dist + '.distance', value=foreArm_len, driverValue=sumLen)

	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=arm_dist + '.distance', value=(foreArm_len*2), driverValue=(sumLen*2))

	pm.keyTangent(ik_joint_2, ik_joint_3,'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.setInfinity(ik_joint_2, ik_joint_3, poi='linear')


	'''==========================================================================================================================='''

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(lt_arm_root, loc_3, mo=0)
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
	temp_constraint = pm.parentConstraint(arm_joint_3, loc_5, mo=0)
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
	temp_constraint = pm.pointConstraint(lt_arm_root, transform_1, mo=0)
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
	temp_constraint = pm.pointConstraint(arm_joint_3, transform_2, mo=0)
	pm.delete(temp_constraint)

	node_name = transform_1.replace('01','02')
	transform_2.rename(node_name)

	pm.connectAttr(loc_4 + '.worldPosition', snap_dist_2 + '.startPoint')

	pm.connectAttr(loc_5 + '.worldPosition', snap_dist_2 + '.endPoint')

	pm.parent(loc_4, elbow_icon)

	pm.parent(loc_5, lt_arm_icon)

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

	hybrid_fk_joints = pm.duplicate(ik_joint_2)
	pm.parent(hybrid_fk_joints, w=1)

	pm.select(hybrid_fk_joints)
	hJoints = pm.ls(sl=True,  dag=True)
	hJ_1 = hJoints[0]
	hJ_2 = hJoints[1]
	# print hJ_1
	# print hJ_2

	jnt_name = ik_joint_2.replace('ik', 'hybridFk')
	hJ_1.rename(jnt_name)

	jnt_name = hJ_1.replace('02', '03')
	hJ_2.rename(jnt_name)


	hybridFk_icon = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 2:', hybridFk_icon
	temp_constraint = pm.parentConstraint(ik_joint_2, hybridFk_icon)
	pm.delete(temp_constraint)
	hybridFk_pad = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(ik_joint_2, hybridFk_pad)
	pm.delete(temp_constraint)
	pm.parent(hybridFk_icon, hybridFk_pad)
	pm.select(hybridFk_icon)
	freezeTransform()

	'''
	Rename the icons and the pads
	'''

	hybridFk_icon_name = lt_ik_root.replace('01_ik', 'hybridFk_icon')
	hybridFk_icon.rename(hybridFk_icon_name)

	hybridFk_pad_name = hybridFk_icon.replace('icon', 'local')
	hybridFk_pad.rename(hybridFk_pad_name) 

	'''
	Create length attr
	'''
	pm.addAttr(hybridFk_icon, ln='length', at='double', min=0, dv=1)
	hybridFk_icon.length.set(e=1, keyable=True)
	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=hybridFk_icon + '.length')
	hybridFk_icon.length.set(0)
	ik_joint_3.tx.set(0)
	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=hybridFk_icon + '.length')
	hybridFk_icon.length.set(1)
	pm.keyTangent(ik_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(ik_joint_3 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	temp_constraint = pm.pointConstraint(elbow_icon, hJ_1, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(hJ_1)

	temp_constraint = pm.pointConstraint(elbow_icon, hybridFk_pad, mo=0)
	pm.delete(temp_constraint)

	pm.orientConstraint(hybridFk_icon, hJ_1)

	ik_cons_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(arm_joint_3, ik_cons_grp)
	pm.delete(temp_constraint)
	freezeTransform(ik_cons_grp)
	pm.parent(arm_ikh, loc_5, ik_cons_grp)
	grp_name = twist_grp.replace('twist', 'cons')
	ik_cons_grp.rename(grp_name)
	constraint_1 = pm.parentConstraint(lt_arm_icon, ik_cons_grp, mo=0)
	const_1_targets = constraint_1.getWeightAliasList()[0]
	# print const_1_targets
	constraint_2 = pm.parentConstraint(hJ_2, ik_cons_grp, mo=0)
	const_2_targets = constraint_2.getWeightAliasList()[1]
	# print const_2_targets
	pm.parent(hybridFk_pad, elbow_icon)


	pm.addAttr(elbow_icon, ln='FK_foreArmBlend', at='double', min=0, max=1, dv=0)
	elbow_icon.FK_foreArmBlend.set(e=1, keyable=True)

	elbow_icon.FK_foreArmBlend.set(1)
	const_1_targets.set(0)
	pm.setDrivenKeyframe(const_1_targets, const_2_targets, currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hybridFk_icon + '.v',  currentDriver=elbow_icon + '.FK_foreArmBlend')
	elbow_icon.FK_foreArmBlend.set(0)
	const_1_targets.set(1)
	const_2_targets.set(0)
	hybridFk_icon.v.set(0)
	pm.setDrivenKeyframe(const_1_targets, const_2_targets, currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hybridFk_icon + '.v',  currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hJ_2 + '.tx', currentDriver=hybridFk_icon + '.length')
	hybridFk_icon.length.set(0)
	hJ_2.tx.set(0)
	length_sdk = pm.setDrivenKeyframe(hJ_2 + '.tx', currentDriver=hybridFk_icon + '.length')
	pm.keyTangent(hJ_2, itt='clamped', ott='clamped')
	pm.setInfinity(hJ_2, poi='linear')
	hybridFk_icon.length.set(1)

	pm.select(loc_1, loc_2, loc_3, loc_4, loc_5, snap_dist_1, snap_dist_2, lt_ik_root, arm_dist, arm_ikh, arm_ik_1, arm_ik_2, lt_arm_root, arm_curve_1, arm_curve_2, hJ_1)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	pm.select(cl=1)

def rt_armSetup(*args):
	global rt_arm_root, rt_fk_root, rt_ik_root, rt_joint_12, rt_arm_icon
	pm.select(rt_arm_01_bind)
	arm_system = pm.ls(sl=True, dag=True)
	rt_arm_root = arm_system[0]
	arm_joint_2 = arm_system[1]
	arm_joint_3 = arm_system[2]
	# print 'Main Root:', rt_arm_root
	# print 'Main Joint 2:', arm_joint_2
	# print 'Main Joint 3:', arm_joint_3

	pm.joint(rt_arm_root, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	arm_joint_3.jointOrientX.set(0)
	arm_joint_3.jointOrientY.set(0)
	rt_arm_root.rotateOrder.set(3)


	ik_joints = pm.duplicate(rt_arm_root)
	ik_joints = pm.ls(sl=True, dag=True)
	rt_ik_root = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	# print 'Ik Root:', rt_ik_root
	# print 'Ik Joint 2:', ik_joint_2
	# print 'Ik Joint 3:', ik_joint_3

	
	for each in ik_joints:
		joint_name = rt_arm_root.replace('bind', 'ik')
		rt_ik_root.rename(joint_name)

	joint_name = rt_ik_root.replace('1', '2')
	ik_joint_2.rename(joint_name)

	joint_name = ik_joint_2.replace('2', '3')
	ik_joint_3.rename(joint_name)

	fk_joints = pm.duplicate(rt_arm_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=True, dag=True)
	rt_fk_root = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	# print 'Fk Root:', rt_fk_root
	# print 'Fk Joint 2:', fk_joint_2
	# print 'Fk Joint 3:', fk_joint_3

	
	joint_name = rt_ik_root.replace('ik', 'fk')
	rt_fk_root.rename(joint_name)

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
	


	twist_joints = pm.duplicate(rt_arm_root)
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
	rt_joint_12 = twist_joints[1]

	pm.delete(end_joint)

	jnt_name_12 = rt_joint_12.replace('07', '12')
	rt_joint_12.rename(jnt_name_12)
	jnt_name_7 = joint_7.replace('06_twist1', '07_twist')
	joint_7.rename(jnt_name_7)

	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_1 = pm.pointConstraint(joint_7, loc_1, mo=0, w=0)
	point_constraint_2 = pm.pointConstraint(rt_joint_12, loc_1, mo=0, w=1)
	jnt_name_11 = rt_joint_12.replace('12', '11')
	joint_11 = pm.joint(loc_1, name=jnt_name_11)

	loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_1 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_3 = pm.pointConstraint(joint_7 , loc_2, mo=0, w=.25)
	point_constraint_4 = pm.pointConstraint(rt_joint_12 , loc_2, mo=0, w=.75)
	jnt_name_10 = joint_11.replace('11', '10')
	joint_10 = pm.joint(loc_2, n=jnt_name_10)

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_2 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_5 = pm.pointConstraint(joint_7 ,loc_3, mo=0, w=.5)
	point_constraint_6 = pm.pointConstraint(rt_joint_12 ,loc_3, mo=0, w=.5)
	jnt_name_9 = joint_10.replace('10', '09')
	joint_9 = pm.joint(loc_3, n=jnt_name_9)

	loc_4 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_3 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_7 = pm.pointConstraint(joint_7 ,loc_4, mo=0, w=.75)
	point_constraint_8 = pm.pointConstraint(rt_joint_12 ,loc_4, mo=0, w=.25)
	jnt_name_8 = joint_9.replace('9', '8')
	joint_8 = pm.joint(loc_4, n=jnt_name_8)

	pm.parent(joint_11, joint_10)
	pm.parent(joint_10, joint_9)
	pm.parent(joint_9, joint_8)
	pm.parent(joint_8, joint_7)

	pm.delete(loc_1, loc_2, loc_3, loc_4)

	pm.parent(rt_joint_12, joint_11)


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

	cb_joint_3 = pm.duplicate(rt_joint_12)[0]

	bind_name = cb_joint_2.replace('2', '3')
	cb_joint_3.rename(bind_name)

	pm.parent(cb_joint_3, w=1)

	tempBind = pm.duplicate(rt_arm_root)

	pm.select(tempBind)
	temp_joints = pm.ls(sl=True, dag=True)
	temp_1 = temp_joints[0]
	temp_2 = temp_joints[1]
	temp_3 = temp_joints[2]

	temp_name = rt_arm_root.replace('bind', 'temp')
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

	pm.select(end_joint, rt_joint_12, arm_curve_2)
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

	pm.parentConstraint(arm_joint_3, cb_joint_3, mo=1)
	pm.parentConstraint(arm_joint_2, cb_joint_2, mo=1)
	pm.pointConstraint(rt_arm_root, cb_joint_1, mo=1)


	'''================================================================================================================'''
	root_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = rt_arm_root.replace('bind', 'rot_ikfk_blend')
	root_rot_ikfk.rename(node_name)

	pm.connectAttr(rt_ik_root + '.rotate', root_rot_ikfk + '.color2')
	pm.connectAttr(rt_fk_root + '.rotate', root_rot_ikfk + '.color1')
	pm.connectAttr(root_rot_ikfk + '.output', rt_arm_root + '.rotate')

	arm_joint_2_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_rot_ikfk.replace('1', '2')
	arm_joint_2_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_2 + '.rotate', arm_joint_2_rot_ikfk + '.color2')
	pm.connectAttr(fk_joint_2 + '.rotate', arm_joint_2_rot_ikfk + '.color1')
	pm.connectAttr(arm_joint_2_rot_ikfk + '.output', arm_joint_2 + '.rotate')

	arm_joint_3_rot_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_rot_ikfk.replace('1', '3')
	arm_joint_3_rot_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_3 + '.rotate', arm_joint_3_rot_ikfk + '.color2')
	pm.connectAttr(fk_joint_3 + '.rotate', arm_joint_3_rot_ikfk + '.color1')
	pm.connectAttr(arm_joint_3_rot_ikfk + '.output', arm_joint_3 + '.rotate')

	root_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = rt_arm_root.replace('bind', 'trans_ikfk_blend')
	root_trans_ikfk.rename(node_name)

	pm.connectAttr(rt_ik_root + '.translate', root_trans_ikfk + '.color2')
	pm.connectAttr(rt_fk_root + '.translate', root_trans_ikfk + '.color1')
	pm.connectAttr(root_trans_ikfk + '.output', rt_arm_root + '.translate')

	arm_joint_2_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_trans_ikfk.replace('1', '2')
	arm_joint_2_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_2 + '.translate', arm_joint_2_trans_ikfk + '.color2')
	pm.connectAttr(fk_joint_2 + '.translate', arm_joint_2_trans_ikfk + '.color1')
	pm.connectAttr(arm_joint_2_trans_ikfk + '.output', arm_joint_2 + '.translate')

	arm_joint_3_trans_ikfk = pm.shadingNode('blendColors', asUtility=1)
	node_name = root_trans_ikfk.replace('1', '3')
	arm_joint_3_trans_ikfk.rename(node_name)

	pm.connectAttr(ik_joint_3 + '.translate', arm_joint_3_trans_ikfk + '.color2')
	pm.connectAttr(fk_joint_3 + '.translate', arm_joint_3_trans_ikfk + '.color1')
	pm.connectAttr(arm_joint_3_trans_ikfk + '.output', arm_joint_3 + '.translate')

	if pm.objExists('rt_rt_arm_icon'):
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
		temp_constraint = pm.pointConstraint(arm_joint_3, switch, mo=0, w=1)
		pm.delete(temp_constraint)
		pm.select(switch)
		freezeTransform()
		switch_name = rt_arm_root.replace('01_bind', 'IkFk_switch')
		switch.rename(switch_name)
		pm.parentConstraint(arm_joint_3, switch, mo=1)



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
		pm.connectAttr(switch + '.IkFk', arm_joint_2_rot_ikfk + '.blender')
		pm.connectAttr(switch + '.IkFk', arm_joint_3_rot_ikfk + '.blender')
		pm.connectAttr(switch + '.IkFk', root_trans_ikfk + '.blender')
		pm.connectAttr(switch + '.IkFk', arm_joint_2_trans_ikfk + '.blender')
		pm.connectAttr(switch + '.IkFk', arm_joint_3_trans_ikfk + '.blender')

		'''
		Create fk icons
		'''
		fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
		# print 'Fk icon 1:', fk_icon_1
		temp_constraint = pm.parentConstraint(rt_fk_root, fk_icon_1)
		pm.delete(temp_constraint)
		fk_pad_1 = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(rt_fk_root, fk_pad_1)
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
		fk_icon1_name = rt_fk_root.replace('fk', 'fk_icon')
		fk_icon_1.rename(fk_icon1_name)

		fk_icon2_name = fk_icon_1.replace('01', '02')
		fk_icon_2.rename(fk_icon2_name)

		fk_pad1_name = fk_icon_1.replace('icon', 'local')
		fk_pad_1.rename(fk_pad1_name)

		fk_pad2_name = fk_icon_2.replace('icon', 'local')
		fk_pad_2.rename(fk_pad2_name) 



		pm.parentConstraint(fk_icon_1, rt_fk_root)
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
		pm.select(rt_ik_root, ik_joint_3)
		arm_ikh = pm.ikHandle()[0]

		ikh_name = rt_arm_root.replace('bind', 'ikh')
		arm_ikh.rename(ikh_name)


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
		temp_constraint = pm.pointConstraint(arm_joint_2, elbow_icon)
		pm.delete(temp_constraint)
		freezeTransform(elbow_icon)
		pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
		freezeTransform(elbow_icon)

		'''
		Rename elbow icon
		'''
		elbow_icon_name = rt_arm_root.replace('arm_01_bind', 'elbow_icon')
		elbow_icon.rename(elbow_icon_name)

		'''
		Create the pole vector for the elbow
		'''
		pm.poleVectorConstraint(elbow_icon, arm_ikh)

		'''
		Parent the arm_ikh under the rt_arm_icon
		'''
		pm.parent(arm_ikh, rt_arm_icon)

		'''
		Icon visibility SDKs
		'''
		fk_pad_1.v.set(0)
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(rt_arm_icon + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
		switch.IkFk.set(1)
		fk_pad_1.v.set(1)
		rt_arm_icon.v.set(0)
		elbow_icon.v.set(0)
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(rt_arm_icon + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
		switch.IkFk.set(0.1)
		fk_pad_1.v.set(1)
		rt_arm_icon.v.set(1)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(rt_arm_icon + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
		switch.IkFk.set(0.99)
		fk_pad_1.v.set(1)
		rt_arm_icon.v.set(1)
		elbow_icon.v.set(1)
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(rt_arm_icon + '.v', currentDriver= switch + '.IkFk')
		pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
		switch.IkFk.set(0)

		upperArm_info = pm.shadingNode('curveInfo', asUtility=1)
		node_name = rt_arm_root.replace('01_bind', 'info')
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

		jnt_name = rt_arm_root.replace('bind', 'twist')
		rt_arm_root.rename(jnt_name)

		jnt_name = root_joint.replace('twist', 'bind')
		root_joint.rename(jnt_name)

		jnt_name = rt_arm_root.replace('t1', 't')
		rt_arm_root.rename(jnt_name)

		jnt_name = rt_arm_root.replace('01', '02')
		arm_joint_2.rename(jnt_name)

		jnt_name = rt_arm_root.replace('01', '03')
		arm_joint_3.rename(jnt_name)

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
		rt_joint_12.rename(jnt_name)

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

		temp_constraint = pm.parentConstraint(rt_arm_root, loc_1, mo=0)
		pm.delete(temp_constraint)
		pm.select(loc_1)
		freezeTransform(loc_1)

		loc_name = root_joint.replace('01_bind', 'start_loc')
		loc_1.rename(loc_name)

		temp_constraint = pm.parentConstraint(arm_joint_3, loc_2, mo=0)
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

		pm.parentConstraint(rt_arm_icon, loc_2)

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
		pm.connectAttr(stretch_invert + '.outputX', rt_joint_12 + '.sy')

		pm.connectAttr(stretch_invert + '.outputX', joint_7 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', joint_8 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', joint_9 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', joint_10 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', joint_11 + '.sz')
		pm.connectAttr(stretch_invert + '.outputX', rt_joint_12 + '.sz')
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
		temp_constraint = pm.parentConstraint(arm_joint_3, loc_5, mo=0)
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
		temp_constraint = pm.pointConstraint(rt_arm_root, transform_1, mo=0)
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
		temp_constraint = pm.pointConstraint(arm_joint_3, transform_2, mo=0)
		pm.delete(temp_constraint)

		node_name = transform_1.replace('01','02')
		transform_2.rename(node_name)

		pm.connectAttr(loc_4 + '.worldPosition', snap_dist_2 + '.startPoint')

		pm.connectAttr(loc_5 + '.worldPosition', snap_dist_2 + '.endPoint')

		pm.parent(loc_4, elbow_icon)

		pm.parent(loc_5, rt_arm_icon)

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
		temp_constraint = pm.parentConstraint(arm_joint_3, ik_cons_grp)
		pm.delete(temp_constraint)
		freezeTransform(ik_cons_grp)
		pm.parent(arm_ikh, loc_5, ik_cons_grp)
		grp_name = twist_grp.replace('twist', 'cons')
		ik_cons_grp.rename(grp_name)
		constraint_1 = pm.parentConstraint(rt_arm_icon, ik_cons_grp, mo=0)
		const_1_targets = constraint_1.getWeightAliasList()[0]
		# print const_1_targets
		constraint_2 = pm.parentConstraint(hJ_2, ik_cons_grp, mo=0)
		const_2_targets = constraint_2.getWeightAliasList()[1]
		# print const_2_targets
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

		dnt_grp = pm.group(loc_1,loc_2, loc_3, arm_dist, twist_grp, rt_arm_root, rt_ik_root, rt_fk_root, snap_dist_1, snap_dist_2, ik_cons_grp, hJpad)
		grp_name = twist_grp.replace('twist_grp', 'DO____NOT____TOUCH')
		dnt_grp.rename(grp_name)

		pad = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(rt_arm_root, pad, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(pad)

		pm.parent(root_joint, joint_7, pad)
		pad_name = root_joint.replace('01_bind', '00_pad')
		pad.rename(pad_name)

		ik_grp = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(rt_arm_root, ik_grp, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(ik_grp)
		pm.parent(ik_grp, dnt_grp)
		pm.parent(rt_ik_root, loc_1, loc_2, ik_grp)

		grp_name = rt_ik_root.replace('01_ik', '00_ik_cons_grp')
		ik_grp.rename(grp_name)

		twist_jnt_grp = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(rt_arm_root, twist_jnt_grp, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(twist_jnt_grp)
		pm.parent(twist_jnt_grp, dnt_grp)
		pm.parent(rt_arm_root, twist_jnt_grp)	

		grp_name = ik_grp.replace('ik', 'twist')
		twist_jnt_grp.rename(grp_name)


		arm_global = pm.group(empty=True)

		temp_constraint = pm.parentConstraint(rt_arm_root, arm_global)
		pm.delete(temp_constraint)
		freezeTransform(arm_global)
		pm.parent(rt_arm_icon, elbow_icon, pad, switch, fk_pad_1, dnt_grp, arm_global)
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
			# print 'shape 1:', cShape_1
			# print 'shape 2:', cShape_2
			# print 'shape 3:', cShape_3

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
			grp_name = rt_arm_root.replace('rt_arm_01_twist', 'joint_grp')
			jnt_grp.rename(grp_name)
			# print jnt_grp
			# pm.parent(pad, jnt_grp)
			pm.scaleConstraint(moveAll, jnt_grp)

		if pm.objExists('*icon_grp'):
			pm.select('*icon_grp')
			icon_grp = pm.ls(sl=True)[0] 
			pm.parent(moveAll, '*icon_grp')
			# pm.parent(rt_arm_icon, fk_pad_1, elbow_icon, moveAll)

		else:
			icon_grp = pm.group(empty=True)
			pm.parent(moveAll, icon_grp)
			group_name = jnt_grp.replace('joint', 'icon')
			icon_grp.rename(group_name)
			# pm.parent(rt_arm_icon, fk_pad_1, elbow_icon, moveAll)
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

		icon_name = rt_arm_icon.replace('arm', 'arm_gimbal_core')
		core_icon.rename(icon_name)

		shape_name = core_icon.replace('_icon', 'Shape1')
		shape_1.rename(shape_name)

		shape_name = shape_1.replace('1', '2')
		shape_2.rename(shape_name)

		temp_constraint = pm.pointConstraint(rt_arm_root, core_icon, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(core_icon)

		pm.parent(core_icon, arm_global)
		pm.orientConstraint(core_icon, fk_pad_1, mo=1)


		twist_gimbal_grp = pm.group(empty=True)
		temp_constraint = pm.parentConstraint(rt_arm_root, twist_gimbal_grp, mo=0)
		pm.delete(temp_constraint)
		freezeTransform(twist_gimbal_grp)

		pm.parent(twist_gimbal_grp, twist_jnt_grp)

		pm.parent(rt_arm_root, twist_gimbal_grp)


		grp_name = core_icon.replace('arm_gimbal_core_icon', 'twist_gimbal_core_grp')
		twist_gimbal_grp.rename(grp_name)

		gimbal_core_tog = pm.shadingNode('blendColors', asUtility=1)

		node_name = rt_arm_icon.replace('icon', 'gimbal_core_tog_blendColors')
		gimbal_core_tog.rename(node_name)

		pm.connectAttr(core_icon + '.r', gimbal_core_tog + '.color2')
		gimbal_core_tog.color1R.set(0)
		gimbal_core_tog.color1G.set(0)
		gimbal_core_tog.color1B.set(0)
		pm.connectAttr(gimbal_core_tog + '.output', twist_jnt_grp + '.r')
		pm.connectAttr(switch + '.IkFk', gimbal_core_tog + '.blender')
		pm.connectAttr(switch + '.IkFk', core_icon + '.v')


		pm.select(loc_1, loc_2, loc_3, loc_4, loc_5, snap_dist_1, snap_dist_2, rt_ik_root, arm_dist, arm_ikh, arm_ik_1, arm_ik_2, rt_arm_root, arm_curve_1, arm_curve_2, hJ_1, rt_fk_root)
		selection = pm.ls(sl=1)
		for each in selection:
			pm.setAttr(each + '.visibility', 0)
	else:
		'''
		Create the arm icon
		'''
		rt_arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
		temp_constraint = pm.pointConstraint(arm_joint_3, rt_arm_icon)
		pm.delete(temp_constraint)
		freezeTransform()
		deleteHistory()

		'''
		Rename arm icon
		'''
		rt_arm_icon_name = rt_arm_root.replace('01_bind', 'icon')
		rt_arm_icon.rename(rt_arm_icon_name)


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
	temp_constraint = pm.pointConstraint(arm_joint_3, switch, mo=0, w=1)
	pm.delete(temp_constraint)
	pm.select(switch)
	freezeTransform()
	switch_name = rt_arm_root.replace('01_bind', 'IkFk_switch')
	switch.rename(switch_name)
	pm.parentConstraint(arm_joint_3, switch, mo=1)



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
	pm.connectAttr(switch + '.IkFk', arm_joint_2_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', arm_joint_3_rot_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', root_trans_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', arm_joint_2_trans_ikfk + '.blender')
	pm.connectAttr(switch + '.IkFk', arm_joint_3_trans_ikfk + '.blender')

	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(rt_fk_root, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(rt_fk_root, fk_pad_1)
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
	fk_icon1_name = rt_fk_root.replace('fk', 'fk_icon')
	fk_icon_1.rename(fk_icon1_name)

	fk_icon2_name = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(fk_icon2_name)

	fk_pad1_name = fk_icon_1.replace('icon', 'local')
	fk_pad_1.rename(fk_pad1_name)

	fk_pad2_name = fk_icon_2.replace('icon', 'local')
	fk_pad_2.rename(fk_pad2_name) 



	pm.parentConstraint(fk_icon_1, rt_fk_root)
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
	pm.select(rt_ik_root, ik_joint_3)
	arm_ikh = pm.ikHandle()[0]

	ikh_name = rt_arm_root.replace('bind', 'ikh')
	arm_ikh.rename(ikh_name)


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
	temp_constraint = pm.pointConstraint(arm_joint_2, elbow_icon)
	pm.delete(temp_constraint)
	freezeTransform(elbow_icon)
	pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
	freezeTransform(elbow_icon)

	'''
	Rename elbow icon
	'''
	elbow_icon_name = rt_arm_root.replace('arm_01_bind', 'elbow_icon')
	elbow_icon.rename(elbow_icon_name)

	'''
	Create the pole vector for the elbow
	'''
	pm.poleVectorConstraint(elbow_icon, arm_ikh)

	'''
	Parent the arm_ikh under the rt_arm_icon
	'''
	pm.parent(arm_ikh, rt_arm_icon)

	'''
	Icon visibility SDKs
	'''
	fk_pad_1.v.set(0)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(rt_arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(1)
	fk_pad_1.v.set(1)
	rt_arm_icon.v.set(0)
	elbow_icon.v.set(0)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(rt_arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0.1)
	fk_pad_1.v.set(1)
	rt_arm_icon.v.set(1)
	elbow_icon.v.set(1)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(rt_arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0.99)
	fk_pad_1.v.set(1)
	rt_arm_icon.v.set(1)
	elbow_icon.v.set(1)
	pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(rt_arm_icon + '.v', currentDriver= switch + '.IkFk')
	pm.setDrivenKeyframe(elbow_icon + '.v', currentDriver= switch + '.IkFk')
	switch.IkFk.set(0)

	upperArm_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = rt_arm_root.replace('01_bind', 'info')
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

	jnt_name = rt_arm_root.replace('bind', 'twist')
	rt_arm_root.rename(jnt_name)

	jnt_name = root_joint.replace('twist', 'bind')
	root_joint.rename(jnt_name)

	jnt_name = rt_arm_root.replace('t1', 't')
	rt_arm_root.rename(jnt_name)

	jnt_name = rt_arm_root.replace('01', '02')
	arm_joint_2.rename(jnt_name)

	jnt_name = rt_arm_root.replace('01', '03')
	arm_joint_3.rename(jnt_name)

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
	rt_joint_12.rename(jnt_name)

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

	temp_constraint = pm.parentConstraint(rt_arm_root, loc_1, mo=0)
	pm.delete(temp_constraint)
	pm.select(loc_1)
	freezeTransform(loc_1)

	loc_name = root_joint.replace('01_bind', 'start_loc')
	loc_1.rename(loc_name)

	temp_constraint = pm.parentConstraint(arm_joint_3, loc_2, mo=0)
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

	pm.parentConstraint(rt_arm_icon, loc_2)

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
	pm.connectAttr(stretch_invert + '.outputX', rt_joint_12 + '.sy')

	pm.connectAttr(stretch_invert + '.outputX', joint_7 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_8 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_9 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_10 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', joint_11 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', rt_joint_12 + '.sz')
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
	temp_constraint = pm.parentConstraint(arm_joint_3, loc_5, mo=0)
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
	temp_constraint = pm.pointConstraint(rt_arm_root, transform_1, mo=0)
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
	temp_constraint = pm.pointConstraint(arm_joint_3, transform_2, mo=0)
	pm.delete(temp_constraint)

	node_name = transform_1.replace('01','02')
	transform_2.rename(node_name)

	pm.connectAttr(loc_4 + '.worldPosition', snap_dist_2 + '.startPoint')

	pm.connectAttr(loc_5 + '.worldPosition', snap_dist_2 + '.endPoint')

	pm.parent(loc_4, elbow_icon)

	pm.parent(loc_5, rt_arm_icon)

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
	temp_constraint = pm.parentConstraint(arm_joint_3, ik_cons_grp)
	pm.delete(temp_constraint)
	freezeTransform(ik_cons_grp)
	pm.parent(arm_ikh, loc_5, ik_cons_grp)
	grp_name = twist_grp.replace('twist', 'cons')
	ik_cons_grp.rename(grp_name)
	constraint_1 = pm.parentConstraint(rt_arm_icon, ik_cons_grp, mo=0)
	const_1_targets = constraint_1.getWeightAliasList()[0]
	# print const_1_targets
	constraint_2 = pm.parentConstraint(hJ_2, ik_cons_grp, mo=0)
	const_2_targets = constraint_2.getWeightAliasList()[1]
	# print const_2_targets
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

	dnt_grp = pm.group(loc_1,loc_2, loc_3, arm_dist, twist_grp, rt_arm_root, rt_ik_root, rt_fk_root, snap_dist_1, snap_dist_2, ik_cons_grp, hJpad)
	grp_name = twist_grp.replace('twist_grp', 'DO____NOT____TOUCH')
	dnt_grp.rename(grp_name)

	pad = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(rt_arm_root, pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(pad)

	pm.parent(root_joint, joint_7, pad)
	pad_name = root_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	ik_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(rt_arm_root, ik_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(ik_grp)
	pm.parent(ik_grp, dnt_grp)
	pm.parent(rt_ik_root, loc_1, loc_2, ik_grp)

	grp_name = rt_ik_root.replace('01_ik', '00_ik_cons_grp')
	ik_grp.rename(grp_name)

	twist_jnt_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(rt_arm_root, twist_jnt_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(twist_jnt_grp)
	pm.parent(twist_jnt_grp, dnt_grp)
	pm.parent(rt_arm_root, twist_jnt_grp)	

	grp_name = ik_grp.replace('ik', 'twist')
	twist_jnt_grp.rename(grp_name)


	arm_global = pm.group(empty=True)

	temp_constraint = pm.parentConstraint(rt_arm_root, arm_global)
	pm.delete(temp_constraint)
	freezeTransform(arm_global)
	pm.parent(rt_arm_icon, elbow_icon, pad, switch, fk_pad_1, dnt_grp, arm_global)
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
		# print 'shape 1:', cShape_1
		# print 'shape 2:', cShape_2
		# print 'shape 3:', cShape_3

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
		grp_name = rt_arm_root.replace('rt_arm_01_twist', 'joint_grp')
		jnt_grp.rename(grp_name)
		# print jnt_grp
		# pm.parent(pad, jnt_grp)
		pm.scaleConstraint(moveAll, jnt_grp)

	if pm.objExists('*icon_grp'):
		pm.select('*icon_grp')
		icon_grp = pm.ls(sl=True)[0] 
		pm.parent(moveAll, '*icon_grp')
		# pm.parent(rt_arm_icon, fk_pad_1, elbow_icon, moveAll)

	else:
		icon_grp = pm.group(empty=True)
		pm.parent(moveAll, icon_grp)
		group_name = jnt_grp.replace('joint', 'icon')
		icon_grp.rename(group_name)
		# pm.parent(rt_arm_icon, fk_pad_1, elbow_icon, moveAll)
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

	icon_name = rt_arm_icon.replace('arm', 'arm_gimbal_core')
	core_icon.rename(icon_name)

	shape_name = core_icon.replace('_icon', 'Shape1')
	shape_1.rename(shape_name)

	shape_name = shape_1.replace('1', '2')
	shape_2.rename(shape_name)

	temp_constraint = pm.pointConstraint(rt_arm_root, core_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(core_icon)

	pm.parent(core_icon, arm_global)
	pm.orientConstraint(core_icon, fk_pad_1, mo=1)


	twist_gimbal_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(rt_arm_root, twist_gimbal_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(twist_gimbal_grp)

	pm.parent(twist_gimbal_grp, twist_jnt_grp)

	pm.parent(rt_arm_root, twist_gimbal_grp)


	grp_name = core_icon.replace('arm_gimbal_core_icon', 'twist_gimbal_core_grp')
	twist_gimbal_grp.rename(grp_name)

	gimbal_core_tog = pm.shadingNode('blendColors', asUtility=1)

	node_name = rt_arm_icon.replace('icon', 'gimbal_core_tog_blendColors')
	gimbal_core_tog.rename(node_name)

	pm.connectAttr(core_icon + '.r', gimbal_core_tog + '.color2')
	gimbal_core_tog.color1R.set(0)
	gimbal_core_tog.color1G.set(0)
	gimbal_core_tog.color1B.set(0)
	pm.connectAttr(gimbal_core_tog + '.output', twist_jnt_grp + '.r')
	pm.connectAttr(switch + '.IkFk', gimbal_core_tog + '.blender')
	pm.connectAttr(switch + '.IkFk', core_icon + '.v')


	pm.select(loc_1, loc_2, loc_3, loc_4, loc_5, snap_dist_1, snap_dist_2, rt_ik_root, arm_dist, arm_ikh, arm_ik_1, arm_ik_2, rt_arm_root, arm_curve_1, arm_curve_2, hJ_1, rt_fk_root)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

def rt_fkArmSetup(*args):
	pm.select(rt_arm_01_bind)
	arm_system = pm.ls(sl=True, dag=True)
	rt_arm_root = arm_system[0]
	arm_joint_2 = arm_system[1]
	arm_joint_3 = arm_system[2]
	# print 'Main Root:', rt_arm_root
	# print 'Main Joint 2:', arm_joint_2
	# print 'Main Joint 3:', arm_joint_3

	pm.joint(rt_arm_root, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	arm_joint_3.jointOrientX.set(0)
	arm_joint_3.jointOrientY.set(0)
	rt_arm_root.rotateOrder.set(3)

	fk_joints = pm.duplicate(rt_arm_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=True, dag=True)
	rt_fk_root = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	# print 'Fk Root:', rt_fk_root
	# print 'Fk Joint 2:', fk_joint_2
	# print 'Fk Joint 3:', fk_joint_3

	joint_name = rt_arm_root.replace('bind', 'fk')
	rt_fk_root.rename(joint_name)

	joint_name = fk_joint_2.replace('01', '02')
	fk_joint_2.rename(joint_name)

	joint_name = fk_joint_3.replace('02', '03')
	fk_joint_3.rename(joint_name)


	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(rt_fk_root, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(rt_fk_root, fk_pad_1)
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
	fk_icon1_name = rt_fk_root.replace('fk', 'fk_icon')
	fk_icon_1.rename(fk_icon1_name)

	fk_icon2_name = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(fk_icon2_name)

	fk_pad1_name = fk_icon_1.replace('icon', 'local')
	fk_pad_1.rename(fk_pad1_name)

	fk_pad2_name = fk_icon_2.replace('icon', 'local')
	fk_pad_2.rename(fk_pad2_name) 



	pm.parentConstraint(fk_icon_1, rt_fk_root)
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

	pm.connectAttr(rt_fk_root + '.rotate', rt_arm_root + '.rotate')
	pm.connectAttr(fk_joint_2 + '.rotate', arm_joint_2 + '.rotate')
	pm.connectAttr(fk_joint_3 + '.rotate', arm_joint_3 + '.rotate')

	pm.connectAttr(rt_fk_root + '.translate', rt_arm_root + '.translate')
	pm.connectAttr(fk_joint_2 + '.translate', arm_joint_2 + '.translate')
	pm.connectAttr(fk_joint_3 + '.translate', arm_joint_3 + '.translate')

	rt_fk_root.v.set(0)

def rt_ikArmSetup(*args):
	pm.select(rt_arm_01_bind)
	arm_system = pm.ls(sl=True, dag=True)
	rt_arm_root = arm_system[0]
	arm_joint_2 = arm_system[1]
	arm_joint_3 = arm_system[2]
	# print 'Main Root:', rt_arm_root
	# print 'Main Joint 2:', arm_joint_2
	# print 'Main Joint 3:', arm_joint_3

	pm.joint(rt_arm_root, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='ydown')
	arm_joint_3.jointOrientX.set(0)
	arm_joint_3.jointOrientY.set(0)
	rt_arm_root.rotateOrder.set(3)


	ik_joints = pm.duplicate(rt_arm_root)
	ik_joints = pm.ls(sl=True, dag=True)
	rt_ik_root = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	# print 'Ik Root:', rt_ik_root
	# print 'Ik Joint 2:', ik_joint_2
	# print 'Ik Joint 3:', ik_joint_3

	
	for each in ik_joints:
		joint_name = rt_arm_root.replace('bind', 'ik')
		rt_ik_root.rename(joint_name)

	joint_name = rt_ik_root.replace('1', '2')
	ik_joint_2.rename(joint_name)

	joint_name = ik_joint_2.replace('2', '3')
	ik_joint_3.rename(joint_name)

	twist_joints = pm.duplicate(rt_arm_root)
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
	rt_joint_12 = twist_joints[1]

	pm.delete(end_joint)

	jnt_name_12 = rt_joint_12.replace('07', '12')
	rt_joint_12.rename(jnt_name_12)
	jnt_name_7 = joint_7.replace('06_twist1', '07_twist')
	joint_7.rename(jnt_name_7)

	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_1 = pm.pointConstraint(joint_7, loc_1, mo=0, w=0)
	point_constraint_2 = pm.pointConstraint(rt_joint_12, loc_1, mo=0, w=1)
	jnt_name_11 = rt_joint_12.replace('12', '11')
	joint_11 = pm.joint(loc_1, name=jnt_name_11)

	loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_1 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_3 = pm.pointConstraint(joint_7 , loc_2, mo=0, w=.25)
	point_constraint_4 = pm.pointConstraint(rt_joint_12 , loc_2, mo=0, w=.75)
	jnt_name_10 = joint_11.replace('11', '10')
	joint_10 = pm.joint(loc_2, n=jnt_name_10)

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_2 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_5 = pm.pointConstraint(joint_7 ,loc_3, mo=0, w=.5)
	point_constraint_6 = pm.pointConstraint(rt_joint_12 ,loc_3, mo=0, w=.5)
	jnt_name_9 = joint_10.replace('10', '09')
	joint_9 = pm.joint(loc_3, n=jnt_name_9)

	loc_4 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint_3 = pm.orientConstraint(joint_7, loc_1, mo=0)
	point_constraint_7 = pm.pointConstraint(joint_7 ,loc_4, mo=0, w=.75)
	point_constraint_8 = pm.pointConstraint(rt_joint_12 ,loc_4, mo=0, w=.25)
	jnt_name_8 = joint_9.replace('9', '8')
	joint_8 = pm.joint(loc_4, n=jnt_name_8)

	pm.parent(joint_11, joint_10)
	pm.parent(joint_10, joint_9)
	pm.parent(joint_9, joint_8)
	pm.parent(joint_8, joint_7)

	pm.delete(loc_1, loc_2, loc_3, loc_4)

	pm.parent(rt_joint_12, joint_11)


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

	cb_joint_3 = pm.duplicate(rt_joint_12)[0]

	bind_name = cb_joint_2.replace('2', '3')
	cb_joint_3.rename(bind_name)

	pm.parent(cb_joint_3, w=1)

	tempBind = pm.duplicate(rt_arm_root)

	pm.select(tempBind)
	temp_joints = pm.ls(sl=True, dag=True)
	temp_1 = temp_joints[0]
	temp_2 = temp_joints[1]
	temp_3 = temp_joints[2]

	temp_name = rt_arm_root.replace('bind', 'temp')
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

	ik_name = arm_curve_1.replace('crv', 'twist_ikh')
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

	pm.select(end_joint, rt_joint_12, arm_curve_2)
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

	pm.parentConstraint(arm_joint_3, cb_joint_3, mo=1)
	pm.parentConstraint(arm_joint_2, cb_joint_2, mo=1)
	pm.pointConstraint(rt_arm_root, cb_joint_1, mo=1)


	'''================================================================================================================'''
	pm.connectAttr(rt_ik_root + '.rotate', rt_arm_root + '.rotate')
	pm.connectAttr(ik_joint_2 + '.rotate', arm_joint_2 + '.rotate')
	pm.connectAttr(ik_joint_3 + '.rotate', arm_joint_3 + '.rotate')

	pm.connectAttr(rt_ik_root + '.translate', rt_arm_root + '.translate')
	pm.connectAttr(ik_joint_2 + '.translate', arm_joint_2 + '.translate')
	pm.connectAttr(ik_joint_3 + '.translate', arm_joint_3 + '.translate')

	'''
	Create the arm icon
	'''
	rt_arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	temp_constraint = pm.pointConstraint(arm_joint_3, rt_arm_icon)
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()

	'''
	Rename arm icon
	'''
	rt_arm_icon_name = rt_arm_root.replace('01_bind', 'icon')
	rt_arm_icon.rename(rt_arm_icon_name)


	'''
	Create the ik
	'''
	pm.select(rt_ik_root, ik_joint_3)
	arm_ikh = pm.ikHandle()[0]

	ikh_name = rt_arm_root.replace('bind', 'ikh')
	arm_ikh.rename(ikh_name)


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
	temp_constraint = pm.pointConstraint(arm_joint_2, elbow_icon)
	pm.delete(temp_constraint)
	freezeTransform(elbow_icon)
	pm.xform(elbow_icon, t=[0,0,-10], scale=[.5, .5, .5], ro=[90, 0, 0])
	freezeTransform(elbow_icon)

	'''
	Rename elbow icon
	'''
	elbow_icon_name = rt_arm_root.replace('arm_01_bind', 'elbow_icon')
	elbow_icon.rename(elbow_icon_name)

	'''
	Create the pole vector for the elbow
	'''
	pm.poleVectorConstraint(elbow_icon, arm_ikh)

	'''
	Parent the arm_ikh under the rt_arm_icon
	'''
	pm.parent(arm_ikh, rt_arm_icon)

	'''==========================================================================================================================='''

	upperArm_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = rt_arm_root.replace('01_bind', 'info')
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

	jnt_name = rt_arm_root.replace('bind', 'twist')
	rt_arm_root.rename(jnt_name)

	jnt_name = root_joint.replace('twist', 'bind')
	root_joint.rename(jnt_name)

	jnt_name = rt_arm_root.replace('t1', 't')
	rt_arm_root.rename(jnt_name)

	jnt_name = rt_arm_root.replace('01', '02')
	arm_joint_2.rename(jnt_name)

	jnt_name = rt_arm_root.replace('01', '03')
	arm_joint_3.rename(jnt_name)

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
	rt_joint_12.rename(jnt_name)

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

	temp_constraint = pm.parentConstraint(rt_arm_root, loc_1, mo=0)
	pm.delete(temp_constraint)
	pm.select(loc_1)
	freezeTransform(loc_1)

	loc_name = rt_arm_root.replace('01_twist', 'start_loc')
	loc_1.rename(loc_name)

	temp_constraint = pm.parentConstraint(arm_joint_3, loc_2, mo=0)
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

	pm.parentConstraint(rt_arm_icon, loc_2)

	upperArm_len = pm.getAttr(ik_joint_2 + '.tx')

	foreArm_len = pm.getAttr(ik_joint_3 + '.tx')

	sumLen = upperArm_len + foreArm_len

	pm.setDrivenKeyframe(ik_joint_2 + '.tx', currentDriver=arm_dist + '.distance', value=upperArm_len, driverValue=sumLen)

	pm.setDrivenKeyframe(ik_joint_2 + '.tx',  currentDriver=arm_dist + '.distance', value=(upperArm_len*2), driverValue=(sumLen*2))

	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=arm_dist + '.distance', value=foreArm_len, driverValue=sumLen)

	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=arm_dist + '.distance', value=(foreArm_len*2), driverValue=(sumLen*2))

	pm.keyTangent(ik_joint_2, ik_joint_3,'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.setInfinity(ik_joint_2, ik_joint_3, poi='linear')


	'''==========================================================================================================================='''

	loc_3 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(rt_arm_root, loc_3, mo=0)
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
	temp_constraint = pm.parentConstraint(arm_joint_3, loc_5, mo=0)
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
	temp_constraint = pm.pointConstraint(rt_arm_root, transform_1, mo=0)
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
	temp_constraint = pm.pointConstraint(arm_joint_3, transform_2, mo=0)
	pm.delete(temp_constraint)

	node_name = transform_1.replace('01','02')
	transform_2.rename(node_name)

	pm.connectAttr(loc_4 + '.worldPosition', snap_dist_2 + '.startPoint')

	pm.connectAttr(loc_5 + '.worldPosition', snap_dist_2 + '.endPoint')

	pm.parent(loc_4, elbow_icon)

	pm.parent(loc_5, rt_arm_icon)

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

	hybrid_fk_joints = pm.duplicate(ik_joint_2)
	pm.parent(hybrid_fk_joints, w=1)

	pm.select(hybrid_fk_joints)
	hJoints = pm.ls(sl=True,  dag=True)
	hJ_1 = hJoints[0]
	hJ_2 = hJoints[1]
	# print hJ_1
	# print hJ_2

	jnt_name = ik_joint_2.replace('ik', 'hybridFk')
	hJ_1.rename(jnt_name)

	jnt_name = hJ_1.replace('02', '03')
	hJ_2.rename(jnt_name)


	hybridFk_icon = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 2:', hybridFk_icon
	temp_constraint = pm.parentConstraint(ik_joint_2, hybridFk_icon)
	pm.delete(temp_constraint)
	hybridFk_pad = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(ik_joint_2, hybridFk_pad)
	pm.delete(temp_constraint)
	pm.parent(hybridFk_icon, hybridFk_pad)
	pm.select(hybridFk_icon)
	freezeTransform()

	'''
	Rename the icons and the pads
	'''

	hybridFk_icon_name = rt_ik_root.replace('01_ik', 'hybridFk_icon')
	hybridFk_icon.rename(hybridFk_icon_name)

	hybridFk_pad_name = hybridFk_icon.replace('icon', 'local')
	hybridFk_pad.rename(hybridFk_pad_name) 

	'''
	Create length attr
	'''
	pm.addAttr(hybridFk_icon, ln='length', at='double', min=0, dv=1)
	hybridFk_icon.length.set(e=1, keyable=True)
	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=hybridFk_icon + '.length')
	hybridFk_icon.length.set(0)
	ik_joint_3.tx.set(0)
	pm.setDrivenKeyframe(ik_joint_3 + '.tx', currentDriver=hybridFk_icon + '.length')
	hybridFk_icon.length.set(1)
	pm.keyTangent(ik_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(ik_joint_3 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	temp_constraint = pm.pointConstraint(elbow_icon, hJ_1, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(hJ_1)

	temp_constraint = pm.pointConstraint(elbow_icon, hybridFk_pad, mo=0)
	pm.delete(temp_constraint)

	pm.orientConstraint(hybridFk_icon, hJ_1)

	ik_cons_grp = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(arm_joint_3, ik_cons_grp)
	pm.delete(temp_constraint)
	freezeTransform(ik_cons_grp)
	pm.parent(arm_ikh, loc_5, ik_cons_grp)
	grp_name = twist_grp.replace('twist', 'cons')
	ik_cons_grp.rename(grp_name)
	constraint_1 = pm.parentConstraint(rt_arm_icon, ik_cons_grp, mo=0)
	const_1_targets = constraint_1.getWeightAliasList()[0]
	# print const_1_targets
	constraint_2 = pm.parentConstraint(hJ_2, ik_cons_grp, mo=0)
	const_2_targets = constraint_2.getWeightAliasList()[1]
	# print const_2_targets
	pm.parent(hybridFk_pad, elbow_icon)


	pm.addAttr(elbow_icon, ln='FK_foreArmBlend', at='double', min=0, max=1, dv=0)
	elbow_icon.FK_foreArmBlend.set(e=1, keyable=True)

	elbow_icon.FK_foreArmBlend.set(1)
	const_1_targets.set(0)
	pm.setDrivenKeyframe(const_1_targets, const_2_targets, currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hybridFk_icon + '.v',  currentDriver=elbow_icon + '.FK_foreArmBlend')
	elbow_icon.FK_foreArmBlend.set(0)
	const_1_targets.set(1)
	const_2_targets.set(0)
	hybridFk_icon.v.set(0)
	pm.setDrivenKeyframe(const_1_targets, const_2_targets, currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hybridFk_icon + '.v',  currentDriver=elbow_icon + '.FK_foreArmBlend')
	pm.setDrivenKeyframe(hJ_2 + '.tx', currentDriver=hybridFk_icon + '.length')
	hybridFk_icon.length.set(0)
	hJ_2.tx.set(0)
	length_sdk = pm.setDrivenKeyframe(hJ_2 + '.tx', currentDriver=hybridFk_icon + '.length')
	pm.keyTangent(hJ_2, itt='clamped', ott='clamped')
	pm.setInfinity(hJ_2, poi='linear')
	hybridFk_icon.length.set(1)

	pm.select(loc_1, loc_2, loc_3, loc_4, loc_5, snap_dist_1, snap_dist_2, rt_ik_root, arm_dist, arm_ikh, arm_ik_1, arm_ik_2, rt_arm_root, arm_curve_1, arm_curve_2, hJ_1)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	pm.select(cl=1)

def armSetup(*args):
	lt_armSetup()
	rt_armSetup()

def ikArmSetup(*args):
	lt_ikArmSetup()
	rt_ikArmSetup()	

def fkArmSetup(*args):
	lt_fkArmSetup()
	rt_fkArmSetup()

def armSystem(*args):
	ori_selection_type = pm.radioButtonGrp('arm_orientationOption', q=1, sl=1) 
	# print 'Orientation Selection:', ori_selection_type

	system_selection_type = pm.radioButtonGrp('arm_systemOption', q=1, sl=1)
	# print 'System Selection:', system_selection_type

	if ori_selection_type == 1:
		pass 
		if system_selection_type == 1:
			lt_fkArmSetup()
	if ori_selection_type == 2:
		pass
		if system_selection_type == 1:
			rt_fkArmSetup()
	if ori_selection_type == 3:
		pass
		if system_selection_type == 1:
			fkArmSetup()

	if ori_selection_type == 1:
		pass 
		if system_selection_type == 2:
			lt_ikArmSetup()
	if ori_selection_type == 2:
		pass
		if system_selection_type == 2:
			rt_ikArmSetup()
	if ori_selection_type == 3:
		pass
		if system_selection_type == 2:
			ikArmSetup()
	if ori_selection_type == 1:
		pass 
		if system_selection_type == 3:
			lt_armSetup()
	if ori_selection_type == 2:
		pass
		if system_selection_type == 3:
			rt_armSetup()
	if ori_selection_type == 3:
		pass
		if system_selection_type == 3:
			armSetup()

def lt_handSetup(*args):
	global lt_arm_joint_12, lt_arm_joint_3, lt_hand_root, lt_hand_joint_2, lt_hand_icon, lt_world_pad, lt_hand_local
	if pm.objExists('lt_arm_12_bind'):
		pm.select('lt_arm_12_bind')
		lt_arm_joint_12 = pm.ls(sl=1, dag=1)
		print 'Arm Joint 12:', lt_arm_joint_12

		pm.select(lt_hand_01_bind)
		hand_joints = pm.ls(sl=1, dag=1)
		lt_hand_root = hand_joints[0]
		lt_hand_joint_2 = hand_joints[1]

		create_circle()
		print 'Hand Icon:', icon
		pm.select(icon)
		lt_hand_icon = pm.ls(sl=1)
		temp_constraint = pm.parentConstraint(lt_hand_root, lt_hand_icon, mo=0)
		pm.delete(temp_constraint)
		freezeTransform()

		icon_name = lt_hand_root.replace('01_bind', 'icon')
		print 'Icon name:', icon_name
		icon.rename(icon_name)

		lt_hand_local = pm.group(empty=1)

		temp_constraint = pm.parentConstraint(lt_hand_root, lt_hand_local, mo=0)
		pm.delete(temp_constraint)

		local_name = icon.replace('icon', 'local')
		print 'Local Name:', local_name
		lt_hand_local.rename(local_name)

		pm.parent(lt_hand_icon, lt_hand_local)
		freezeTransform(icon)
		deleteHistory(icon)

		local_const = pm.pointConstraint(lt_arm_joint_12, lt_hand_local)


		lt_world_pad = pm.group(empty=1)
		temp_constraint = pm.parentConstraint(lt_hand_root, lt_world_pad, mo=0)
		pm.delete(temp_constraint)

		world_name = lt_hand_local.replace('local', 'world')
		lt_world_pad.rename(world_name)

		pm.parentConstraint(lt_hand_icon, lt_hand_root, mo=1)

		pm.select(lt_arm_joint_12, lt_world_pad, lt_hand_local)
		const = pm.orientConstraint(lt_arm_joint_12, lt_world_pad, lt_hand_local, mo=0)
		local_const = const.getWeightAliasList()[0]
		world_const = const.getWeightAliasList()[1]

		print 'Local Const:', local_const
		print 'World Const:', world_const

		pm.addAttr(lt_hand_icon, ln="localWorld", max=10, dv=0, at='double', min=0)
		icon.localWorld.set(e=1, keyable=True)

		world_const.set(0)
		pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')
		icon.localWorld.set(10)
		world_const.set(1)
		local_const.set(0)
		pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')

		pm.addAttr(lt_hand_icon, ln="fkVis", at='bool')
		icon.fkVis.set(e=1, keyable=True)
	else:
		pm.select(lt_arm_01_bind)
		arm_joints = pm.ls(sl=1, dag=1)
		lt_arm_joint_3 = arm_joints[2]
		print 'Arm Joint 3:', lt_arm_joint_3

		'''
		Create the arm icon
		'''
		arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
		temp_constraint = pm.pointConstraint(lt_arm_joint_3, arm_icon)
		pm.delete(temp_constraint)
		freezeTransform()
		deleteHistory()


		pm.select(lt_hand_01_bind)
		hand_joints = pm.ls(sl=1, dag=1)
		lt_hand_root = hand_joints[0]
		lt_hand_joint_2 = hand_joints[1]

		pm.select(arm_icon)
		ctrlPadding()

		create_circle()
		print 'Hand Icon:', icon
		pm.select(icon)
		lt_hand_icon = pm.ls(sl=1)
		temp_constraint = pm.parentConstraint(lt_hand_root, lt_hand_icon, mo=0)
		pm.delete(temp_constraint)
		freezeTransform()

		icon_name = lt_hand_root.replace('01_bind', 'icon')
		print 'Icon name:', icon_name
		icon.rename(icon_name)

		lt_hand_local = pm.group(empty=1)

		temp_constraint = pm.parentConstraint(lt_hand_root, lt_hand_local, mo=0)
		pm.delete(temp_constraint)

		local_name = icon.replace('icon', 'local')
		print 'Local Name:', local_name
		lt_hand_local.rename(local_name)

		pm.parent(lt_hand_icon, lt_hand_local)
		freezeTransform(icon)
		deleteHistory(icon)

		local_const = pm.pointConstraint(lt_arm_joint_3, lt_hand_local)


		lt_world_pad = pm.group(empty=1)
		temp_constraint = pm.parentConstraint(lt_hand_root, lt_world_pad, mo=0)
		pm.delete(temp_constraint)

		world_name = lt_hand_local.replace('local', 'world')
		lt_world_pad.rename(world_name)

		pm.parentConstraint(lt_hand_icon, lt_hand_root, mo=1)

		pm.select(lt_arm_joint_3, lt_world_pad, lt_hand_local)
		const = pm.orientConstraint(lt_arm_joint_3, lt_world_pad, lt_hand_local, mo=0)
		local_const = const.getWeightAliasList()[0]
		world_const = const.getWeightAliasList()[1]

		print 'Local Const:', local_const
		print 'World Const:', world_const

		pm.addAttr(lt_hand_icon, ln="localWorld", max=10, dv=0, at='double', min=0)
		icon.localWorld.set(e=1, keyable=True)

		world_const.set(0)
		pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')
		icon.localWorld.set(10)
		world_const.set(1)
		local_const.set(0)
		pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')

		pm.addAttr(lt_hand_icon, ln="fkVis", at='bool')
		icon.fkVis.set(e=1, keyable=True)

def rt_handSetup(*args):
	global rt_arm_joint_12, rt_arm_joint_3, rt_hand_root, rt_hand_joint_2, rt_hand_icon, rt_world_pad, rt_hand_local
	if pm.objExists('rt_arm_12_bind'):
		pm.select('rt_arm_12_bind')
		rt_arm_joint_12 = pm.ls(sl=1, dag=1)
		print 'Arm Joint 12:', rt_arm_joint_12

		pm.select(rt_hand_01_bind)
		hand_joints = pm.ls(sl=1, dag=1)
		rt_hand_root = hand_joints[0]
		rt_hand_joint_2 = hand_joints[1]

		create_circle()
		print 'Hand Icon:', icon
		pm.select(icon)
		rt_hand_icon = pm.ls(sl=1)
		temp_constraint = pm.parentConstraint(rt_hand_root, rt_hand_icon, mo=0)
		pm.delete(temp_constraint)
		freezeTransform()

		icon_name = rt_hand_root.replace('01_bind', 'icon')
		print 'Icon name:', icon_name
		icon.rename(icon_name)

		rt_hand_local = pm.group(empty=1)

		temp_constraint = pm.parentConstraint(rt_hand_root, rt_hand_local, mo=0)
		pm.delete(temp_constraint)

		local_name = icon.replace('icon', 'local')
		print 'Local Name:', local_name
		rt_hand_local.rename(local_name)

		pm.parent(rt_hand_icon, rt_hand_local)
		freezeTransform(icon)
		deleteHistory(icon)

		local_const = pm.pointConstraint(rt_arm_joint_12, rt_hand_local)


		rt_world_pad = pm.group(empty=1)
		temp_constraint = pm.parentConstraint(rt_hand_root, rt_world_pad, mo=0)
		pm.delete(temp_constraint)

		world_name = rt_hand_local.replace('local', 'world')
		rt_world_pad.rename(world_name)

		pm.parentConstraint(rt_hand_icon, rt_hand_root, mo=1)

		pm.select(rt_arm_joint_12, rt_world_pad, rt_hand_local)
		const = pm.orientConstraint(rt_arm_joint_12, rt_world_pad, rt_hand_local, mo=0)
		local_const = const.getWeightAliasList()[0]
		world_const = const.getWeightAliasList()[1]

		print 'Local Const:', local_const
		print 'World Const:', world_const

		pm.addAttr(rt_hand_icon, ln="localWorld", max=10, dv=0, at='double', min=0)
		icon.localWorld.set(e=1, keyable=True)

		world_const.set(0)
		pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')
		icon.localWorld.set(10)
		world_const.set(1)
		local_const.set(0)
		pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')

		pm.addAttr(rt_hand_icon, ln="fkVis", at='bool')
		icon.fkVis.set(e=1, keyable=True)
	else:
		pm.select(rt_arm_01_bind)
		arm_joints = pm.ls(sl=1, dag=1)
		rt_arm_joint_3 = arm_joints[2]
		print 'Arm Joint 3:', rt_arm_joint_3

		'''
		Create the arm icon
		'''
		arm_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
		temp_constraint = pm.pointConstraint(rt_arm_joint_3, arm_icon)
		pm.delete(temp_constraint)
		freezeTransform()
		deleteHistory()


		pm.select(rt_hand_01_bind)
		hand_joints = pm.ls(sl=1, dag=1)
		rt_hand_root = hand_joints[0]
		rt_hand_joint_2 = hand_joints[1]

		pm.select(arm_icon)
		ctrlPadding()

		create_circle()
		print 'Hand Icon:', icon
		pm.select(icon)
		rt_hand_icon = pm.ls(sl=1)
		temp_constraint = pm.parentConstraint(rt_hand_root, rt_hand_icon, mo=0)
		pm.delete(temp_constraint)
		freezeTransform()

		icon_name = rt_hand_root.replace('01_bind', 'icon')
		print 'Icon name:', icon_name
		icon.rename(icon_name)

		rt_hand_local = pm.group(empty=1)

		temp_constraint = pm.parentConstraint(rt_hand_root, rt_hand_local, mo=0)
		pm.delete(temp_constraint)

		local_name = icon.replace('icon', 'local')
		print 'Local Name:', local_name
		rt_hand_local.rename(local_name)

		pm.parent(rt_hand_icon, rt_hand_local)
		freezeTransform(icon)
		deleteHistory(icon)

		local_const = pm.pointConstraint(rt_arm_joint_3, rt_hand_local)


		rt_world_pad = pm.group(empty=1)
		temp_constraint = pm.parentConstraint(rt_hand_root, rt_world_pad, mo=0)
		pm.delete(temp_constraint)

		world_name = rt_hand_local.replace('local', 'world')
		rt_world_pad.rename(world_name)

		pm.parentConstraint(rt_hand_icon, rt_hand_root, mo=1)

		pm.select(rt_arm_joint_3, rt_world_pad, rt_hand_local)
		const = pm.orientConstraint(rt_arm_joint_3, rt_world_pad, rt_hand_local, mo=0)
		local_const = const.getWeightAliasList()[0]
		world_const = const.getWeightAliasList()[1]

		print 'Local Const:', local_const
		print 'World Const:', world_const

		pm.addAttr(rt_hand_icon, ln="localWorld", max=10, dv=0, at='double', min=0)
		icon.localWorld.set(e=1, keyable=True)

		world_const.set(0)
		pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')
		icon.localWorld.set(10)
		world_const.set(1)
		local_const.set(0)
		pm.setDrivenKeyframe(world_const, local_const, currentDriver= icon + '.localWorld')

		pm.addAttr(rt_hand_icon, ln="fkVis", at='bool')
		icon.fkVis.set(e=1, keyable=True)

def handSetup(*args):
	lt_handSetup()
	rt_handSetup()

def handSystem(*args):
	ori_selection_type = pm.radioButtonGrp('hand_orientationOption', q=1, sl=1) 
	# print 'Orientation Selection:', ori_selection_type

	if ori_selection_type == 1:
		lt_handSetup()
	if ori_selection_type == 2:
		rt_handSetup()
	if ori_selection_type == 3:
		handSetup()

def backSetup(*args):
	global back_root, back_joint_2, back_joint_3, back_joint_4, back_joint_5, back_joint_6, back_joint_7
	global back_ik, back_pad, chest_icon, hip_icon, back_fk_local_1, back_fk_icon_1
	pm.select(ct_back_01_bind)
	bind_system = pm.ls(sl=True, dag=True)

	back_root = bind_system[0]
	back_joint_2 = bind_system[1]
	back_joint_3 = bind_system[2]
	back_joint_4 = bind_system[3]
	back_joint_5 = bind_system[4]
	back_joint_6 = bind_system[5]
	back_joint_7 = bind_system[6]

	back_pad = pm.group(empty=True)

	temp_constraint = pm.pointConstraint(back_root, back_pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(back_pad)
	deleteHistory(back_pad)

	pm.parent(back_root, back_pad)
	grp_name = back_root.replace('01_bind', '00_pad')
	back_pad.rename(grp_name)

	pm.select(back_pad)

	bind_system = pm.ls(sl=True, dag=True)

	back_pad = bind_system[0]
	back_root = bind_system[1]
	back_joint_2 = bind_system[2]
	back_joint_3 = bind_system[3]
	back_joint_4 = bind_system[4]
	back_joint_5 = bind_system[5]
	back_joint_6 = bind_system[6]
	back_joint_7 = bind_system[7]

	pm.select(back_root)
	joints = joint_positions(back_root) 
	back_curve = pm.curve(d = 1, p=joints)
	# print back_curve
	
	curve_joints = pm.duplicate(back_root)

	pm.select(curve_joints)
	curve_joints = pm.ls(sl=True, dag=True)
	cB_back_joint_1 = curve_joints[0]
	cB_back_joint_2 = curve_joints[1]
	cB_back_joint_3 = curve_joints[2]
	cB_back_joint_4 = curve_joints[3]
	cB_back_joint_5 = curve_joints[4]
	cB_back_joint_6 = curve_joints[5]
	cB_back_joint_7 = curve_joints[6]

	fk_joints = pm.duplicate(back_root)

	pm.select(fk_joints)
	fk_joints = pm.ls(sl=True, dag=True)

	fk_back_joint_1 = fk_joints[0]
	fk_back_joint_2 = fk_joints[1]
	fk_back_joint_3 = fk_joints[2]
	fk_back_joint_4 = fk_joints[3]
	fk_back_joint_5 = fk_joints[4]
	fk_back_joint_6 = fk_joints[5]
	fk_back_joint_7 = fk_joints[6]

	'''
	Step one: Create the ik
	'''
	pm.select(back_root, back_joint_7, back_curve)
	back_ik = pm.ikHandle(sol='ikSplineSolver', pcv=False, ccv=False)[0]
	ik_name = back_root.replace('01_bind', 'ikh')
	back_ik.rename(ik_name)
	curve_name = back_ik.replace('ikh', 'crv')
	back_curve.rename(curve_name)
	back_ik.twist.set(-90)
	back_curve.inheritsTransform.set(0)

	'''
	Step two: Rename and bind the curveBind
	'''
	pm.parent(cB_back_joint_7, back_pad)
	back_7_name = back_pad.replace('00_pad', '02_curveBind')
	cB_back_joint_7.rename(back_7_name)

	pm.delete(cB_back_joint_2)

	back_1_name = cB_back_joint_7.replace('02', '01')
	cB_back_joint_1.rename(back_1_name)

	pm.select(cB_back_joint_1, cB_back_joint_7, back_curve)
	pm.mel.SmoothBindSkin()

	'''
	Step Three: Create and move the chest and hip icons
	'''
	hip_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	temp_constraint = pm.parentConstraint(back_root, hip_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(hip_icon)
	deleteHistory(hip_icon)
	icon_naame = back_root.replace('back_01_bind', 'hip_icon')
	hip_icon.rename(icon_naame)

	chest_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	deleteHistory(chest_icon)
	icon_naame = hip_icon.replace('hip', 'chest')
	chest_icon.rename(icon_naame)

	temp_constraint = pm.pointConstraint(back_joint_7, chest_icon)
	pm.delete(temp_constraint)
	freezeTransform()

	hip_icon.rotateOrder.set(2)
	chest_icon.rotateOrder.set(2)
	cB_back_joint_1.rotateOrder.set(2)
	cB_back_joint_7.rotateOrder.set(2)

	pm.parentConstraint(chest_icon, cB_back_joint_7, mo=1)
	pm.parentConstraint(hip_icon, cB_back_joint_1, mo=1)


	back_ik.dTwistControlEnable.set(1)
	back_ik.dWorldUpType.set(4)

	back_ik.dWorldUpAxis.set(1)
	back_ik.dWorldUpVectorY.set(-1)
	back_ik.dWorldUpVectorEndY.set(-1)
	back_ik.dWorldUpVectorEndZ.set(0)

	pm.connectAttr(cB_back_joint_1 + '.xformMatrix', back_ik + '.dWorldUpMatrix')
	pm.connectAttr(cB_back_joint_7 + '.xformMatrix', back_ik + '.dWorldUpMatrixEnd')


	'''
	Step Four: Create the fk System
	'''
	pm.parent(fk_back_joint_3, fk_back_joint_1)
	pm.delete(fk_back_joint_2)
	pm.parent(fk_back_joint_5, fk_back_joint_3)
	pm.delete(fk_back_joint_4)
	pm.parent(fk_back_joint_7, fk_back_joint_5)
	pm.delete(fk_back_joint_6)

	back_joint_name = fk_back_joint_1.replace('bind2', 'fk')
	fk_back_joint_1.rename(back_joint_name)

	back_joint_name = fk_back_joint_1.replace('01', '02')
	fk_back_joint_3.rename(back_joint_name)

	back_joint_name = fk_back_joint_3.replace('02', '03')
	fk_back_joint_5.rename(back_joint_name)

	back_joint_name = fk_back_joint_7.replace('07_waste', '04_fk')
	fk_back_joint_7.rename(back_joint_name)

	fk_back_joint_1.rotateOrder.set(1)
	fk_back_joint_3.rotateOrder.set(1)
	fk_back_joint_5.rotateOrder.set(1)
	fk_back_joint_7.rotateOrder.set(1)

	hip_local = pm.group(hip_icon)

	chest_local = pm.group(chest_icon)

	local_name = hip_icon.replace('icon', 'local')
	hip_local.rename(local_name)

	local_name = chest_icon.replace('icon', 'local')
	chest_local.rename(local_name)

	pm.parentConstraint(fk_back_joint_1, hip_local, mo=1)
	pm.parentConstraint(fk_back_joint_7, chest_local, mo=1)

	back_fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	deleteHistory(back_fk_icon_1)
	back_fk_icon_2 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(1, 0, 0))[0]
	deleteHistory(back_fk_icon_2)

	temp_constraint = pm.parentConstraint(fk_back_joint_3, back_fk_icon_1, mo=0)
	pm.delete(temp_constraint)
	temp_constraint = pm.parentConstraint(fk_back_joint_5, back_fk_icon_2, mo=0)
	pm.delete(temp_constraint)
	pm.orientConstraint(back_fk_icon_1, fk_back_joint_3, mo=1)
	pm.orientConstraint(back_fk_icon_2, fk_back_joint_5, mo=1)

	back_fk_local_1 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_back_joint_3, back_fk_local_1)
	pm.delete(temp_constraint)
	pm.parent(back_fk_icon_1, back_fk_local_1)	

	back_fk_local_2 = pm.group(empty=True)
	temp_constraint = pm.parentConstraint(fk_back_joint_5, back_fk_local_2)
	pm.delete(temp_constraint)
	pm.parent(back_fk_icon_2, back_fk_local_2)
	pm.select(back_fk_icon_1, back_fk_icon_2)
	freezeTransform()

	pm.parent(back_fk_local_2, back_fk_icon_1)

	icon_naame = hip_icon.replace('hip', 'back_01_fk')
	back_fk_icon_1.rename(icon_naame)

	icon_naame = back_fk_icon_1.replace('01', '02')
	back_fk_icon_2.rename(icon_naame)

	local_name = back_fk_icon_1.replace('icon', 'local')
	back_fk_local_1.rename(local_name)

	local_name =back_fk_icon_2.replace('icon', 'local')
	back_fk_local_2.rename(local_name)

	'''
	Step five: Node Network
	'''
	curve_info = pm.shadingNode('curveInfo', asUtility=1)
	node_name = back_curve.replace('crv', 'info')
	curve_info.rename(node_name)

	pm.connectAttr(back_curve + '.worldSpace', curve_info + '.inputCurve')

	stretch_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	node_name = curve_info.replace('info', 'mult')
	stretch_mult.rename(node_name)
	stretch_mult.operation.set(2)

	pm.connectAttr(curve_info + '.arcLength', stretch_mult + '.input1X')

	arcLen = curve_info.arcLength.get()
	stretch_mult.input2X.set(arcLen)
	pm.connectAttr(stretch_mult + '.outputX', back_root + '.sx')
	pm.connectAttr(stretch_mult + '.outputX', back_joint_2 + '.sx')
	pm.connectAttr(stretch_mult + '.outputX', back_joint_3 + '.sx')
	pm.connectAttr(stretch_mult + '.outputX', back_joint_4 + '.sx')
	pm.connectAttr(stretch_mult + '.outputX', back_joint_5 + '.sx')
	pm.connectAttr(stretch_mult + '.outputX', back_joint_6 + '.sx')

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


	pm.connectAttr(stretch_invert + '.outputX', back_root + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_2 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_3 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_4 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_5 + '.sy')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_6 + '.sy')

	pm.connectAttr(stretch_invert + '.outputX', back_root + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_2 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_3 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_4 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_5 + '.sz')
	pm.connectAttr(stretch_invert + '.outputX', back_joint_6 + '.sz')

	'''
	Step six: Back Global
	'''

	back_global = pm.curve(p=[(0.5, 0, 0.5), (-0.5, 0, 0.5), (-0.5, 0, -0.5), (0.5, 0, -0.5), (0.5, 0, 0.5)], k=[0, 1, 2, 3, 4], d=1)
	icon_naame = hip_icon.replace('hip', 'body')
	back_global.rename(icon_naame)

	temp_constraint = pm.pointConstraint(back_root, back_global, mo=0)
	pm.delete(temp_constraint)
	pm.select(back_global)
	deleteHistory()
	freezeTransform()
	back_global.rotateOrder.set(2)

	pm.parent(back_fk_local_1, chest_local, hip_local, back_ik, back_pad)

	pm.parentConstraint(back_global, back_pad, mo=1)

	'''
	Step eight: DNT grp
	'''
	dnt_grp = pm.group(back_curve, cB_back_joint_1, cB_back_joint_7, fk_back_joint_1)
	grp_name = back_pad.replace('00_pad', 'DO____NOT____TOUCH')
	dnt_grp.rename(grp_name)
	dnt_grp.overrideEnabled.set(1)
	dnt_grp.overrideDisplayType.set(2)
	dnt_grp.v.set(0)

	pm.setAttr(back_fk_icon_1 + '.tx', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_1 + '.ty', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_1 + '.tz', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_1 + '.sx', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_1 + '.sy', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_1 + '.sz', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_1 + '.v', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_2 + '.tx', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_2 + '.ty', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_2 + '.tz', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_2 + '.sx', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_2 + '.sy', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_2 + '.sz', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_fk_icon_2 + '.v', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_global + '.sx', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_global +'.sy', lock=True, channelBox=False, keyable=False)
	pm.setAttr(back_global + '.sz', lock=True, channelBox=False, keyable=False)
	
	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(back_root, loc_1)
	pm.delete(temp_constraint)
	freezeTransform(loc_1)

	loc_name = back_global.replace('_icon', 'Space_loc')
	loc_1.rename(loc_name)

	pm.parent(loc_1, dnt_grp)
	pm.parent(dnt_grp, back_pad)

def hipSetup(*args):
	global hip_joint, hip_loc
	pm.select(ct_hip_bind)
	selection = pm.ls(sl=1)
	hip_joint = selection[0]

	hip_loc = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.parentConstraint(hip_joint, hip_loc, mo=0)
	pm.delete(temp_constraint)
	pm.select(hip_loc)
	freezeTransform(hip_loc)

	loc_name = hip_joint.replace('_01_bind', '_space_loc')
	hip_loc.rename(loc_name)
	pm.parent(hip_loc, hip_joint)

	global root_joint, root_loc
	pm.select(ct_root_waste)
	selection = pm.ls(sl=1)
	root_joint = selection[0]

	root_loc = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.parentConstraint(root_joint, root_loc, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(root_loc)

	loc_name = root_joint.replace('waste', 'space_loc')
	root_loc.rename(loc_name)
	pm.parent(root_loc, root_joint)

def lt_legSetup(*args):
	global lt_leg_pad, lt_foot_icon, lt_knee_dist_1, lt_knee_dist_2, lt_leg_dist, lt_switch, lt_leg_fk_local_1
	global lt_loc_1, lt_loc_2, lt_leg_ikh, lt_ankle_ikh, lt_toe_ikh, lt_noFlip_local
	global lt_leg_fk_icon_1, lt_leg_fk_icon_2, lt_leg_fk_icon_3, lt_leg_fk_icon_4
	global lt_leg_root, lt_leg_joint_2, lt_leg_joint_3, lt_leg_joint_4
	'''
	Get bind joints
	'''
	pm.select(lt_leg_01_bind)
	selection = pm.ls(sl=1, dag=1)
	lt_leg_root = selection[0]
	lt_leg_joint_2 = selection[1]
	lt_leg_joint_3 = selection[2]
	lt_leg_joint_4 = selection[3]
	lt_leg_joint_5 = selection[4]
	# print 'Leg Root:', lt_leg_root
	# print 'Leg Joint 2:', lt_leg_joint_2
	# print 'Leg Joint 3:', lt_leg_joint_3
	# print 'Leg Joint 4:', lt_leg_joint_4
	# print 'Leg Joint 5:', lt_leg_joint_5
	pm.joint(zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='xup')
	lt_leg_joint_5.jointOrientX.set(0)
	lt_leg_joint_5.jointOrientZ.set(0)
	for each in selection:
		each.rotateOrder.set(3)

	'''
	Make ik joints
	'''

	ik_joints = pm.duplicate(lt_leg_root)
	pm.select(ik_joints)
	ik_joints = pm.ls(sl=1, dag=1)
	lt_ik_root = ik_joints[0]
	lt_ik_joint_2 = ik_joints[1]
	lt_ik_joint_3 = ik_joints[2]
	lt_ik_joint_4 = ik_joints[3]
	lt_ik_joint_5 = ik_joints[4]

	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'ik'
	for each in ik_joints:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)


	# print 'IK Root:', lt_ik_root
	# print 'IK Joint 2:', lt_ik_joint_2
	# print 'IK Joint 3:', lt_ik_joint_3
	# print 'IK Joint 4:', lt_ik_joint_4
	# print 'IK Joint 5:', lt_ik_joint_5
		
	'''
	Make fk joints
	'''

	fk_joints = pm.duplicate(lt_leg_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=1, dag=1)
	lt_fk_root = fk_joints[0]
	lt_fk_joint_2 = fk_joints[1]
	lt_fk_joint_3 = fk_joints[2]
	lt_fk_joint_4 = fk_joints[3]
	lt_fk_joint_5 = fk_joints[4]


	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'fk'
	for each in fk_joints:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)

	# print 'FK Root:', lt_fk_root
	# print 'FK Joint 2:', lt_fk_joint_2
	# print 'FK Joint 3:', lt_fk_joint_3
	# print 'FK Joint 4:', lt_fk_joint_4
	# print 'FK Joint 5:', lt_fk_joint_5

	ikfk_blend_1 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_2 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_3 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_4 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_1, ikfk_blend_2, ikfk_blend_3, ikfk_blend_4)
	ikfk_rot_blenders = pm.ls(sl=1)
	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_rot_blend'
	for each in ikfk_rot_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	pm.connectAttr(lt_ik_root + '.rotate', ikfk_blend_1 + '.color2')
	pm.connectAttr(lt_fk_root + '.rotate', ikfk_blend_1 + '.color1')

	pm.connectAttr(lt_ik_joint_2 + '.rotate', ikfk_blend_2 + '.color2')
	pm.connectAttr(lt_fk_joint_2 + '.rotate', ikfk_blend_2 + '.color1')

	pm.connectAttr(lt_ik_joint_3 + '.rotate', ikfk_blend_3 + '.color2')
	pm.connectAttr(lt_fk_joint_3 + '.rotate', ikfk_blend_3 + '.color1')

	pm.connectAttr(lt_ik_joint_4 + '.rotate', ikfk_blend_4 + '.color2')
	pm.connectAttr(lt_fk_joint_4 + '.rotate', ikfk_blend_4 + '.color1')


	'''
	Create the IK/FK switch
	'''
	ikfk_shape_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	ikfk_shape_2 = pm.curve(p=[(0, 0, -1), (0, 0, 1)], k=[0, 1], d=1)
	ikfk_shape_3 = pm.curve(p=[(-1, 0, 0), (1, 0, 0)], k=[0, 1], d=1)
	ikfk_shape_4 = pm.curve(p=[(0, 0, 1), (0, 0, 3)], k=[0, 1], d=1)

	pm.select(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4)
	ikfk_shapes = pm.ls(sl=1)

	suffix = 'ikfk_curve'

	for each in ikfk_shapes:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)

	lt_switch = pm.group(empty=True)
	pm.select(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4, lt_switch)
	shapes = pm.ls(selection=True, dag=True)
	curveShape_1 = shapes[1]
	curveShape_2 = shapes[3]
	curveShape_3 = shapes[5]
	curveShape_4 = shapes[7]
	lt_switch_grp = shapes[8]
	# print 'Curve Shape 1:', curveShape_1
	# print 'Curve Shape 2:', curveShape_2
	# print 'Curve Shape 3:', curveShape_3
	# print 'Curve Shape 4:', curveShape_4
	# print 'Switch:', lt_switch_grp
	pm.select(ikfk_shape_2, ikfk_shape_3)

	pm.cmds.scale(0.768, 0.768, 0.768)
	freezeTransform()

	pm.parent(curveShape_1, curveShape_2, curveShape_3, curveShape_4, lt_switch, s=1, r=1)
	pm.delete(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4)
	pm.cmds.move(0, 0, 3, lt_switch + '.scalePivot', lt_switch + '.rotatePivot', rpr=1)

	pm.xform(lt_switch, ro=[0,0,90], scale=[1.5,1.5,1.5])
	freezeTransform(lt_switch)
	deleteHistory()
	temp_constraint = pm.pointConstraint(lt_leg_joint_3, lt_switch, mo=0, w=1)
	pm.delete(temp_constraint)
	pm.select(lt_switch)
	freezeTransform()
	lt_switch_name = lt_leg_root.replace('01_bind', 'IkFk_switch')
	lt_switch.rename(lt_switch_name)
	pm.parentConstraint(lt_leg_joint_3, lt_switch, mo=1)

	'''
	Add IkFk attribute
	'''
	pm.addAttr(lt_switch, ln="IkFk", nn='Ik/Fk', max=1, dv=0, at='double', min=0)
	lt_switch.IkFk.set(e=1, keyable=True)

	'''
	Lock Attrs
	'''
	lock_and_hide(lt_switch, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])

	'''
	Connect the switch to the blenders
	'''
	pm.connectAttr(lt_switch + '.IkFk', ikfk_blend_1 + '.blender')
	pm.connectAttr(lt_switch + '.IkFk', ikfk_blend_2 + '.blender')
	pm.connectAttr(lt_switch + '.IkFk', ikfk_blend_3 + '.blender')
	pm.connectAttr(lt_switch + '.IkFk', ikfk_blend_4 + '.blender')

	'''
	Connect the output to the bind
	'''
	pm.connectAttr(ikfk_blend_1 + '.output', lt_leg_root + '.rotate')
	pm.connectAttr(ikfk_blend_2 + '.output', lt_leg_joint_2 + '.rotate')
	pm.connectAttr(ikfk_blend_3 + '.output', lt_leg_joint_3 + '.rotate')
	pm.connectAttr(ikfk_blend_4 + '.output', lt_leg_joint_4 + '.rotate')


	ikfk_blend_5 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_6 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_7 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_8 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_5, ikfk_blend_6, ikfk_blend_7, ikfk_blend_8)
	ikfk_tran_blenders = pm.ls(sl=1)
	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_tran_blend'
	for each in ikfk_tran_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	pm.connectAttr(lt_ik_root + '.translate', ikfk_blend_5 + '.color2')
	pm.connectAttr(lt_fk_root + '.translate', ikfk_blend_5 + '.color1')

	pm.connectAttr(lt_ik_joint_2 + '.translate', ikfk_blend_6 + '.color2')
	pm.connectAttr(lt_fk_joint_2 + '.translate', ikfk_blend_6 + '.color1')

	pm.connectAttr(lt_ik_joint_3 + '.translate', ikfk_blend_7 + '.color2')
	pm.connectAttr(lt_fk_joint_3 + '.translate', ikfk_blend_7 + '.color1')

	pm.connectAttr(lt_ik_joint_4 + '.translate', ikfk_blend_8 + '.color2')
	pm.connectAttr(lt_fk_joint_4 + '.translate', ikfk_blend_8 + '.color1')

	pm.connectAttr(lt_switch + '.IkFk', ikfk_blend_5 + '.blender')
	pm.connectAttr(lt_switch + '.IkFk', ikfk_blend_6 + '.blender')
	pm.connectAttr(lt_switch + '.IkFk', ikfk_blend_7 + '.blender')
	pm.connectAttr(lt_switch + '.IkFk', ikfk_blend_8 + '.blender')

	pm.connectAttr(ikfk_blend_5 + '.output', lt_leg_root + '.translate')
	pm.connectAttr(ikfk_blend_6 + '.output', lt_leg_joint_2 + '.translate')
	pm.connectAttr(ikfk_blend_7 + '.output', lt_leg_joint_3 + '.translate')
	pm.connectAttr(ikfk_blend_8 + '.output', lt_leg_joint_4 + '.translate')

	'''
	Create fk icons
	'''
	lt_leg_fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', lt_leg_fk_icon_1
	temp_constraint = pm.parentConstraint(lt_fk_root, lt_leg_fk_icon_1)
	pm.delete(temp_constraint)
	lt_leg_fk_local_1 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_fk_root, lt_leg_fk_local_1)
	pm.delete(temp_constraint)
	pm.parent(lt_leg_fk_icon_1, lt_leg_fk_local_1)
	pm.select(lt_leg_fk_icon_1)
	freezeTransform()


	lt_leg_fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 2:', lt_leg_fk_icon_2
	temp_constraint = pm.parentConstraint(lt_fk_joint_2, lt_leg_fk_icon_2)
	pm.delete(temp_constraint)
	lt_leg_fk_local_2 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_fk_joint_2, lt_leg_fk_local_2)
	pm.delete(temp_constraint)
	pm.parent(lt_leg_fk_icon_2, lt_leg_fk_local_2)
	pm.select(lt_leg_fk_icon_2)
	freezeTransform()
	pm.parent(lt_leg_fk_local_2, lt_leg_fk_icon_1)

	lt_leg_fk_icon_3 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 3:', lt_leg_fk_icon_3
	temp_constraint = pm.parentConstraint(lt_fk_joint_3, lt_leg_fk_icon_3)
	pm.delete(temp_constraint)
	lt_leg_fk_local_3 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_fk_joint_3, lt_leg_fk_local_3)
	pm.delete(temp_constraint)
	pm.parent(lt_leg_fk_icon_3, lt_leg_fk_local_3)
	pm.select(lt_leg_fk_icon_3)
	freezeTransform()
	pm.parent(lt_leg_fk_local_3, lt_leg_fk_icon_2)

	lt_leg_fk_icon_4 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 4:', lt_leg_fk_icon_4
	temp_constraint = pm.parentConstraint(lt_fk_joint_4, lt_leg_fk_icon_4)
	pm.delete(temp_constraint)
	lt_leg_fk_local_4 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_fk_joint_4, lt_leg_fk_local_4)
	pm.delete(temp_constraint)
	pm.parent(lt_leg_fk_icon_4, lt_leg_fk_local_4)
	pm.select(lt_leg_fk_icon_4)
	freezeTransform()
	pm.parent(lt_leg_fk_local_4, lt_leg_fk_icon_3)

	pm.select(lt_leg_fk_icon_1, lt_leg_fk_icon_2, lt_leg_fk_icon_3, lt_leg_fk_icon_4)
	fk_icons = pm.ls(sl=1)


	pm.select(lt_leg_fk_local_1, lt_leg_fk_local_2, lt_leg_fk_local_3, lt_leg_fk_local_4)
	fk_locals = pm.ls(sl=1)

	count = 0
	suffix = 'fk_icon'
	for each in fk_icons:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	count = 0
	suffix = 'fk_local'
	for each in fk_locals:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	pm.orientConstraint(lt_leg_fk_icon_1, lt_fk_root, mo=0)
	pm.orientConstraint(lt_leg_fk_icon_2, lt_fk_joint_2, mo=0)
	pm.orientConstraint(lt_leg_fk_icon_3, lt_fk_joint_3, mo=0)
	pm.orientConstraint(lt_leg_fk_icon_4, lt_fk_joint_4, mo=0)

	pm.addAttr(lt_leg_fk_icon_1, ln='length', dv=1, min=0, at='double' )
	lt_leg_fk_icon_1.length.set(e=1, keyable=1)
	pm.addAttr(lt_leg_fk_icon_2, ln='length', dv=1, min=0, at='double' )
	lt_leg_fk_icon_2.length.set(e=1, keyable=1)

	pm.setDrivenKeyframe(lt_fk_joint_2 + '.translateX', currentDriver=lt_leg_fk_icon_1  + '.length')
	lt_leg_fk_icon_1.length.set(0)
	lt_fk_joint_2.tx.set(0)
	pm.setDrivenKeyframe(lt_fk_joint_2 + '.translateX', currentDriver=lt_leg_fk_icon_1  + '.length')
	lt_leg_fk_icon_1.length.set(1)

	pm.keyTangent(lt_fk_joint_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(lt_fk_joint_2 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	pm.setDrivenKeyframe(lt_fk_joint_3 + '.translateX', currentDriver=lt_leg_fk_icon_2  + '.length')
	lt_leg_fk_icon_2.length.set(0)
	lt_fk_joint_3.tx.set(0)
	pm.setDrivenKeyframe(lt_fk_joint_3 + '.translateX', currentDriver=lt_leg_fk_icon_2  + '.length')
	lt_leg_fk_icon_2.length.set(1)

	pm.keyTangent(lt_fk_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(lt_fk_joint_3 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	'''
	Create the ik handles 
	'''
	lt_leg_ikh = pm.ikHandle(sj=lt_ik_root, ee=lt_ik_joint_3)[0]
	lt_ankle_ikh = pm.ikHandle(sj=lt_ik_joint_3, ee=lt_ik_joint_4)[0]
	lt_toe_ikh = pm.ikHandle(sj=lt_ik_joint_4, ee=lt_ik_joint_5)[0]

	ikh_name = lt_leg_root.replace('01_bind', 'ikh')
	lt_leg_ikh.rename(ikh_name)

	ikh_name = lt_leg_ikh.replace('leg', 'ankle')
	lt_ankle_ikh.rename(ikh_name)

	ikh_name = lt_ankle_ikh.replace('ankle', 'toe')
	lt_toe_ikh.rename(ikh_name)

	'''
	Create the foot icon
	'''
	lt_footCurve_1 = pm.curve(p=[(-1.67422e-06, 0, 2.182925), (-0.13416, 0, 2.16342), (-0.266779, 0, 2.095529), (-0.395472, 0, 1.99807), (-0.518993, 0, 1.858632), (-0.636496, 0, 1.679268), (-0.737632, 0, 1.452024), (-0.819474, 0, 1.166445), (-0.846144, 0, 0.821387), (-0.824602, 0, 0.556128), (-0.749206, 0, 0.167213), (-0.673656, 0, -0.127237), (-0.597808, 0, -0.419587), (-0.545054, 0, -0.746104), (-0.544891, 0, -1.097217), (-0.571904, 0, -1.448294), (-0.512279, 0, -1.753435), (-0.393271, 0, -1.92306), (-0.266839, 0, -2.035747), (-0.133965, 0, -2.097731), (0, 0, -2.120128), (0.133965, 0, -2.097731), (0.266839, 0, -2.035747), (0.393271, 0, -1.92306), (0.512279, 0, -1.753435), (0.571904, 0, -1.448294), (0.544891, 0, -1.097217), (0.545054, 0, -0.746104), (0.597807, 0, -0.419586), (0.673656, 0, -0.127237), (0.749207, 0, 0.167214), (0.824602, 0, 0.556128), (0.846144, 0, 0.82139), (0.819474, 0, 1.166447), (0.737631, 0, 1.452029), (0.636486, 0, 1.679267), (0.519008, 0, 1.858641), (0.395504, 0, 1.9981), (0.266596, 0, 2.09545), (0.134293, 0, 2.163449), (-1.67422e-06, 0, 2.182925)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 38], d=3)
	lt_footCurve_2 = pm.curve(p=[(-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217)], k=[0, 0, 0, 1, 2, 3, 3, 3], d=3)

	lt_foot_icon = pm.group(empty=1)

	pm.select(lt_footCurve_1, lt_footCurve_2, lt_foot_icon)
	lt_foot_shapes = pm.ls(sl=1, dag=1)
	lt_curveShape_1 = lt_foot_shapes[1]
	lt_curveShape_2 = lt_foot_shapes[3]
	lt_foot_icon_grp = lt_foot_shapes[4]
	pm.parent(lt_curveShape_1, lt_curveShape_2, lt_foot_icon, s=1, r=1)
	pm.delete(lt_footCurve_1, lt_footCurve_2)
	pm.xform(lt_foot_icon, scale= [3.5, 3.5, 3.5])
	pm.select(lt_foot_icon)
	freezeTransform()

	'''
	Move the foot icon
	'''
	temp_constraint = pm.pointConstraint(lt_ik_joint_3, lt_foot_icon)
	pm.delete(temp_constraint)
	lt_foot_icon.ty.set(0)
	lt_foot_icon.tz.set(6)
	pm.select(lt_foot_icon)
	freezeTransform()
	

	'''
	Rename the foot icon
	'''
	icon_name = lt_leg_root.replace('leg_01_bind', 'foot_icon')
	lt_foot_icon.rename(icon_name)

	'''
	Add foot attrs
	'''
	pm.addAttr(lt_foot_icon, ln='legAttrs', en='------:', at='enum')
	pm.addAttr(lt_foot_icon, ln='stretch', at='bool')

	pm.addAttr(lt_foot_icon, ln='kneeAttrs', at='enum', en='------:')
	lockAttrs(lt_foot_icon, ['kneeAttrs'])
	unhideAttrs(lt_foot_icon, ['kneeAttrs'])


	pm.addAttr(lt_foot_icon, ln='kneeTwist', at='double', dv=0)
	unlock_and_unhide(lt_foot_icon, ['kneeTwist'])

	pm.addAttr(lt_foot_icon, ln='autoKnee', at='bool')
	unlock_and_unhide(lt_foot_icon, ['autoKnee'])

	pm.addAttr(lt_foot_icon, ln='kneeSnap', at='bool')
	unhideAttrs(lt_foot_icon, ['kneeSnap'])


	pm.addAttr(lt_foot_icon, ln='footAttrs', en='------:', at='enum')
	pm.addAttr(lt_foot_icon, ln='roll', dv=0, at='double')
	pm.addAttr(lt_foot_icon, ln='bendLimitAngle', dv=45, at='double')
	pm.addAttr(lt_foot_icon, ln='toeStraightAngle', dv=75, at='double')
	pm.addAttr(lt_foot_icon, ln='tilt', dv=0, at='double')
	pm.addAttr(lt_foot_icon, ln='lean', dv=0, at='double')
	pm.addAttr(lt_foot_icon, ln='toeSpin', dv=0, at='double')
	pm.addAttr(lt_foot_icon, ln='toeTap', dv=0, at='double')
	

	lockAttrs(lt_foot_icon, ['footAttrs', 'legAttrs'])
	unhideAttrs(lt_foot_icon, ['footAttrs', 'legAttrs'])
	unlock_and_unhide(lt_foot_icon, ['roll', 'bendLimitAngle', 'toeStraightAngle', 'tilt', 'lean', 'toeSpin', 'toeTap', 'stretch'])


	'''
	Parent the ikhs under the foot icon
	'''
	pm.parent(lt_leg_ikh, lt_ankle_ikh, lt_toe_ikh, lt_foot_icon)

	'''
	Move the pivot of the foot icon
	'''
	driver_translation = lt_leg_joint_3.getTranslation(ws=1)
	lt_foot_icon.setPivots(driver_translation, ws=1)
	lt_foot_icon.rotateOrder.set(2)

	'''
	Create the distance node
	'''
	lt_loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(lt_leg_root, lt_loc_1, mo=0)
	pm.delete(temp_constraint)
	loc_name = lt_leg_root.replace('01_bind', 'startLoc')
	lt_loc_1.rename(loc_name)

	lt_loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(lt_leg_joint_3, lt_loc_2, mo=0)
	pm.delete(temp_constraint)
	loc_name = lt_leg_root.replace('01_bind', 'endLoc')
	lt_loc_2.rename(loc_name)

	lt_leg_dist = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.connectAttr(lt_loc_1 + '.worldPosition', lt_leg_dist + '.startPoint')
	pm.connectAttr(lt_loc_2 + '.worldPosition', lt_leg_dist + '.endPoint')

	node_name = lt_leg_root.replace('01_bind', 'dist')
	lt_leg_dist.rename(node_name)

	pm.parent(lt_loc_2, lt_foot_icon)

	rootLength = pm.getAttr(lt_ik_joint_2 + '.translateX')
	joint2Length = pm.getAttr(lt_ik_joint_3  + '.translateX')
	sumLength = (rootLength + joint2Length)
	# print sumLength

	pm.setDrivenKeyframe(lt_ik_joint_2+ '.translateX', dv=sumLength, currentDriver=lt_leg_dist + '.distance', at='.translateX', value=rootLength)

	pm.setDrivenKeyframe(lt_ik_joint_2+ '.translateX', dv=(sumLength*2), currentDriver=lt_leg_dist + '.distance', at='.translateX', value=(rootLength*2))


	pm.setDrivenKeyframe(lt_ik_joint_3+ '.translateX', dv=sumLength, currentDriver=lt_leg_dist + '.distance', at='.translateX', value=joint2Length)

	pm.setDrivenKeyframe(lt_ik_joint_3+ '.translateX', dv=(sumLength*2), currentDriver=lt_leg_dist + '.distance', at='.translateX', value=(joint2Length*2))

	pm.keyTangent(lt_ik_joint_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey(lt_ik_joint_2 + '_translateX', add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.keyTangent(lt_ik_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey(lt_ik_joint_3 + '_translateX', add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.select(lt_leg_ikh, lt_ankle_ikh, lt_toe_ikh, lt_loc_1, lt_loc_2, lt_leg_dist)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.v', 0)

	'''
	Create the lt_knee icon.
	'''

	lt_knee_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
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

	pm.select(lt_knee_icon)
	centerPivot(lt_knee_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the knee icon.
	'''
	temp_constraint = pm.pointConstraint(lt_leg_joint_2, lt_knee_icon)
	pm.delete(temp_constraint)
	freezeTransform(lt_knee_icon)
	pm.xform(lt_knee_icon, t=[0, 0, 10], scale=[.5, .5, .5], ro=[90, 180, 0])
	freezeTransform(lt_knee_icon)

	'''
	Rename knee icon
	'''
	lt_knee_icon_name = lt_leg_root.replace('lt_leg_01_bind', 'lt_knee_icon')
	lt_knee_icon.rename(lt_knee_icon_name)

	
	lt_noFlip_loc = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(lt_ik_joint_3, lt_noFlip_loc, mo=0)
	pm.delete(temp_constraint)
	lt_noFlip_loc.tx.set(10)
	'''
	Create the no flip local
	'''
	lt_noFlip_local = pm.group(empty=1)
	temp_constraint = pm.pointConstraint(lt_ik_joint_3, lt_noFlip_local, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	pm.parent(lt_noFlip_loc, lt_noFlip_local)

	local_name = lt_knee_icon.replace('knee_icon', 'noFlip_local')
	lt_noFlip_local.rename(local_name)

	loc_name = lt_knee_icon.replace('knee_icon', 'noFlip_loc')
	lt_noFlip_loc.rename(loc_name)

	pm.parent(lt_noFlip_local, lt_foot_icon)

	'''
	Create the pole vector for the lt_knee
	'''
	knee_const = pm.poleVectorConstraint(lt_noFlip_loc, lt_knee_icon, lt_leg_ikh)

	const_target_1 = knee_const.getWeightAliasList()[0]
	const_target_2 = knee_const.getWeightAliasList()[1]
	# print const_target_1
	# print const_target_2

	pm.connectAttr(lt_foot_icon + '.kneeTwist', lt_noFlip_local + '.rotateY')


	lt_noFlip_loc.v.set(0)
	lt_foot_icon.autoKnee.set(1)
	const_target_2.set(0)
	lt_leg_ikh.twist.set(90)
	lt_knee_icon.v.set(0)
	pm.setDrivenKeyframe([lt_knee_icon + '.visibility', const_target_1, const_target_2, lt_leg_ikh + '.twist'], currentDriver=lt_foot_icon + '.autoKnee')

	lt_foot_icon.autoKnee.set(0)
	const_target_1.set(0)
	const_target_2.set(1)
	lt_leg_ikh.twist.set(0)
	lt_knee_icon.v.set(1)
	pm.setDrivenKeyframe([lt_knee_icon + '.visibility', const_target_1, const_target_2, lt_leg_ikh + '.twist'], currentDriver=lt_foot_icon + '.autoKnee')
	lt_foot_icon.autoKnee.set(1)


	lt_knee_loc = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.pointConstraint(lt_knee_icon, lt_knee_loc, mo=0)
	pm.delete(temp_constraint)

	loc_name = lt_knee_icon.replace('icon', 'loc')
	lt_knee_loc.rename(loc_name)

	lt_knee_dist_1 = pm.shadingNode('distanceDimShape', asUtility=1)
	pm.connectAttr(lt_loc_1 + '.worldPosition', lt_knee_dist_1 + '.startPoint')
	pm.connectAttr(lt_knee_loc + '.worldPosition', lt_knee_dist_1 + '.endPoint')
	node_name = lt_knee_loc.replace('loc', '01_dist')
	lt_knee_dist_1.rename(node_name)



	lt_knee_dist_2 = pm.shadingNode('distanceDimShape', asUtility=1)
	pm.connectAttr(lt_loc_2 + '.worldPosition', lt_knee_dist_2 + '.startPoint')
	pm.connectAttr(lt_knee_loc + '.worldPosition', lt_knee_dist_2 + '.endPoint')
	node_name = lt_knee_loc.replace('loc', '02_dist')
	lt_knee_dist_2.rename(node_name)

	pm.parent(lt_knee_loc, lt_knee_icon)

	

	lt_kneeSnapBlend = pm.shadingNode('blendColors', asUtility=1)
	node_name = lt_knee_icon.replace('icon', 'snapBlend')
	lt_kneeSnapBlend.rename(node_name)

	pm.disconnectAttr(lt_ik_joint_2 +'_translateX.output', lt_ik_joint_2 + '.translateX')

	pm.disconnectAttr(lt_ik_joint_3 +'_translateX.output', lt_ik_joint_3 + '.translateX')

	pm.connectAttr(lt_knee_dist_1 + '.distance', lt_kneeSnapBlend + '.color1R')
	pm.connectAttr(lt_knee_dist_2 + '.distance', lt_kneeSnapBlend + '.color1G')

	pm.connectAttr(lt_ik_joint_2 +'_translateX.output', lt_kneeSnapBlend + '.color2R')
	pm.connectAttr(lt_ik_joint_3 +'_translateX.output', lt_kneeSnapBlend + '.color2G')


	pm.connectAttr(lt_kneeSnapBlend + '.outputR', lt_ik_joint_2 + '.translateX')
	pm.connectAttr(lt_kneeSnapBlend + '.outputG', lt_ik_joint_3 + '.translateX')

	pm.connectAttr(lt_foot_icon + '.kneeSnap', lt_kneeSnapBlend + '.blender')

	pm.select(lt_knee_loc, lt_knee_dist_1, lt_knee_dist_2)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	lt_leg_fk_icon_1.v.set(0)
	pm.setDrivenKeyframe([lt_foot_icon + '.visibility', lt_leg_fk_icon_1 + '.visibility'], currentDriver=lt_switch + '.IkFk')
	lt_switch.IkFk.set(1)
	lt_foot_icon.v.set(0)
	lt_leg_fk_icon_1.v.set(1)
	pm.setDrivenKeyframe([lt_foot_icon + '.visibility', lt_leg_fk_icon_1 + '.visibility'], currentDriver=lt_switch + '.IkFk')
	lt_switch.IkFk.set(0)

	lt_leg_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_leg_root, lt_leg_pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()
	pm.parent(lt_leg_root, lt_ik_root, lt_fk_root, lt_leg_pad)

	pm.select(lt_ik_root, lt_fk_root)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	pad_name = lt_leg_root.replace('01_bind', '00_pad')
	lt_leg_pad.rename(pad_name)

	pm.select(lt_leg_fk_icon_1, lt_leg_fk_icon_2, lt_leg_fk_icon_3, lt_leg_fk_icon_4, lt_fk_joint_5, lt_foot_icon)
	selection = pm.ls(sl=1)
	for each in selection:
		lock_and_hide(each, ['sx', 'sy', 'sz', 'visibility'])
		deleteHistory()

	pm.select(lt_leg_fk_icon_1, lt_leg_fk_icon_2, lt_leg_fk_icon_3, lt_leg_fk_icon_4, lt_fk_joint_5)
	selection = pm.ls(sl=1)
	for each in selection:
		lock_and_hide(each, ['tx', 'ty', 'tz'])


	stretchBlend = pm.shadingNode('blendColors', asUtility=1)
	pm.connectAttr(lt_leg_dist + '.distance', stretchBlend + '.color1R', f=1)
	stretchBlend.color2R.set(1)
	pm.disconnectAttr(lt_leg_dist  +'.distance', lt_ik_joint_2  + '_translateX.input')
	pm.connectAttr(stretchBlend + '.outputR', lt_ik_joint_2 + '_translateX.input', f=1)
	pm.disconnectAttr(lt_leg_dist  +'.distance', lt_ik_joint_3 + '_translateX.input')
	pm.connectAttr(stretchBlend  + '.outputR', lt_ik_joint_3 + '_translateX.input', f=1)
	pm.connectAttr(lt_foot_icon + '.stretch', stretchBlend + '.blender', f=1)
	lt_foot_icon.stretch.set(1)

	node_name = lt_leg_root.replace('01_bind', 'stretchBlend')
	stretchBlend.rename(node_name)

def lt_ikLegSetup(*args):
	global lt_leg_pad, lt_foot_icon, lt_knee_dist_1, lt_knee_dist_2, lt_leg_dist
	global lt_loc_1, lt_loc_2, lt_leg_ikh, lt_ankle_ikh, lt_toe_ikh, lt_noFlip_local
	global lt_leg_root, lt_leg_joint_2, lt_leg_joint_3, lt_leg_joint_4
	'''
	Get bind joints
	'''
	pm.select(lt_leg_01_bind)
	selection = pm.ls(sl=1, dag=1)
	lt_leg_root = selection[0]
	lt_leg_joint_2 = selection[1]
	lt_leg_joint_3 = selection[2]
	lt_leg_joint_4 = selection[3]
	lt_leg_joint_5 = selection[4]
	# print 'Leg Root:', lt_leg_root
	# print 'Leg Joint 2:', lt_leg_joint_2
	# print 'Leg Joint 3:', lt_leg_joint_3
	# print 'Leg Joint 4:', lt_leg_joint_4
	# print 'Leg Joint 5:', lt_leg_joint_5

	pm.joint(zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='xup')
	lt_leg_joint_5.jointOrientX.set(0)
	lt_leg_joint_5.jointOrientZ.set(0)

	'''
	Make ik joints
	'''

	ik_joints = pm.duplicate(lt_leg_root)
	pm.select(ik_joints)
	ik_joints = pm.ls(sl=1, dag=1)
	lt_ik_root = ik_joints[0]
	lt_ik_joint_2 = ik_joints[1]
	lt_ik_joint_3 = ik_joints[2]
	lt_ik_joint_4 = ik_joints[3]
	lt_ik_joint_5 = ik_joints[4]

	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'ik'
	for each in ik_joints:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)

	# print 'IK Root:', lt_ik_root
	# print 'IK Joint 2:', lt_ik_joint_2
	# print 'IK Joint 3:', lt_ik_joint_3
	# print 'IK Joint 4:', lt_ik_joint_4
	# print 'IK Joint 5:', lt_ik_joint_5

	ikfk_blend_1 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_2 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_3 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_4 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_1, ikfk_blend_2, ikfk_blend_3, ikfk_blend_4)
	ikfk_blenders = pm.ls(sl=1)
	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_blend'
	for each in ikfk_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)
		each.blender.set(1)

	pm.connectAttr(lt_ik_root + '.rotate', ikfk_blend_1 + '.color1')
	pm.connectAttr(lt_ik_joint_2 + '.rotate', ikfk_blend_2 + '.color1')
	pm.connectAttr(lt_ik_joint_3 + '.rotate', ikfk_blend_3 + '.color1')
	pm.connectAttr(lt_ik_joint_4 + '.rotate', ikfk_blend_4 + '.color1')

	'''
	Connect the output to the bind
	'''
	pm.connectAttr(ikfk_blend_1 + '.output', lt_leg_root + '.rotate')
	pm.connectAttr(ikfk_blend_2 + '.output', lt_leg_joint_2 + '.rotate')
	pm.connectAttr(ikfk_blend_3 + '.output', lt_leg_joint_3 + '.rotate')
	pm.connectAttr(ikfk_blend_4 + '.output', lt_leg_joint_4 + '.rotate')



	ikfk_blend_5 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_6 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_7 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_8 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_5, ikfk_blend_6, ikfk_blend_7, ikfk_blend_8)
	ikfk_tran_blenders = pm.ls(sl=1)
	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_tran_blend'
	for each in ikfk_tran_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)
		each.blender.set(1)

	pm.connectAttr(lt_ik_root + '.translate', ikfk_blend_5 + '.color1')
	pm.connectAttr(lt_ik_joint_2 + '.translate', ikfk_blend_6 + '.color1')
	pm.connectAttr(lt_ik_joint_3 + '.translate', ikfk_blend_7 + '.color1')
	pm.connectAttr(lt_ik_joint_4 + '.translate', ikfk_blend_8 + '.color1')


	pm.connectAttr(ikfk_blend_5 + '.output', lt_leg_root + '.translate')
	pm.connectAttr(ikfk_blend_6 + '.output', lt_leg_joint_2 + '.translate')
	pm.connectAttr(ikfk_blend_7 + '.output', lt_leg_joint_3 + '.translate')
	pm.connectAttr(ikfk_blend_8 + '.output', lt_leg_joint_4 + '.translate')


	
	'''
	Create the ik handles 
	'''
	lt_leg_ikh = pm.ikHandle(sj=lt_ik_root, ee=lt_ik_joint_3)[0]
	lt_ankle_ikh = pm.ikHandle(sj=lt_ik_joint_3, ee=lt_ik_joint_4)[0]
	lt_toe_ikh = pm.ikHandle(sj=lt_ik_joint_4, ee=lt_ik_joint_5)[0]

	ikh_name = lt_leg_root.replace('01_bind', 'ikh')
	lt_leg_ikh.rename(ikh_name)

	ikh_name = lt_leg_ikh.replace('leg', 'ankle')
	lt_ankle_ikh.rename(ikh_name)

	ikh_name = lt_ankle_ikh.replace('ankle', 'toe')
	lt_toe_ikh.rename(ikh_name)

	'''
	Create the foot icon
	'''
	lt_footCurve_1 = pm.curve(p=[(-1.67422e-06, 0, 2.182925), (-0.13416, 0, 2.16342), (-0.266779, 0, 2.095529), (-0.395472, 0, 1.99807), (-0.518993, 0, 1.858632), (-0.636496, 0, 1.679268), (-0.737632, 0, 1.452024), (-0.819474, 0, 1.166445), (-0.846144, 0, 0.821387), (-0.824602, 0, 0.556128), (-0.749206, 0, 0.167213), (-0.673656, 0, -0.127237), (-0.597808, 0, -0.419587), (-0.545054, 0, -0.746104), (-0.544891, 0, -1.097217), (-0.571904, 0, -1.448294), (-0.512279, 0, -1.753435), (-0.393271, 0, -1.92306), (-0.266839, 0, -2.035747), (-0.133965, 0, -2.097731), (0, 0, -2.120128), (0.133965, 0, -2.097731), (0.266839, 0, -2.035747), (0.393271, 0, -1.92306), (0.512279, 0, -1.753435), (0.571904, 0, -1.448294), (0.544891, 0, -1.097217), (0.545054, 0, -0.746104), (0.597807, 0, -0.419586), (0.673656, 0, -0.127237), (0.749207, 0, 0.167214), (0.824602, 0, 0.556128), (0.846144, 0, 0.82139), (0.819474, 0, 1.166447), (0.737631, 0, 1.452029), (0.636486, 0, 1.679267), (0.519008, 0, 1.858641), (0.395504, 0, 1.9981), (0.266596, 0, 2.09545), (0.134293, 0, 2.163449), (-1.67422e-06, 0, 2.182925)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 38], d=3)
	lt_footCurve_2 = pm.curve(p=[(-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217)], k=[0, 0, 0, 1, 2, 3, 3, 3], d=3)

	lt_foot_icon = pm.group(empty=1)

	pm.select(lt_footCurve_1, lt_footCurve_2, lt_foot_icon)
	lt_foot_shapes = pm.ls(sl=1, dag=1)
	lt_curveShape_1 = lt_foot_shapes[1]
	lt_curveShape_2 = lt_foot_shapes[3]
	lt_foot_icon_grp = lt_foot_shapes[4]
	pm.parent(lt_curveShape_1, lt_curveShape_2, lt_foot_icon, s=1, r=1)
	pm.delete(lt_footCurve_1, lt_footCurve_2)
	pm.xform(lt_foot_icon, scale= [3.5, 3.5, 3.5])
	pm.select(lt_foot_icon)
	freezeTransform()

	'''
	Move the foot icon
	'''
	temp_constraint = pm.pointConstraint(lt_ik_joint_3, lt_foot_icon)
	pm.delete(temp_constraint)
	lt_foot_icon.ty.set(0)
	lt_foot_icon.tz.set(6)
	pm.select(lt_foot_icon)
	freezeTransform()
	

	'''
	Rename the foot icon
	'''
	icon_name = lt_leg_root.replace('leg_01_bind', 'foot_icon')
	lt_foot_icon.rename(icon_name)

	'''
	Add foot attrs
	'''
	pm.addAttr(lt_foot_icon, ln='legAttrs', en='------:', at='enum')
	pm.addAttr(lt_foot_icon, ln='stretch', at='bool')

	pm.addAttr(lt_foot_icon, ln='kneeAttrs', at='enum', en='------:')
	lockAttrs(lt_foot_icon, ['kneeAttrs'])
	unhideAttrs(lt_foot_icon, ['kneeAttrs'])


	pm.addAttr(lt_foot_icon, ln='kneeTwist', at='double', dv=0)
	unlock_and_unhide(lt_foot_icon, ['kneeTwist'])

	pm.addAttr(lt_foot_icon, ln='autoKnee', at='bool')
	unlock_and_unhide(lt_foot_icon, ['autoKnee'])

	pm.addAttr(lt_foot_icon, ln='kneeSnap', at='bool')
	unhideAttrs(lt_foot_icon, ['kneeSnap'])


	pm.addAttr(lt_foot_icon, ln='footAttrs', en='------:', at='enum')
	pm.addAttr(lt_foot_icon, ln='roll', dv=0, at='double')
	pm.addAttr(lt_foot_icon, ln='bendLimitAngle', dv=45, at='double')
	pm.addAttr(lt_foot_icon, ln='toeStraightAngle', dv=75, at='double')
	pm.addAttr(lt_foot_icon, ln='tilt', dv=0, at='double')
	pm.addAttr(lt_foot_icon, ln='lean', dv=0, at='double')
	pm.addAttr(lt_foot_icon, ln='toeSpin', dv=0, at='double')
	pm.addAttr(lt_foot_icon, ln='toeTap', dv=0, at='double')
	

	lockAttrs(lt_foot_icon, ['footAttrs', 'legAttrs'])
	unhideAttrs(lt_foot_icon, ['footAttrs', 'legAttrs'])
	unlock_and_unhide(lt_foot_icon, ['roll', 'bendLimitAngle', 'toeStraightAngle', 'tilt', 'lean', 'toeSpin', 'toeTap', 'stretch'])


	'''
	Parent the ikhs under the foot icon
	'''
	pm.parent(lt_leg_ikh, lt_ankle_ikh, lt_toe_ikh, lt_foot_icon)

	'''
	Move the pivot of the foot icon
	'''
	driver_translation = lt_leg_joint_3.getTranslation(ws=1)
	lt_foot_icon.setPivots(driver_translation, ws=1)
	lt_foot_icon.rotateOrder.set(2)

	'''
	Create the distance node
	'''
	lt_loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(lt_leg_root, lt_loc_1, mo=0)
	pm.delete(temp_constraint)
	loc_name = lt_leg_root.replace('01_bind', 'startLoc')
	lt_loc_1.rename(loc_name)

	lt_loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(lt_leg_joint_3, lt_loc_2, mo=0)
	pm.delete(temp_constraint)
	loc_name = lt_leg_root.replace('01_bind', 'endLoc')
	lt_loc_2.rename(loc_name)

	lt_leg_dist = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.connectAttr(lt_loc_1 + '.worldPosition', lt_leg_dist + '.startPoint')
	pm.connectAttr(lt_loc_2 + '.worldPosition', lt_leg_dist + '.endPoint')

	node_name = lt_leg_root.replace('01_bind', 'dist')
	lt_leg_dist.rename(node_name)

	pm.parent(lt_loc_2, lt_foot_icon)

	rootLength = pm.getAttr(lt_ik_joint_2 + '.translateX')
	joint2Length = pm.getAttr(lt_ik_joint_3  + '.translateX')
	sumLength = (rootLength + joint2Length)
	# print sumLength

	pm.setDrivenKeyframe(lt_ik_joint_2+ '.translateX', dv=sumLength, currentDriver=lt_leg_dist + '.distance', at='.translateX', value=rootLength)

	pm.setDrivenKeyframe(lt_ik_joint_2+ '.translateX', dv=(sumLength*2), currentDriver=lt_leg_dist + '.distance', at='.translateX', value=(rootLength*2))


	pm.setDrivenKeyframe(lt_ik_joint_3+ '.translateX', dv=sumLength, currentDriver=lt_leg_dist + '.distance', at='.translateX', value=joint2Length)

	pm.setDrivenKeyframe(lt_ik_joint_3+ '.translateX', dv=(sumLength*2), currentDriver=lt_leg_dist + '.distance', at='.translateX', value=(joint2Length*2))

	pm.keyTangent(lt_ik_joint_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey(lt_ik_joint_2 + '_translateX', add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.keyTangent(lt_ik_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey(lt_ik_joint_3 + '_translateX', add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.select(lt_leg_ikh, lt_ankle_ikh, lt_toe_ikh, lt_loc_1, lt_loc_2, lt_leg_dist)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.v', 0)

	'''
	Create the lt_knee icon.
	'''

	lt_knee_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
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

	pm.select(lt_knee_icon)
	centerPivot(lt_knee_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the knee icon.
	'''
	temp_constraint = pm.pointConstraint(lt_leg_joint_2, lt_knee_icon)
	pm.delete(temp_constraint)
	freezeTransform(lt_knee_icon)
	pm.xform(lt_knee_icon, t=[0, 0, 10], scale=[.5, .5, .5], ro=[90, 180, 0])
	freezeTransform(lt_knee_icon)

	'''
	Rename knee icon
	'''
	lt_knee_icon_name = lt_leg_root.replace('lt_leg_01_bind', 'lt_knee_icon')
	lt_knee_icon.rename(lt_knee_icon_name)

	
	lt_noFlip_loc = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(lt_ik_joint_3, lt_noFlip_loc, mo=0)
	pm.delete(temp_constraint)
	lt_noFlip_loc.tx.set(10)
	'''
	Create the no flip local
	'''
	lt_noFlip_local = pm.group(empty=1)
	temp_constraint = pm.pointConstraint(lt_ik_joint_3, lt_noFlip_local, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	pm.parent(lt_noFlip_loc, lt_noFlip_local)

	local_name = lt_knee_icon.replace('knee_icon', 'noFlip_local')
	lt_noFlip_local.rename(local_name)

	loc_name = lt_knee_icon.replace('knee_icon', 'noFlip_loc')
	lt_noFlip_loc.rename(loc_name)

	pm.parent(lt_noFlip_local, lt_foot_icon)

	'''
	Create the pole vector for the lt_knee
	'''
	knee_const = pm.poleVectorConstraint(lt_noFlip_loc, lt_knee_icon, lt_leg_ikh)

	const_target_1 = knee_const.getWeightAliasList()[0]
	const_target_2 = knee_const.getWeightAliasList()[1]
	# print const_target_1
	# print const_target_2

	pm.connectAttr(lt_foot_icon + '.kneeTwist', lt_noFlip_local + '.rotateY')


	lt_noFlip_loc.v.set(0)
	lt_foot_icon.autoKnee.set(1)
	const_target_2.set(0)
	lt_leg_ikh.twist.set(90)
	lt_knee_icon.v.set(0)
	pm.setDrivenKeyframe([lt_knee_icon + '.visibility', const_target_1, const_target_2, lt_leg_ikh + '.twist'], currentDriver=lt_foot_icon + '.autoKnee')

	lt_foot_icon.autoKnee.set(0)
	const_target_1.set(0)
	const_target_2.set(1)
	lt_leg_ikh.twist.set(0)
	lt_knee_icon.v.set(1)
	pm.setDrivenKeyframe([lt_knee_icon + '.visibility', const_target_1, const_target_2, lt_leg_ikh + '.twist'], currentDriver=lt_foot_icon + '.autoKnee')
	lt_foot_icon.autoKnee.set(1)


	lt_knee_loc = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.pointConstraint(lt_knee_icon, lt_knee_loc, mo=0)
	pm.delete(temp_constraint)

	loc_name = lt_knee_icon.replace('icon', 'loc')
	lt_knee_loc.rename(loc_name)

	lt_knee_dist_1 = pm.shadingNode('distanceDimShape', asUtility=1)
	pm.connectAttr(lt_loc_1 + '.worldPosition', lt_knee_dist_1 + '.startPoint')
	pm.connectAttr(lt_knee_loc + '.worldPosition', lt_knee_dist_1 + '.endPoint')
	node_name = lt_knee_loc.replace('loc', '01_dist')
	lt_knee_dist_1.rename(node_name)


	lt_knee_dist_2 = pm.shadingNode('distanceDimShape', asUtility=1)
	pm.connectAttr(lt_loc_2 + '.worldPosition', lt_knee_dist_2 + '.startPoint')
	pm.connectAttr(lt_knee_loc + '.worldPosition', lt_knee_dist_2 + '.endPoint')
	node_name = lt_knee_loc.replace('loc', '02_dist')
	lt_knee_dist_2.rename(node_name)

	pm.parent(lt_knee_loc, lt_knee_icon)


	lt_kneeSnapBlend = pm.shadingNode('blendColors', asUtility=1)
	node_name = lt_knee_icon.replace('icon', 'snapBlend')
	lt_kneeSnapBlend.rename(node_name)

	pm.disconnectAttr(lt_ik_joint_2 +'_translateX.output', lt_ik_joint_2 + '.translateX')

	pm.disconnectAttr(lt_ik_joint_3 +'_translateX.output', lt_ik_joint_3 + '.translateX')

	pm.connectAttr(lt_knee_dist_1 + '.distance', lt_kneeSnapBlend + '.color1R')
	pm.connectAttr(lt_knee_dist_2 + '.distance', lt_kneeSnapBlend + '.color1G')

	pm.connectAttr(lt_ik_joint_2 +'_translateX.output', lt_kneeSnapBlend + '.color2R')
	pm.connectAttr(lt_ik_joint_3 +'_translateX.output', lt_kneeSnapBlend + '.color2G')


	pm.connectAttr(lt_kneeSnapBlend + '.outputR', lt_ik_joint_2 + '.translateX')
	pm.connectAttr(lt_kneeSnapBlend + '.outputG', lt_ik_joint_3 + '.translateX')

	pm.connectAttr(lt_foot_icon + '.kneeSnap', lt_kneeSnapBlend + '.blender')

	pm.select(lt_knee_loc, lt_knee_dist_1, lt_knee_dist_2)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	lt_leg_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_leg_root, lt_leg_pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()
	pm.parent(lt_leg_root, lt_ik_root, lt_leg_pad)

	lt_ik_root.v.set(0)

	pad_name = lt_leg_root.replace('01_bind', '00_pad')
	lt_leg_pad.rename(pad_name)


	stretchBlend = pm.shadingNode('blendColors', asUtility=1)
	pm.connectAttr(lt_leg_dist + '.distance', stretchBlend + '.color1R', f=1)
	stretchBlend.color2R.set(1)
	pm.disconnectAttr(lt_leg_dist  +'.distance', lt_ik_joint_2  + '_translateX.input')
	pm.connectAttr(stretchBlend + '.outputR', lt_ik_joint_2 + '_translateX.input', f=1)
	pm.disconnectAttr(lt_leg_dist  +'.distance', lt_ik_joint_3 + '_translateX.input')
	pm.connectAttr(stretchBlend  + '.outputR', lt_ik_joint_3 + '_translateX.input', f=1)
	pm.connectAttr(lt_foot_icon + '.stretch', stretchBlend + '.blender', f=1)
	lt_foot_icon.stretch.set(1)

	node_name = lt_leg_root.replace('01_bind', 'stretchBlend')
	stretchBlend.rename(node_name)

def lt_fkLegSetup(*args):
	global lt_leg_pad, lt_leg_fk_local_1, lt_leg_fk_icon_1, lt_leg_fk_icon_2, lt_leg_fk_icon_3, lt_leg_fk_icon_4
	'''
	Get bind joints
	'''
	pm.select(lt_leg_01_bind)
	selection = pm.ls(sl=1, dag=1)
	lt_leg_root = selection[0]
	lt_leg_joint_2 = selection[1]
	lt_leg_joint_3 = selection[2]
	lt_leg_joint_4 = selection[3]
	lt_leg_joint_5 = selection[4]
	# print 'Leg Root:', lt_leg_root
	# print 'Leg Joint 2:', lt_leg_joint_2
	# print 'Leg Joint 3:', lt_leg_joint_3
	# print 'Leg Joint 4:', lt_leg_joint_4
	# print 'Leg Joint 5:', lt_leg_joint_5

	pm.joint(zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='xup')
	lt_leg_joint_5.jointOrientX.set(0)
	lt_leg_joint_5.jointOrientZ.set(0)
	
	'''
	Make fk joints
	'''

	fk_joints = pm.duplicate(lt_leg_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=1, dag=1)
	lt_fk_root = fk_joints[0]
	lt_fk_joint_2 = fk_joints[1]
	lt_fk_joint_3 = fk_joints[2]
	lt_fk_joint_4 = fk_joints[3]
	lt_fk_joint_5 = fk_joints[4]


	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'fk'
	for each in fk_joints:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)

	# print 'FK Root:', lt_fk_root
	# print 'FK Joint 2:', lt_fk_joint_2
	# print 'FK Joint 3:', lt_fk_joint_3
	# print 'FK Joint 4:', lt_fk_joint_4
	# print 'FK Joint 5:', lt_fk_joint_5

	ikfk_blend_1 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_2 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_3 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_4 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_1, ikfk_blend_2, ikfk_blend_3, ikfk_blend_4)
	ikfk_rot_blenders = pm.ls(sl=1)
	ori = 'lt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_rot_blend'
	for each in ikfk_rot_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)
		pm.setAttr(each + '.blender', 1)

	pm.connectAttr(lt_fk_root + '.rotate', ikfk_blend_1 + '.color1')
	pm.connectAttr(lt_fk_joint_2 + '.rotate', ikfk_blend_2 + '.color1')
	pm.connectAttr(lt_fk_joint_3 + '.rotate', ikfk_blend_3 + '.color1')
	pm.connectAttr(lt_fk_joint_4 + '.rotate', ikfk_blend_4 + '.color1')


	'''
	Connect the output to the bind
	'''
	pm.connectAttr(ikfk_blend_1 + '.output', lt_leg_root + '.rotate')
	pm.connectAttr(ikfk_blend_2 + '.output', lt_leg_joint_2 + '.rotate')
	pm.connectAttr(ikfk_blend_3 + '.output', lt_leg_joint_3 + '.rotate')
	pm.connectAttr(ikfk_blend_4 + '.output', lt_leg_joint_4 + '.rotate')


	'''
	Create fk icons
	'''
	lt_leg_fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', lt_leg_fk_icon_1
	temp_constraint = pm.parentConstraint(lt_fk_root, lt_leg_fk_icon_1)
	pm.delete(temp_constraint)
	lt_leg_fk_local_1 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_fk_root, lt_leg_fk_local_1)
	pm.delete(temp_constraint)
	pm.parent(lt_leg_fk_icon_1, lt_leg_fk_local_1)
	pm.select(lt_leg_fk_icon_1)
	freezeTransform()


	lt_leg_fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 2:', lt_leg_fk_icon_2
	temp_constraint = pm.parentConstraint(lt_fk_joint_2, lt_leg_fk_icon_2)
	pm.delete(temp_constraint)
	lt_leg_fk_local_2 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_fk_joint_2, lt_leg_fk_local_2)
	pm.delete(temp_constraint)
	pm.parent(lt_leg_fk_icon_2, lt_leg_fk_local_2)
	pm.select(lt_leg_fk_icon_2)
	freezeTransform()
	pm.parent(lt_leg_fk_local_2, lt_leg_fk_icon_1)

	lt_leg_fk_icon_3 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 3:', lt_leg_fk_icon_3
	temp_constraint = pm.parentConstraint(lt_fk_joint_3, lt_leg_fk_icon_3)
	pm.delete(temp_constraint)
	lt_leg_fk_local_3 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_fk_joint_3, lt_leg_fk_local_3)
	pm.delete(temp_constraint)
	pm.parent(lt_leg_fk_icon_3, lt_leg_fk_local_3)
	pm.select(lt_leg_fk_icon_3)
	freezeTransform()
	pm.parent(lt_leg_fk_local_3, lt_leg_fk_icon_2)

	lt_leg_fk_icon_4 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 4:', lt_leg_fk_icon_4
	temp_constraint = pm.parentConstraint(lt_fk_joint_4, lt_leg_fk_icon_4)
	pm.delete(temp_constraint)
	lt_leg_fk_local_4 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_fk_joint_4, lt_leg_fk_local_4)
	pm.delete(temp_constraint)
	pm.parent(lt_leg_fk_icon_4, lt_leg_fk_local_4)
	pm.select(lt_leg_fk_icon_4)
	freezeTransform()
	pm.parent(lt_leg_fk_local_4, lt_leg_fk_icon_3)

	pm.select(lt_leg_fk_icon_1, lt_leg_fk_icon_2, lt_leg_fk_icon_3, lt_leg_fk_icon_4)
	fk_icons = pm.ls(sl=1)


	pm.select(lt_leg_fk_local_1, lt_leg_fk_local_2, lt_leg_fk_local_3, lt_leg_fk_local_4)
	fk_locals = pm.ls(sl=1)

	count = 0
	suffix = 'fk_icon'
	for each in fk_icons:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	count = 0
	suffix = 'fk_local'
	for each in fk_locals:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	pm.orientConstraint(lt_leg_fk_icon_1, lt_fk_root, mo=0)
	pm.orientConstraint(lt_leg_fk_icon_2, lt_fk_joint_2, mo=0)
	pm.orientConstraint(lt_leg_fk_icon_3, lt_fk_joint_3, mo=0)
	pm.orientConstraint(lt_leg_fk_icon_4, lt_fk_joint_4, mo=0)

	pm.addAttr(lt_leg_fk_icon_1, ln='length', dv=1, min=0, at='double' )
	lt_leg_fk_icon_1.length.set(e=1, keyable=1)
	pm.addAttr(lt_leg_fk_icon_2, ln='length', dv=1, min=0, at='double' )
	lt_leg_fk_icon_2.length.set(e=1, keyable=1)

	pm.setDrivenKeyframe(lt_fk_joint_2 + '.translateX', currentDriver=lt_leg_fk_icon_1  + '.length')
	lt_leg_fk_icon_1.length.set(0)
	lt_fk_joint_2.tx.set(0)
	pm.setDrivenKeyframe(lt_fk_joint_2 + '.translateX', currentDriver=lt_leg_fk_icon_1  + '.length')
	lt_leg_fk_icon_1.length.set(1)

	pm.keyTangent(lt_fk_joint_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(lt_fk_joint_2 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	pm.setDrivenKeyframe(lt_fk_joint_3 + '.translateX', currentDriver=lt_leg_fk_icon_2  + '.length')
	lt_leg_fk_icon_2.length.set(0)
	lt_fk_joint_3.tx.set(0)
	pm.setDrivenKeyframe(lt_fk_joint_3 + '.translateX', currentDriver=lt_leg_fk_icon_2  + '.length')
	lt_leg_fk_icon_2.length.set(1)

	pm.keyTangent(lt_fk_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(lt_fk_joint_3 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	lt_leg_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(lt_leg_root, lt_leg_pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	pad_name = lt_leg_root.replace('01_bind', '00_pad')
	lt_leg_pad.rename(pad_name)

	pm.parent(lt_leg_root, lt_fk_root, lt_leg_pad)

	lt_fk_root.v.set(0)

def rt_legSetup(*args):
	global rt_leg_pad, rt_foot_icon, rt_knee_dist_1, rt_knee_dist_2, rt_leg_dist, rt_switch, rt_leg_fk_local_1
	global rt_loc_1, rt_loc_2, rt_leg_ikh, rt_ankle_ikh, rt_toe_ikh, rt_noFlip_local
	global rt_leg_fk_icon_1, rt_leg_fk_icon_2, rt_leg_fk_icon_3, rt_leg_fk_icon_4
	global rt_leg_root, rt_leg_joint_2, rt_leg_joint_3, rt_leg_joint_4
	'''
	Get bind joints
	'''
	pm.select(rt_leg_01_bind)
	selection = pm.ls(sl=1, dag=1)
	rt_leg_root = selection[0]
	rt_leg_joint_2 = selection[1]
	rt_leg_joint_3 = selection[2]
	rt_leg_joint_4 = selection[3]
	rt_leg_joint_5 = selection[4]
	# print 'Leg Root:', rt_leg_root
	# print 'Leg Joint 2:', rt_leg_joint_2
	# print 'Leg Joint 3:', rt_leg_joint_3
	# print 'Leg Joint 4:', rt_leg_joint_4
	# print 'Leg Joint 5:', rt_leg_joint_5
	pm.joint(zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='xup')
	rt_leg_joint_5.jointOrientX.set(0)
	rt_leg_joint_5.jointOrientZ.set(0)
	for each in selection:
		each.rotateOrder.set(3)

	'''
	Make ik joints
	'''

	ik_joints = pm.duplicate(rt_leg_root)
	pm.select(ik_joints)
	ik_joints = pm.ls(sl=1, dag=1)
	rt_ik_root = ik_joints[0]
	rt_ik_joint_2 = ik_joints[1]
	rt_ik_joint_3 = ik_joints[2]
	rt_ik_joint_4 = ik_joints[3]
	rt_ik_joint_5 = ik_joints[4]

	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'ik'
	for each in ik_joints:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)


	# print 'IK Root:', rt_ik_root
	# print 'IK Joint 2:', rt_ik_joint_2
	# print 'IK Joint 3:', rt_ik_joint_3
	# print 'IK Joint 4:', rt_ik_joint_4
	# print 'IK Joint 5:', rt_ik_joint_5
		
	'''
	Make fk joints
	'''

	fk_joints = pm.duplicate(rt_leg_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=1, dag=1)
	rt_fk_root = fk_joints[0]
	rt_fk_joint_2 = fk_joints[1]
	rt_fk_joint_3 = fk_joints[2]
	rt_fk_joint_4 = fk_joints[3]
	rt_fk_joint_5 = fk_joints[4]


	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'fk'
	for each in fk_joints:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)

	# print 'FK Root:', rt_fk_root
	# print 'FK Joint 2:', rt_fk_joint_2
	# print 'FK Joint 3:', rt_fk_joint_3
	# print 'FK Joint 4:', rt_fk_joint_4
	# print 'FK Joint 5:', rt_fk_joint_5

	ikfk_blend_1 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_2 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_3 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_4 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_1, ikfk_blend_2, ikfk_blend_3, ikfk_blend_4)
	ikfk_rot_blenders = pm.ls(sl=1)
	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_rot_blend'
	for each in ikfk_rot_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	pm.connectAttr(rt_ik_root + '.rotate', ikfk_blend_1 + '.color2')
	pm.connectAttr(rt_fk_root + '.rotate', ikfk_blend_1 + '.color1')

	pm.connectAttr(rt_ik_joint_2 + '.rotate', ikfk_blend_2 + '.color2')
	pm.connectAttr(rt_fk_joint_2 + '.rotate', ikfk_blend_2 + '.color1')

	pm.connectAttr(rt_ik_joint_3 + '.rotate', ikfk_blend_3 + '.color2')
	pm.connectAttr(rt_fk_joint_3 + '.rotate', ikfk_blend_3 + '.color1')

	pm.connectAttr(rt_ik_joint_4 + '.rotate', ikfk_blend_4 + '.color2')
	pm.connectAttr(rt_fk_joint_4 + '.rotate', ikfk_blend_4 + '.color1')


	'''
	Create the IK/FK switch
	'''
	ikfk_shape_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	ikfk_shape_2 = pm.curve(p=[(0, 0, -1), (0, 0, 1)], k=[0, 1], d=1)
	ikfk_shape_3 = pm.curve(p=[(-1, 0, 0), (1, 0, 0)], k=[0, 1], d=1)
	ikfk_shape_4 = pm.curve(p=[(0, 0, 1), (0, 0, 3)], k=[0, 1], d=1)

	pm.select(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4)
	ikfk_shapes = pm.ls(sl=1)

	suffix = 'ikfk_curve'

	for each in ikfk_shapes:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)

	rt_switch = pm.group(empty=True)
	pm.select(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4, rt_switch)
	shapes = pm.ls(selection=True, dag=True)
	curveShape_1 = shapes[1]
	curveShape_2 = shapes[3]
	curveShape_3 = shapes[5]
	curveShape_4 = shapes[7]
	rt_switch_grp = shapes[8]
	# print 'Curve Shape 1:', curveShape_1
	# print 'Curve Shape 2:', curveShape_2
	# print 'Curve Shape 3:', curveShape_3
	# print 'Curve Shape 4:', curveShape_4
	# print 'Switch:', rt_switch_grp
	pm.select(ikfk_shape_2, ikfk_shape_3)

	pm.cmds.scale(0.768, 0.768, 0.768)
	freezeTransform()

	pm.parent(curveShape_1, curveShape_2, curveShape_3, curveShape_4, rt_switch, s=1, r=1)
	pm.delete(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4)
	pm.cmds.move(0, 0, 3, rt_switch + '.scalePivot', rt_switch + '.rotatePivot', rpr=1)

	pm.xform(rt_switch, ro=[0,0,90], scale=[1.5,1.5,1.5])
	freezeTransform(rt_switch)
	deleteHistory()
	temp_constraint = pm.pointConstraint(rt_leg_joint_3, rt_switch, mo=0, w=1)
	pm.delete(temp_constraint)
	pm.select(rt_switch)
	freezeTransform()
	rt_switch_name = rt_leg_root.replace('01_bind', 'IkFk_switch')
	rt_switch.rename(rt_switch_name)
	pm.parentConstraint(rt_leg_joint_3, rt_switch, mo=1)

	'''
	Add IkFk attribute
	'''
	pm.addAttr(rt_switch, ln="IkFk", nn='Ik/Fk', max=1, dv=0, at='double', min=0)
	rt_switch.IkFk.set(e=1, keyable=True)

	'''
	Lock Attrs
	'''
	lock_and_hide(rt_switch, ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v'])

	'''
	Connect the switch to the blenders
	'''
	pm.connectAttr(rt_switch + '.IkFk', ikfk_blend_1 + '.blender')
	pm.connectAttr(rt_switch + '.IkFk', ikfk_blend_2 + '.blender')
	pm.connectAttr(rt_switch + '.IkFk', ikfk_blend_3 + '.blender')
	pm.connectAttr(rt_switch + '.IkFk', ikfk_blend_4 + '.blender')

	'''
	Connect the output to the bind
	'''
	pm.connectAttr(ikfk_blend_1 + '.output', rt_leg_root + '.rotate')
	pm.connectAttr(ikfk_blend_2 + '.output', rt_leg_joint_2 + '.rotate')
	pm.connectAttr(ikfk_blend_3 + '.output', rt_leg_joint_3 + '.rotate')
	pm.connectAttr(ikfk_blend_4 + '.output', rt_leg_joint_4 + '.rotate')


	ikfk_blend_5 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_6 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_7 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_8 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_5, ikfk_blend_6, ikfk_blend_7, ikfk_blend_8)
	ikfk_tran_blenders = pm.ls(sl=1)
	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_tran_blend'
	for each in ikfk_tran_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	pm.connectAttr(rt_ik_root + '.translate', ikfk_blend_5 + '.color2')
	pm.connectAttr(rt_fk_root + '.translate', ikfk_blend_5 + '.color1')

	pm.connectAttr(rt_ik_joint_2 + '.translate', ikfk_blend_6 + '.color2')
	pm.connectAttr(rt_fk_joint_2 + '.translate', ikfk_blend_6 + '.color1')

	pm.connectAttr(rt_ik_joint_3 + '.translate', ikfk_blend_7 + '.color2')
	pm.connectAttr(rt_fk_joint_3 + '.translate', ikfk_blend_7 + '.color1')

	pm.connectAttr(rt_ik_joint_4 + '.translate', ikfk_blend_8 + '.color2')
	pm.connectAttr(rt_fk_joint_4 + '.translate', ikfk_blend_8 + '.color1')

	pm.connectAttr(rt_switch + '.IkFk', ikfk_blend_5 + '.blender')
	pm.connectAttr(rt_switch + '.IkFk', ikfk_blend_6 + '.blender')
	pm.connectAttr(rt_switch + '.IkFk', ikfk_blend_7 + '.blender')
	pm.connectAttr(rt_switch + '.IkFk', ikfk_blend_8 + '.blender')

	pm.connectAttr(ikfk_blend_5 + '.output', rt_leg_root + '.translate')
	pm.connectAttr(ikfk_blend_6 + '.output', rt_leg_joint_2 + '.translate')
	pm.connectAttr(ikfk_blend_7 + '.output', rt_leg_joint_3 + '.translate')
	pm.connectAttr(ikfk_blend_8 + '.output', rt_leg_joint_4 + '.translate')

	'''
	Create fk icons
	'''
	rt_leg_fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', rt_leg_fk_icon_1
	temp_constraint = pm.parentConstraint(rt_fk_root, rt_leg_fk_icon_1)
	pm.delete(temp_constraint)
	rt_leg_fk_local_1 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_fk_root, rt_leg_fk_local_1)
	pm.delete(temp_constraint)
	pm.parent(rt_leg_fk_icon_1, rt_leg_fk_local_1)
	pm.select(rt_leg_fk_icon_1)
	freezeTransform()


	rt_leg_fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 2:', rt_leg_fk_icon_2
	temp_constraint = pm.parentConstraint(rt_fk_joint_2, rt_leg_fk_icon_2)
	pm.delete(temp_constraint)
	rt_leg_fk_local_2 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_fk_joint_2, rt_leg_fk_local_2)
	pm.delete(temp_constraint)
	pm.parent(rt_leg_fk_icon_2, rt_leg_fk_local_2)
	pm.select(rt_leg_fk_icon_2)
	freezeTransform()
	pm.parent(rt_leg_fk_local_2, rt_leg_fk_icon_1)

	rt_leg_fk_icon_3 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 3:', rt_leg_fk_icon_3
	temp_constraint = pm.parentConstraint(rt_fk_joint_3, rt_leg_fk_icon_3)
	pm.delete(temp_constraint)
	rt_leg_fk_local_3 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_fk_joint_3, rt_leg_fk_local_3)
	pm.delete(temp_constraint)
	pm.parent(rt_leg_fk_icon_3, rt_leg_fk_local_3)
	pm.select(rt_leg_fk_icon_3)
	freezeTransform()
	pm.parent(rt_leg_fk_local_3, rt_leg_fk_icon_2)

	rt_leg_fk_icon_4 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 4:', rt_leg_fk_icon_4
	temp_constraint = pm.parentConstraint(rt_fk_joint_4, rt_leg_fk_icon_4)
	pm.delete(temp_constraint)
	rt_leg_fk_local_4 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_fk_joint_4, rt_leg_fk_local_4)
	pm.delete(temp_constraint)
	pm.parent(rt_leg_fk_icon_4, rt_leg_fk_local_4)
	pm.select(rt_leg_fk_icon_4)
	freezeTransform()
	pm.parent(rt_leg_fk_local_4, rt_leg_fk_icon_3)

	pm.select(rt_leg_fk_icon_1, rt_leg_fk_icon_2, rt_leg_fk_icon_3, rt_leg_fk_icon_4)
	fk_icons = pm.ls(sl=1)


	pm.select(rt_leg_fk_local_1, rt_leg_fk_local_2, rt_leg_fk_local_3, rt_leg_fk_local_4)
	fk_locals = pm.ls(sl=1)

	count = 0
	suffix = 'fk_icon'
	for each in fk_icons:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	count = 0
	suffix = 'fk_local'
	for each in fk_locals:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	pm.orientConstraint(rt_leg_fk_icon_1, rt_fk_root, mo=0)
	pm.orientConstraint(rt_leg_fk_icon_2, rt_fk_joint_2, mo=0)
	pm.orientConstraint(rt_leg_fk_icon_3, rt_fk_joint_3, mo=0)
	pm.orientConstraint(rt_leg_fk_icon_4, rt_fk_joint_4, mo=0)

	pm.addAttr(rt_leg_fk_icon_1, ln='length', dv=1, min=0, at='double' )
	rt_leg_fk_icon_1.length.set(e=1, keyable=1)
	pm.addAttr(rt_leg_fk_icon_2, ln='length', dv=1, min=0, at='double' )
	rt_leg_fk_icon_2.length.set(e=1, keyable=1)

	pm.setDrivenKeyframe(rt_fk_joint_2 + '.translateX', currentDriver=rt_leg_fk_icon_1  + '.length')
	rt_leg_fk_icon_1.length.set(0)
	rt_fk_joint_2.tx.set(0)
	pm.setDrivenKeyframe(rt_fk_joint_2 + '.translateX', currentDriver=rt_leg_fk_icon_1  + '.length')
	rt_leg_fk_icon_1.length.set(1)

	pm.keyTangent(rt_fk_joint_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(rt_fk_joint_2 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	pm.setDrivenKeyframe(rt_fk_joint_3 + '.translateX', currentDriver=rt_leg_fk_icon_2  + '.length')
	rt_leg_fk_icon_2.length.set(0)
	rt_fk_joint_3.tx.set(0)
	pm.setDrivenKeyframe(rt_fk_joint_3 + '.translateX', currentDriver=rt_leg_fk_icon_2  + '.length')
	rt_leg_fk_icon_2.length.set(1)

	pm.keyTangent(rt_fk_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(rt_fk_joint_3 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	'''
	Create the ik handles 
	'''
	rt_leg_ikh = pm.ikHandle(sj=rt_ik_root, ee=rt_ik_joint_3)[0]
	rt_ankle_ikh = pm.ikHandle(sj=rt_ik_joint_3, ee=rt_ik_joint_4)[0]
	rt_toe_ikh = pm.ikHandle(sj=rt_ik_joint_4, ee=rt_ik_joint_5)[0]

	ikh_name = rt_leg_root.replace('01_bind', 'ikh')
	rt_leg_ikh.rename(ikh_name)

	ikh_name = rt_leg_ikh.replace('leg', 'ankle')
	rt_ankle_ikh.rename(ikh_name)

	ikh_name = rt_ankle_ikh.replace('ankle', 'toe')
	rt_toe_ikh.rename(ikh_name)

	'''
	Create the foot icon
	'''
	rt_footCurve_1 = pm.curve(p=[(-1.67422e-06, 0, 2.182925), (-0.13416, 0, 2.16342), (-0.266779, 0, 2.095529), (-0.395472, 0, 1.99807), (-0.518993, 0, 1.858632), (-0.636496, 0, 1.679268), (-0.737632, 0, 1.452024), (-0.819474, 0, 1.166445), (-0.846144, 0, 0.821387), (-0.824602, 0, 0.556128), (-0.749206, 0, 0.167213), (-0.673656, 0, -0.127237), (-0.597808, 0, -0.419587), (-0.545054, 0, -0.746104), (-0.544891, 0, -1.097217), (-0.571904, 0, -1.448294), (-0.512279, 0, -1.753435), (-0.393271, 0, -1.92306), (-0.266839, 0, -2.035747), (-0.133965, 0, -2.097731), (0, 0, -2.120128), (0.133965, 0, -2.097731), (0.266839, 0, -2.035747), (0.393271, 0, -1.92306), (0.512279, 0, -1.753435), (0.571904, 0, -1.448294), (0.544891, 0, -1.097217), (0.545054, 0, -0.746104), (0.597807, 0, -0.419586), (0.673656, 0, -0.127237), (0.749207, 0, 0.167214), (0.824602, 0, 0.556128), (0.846144, 0, 0.82139), (0.819474, 0, 1.166447), (0.737631, 0, 1.452029), (0.636486, 0, 1.679267), (0.519008, 0, 1.858641), (0.395504, 0, 1.9981), (0.266596, 0, 2.09545), (0.134293, 0, 2.163449), (-1.67422e-06, 0, 2.182925)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 38], d=3)
	rt_footCurve_2 = pm.curve(p=[(-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217)], k=[0, 0, 0, 1, 2, 3, 3, 3], d=3)

	rt_foot_icon = pm.group(empty=1)

	pm.select(rt_footCurve_1, rt_footCurve_2, rt_foot_icon)
	rt_foot_shapes = pm.ls(sl=1, dag=1)
	rt_curveShape_1 = rt_foot_shapes[1]
	rt_curveShape_2 = rt_foot_shapes[3]
	rt_foot_icon_grp = rt_foot_shapes[4]
	pm.parent(rt_curveShape_1, rt_curveShape_2, rt_foot_icon, s=1, r=1)
	pm.delete(rt_footCurve_1, rt_footCurve_2)
	pm.xform(rt_foot_icon, scale= [3.5, 3.5, 3.5])
	pm.select(rt_foot_icon)
	freezeTransform()

	'''
	Move the foot icon
	'''
	temp_constraint = pm.pointConstraint(rt_ik_joint_3, rt_foot_icon)
	pm.delete(temp_constraint)
	rt_foot_icon.ty.set(0)
	rt_foot_icon.tz.set(6)
	pm.select(rt_foot_icon)
	freezeTransform()
	

	'''
	Rename the foot icon
	'''
	icon_name = rt_leg_root.replace('leg_01_bind', 'foot_icon')
	rt_foot_icon.rename(icon_name)

	'''
	Add foot attrs
	'''
	pm.addAttr(rt_foot_icon, ln='legAttrs', en='------:', at='enum')
	pm.addAttr(rt_foot_icon, ln='stretch', at='bool')

	pm.addAttr(rt_foot_icon, ln='kneeAttrs', at='enum', en='------:')
	lockAttrs(rt_foot_icon, ['kneeAttrs'])
	unhideAttrs(rt_foot_icon, ['kneeAttrs'])


	pm.addAttr(rt_foot_icon, ln='kneeTwist', at='double', dv=0)
	unlock_and_unhide(rt_foot_icon, ['kneeTwist'])

	pm.addAttr(rt_foot_icon, ln='autoKnee', at='bool')
	unlock_and_unhide(rt_foot_icon, ['autoKnee'])

	pm.addAttr(rt_foot_icon, ln='kneeSnap', at='bool')
	unhideAttrs(rt_foot_icon, ['kneeSnap'])


	pm.addAttr(rt_foot_icon, ln='footAttrs', en='------:', at='enum')
	pm.addAttr(rt_foot_icon, ln='roll', dv=0, at='double')
	pm.addAttr(rt_foot_icon, ln='bendLimitAngle', dv=45, at='double')
	pm.addAttr(rt_foot_icon, ln='toeStraightAngle', dv=75, at='double')
	pm.addAttr(rt_foot_icon, ln='tilt', dv=0, at='double')
	pm.addAttr(rt_foot_icon, ln='lean', dv=0, at='double')
	pm.addAttr(rt_foot_icon, ln='toeSpin', dv=0, at='double')
	pm.addAttr(rt_foot_icon, ln='toeTap', dv=0, at='double')
	

	lockAttrs(rt_foot_icon, ['footAttrs', 'legAttrs'])
	unhideAttrs(rt_foot_icon, ['footAttrs', 'legAttrs'])
	unlock_and_unhide(rt_foot_icon, ['roll', 'bendLimitAngle', 'toeStraightAngle', 'tilt', 'lean', 'toeSpin', 'toeTap', 'stretch'])


	'''
	Parent the ikhs under the foot icon
	'''
	pm.parent(rt_leg_ikh, rt_ankle_ikh, rt_toe_ikh, rt_foot_icon)

	'''
	Move the pivot of the foot icon
	'''
	driver_translation = rt_leg_joint_3.getTranslation(ws=1)
	rt_foot_icon.setPivots(driver_translation, ws=1)
	rt_foot_icon.rotateOrder.set(2)

	'''
	Create the distance node
	'''
	rt_loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(rt_leg_root, rt_loc_1, mo=0)
	pm.delete(temp_constraint)
	loc_name = rt_leg_root.replace('01_bind', 'startLoc')
	rt_loc_1.rename(loc_name)

	rt_loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(rt_leg_joint_3, rt_loc_2, mo=0)
	pm.delete(temp_constraint)
	loc_name = rt_leg_root.replace('01_bind', 'endLoc')
	rt_loc_2.rename(loc_name)

	rt_leg_dist = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.connectAttr(rt_loc_1 + '.worldPosition', rt_leg_dist + '.startPoint')
	pm.connectAttr(rt_loc_2 + '.worldPosition', rt_leg_dist + '.endPoint')

	node_name = rt_leg_root.replace('01_bind', 'dist')
	rt_leg_dist.rename(node_name)

	pm.parent(rt_loc_2, rt_foot_icon)

	rootLength = pm.getAttr(rt_ik_joint_2 + '.translateX')
	joint2Length = pm.getAttr(rt_ik_joint_3  + '.translateX')
	sumLength = (rootLength + joint2Length)
	# print sumLength

	pm.setDrivenKeyframe(rt_ik_joint_2+ '.translateX', dv=sumLength, currentDriver=rt_leg_dist + '.distance', at='.translateX', value=rootLength)

	pm.setDrivenKeyframe(rt_ik_joint_2+ '.translateX', dv=(sumLength*2), currentDriver=rt_leg_dist + '.distance', at='.translateX', value=(rootLength*2))


	pm.setDrivenKeyframe(rt_ik_joint_3+ '.translateX', dv=sumLength, currentDriver=rt_leg_dist + '.distance', at='.translateX', value=joint2Length)

	pm.setDrivenKeyframe(rt_ik_joint_3+ '.translateX', dv=(sumLength*2), currentDriver=rt_leg_dist + '.distance', at='.translateX', value=(joint2Length*2))

	pm.keyTangent(rt_ik_joint_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey(rt_ik_joint_2 + '_translateX', add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.keyTangent(rt_ik_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey(rt_ik_joint_3 + '_translateX', add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.select(rt_leg_ikh, rt_ankle_ikh, rt_toe_ikh, rt_loc_1, rt_loc_2, rt_leg_dist)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.v', 0)

	'''
	Create the rt_knee icon.
	'''

	rt_knee_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
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

	pm.select(rt_knee_icon)
	centerPivot(rt_knee_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the knee icon.
	'''
	temp_constraint = pm.pointConstraint(rt_leg_joint_2, rt_knee_icon)
	pm.delete(temp_constraint)
	freezeTransform(rt_knee_icon)
	pm.xform(rt_knee_icon, t=[0, 0, 10], scale=[.5, .5, .5], ro=[90, 180, 0])
	freezeTransform(rt_knee_icon)

	'''
	Rename knee icon
	'''
	rt_knee_icon_name = rt_leg_root.replace('rt_leg_01_bind', 'rt_knee_icon')
	rt_knee_icon.rename(rt_knee_icon_name)

	
	rt_noFlip_loc = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(rt_ik_joint_3, rt_noFlip_loc, mo=0)
	pm.delete(temp_constraint)
	rt_noFlip_loc.tx.set(10)
	'''
	Create the no flip local
	'''
	rt_noFlip_local = pm.group(empty=1)
	temp_constraint = pm.pointConstraint(rt_ik_joint_3, rt_noFlip_local, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	pm.parent(rt_noFlip_loc, rt_noFlip_local)

	local_name = rt_knee_icon.replace('knee_icon', 'noFlip_local')
	rt_noFlip_local.rename(local_name)

	loc_name = rt_knee_icon.replace('knee_icon', 'noFlip_loc')
	rt_noFlip_loc.rename(loc_name)

	pm.parent(rt_noFlip_local, rt_foot_icon)

	'''
	Create the pole vector for the rt_knee
	'''
	knee_const = pm.poleVectorConstraint(rt_noFlip_loc, rt_knee_icon, rt_leg_ikh)

	const_target_1 = knee_const.getWeightAliasList()[0]
	const_target_2 = knee_const.getWeightAliasList()[1]
	# print const_target_1
	# print const_target_2

	pm.connectAttr(rt_foot_icon + '.kneeTwist', rt_noFlip_local + '.rotateY')


	rt_noFlip_loc.v.set(0)
	rt_foot_icon.autoKnee.set(1)
	const_target_2.set(0)
	rt_leg_ikh.twist.set(90)
	rt_knee_icon.v.set(0)
	pm.setDrivenKeyframe([rt_knee_icon + '.visibility', const_target_1, const_target_2, rt_leg_ikh + '.twist'], currentDriver=rt_foot_icon + '.autoKnee')

	rt_foot_icon.autoKnee.set(0)
	const_target_1.set(0)
	const_target_2.set(1)
	rt_leg_ikh.twist.set(0)
	rt_knee_icon.v.set(1)
	pm.setDrivenKeyframe([rt_knee_icon + '.visibility', const_target_1, const_target_2, rt_leg_ikh + '.twist'], currentDriver=rt_foot_icon + '.autoKnee')
	rt_foot_icon.autoKnee.set(1)


	rt_knee_loc = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.pointConstraint(rt_knee_icon, rt_knee_loc, mo=0)
	pm.delete(temp_constraint)

	loc_name = rt_knee_icon.replace('icon', 'loc')
	rt_knee_loc.rename(loc_name)

	rt_knee_dist_1 = pm.shadingNode('distanceDimShape', asUtility=1)
	pm.connectAttr(rt_loc_1 + '.worldPosition', rt_knee_dist_1 + '.startPoint')
	pm.connectAttr(rt_knee_loc + '.worldPosition', rt_knee_dist_1 + '.endPoint')
	node_name = rt_knee_loc.replace('loc', '01_dist')
	rt_knee_dist_1.rename(node_name)



	rt_knee_dist_2 = pm.shadingNode('distanceDimShape', asUtility=1)
	pm.connectAttr(rt_loc_2 + '.worldPosition', rt_knee_dist_2 + '.startPoint')
	pm.connectAttr(rt_knee_loc + '.worldPosition', rt_knee_dist_2 + '.endPoint')
	node_name = rt_knee_loc.replace('loc', '02_dist')
	rt_knee_dist_2.rename(node_name)

	pm.parent(rt_knee_loc, rt_knee_icon)

	

	rt_kneeSnapBlend = pm.shadingNode('blendColors', asUtility=1)
	node_name = rt_knee_icon.replace('icon', 'snapBlend')
	rt_kneeSnapBlend.rename(node_name)

	pm.disconnectAttr(rt_ik_joint_2 +'_translateX.output', rt_ik_joint_2 + '.translateX')

	pm.disconnectAttr(rt_ik_joint_3 +'_translateX.output', rt_ik_joint_3 + '.translateX')

	pm.connectAttr(rt_knee_dist_1 + '.distance', rt_kneeSnapBlend + '.color1R')
	pm.connectAttr(rt_knee_dist_2 + '.distance', rt_kneeSnapBlend + '.color1G')

	pm.connectAttr(rt_ik_joint_2 +'_translateX.output', rt_kneeSnapBlend + '.color2R')
	pm.connectAttr(rt_ik_joint_3 +'_translateX.output', rt_kneeSnapBlend + '.color2G')


	pm.connectAttr(rt_kneeSnapBlend + '.outputR', rt_ik_joint_2 + '.translateX')
	pm.connectAttr(rt_kneeSnapBlend + '.outputG', rt_ik_joint_3 + '.translateX')

	pm.connectAttr(rt_foot_icon + '.kneeSnap', rt_kneeSnapBlend + '.blender')

	pm.select(rt_knee_loc, rt_knee_dist_1, rt_knee_dist_2)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	rt_leg_fk_icon_1.v.set(0)
	pm.setDrivenKeyframe([rt_foot_icon + '.visibility', rt_leg_fk_icon_1 + '.visibility'], currentDriver=rt_switch + '.IkFk')
	rt_switch.IkFk.set(1)
	rt_foot_icon.v.set(0)
	rt_leg_fk_icon_1.v.set(1)
	pm.setDrivenKeyframe([rt_foot_icon + '.visibility', rt_leg_fk_icon_1 + '.visibility'], currentDriver=rt_switch + '.IkFk')
	rt_switch.IkFk.set(0)

	rt_leg_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_leg_root, rt_leg_pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()
	pm.parent(rt_leg_root, rt_ik_root, rt_fk_root, rt_leg_pad)

	pm.select(rt_ik_root, rt_fk_root)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	pad_name = rt_leg_root.replace('01_bind', '00_pad')
	rt_leg_pad.rename(pad_name)

	pm.select(rt_leg_fk_icon_1, rt_leg_fk_icon_2, rt_leg_fk_icon_3, rt_leg_fk_icon_4, rt_fk_joint_5, rt_foot_icon)
	selection = pm.ls(sl=1)
	for each in selection:
		lock_and_hide(each, ['sx', 'sy', 'sz', 'visibility'])
		deleteHistory()

	pm.select(rt_leg_fk_icon_1, rt_leg_fk_icon_2, rt_leg_fk_icon_3, rt_leg_fk_icon_4, rt_fk_joint_5)
	selection = pm.ls(sl=1)
	for each in selection:
		lock_and_hide(each, ['tx', 'ty', 'tz'])


	stretchBlend = pm.shadingNode('blendColors', asUtility=1)
	pm.connectAttr(rt_leg_dist + '.distance', stretchBlend + '.color1R', f=1)
	stretchBlend.color2R.set(1)
	pm.disconnectAttr(rt_leg_dist  +'.distance', rt_ik_joint_2  + '_translateX.input')
	pm.connectAttr(stretchBlend + '.outputR', rt_ik_joint_2 + '_translateX.input', f=1)
	pm.disconnectAttr(rt_leg_dist  +'.distance', rt_ik_joint_3 + '_translateX.input')
	pm.connectAttr(stretchBlend  + '.outputR', rt_ik_joint_3 + '_translateX.input', f=1)
	pm.connectAttr(rt_foot_icon + '.stretch', stretchBlend + '.blender', f=1)
	rt_foot_icon.stretch.set(1)

	node_name = rt_leg_root.replace('01_bind', 'stretchBlend')
	stretchBlend.rename(node_name)

def rt_ikLegSetup(*args):
	global rt_leg_pad, rt_foot_icon, rt_knee_dist_1, rt_knee_dist_2, rt_leg_dist
	global rt_loc_1, rt_loc_2, rt_leg_ikh, rt_ankle_ikh, rt_toe_ikh, rt_noFlip_local
	global rt_leg_root, rt_leg_joint_2, rt_leg_joint_3, rt_leg_joint_4
	'''
	Get bind joints
	'''
	pm.select(rt_leg_01_bind)
	selection = pm.ls(sl=1, dag=1)
	rt_leg_root = selection[0]
	rt_leg_joint_2 = selection[1]
	rt_leg_joint_3 = selection[2]
	rt_leg_joint_4 = selection[3]
	rt_leg_joint_5 = selection[4]
	# print 'Leg Root:', rt_leg_root
	# print 'Leg Joint 2:', rt_leg_joint_2
	# print 'Leg Joint 3:', rt_leg_joint_3
	# print 'Leg Joint 4:', rt_leg_joint_4
	# print 'Leg Joint 5:', rt_leg_joint_5

	pm.joint(zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='xup')
	rt_leg_joint_5.jointOrientX.set(0)
	rt_leg_joint_5.jointOrientZ.set(0)

	'''
	Make ik joints
	'''

	ik_joints = pm.duplicate(rt_leg_root)
	pm.select(ik_joints)
	ik_joints = pm.ls(sl=1, dag=1)
	rt_ik_root = ik_joints[0]
	rt_ik_joint_2 = ik_joints[1]
	rt_ik_joint_3 = ik_joints[2]
	rt_ik_joint_4 = ik_joints[3]
	rt_ik_joint_5 = ik_joints[4]

	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'ik'
	for each in ik_joints:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)

	# print 'IK Root:', rt_ik_root
	# print 'IK Joint 2:', rt_ik_joint_2
	# print 'IK Joint 3:', rt_ik_joint_3
	# print 'IK Joint 4:', rt_ik_joint_4
	# print 'IK Joint 5:', rt_ik_joint_5

	ikfk_blend_1 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_2 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_3 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_4 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_1, ikfk_blend_2, ikfk_blend_3, ikfk_blend_4)
	ikfk_blenders = pm.ls(sl=1)
	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_blend'
	for each in ikfk_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)
		each.blender.set(1)

	pm.connectAttr(rt_ik_root + '.rotate', ikfk_blend_1 + '.color1')
	pm.connectAttr(rt_ik_joint_2 + '.rotate', ikfk_blend_2 + '.color1')
	pm.connectAttr(rt_ik_joint_3 + '.rotate', ikfk_blend_3 + '.color1')
	pm.connectAttr(rt_ik_joint_4 + '.rotate', ikfk_blend_4 + '.color1')

	'''
	Connect the output to the bind
	'''
	pm.connectAttr(ikfk_blend_1 + '.output', rt_leg_root + '.rotate')
	pm.connectAttr(ikfk_blend_2 + '.output', rt_leg_joint_2 + '.rotate')
	pm.connectAttr(ikfk_blend_3 + '.output', rt_leg_joint_3 + '.rotate')
	pm.connectAttr(ikfk_blend_4 + '.output', rt_leg_joint_4 + '.rotate')



	ikfk_blend_5 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_6 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_7 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_8 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_5, ikfk_blend_6, ikfk_blend_7, ikfk_blend_8)
	ikfk_tran_blenders = pm.ls(sl=1)
	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_tran_blend'
	for each in ikfk_tran_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)
		each.blender.set(1)

	pm.connectAttr(rt_ik_root + '.translate', ikfk_blend_5 + '.color1')
	pm.connectAttr(rt_ik_joint_2 + '.translate', ikfk_blend_6 + '.color1')
	pm.connectAttr(rt_ik_joint_3 + '.translate', ikfk_blend_7 + '.color1')
	pm.connectAttr(rt_ik_joint_4 + '.translate', ikfk_blend_8 + '.color1')


	pm.connectAttr(ikfk_blend_5 + '.output', rt_leg_root + '.translate')
	pm.connectAttr(ikfk_blend_6 + '.output', rt_leg_joint_2 + '.translate')
	pm.connectAttr(ikfk_blend_7 + '.output', rt_leg_joint_3 + '.translate')
	pm.connectAttr(ikfk_blend_8 + '.output', rt_leg_joint_4 + '.translate')


	
	'''
	Create the ik handles 
	'''
	rt_leg_ikh = pm.ikHandle(sj=rt_ik_root, ee=rt_ik_joint_3)[0]
	rt_ankle_ikh = pm.ikHandle(sj=rt_ik_joint_3, ee=rt_ik_joint_4)[0]
	rt_toe_ikh = pm.ikHandle(sj=rt_ik_joint_4, ee=rt_ik_joint_5)[0]

	ikh_name = rt_leg_root.replace('01_bind', 'ikh')
	rt_leg_ikh.rename(ikh_name)

	ikh_name = rt_leg_ikh.replace('leg', 'ankle')
	rt_ankle_ikh.rename(ikh_name)

	ikh_name = rt_ankle_ikh.replace('ankle', 'toe')
	rt_toe_ikh.rename(ikh_name)

	'''
	Create the foot icon
	'''
	rt_footCurve_1 = pm.curve(p=[(-1.67422e-06, 0, 2.182925), (-0.13416, 0, 2.16342), (-0.266779, 0, 2.095529), (-0.395472, 0, 1.99807), (-0.518993, 0, 1.858632), (-0.636496, 0, 1.679268), (-0.737632, 0, 1.452024), (-0.819474, 0, 1.166445), (-0.846144, 0, 0.821387), (-0.824602, 0, 0.556128), (-0.749206, 0, 0.167213), (-0.673656, 0, -0.127237), (-0.597808, 0, -0.419587), (-0.545054, 0, -0.746104), (-0.544891, 0, -1.097217), (-0.571904, 0, -1.448294), (-0.512279, 0, -1.753435), (-0.393271, 0, -1.92306), (-0.266839, 0, -2.035747), (-0.133965, 0, -2.097731), (0, 0, -2.120128), (0.133965, 0, -2.097731), (0.266839, 0, -2.035747), (0.393271, 0, -1.92306), (0.512279, 0, -1.753435), (0.571904, 0, -1.448294), (0.544891, 0, -1.097217), (0.545054, 0, -0.746104), (0.597807, 0, -0.419586), (0.673656, 0, -0.127237), (0.749207, 0, 0.167214), (0.824602, 0, 0.556128), (0.846144, 0, 0.82139), (0.819474, 0, 1.166447), (0.737631, 0, 1.452029), (0.636486, 0, 1.679267), (0.519008, 0, 1.858641), (0.395504, 0, 1.9981), (0.266596, 0, 2.09545), (0.134293, 0, 2.163449), (-1.67422e-06, 0, 2.182925)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 38], d=3)
	rt_footCurve_2 = pm.curve(p=[(-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217)], k=[0, 0, 0, 1, 2, 3, 3, 3], d=3)

	rt_foot_icon = pm.group(empty=1)

	pm.select(rt_footCurve_1, rt_footCurve_2, rt_foot_icon)
	rt_foot_shapes = pm.ls(sl=1, dag=1)
	rt_curveShape_1 = rt_foot_shapes[1]
	rt_curveShape_2 = rt_foot_shapes[3]
	rt_foot_icon_grp = rt_foot_shapes[4]
	pm.parent(rt_curveShape_1, rt_curveShape_2, rt_foot_icon, s=1, r=1)
	pm.delete(rt_footCurve_1, rt_footCurve_2)
	pm.xform(rt_foot_icon, scale= [3.5, 3.5, 3.5])
	pm.select(rt_foot_icon)
	freezeTransform()

	'''
	Move the foot icon
	'''
	temp_constraint = pm.pointConstraint(rt_ik_joint_3, rt_foot_icon)
	pm.delete(temp_constraint)
	rt_foot_icon.ty.set(0)
	rt_foot_icon.tz.set(6)
	pm.select(rt_foot_icon)
	freezeTransform()
	

	'''
	Rename the foot icon
	'''
	icon_name = rt_leg_root.replace('leg_01_bind', 'foot_icon')
	rt_foot_icon.rename(icon_name)

	'''
	Add foot attrs
	'''
	pm.addAttr(rt_foot_icon, ln='legAttrs', en='------:', at='enum')
	pm.addAttr(rt_foot_icon, ln='stretch', at='bool')

	pm.addAttr(rt_foot_icon, ln='kneeAttrs', at='enum', en='------:')
	lockAttrs(rt_foot_icon, ['kneeAttrs'])
	unhideAttrs(rt_foot_icon, ['kneeAttrs'])


	pm.addAttr(rt_foot_icon, ln='kneeTwist', at='double', dv=0)
	unlock_and_unhide(rt_foot_icon, ['kneeTwist'])

	pm.addAttr(rt_foot_icon, ln='autoKnee', at='bool')
	unlock_and_unhide(rt_foot_icon, ['autoKnee'])

	pm.addAttr(rt_foot_icon, ln='kneeSnap', at='bool')
	unhideAttrs(rt_foot_icon, ['kneeSnap'])


	pm.addAttr(rt_foot_icon, ln='footAttrs', en='------:', at='enum')
	pm.addAttr(rt_foot_icon, ln='roll', dv=0, at='double')
	pm.addAttr(rt_foot_icon, ln='bendLimitAngle', dv=45, at='double')
	pm.addAttr(rt_foot_icon, ln='toeStraightAngle', dv=75, at='double')
	pm.addAttr(rt_foot_icon, ln='tilt', dv=0, at='double')
	pm.addAttr(rt_foot_icon, ln='lean', dv=0, at='double')
	pm.addAttr(rt_foot_icon, ln='toeSpin', dv=0, at='double')
	pm.addAttr(rt_foot_icon, ln='toeTap', dv=0, at='double')
	

	lockAttrs(rt_foot_icon, ['footAttrs', 'legAttrs'])
	unhideAttrs(rt_foot_icon, ['footAttrs', 'legAttrs'])
	unlock_and_unhide(rt_foot_icon, ['roll', 'bendLimitAngle', 'toeStraightAngle', 'tilt', 'lean', 'toeSpin', 'toeTap', 'stretch'])


	'''
	Parent the ikhs under the foot icon
	'''
	pm.parent(rt_leg_ikh, rt_ankle_ikh, rt_toe_ikh, rt_foot_icon)

	'''
	Move the pivot of the foot icon
	'''
	driver_translation = rt_leg_joint_3.getTranslation(ws=1)
	rt_foot_icon.setPivots(driver_translation, ws=1)
	rt_foot_icon.rotateOrder.set(2)

	'''
	Create the distance node
	'''
	rt_loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(rt_leg_root, rt_loc_1, mo=0)
	pm.delete(temp_constraint)
	loc_name = rt_leg_root.replace('01_bind', 'startLoc')
	rt_loc_1.rename(loc_name)

	rt_loc_2 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(rt_leg_joint_3, rt_loc_2, mo=0)
	pm.delete(temp_constraint)
	loc_name = rt_leg_root.replace('01_bind', 'endLoc')
	rt_loc_2.rename(loc_name)

	rt_leg_dist = pm.shadingNode('distanceDimShape', asUtility=1)

	pm.connectAttr(rt_loc_1 + '.worldPosition', rt_leg_dist + '.startPoint')
	pm.connectAttr(rt_loc_2 + '.worldPosition', rt_leg_dist + '.endPoint')

	node_name = rt_leg_root.replace('01_bind', 'dist')
	rt_leg_dist.rename(node_name)

	pm.parent(rt_loc_2, rt_foot_icon)

	rootLength = pm.getAttr(rt_ik_joint_2 + '.translateX')
	joint2Length = pm.getAttr(rt_ik_joint_3  + '.translateX')
	sumLength = (rootLength + joint2Length)
	# print sumLength

	pm.setDrivenKeyframe(rt_ik_joint_2+ '.translateX', dv=sumLength, currentDriver=rt_leg_dist + '.distance', at='.translateX', value=rootLength)

	pm.setDrivenKeyframe(rt_ik_joint_2+ '.translateX', dv=(sumLength*2), currentDriver=rt_leg_dist + '.distance', at='.translateX', value=(rootLength*2))


	pm.setDrivenKeyframe(rt_ik_joint_3+ '.translateX', dv=sumLength, currentDriver=rt_leg_dist + '.distance', at='.translateX', value=joint2Length)

	pm.setDrivenKeyframe(rt_ik_joint_3+ '.translateX', dv=(sumLength*2), currentDriver=rt_leg_dist + '.distance', at='.translateX', value=(joint2Length*2))

	pm.keyTangent(rt_ik_joint_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey(rt_ik_joint_2 + '_translateX', add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.keyTangent(rt_ik_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.selectKey(rt_ik_joint_3 + '_translateX', add=1, k=1, f=(1, 82.555611))
	pm.setInfinity(poi='linear')

	pm.select(rt_leg_ikh, rt_ankle_ikh, rt_toe_ikh, rt_loc_1, rt_loc_2, rt_leg_dist)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.v', 0)

	'''
	Create the rt_knee icon.
	'''

	rt_knee_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
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

	pm.select(rt_knee_icon)
	centerPivot(rt_knee_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the knee icon.
	'''
	temp_constraint = pm.pointConstraint(rt_leg_joint_2, rt_knee_icon)
	pm.delete(temp_constraint)
	freezeTransform(rt_knee_icon)
	pm.xform(rt_knee_icon, t=[0, 0, 10], scale=[.5, .5, .5], ro=[90, 180, 0])
	freezeTransform(rt_knee_icon)

	'''
	Rename knee icon
	'''
	rt_knee_icon_name = rt_leg_root.replace('rt_leg_01_bind', 'rt_knee_icon')
	rt_knee_icon.rename(rt_knee_icon_name)

	
	rt_noFlip_loc = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(rt_ik_joint_3, rt_noFlip_loc, mo=0)
	pm.delete(temp_constraint)
	rt_noFlip_loc.tx.set(10)
	'''
	Create the no flip local
	'''
	rt_noFlip_local = pm.group(empty=1)
	temp_constraint = pm.pointConstraint(rt_ik_joint_3, rt_noFlip_local, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	pm.parent(rt_noFlip_loc, rt_noFlip_local)

	local_name = rt_knee_icon.replace('knee_icon', 'noFlip_local')
	rt_noFlip_local.rename(local_name)

	loc_name = rt_knee_icon.replace('knee_icon', 'noFlip_loc')
	rt_noFlip_loc.rename(loc_name)

	pm.parent(rt_noFlip_local, rt_foot_icon)

	'''
	Create the pole vector for the rt_knee
	'''
	knee_const = pm.poleVectorConstraint(rt_noFlip_loc, rt_knee_icon, rt_leg_ikh)

	const_target_1 = knee_const.getWeightAliasList()[0]
	const_target_2 = knee_const.getWeightAliasList()[1]
	# print const_target_1
	# print const_target_2

	pm.connectAttr(rt_foot_icon + '.kneeTwist', rt_noFlip_local + '.rotateY')


	rt_noFlip_loc.v.set(0)
	rt_foot_icon.autoKnee.set(1)
	const_target_2.set(0)
	rt_leg_ikh.twist.set(90)
	rt_knee_icon.v.set(0)
	pm.setDrivenKeyframe([rt_knee_icon + '.visibility', const_target_1, const_target_2, rt_leg_ikh + '.twist'], currentDriver=rt_foot_icon + '.autoKnee')

	rt_foot_icon.autoKnee.set(0)
	const_target_1.set(0)
	const_target_2.set(1)
	rt_leg_ikh.twist.set(0)
	rt_knee_icon.v.set(1)
	pm.setDrivenKeyframe([rt_knee_icon + '.visibility', const_target_1, const_target_2, rt_leg_ikh + '.twist'], currentDriver=rt_foot_icon + '.autoKnee')
	rt_foot_icon.autoKnee.set(1)


	rt_knee_loc = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.pointConstraint(rt_knee_icon, rt_knee_loc, mo=0)
	pm.delete(temp_constraint)

	loc_name = rt_knee_icon.replace('icon', 'loc')
	rt_knee_loc.rename(loc_name)

	rt_knee_dist_1 = pm.shadingNode('distanceDimShape', asUtility=1)
	pm.connectAttr(rt_loc_1 + '.worldPosition', rt_knee_dist_1 + '.startPoint')
	pm.connectAttr(rt_knee_loc + '.worldPosition', rt_knee_dist_1 + '.endPoint')
	node_name = rt_knee_loc.replace('loc', '01_dist')
	rt_knee_dist_1.rename(node_name)


	rt_knee_dist_2 = pm.shadingNode('distanceDimShape', asUtility=1)
	pm.connectAttr(rt_loc_2 + '.worldPosition', rt_knee_dist_2 + '.startPoint')
	pm.connectAttr(rt_knee_loc + '.worldPosition', rt_knee_dist_2 + '.endPoint')
	node_name = rt_knee_loc.replace('loc', '02_dist')
	rt_knee_dist_2.rename(node_name)

	pm.parent(rt_knee_loc, rt_knee_icon)


	rt_kneeSnapBlend = pm.shadingNode('blendColors', asUtility=1)
	node_name = rt_knee_icon.replace('icon', 'snapBlend')
	rt_kneeSnapBlend.rename(node_name)

	pm.disconnectAttr(rt_ik_joint_2 +'_translateX.output', rt_ik_joint_2 + '.translateX')

	pm.disconnectAttr(rt_ik_joint_3 +'_translateX.output', rt_ik_joint_3 + '.translateX')

	pm.connectAttr(rt_knee_dist_1 + '.distance', rt_kneeSnapBlend + '.color1R')
	pm.connectAttr(rt_knee_dist_2 + '.distance', rt_kneeSnapBlend + '.color1G')

	pm.connectAttr(rt_ik_joint_2 +'_translateX.output', rt_kneeSnapBlend + '.color2R')
	pm.connectAttr(rt_ik_joint_3 +'_translateX.output', rt_kneeSnapBlend + '.color2G')


	pm.connectAttr(rt_kneeSnapBlend + '.outputR', rt_ik_joint_2 + '.translateX')
	pm.connectAttr(rt_kneeSnapBlend + '.outputG', rt_ik_joint_3 + '.translateX')

	pm.connectAttr(rt_foot_icon + '.kneeSnap', rt_kneeSnapBlend + '.blender')

	pm.select(rt_knee_loc, rt_knee_dist_1, rt_knee_dist_2)
	selection = pm.ls(sl=1)
	for each in selection:
		pm.setAttr(each + '.visibility', 0)

	rt_leg_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_leg_root, rt_leg_pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()
	pm.parent(rt_leg_root, rt_ik_root, rt_leg_pad)

	rt_ik_root.v.set(0)

	pad_name = rt_leg_root.replace('01_bind', '00_pad')
	rt_leg_pad.rename(pad_name)


	stretchBlend = pm.shadingNode('blendColors', asUtility=1)
	pm.connectAttr(rt_leg_dist + '.distance', stretchBlend + '.color1R', f=1)
	stretchBlend.color2R.set(1)
	pm.disconnectAttr(rt_leg_dist  +'.distance', rt_ik_joint_2  + '_translateX.input')
	pm.connectAttr(stretchBlend + '.outputR', rt_ik_joint_2 + '_translateX.input', f=1)
	pm.disconnectAttr(rt_leg_dist  +'.distance', rt_ik_joint_3 + '_translateX.input')
	pm.connectAttr(stretchBlend  + '.outputR', rt_ik_joint_3 + '_translateX.input', f=1)
	pm.connectAttr(rt_foot_icon + '.stretch', stretchBlend + '.blender', f=1)
	rt_foot_icon.stretch.set(1)

	node_name = rt_leg_root.replace('01_bind', 'stretchBlend')
	stretchBlend.rename(node_name)

def rt_fkLegSetup(*args):
	global rt_leg_pad, rt_leg_fk_local_1, rt_leg_fk_icon_1, rt_leg_fk_icon_2, rt_leg_fk_icon_3, rt_leg_fk_icon_4
	'''
	Get bind joints
	'''
	pm.select(rt_leg_01_bind)
	selection = pm.ls(sl=1, dag=1)
	rt_leg_root = selection[0]
	rt_leg_joint_2 = selection[1]
	rt_leg_joint_3 = selection[2]
	rt_leg_joint_4 = selection[3]
	rt_leg_joint_5 = selection[4]
	# print 'Leg Root:', rt_leg_root
	# print 'Leg Joint 2:', rt_leg_joint_2
	# print 'Leg Joint 3:', rt_leg_joint_3
	# print 'Leg Joint 4:', rt_leg_joint_4
	# print 'Leg Joint 5:', rt_leg_joint_5

	pm.joint(zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='xup')
	rt_leg_joint_5.jointOrientX.set(0)
	rt_leg_joint_5.jointOrientZ.set(0)
	
	'''
	Make fk joints
	'''

	fk_joints = pm.duplicate(rt_leg_root)
	pm.select(fk_joints)
	fk_joints = pm.ls(sl=1, dag=1)
	rt_fk_root = fk_joints[0]
	rt_fk_joint_2 = fk_joints[1]
	rt_fk_joint_3 = fk_joints[2]
	rt_fk_joint_4 = fk_joints[3]
	rt_fk_joint_5 = fk_joints[4]


	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'fk'
	for each in fk_joints:
		count = count + 1
		new_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(new_name)

	# print 'FK Root:', rt_fk_root
	# print 'FK Joint 2:', rt_fk_joint_2
	# print 'FK Joint 3:', rt_fk_joint_3
	# print 'FK Joint 4:', rt_fk_joint_4
	# print 'FK Joint 5:', rt_fk_joint_5

	ikfk_blend_1 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_2 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_3 = pm.shadingNode('blendColors', asUtility=1)
	ikfk_blend_4 = pm.shadingNode('blendColors', asUtility=1)
	pm.select(ikfk_blend_1, ikfk_blend_2, ikfk_blend_3, ikfk_blend_4)
	ikfk_rot_blenders = pm.ls(sl=1)
	ori = 'rt'
	system_name = 'leg'
	count = 0
	suffix = 'ikfk_rot_blend'
	for each in ikfk_rot_blenders:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)
		pm.setAttr(each + '.blender')

	pm.connectAttr(rt_fk_root + '.rotate', ikfk_blend_1 + '.color1')
	pm.connectAttr(rt_fk_joint_2 + '.rotate', ikfk_blend_2 + '.color1')
	pm.connectAttr(rt_fk_joint_3 + '.rotate', ikfk_blend_3 + '.color1')
	pm.connectAttr(rt_fk_joint_4 + '.rotate', ikfk_blend_4 + '.color1')


	'''
	Connect the output to the bind
	'''
	pm.connectAttr(ikfk_blend_1 + '.output', rt_leg_root + '.rotate')
	pm.connectAttr(ikfk_blend_2 + '.output', rt_leg_joint_2 + '.rotate')
	pm.connectAttr(ikfk_blend_3 + '.output', rt_leg_joint_3 + '.rotate')
	pm.connectAttr(ikfk_blend_4 + '.output', rt_leg_joint_4 + '.rotate')


	'''
	Create fk icons
	'''
	rt_leg_fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	# print 'Fk icon 1:', rt_leg_fk_icon_1
	temp_constraint = pm.parentConstraint(rt_fk_root, rt_leg_fk_icon_1)
	pm.delete(temp_constraint)
	rt_leg_fk_local_1 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_fk_root, rt_leg_fk_local_1)
	pm.delete(temp_constraint)
	pm.parent(rt_leg_fk_icon_1, rt_leg_fk_local_1)
	pm.select(rt_leg_fk_icon_1)
	freezeTransform()


	rt_leg_fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 2:', rt_leg_fk_icon_2
	temp_constraint = pm.parentConstraint(rt_fk_joint_2, rt_leg_fk_icon_2)
	pm.delete(temp_constraint)
	rt_leg_fk_local_2 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_fk_joint_2, rt_leg_fk_local_2)
	pm.delete(temp_constraint)
	pm.parent(rt_leg_fk_icon_2, rt_leg_fk_local_2)
	pm.select(rt_leg_fk_icon_2)
	freezeTransform()
	pm.parent(rt_leg_fk_local_2, rt_leg_fk_icon_1)

	rt_leg_fk_icon_3 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 3:', rt_leg_fk_icon_3
	temp_constraint = pm.parentConstraint(rt_fk_joint_3, rt_leg_fk_icon_3)
	pm.delete(temp_constraint)
	rt_leg_fk_local_3 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_fk_joint_3, rt_leg_fk_local_3)
	pm.delete(temp_constraint)
	pm.parent(rt_leg_fk_icon_3, rt_leg_fk_local_3)
	pm.select(rt_leg_fk_icon_3)
	freezeTransform()
	pm.parent(rt_leg_fk_local_3, rt_leg_fk_icon_2)

	rt_leg_fk_icon_4 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	# print 'Fk icon 4:', rt_leg_fk_icon_4
	temp_constraint = pm.parentConstraint(rt_fk_joint_4, rt_leg_fk_icon_4)
	pm.delete(temp_constraint)
	rt_leg_fk_local_4 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_fk_joint_4, rt_leg_fk_local_4)
	pm.delete(temp_constraint)
	pm.parent(rt_leg_fk_icon_4, rt_leg_fk_local_4)
	pm.select(rt_leg_fk_icon_4)
	freezeTransform()
	pm.parent(rt_leg_fk_local_4, rt_leg_fk_icon_3)

	pm.select(rt_leg_fk_icon_1, rt_leg_fk_icon_2, rt_leg_fk_icon_3, rt_leg_fk_icon_4)
	fk_icons = pm.ls(sl=1)


	pm.select(rt_leg_fk_local_1, rt_leg_fk_local_2, rt_leg_fk_local_3, rt_leg_fk_local_4)
	fk_locals = pm.ls(sl=1)

	count = 0
	suffix = 'fk_icon'
	for each in fk_icons:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	count = 0
	suffix = 'fk_local'
	for each in fk_locals:
		count = count + 1
		node_name = '{0}_{1}_0{2}_{3}'.format(ori, system_name, count, suffix)
		each.rename(node_name)

	pm.orientConstraint(rt_leg_fk_icon_1, rt_fk_root, mo=0)
	pm.orientConstraint(rt_leg_fk_icon_2, rt_fk_joint_2, mo=0)
	pm.orientConstraint(rt_leg_fk_icon_3, rt_fk_joint_3, mo=0)
	pm.orientConstraint(rt_leg_fk_icon_4, rt_fk_joint_4, mo=0)

	pm.addAttr(rt_leg_fk_icon_1, ln='length', dv=1, min=0, at='double' )
	rt_leg_fk_icon_1.length.set(e=1, keyable=1)
	pm.addAttr(rt_leg_fk_icon_2, ln='length', dv=1, min=0, at='double' )
	rt_leg_fk_icon_2.length.set(e=1, keyable=1)

	pm.setDrivenKeyframe(rt_fk_joint_2 + '.translateX', currentDriver=rt_leg_fk_icon_1  + '.length')
	rt_leg_fk_icon_1.length.set(0)
	rt_fk_joint_2.tx.set(0)
	pm.setDrivenKeyframe(rt_fk_joint_2 + '.translateX', currentDriver=rt_leg_fk_icon_1  + '.length')
	rt_leg_fk_icon_1.length.set(1)

	pm.keyTangent(rt_fk_joint_2, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(rt_fk_joint_2 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	pm.setDrivenKeyframe(rt_fk_joint_3 + '.translateX', currentDriver=rt_leg_fk_icon_2  + '.length')
	rt_leg_fk_icon_2.length.set(0)
	rt_fk_joint_3.tx.set(0)
	pm.setDrivenKeyframe(rt_fk_joint_3 + '.translateX', currentDriver=rt_leg_fk_icon_2  + '.length')
	rt_leg_fk_icon_2.length.set(1)

	pm.keyTangent(rt_fk_joint_3, 'graphEditor1FromOutliner', itt='spline', animation='objects', ott='spline')
	pm.mel.selectKey(rt_fk_joint_3 + '.tx', add=1, k=1, f=1)
	pm.setInfinity(poi='linear')

	rt_leg_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(rt_leg_root, rt_leg_pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()

	pad_name = rt_leg_root.replace('01_bind', '00_pad')
	rt_leg_pad.rename(pad_name)

	pm.parent(rt_leg_root, rt_fk_root, rt_leg_pad)

	rt_fk_root.v.set(0)

def fk_legSetup(*args):
	lt_fkLegSetup()
	rt_fkLegSetup()

def ik_legSetup(*args):
	lt_ikLegSetup()
	rt_ikLegSetup()

def legSetup(*args):
	lt_legSetup()
	rt_legSetup()

def legSystem(*args):
	ori_selection_type = pm.radioButtonGrp('leg_orientationOption', q=1, sl=1) 
	# print 'Orientation Selection:', ori_selection_type

	system_selection_type = pm.radioButtonGrp('leg_systemOption', q=1, sl=1)
	# print 'System Selection:', system_selection_type

	if ori_selection_type == 1:
		pass 
		if system_selection_type == 1:
			lt_fkLegSetup()
	if ori_selection_type == 2:
		pass
		if system_selection_type == 1:
			rt_fkLegSetup()
	if ori_selection_type == 3:
		pass
		if system_selection_type == 1:
			fkLegSetup()

	if ori_selection_type == 1:
		pass 
		if system_selection_type == 2:
			lt_ikLegSetup()
	if ori_selection_type == 2:
		pass
		if system_selection_type == 2:
			rt_ikLegSetup()
	if ori_selection_type == 3:
		pass
		if system_selection_type == 2:
			ikLegSetup()
	if ori_selection_type == 1:
		pass 
		if system_selection_type == 3:
			lt_legSetup()
	if ori_selection_type == 2:
		pass
		if system_selection_type == 3:
			rt_legSetup()
	if ori_selection_type == 3:
		pass
		if system_selection_type == 3:
			legSetup()

def lt_rflPrep(*args):
	global lt_leg_root, lt_leg_joint_2, lt_leg_joint_3, lt_leg_joint_4, lt_leg_joint_5
	global lt_heel_loc, lt_outerBank_loc, lt_innerBank_loc, lt_toe_loc, lt_ball_loc, lt_ankle_loc
	'''
	Create the locators
	'''
	lt_heel_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 1:', lt_heel_loc

	lt_outerBank_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 2:', lt_outerBank_loc
	pm.xform(lt_outerBank_loc, t=[-3, 0, 10])

	lt_innerBank_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 3:', lt_innerBank_loc
	pm.xform(lt_innerBank_loc, t=[3, 0, 10])
	
	lt_toe_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 4:', lt_toe_loc
	pm.xform(lt_toe_loc, t=[0, 0, 14])

	lt_ball_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 5:', lt_ball_loc 
	pm.xform(lt_ball_loc, t=[0, 0, 10])

	lt_ankle_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 6:', lt_ankle_loc 
	pm.xform(lt_ankle_loc, t=[0, 7, 2])

	locs = pm.select(lt_heel_loc, lt_outerBank_loc, lt_innerBank_loc, lt_toe_loc, lt_ball_loc, lt_ankle_loc)
	freezeTransform(locs)

	pm.parent(lt_outerBank_loc, lt_heel_loc)
	pm.parent(lt_innerBank_loc, lt_outerBank_loc)
	pm.parent(lt_toe_loc, lt_innerBank_loc)
	pm.parent(lt_ball_loc, lt_toe_loc)
	pm.parent(lt_ankle_loc, lt_ball_loc)

	'''
	Rename the locs
	'''
	loc_name = lt_leg_root.replace('leg_01_bind', 'heel_loc')
	lt_heel_loc.rename(loc_name)
	loc_name = lt_heel_loc.replace('heel', 'innerBank')
	lt_outerBank_loc.rename(loc_name)
	loc_name = lt_outerBank_loc.replace('inner', 'outer')
	lt_innerBank_loc.rename(loc_name)
	loc_name = lt_heel_loc.replace('heel', 'toe')
	lt_toe_loc.rename(loc_name)
	loc_name = lt_toe_loc.replace('toe', 'ball')
	lt_ball_loc.rename(loc_name)
	loc_name = lt_ball_loc.replace('ball', 'ankle')
	lt_ankle_loc.rename(loc_name)

def lt_rflSetup(*args):
	global lt_heel_rot_clamp, lt_ball_rot_clamp, lt_footBtoS_clamp, lt_footBtoS_percent, lt_foot_roll_mult, lt_toeTap_invert_mult 
	global lt_ball_0toB_percent, lt_foot_invert_percent, lt_ball_percent_mult, lt_ball_roll_mult, lt_ball_rot_clamp
	pm.select(lt_heel_loc)
	freezeTransform()
	
	'''
	Create and rename the heel rot clamp
	'''
	lt_heel_rot_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = lt_heel_loc.replace('loc', 'rot_clamp')
	lt_heel_rot_clamp.rename(clamp_name)
	# print 'Heel rot clamp:', lt_heel_rot_clamp

	lt_ball_rot_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = lt_heel_rot_clamp.replace('heel', 'ball')
	lt_ball_rot_clamp.rename(clamp_name)
	# print 'Ball rot clamp:', lt_ball_rot_clamp

	lt_footBtoS_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = lt_heel_rot_clamp.replace('lt_heel_rot', 'lt_footBtoS')
	lt_footBtoS_clamp.rename(clamp_name)
	# print 'Foot BtoS clamp:', lt_footBtoS_clamp

	lt_footBtoS_percent = pm.shadingNode('setRange', asUtility=1)
	clamp_name = lt_footBtoS_clamp.replace('clamp', 'percent')
	lt_footBtoS_percent.rename(clamp_name)
	# print 'Foot BtoS perect:', lt_footBtoS_percent

	lt_foot_roll_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = lt_foot_icon.replace('icon', 'roll_mult')
	lt_foot_roll_mult.rename(clamp_name)
	# print 'Foot roll mult:', lt_foot_roll_mult

	lt_toeTap_invert_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = lt_foot_icon.replace('lt_foot_icon', 'lt_toeTap_invert_mult')
	lt_toeTap_invert_mult.rename(clamp_name)

	pm.connectAttr(lt_foot_icon + '.roll', lt_heel_rot_clamp + '.inputR')
	lt_heel_rot_clamp.minR.set(-90)
	pm.connectAttr(lt_heel_rot_clamp + '.outputR', lt_heel_loc + '.rotateX')
	pm.connectAttr(lt_foot_icon + '.roll', lt_ball_rot_clamp + '.inputR')
	lt_ball_rot_clamp.maxR.set(90)
	pm.connectAttr(lt_ball_rot_clamp + '.outputR', lt_ball_loc + '.rotateX')

	pm.connectAttr(lt_foot_icon + '.toeStraightAngle', lt_footBtoS_clamp + '.maxR')
	pm.connectAttr(lt_foot_icon + '.bendLimitAngle', lt_footBtoS_clamp + '.minR')
	pm.connectAttr(lt_foot_icon + '.roll', lt_footBtoS_clamp + '.inputR')

	pm.connectAttr(lt_footBtoS_clamp + '.maxR', lt_footBtoS_percent + '.oldMaxX')
	pm.connectAttr(lt_footBtoS_clamp + '.minR', lt_footBtoS_percent + '.oldMinX')
	pm.setAttr(lt_footBtoS_percent + '.maxX', 1)
	pm.connectAttr(lt_footBtoS_clamp + '.inputR', lt_footBtoS_percent + '.valueX')

	pm.connectAttr(lt_footBtoS_percent + '.outValueX', lt_foot_roll_mult + '.input1X')
	pm.connectAttr(lt_footBtoS_clamp + '.inputR', lt_foot_roll_mult + '.input2X')
	pm.connectAttr(lt_foot_roll_mult + '.outputX', lt_toe_loc + '.rotateX')

	pm.disconnectAttr(lt_ball_rot_clamp + '.outputR', lt_ball_loc + '.rotateX')

	pm.connectAttr(lt_foot_icon + '.bendLimitAngle', lt_ball_rot_clamp + '.maxR')

	pm.setDrivenKeyframe(lt_innerBank_loc + '.rotateZ', currentDriver=lt_foot_icon + '.tilt')
	pm.setDrivenKeyframe(lt_outerBank_loc + '.rotateZ', currentDriver=lt_foot_icon + '.tilt')
	lt_foot_icon.tilt.set(-90)
	lt_outerBank_loc.rz.set(90)
	# pm.setAttr("lt_foot_icon.tilt", -90)
	# pm.setAttr("lt_innerBank_loc.rotateZ", 90)
	pm.setDrivenKeyframe(lt_outerBank_loc + '.rotateZ', currentDriver=lt_foot_icon + '.tilt')
	lt_foot_icon.tilt.set(90)
	lt_innerBank_loc.rz.set(-90)
	pm.setDrivenKeyframe(lt_innerBank_loc + '.rotateZ', currentDriver=lt_foot_icon + '.tilt')
	lt_foot_icon.tilt.set(0)

	'''
	Toe Tap Setup
	'''
	lt_toeTap_pivot = pm.group(empty=1, n='lt_toeTap_pivot')
	temp_constraint = pm.parentConstraint(lt_leg_joint_4, lt_toeTap_pivot)
	pm.delete(temp_constraint)
	pm.makeIdentity(lt_toeTap_pivot, apply=1, t=1, r=1, s=1, n=0, pn=1)
	pm.parent(lt_toe_ikh, lt_toeTap_pivot)
	pm.parent(lt_toeTap_pivot, lt_toe_loc)
	pm.setAttr(lt_toeTap_invert_mult + '.input2X', -1)
	pm.connectAttr(lt_foot_icon + '.toeTap', lt_toeTap_invert_mult + '.input1X')
	pm.connectAttr(lt_toeTap_invert_mult + '.input1X', lt_toeTap_pivot + '.rotateX')

	lt_ball_0toB_percent = pm.shadingNode('setRange', asUtility=1)
	clamp_name = lt_footBtoS_percent.replace('lt_footBtoS', 'lt_ball_0toB')
	lt_ball_0toB_percent.rename(clamp_name)
	# print 'Ball ball 0toB percent:', lt_ball_0toB_percent

	lt_foot_invert_percent = pm.shadingNode('plusMinusAverage', asUtility=1)
	clamp_name = lt_foot_icon.replace('icon', 'invert_percent')
	lt_foot_invert_percent.rename(clamp_name)
	# print 'Foot invert percent:', lt_foot_invert_percent

	lt_ball_percent_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = lt_foot_roll_mult.replace('lt_foot_roll', 'lt_ball_percent' )
	lt_ball_percent_mult.rename(clamp_name)
	# print 'ball percent mult:', lt_ball_percent_mult

	clamp_name = lt_heel_rot_clamp.replace('lt_heel_rot', 'lt_ball_0toB')
	lt_ball_rot_clamp.rename(clamp_name)
	# print 'Ball rot clamp:', lt_ball_rot_clamp

	lt_ball_roll_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = lt_ball_percent_mult.replace('percent', 'roll')
	lt_ball_roll_mult.rename(clamp_name)
	# print 'ball roll mult:', lt_ball_roll_mult

	pm.connectAttr(lt_ball_rot_clamp+ '.maxR', lt_ball_0toB_percent+ '.oldMaxX')
	pm.connectAttr(lt_ball_rot_clamp+ '.minR', lt_ball_0toB_percent+ '.oldMinX')
	pm.setAttr(lt_ball_0toB_percent+ '.maxX', 1)
	pm.connectAttr(lt_ball_rot_clamp+ '.inputR', lt_ball_0toB_percent+ '.valueX')

	pm.setAttr(lt_foot_invert_percent+ '.input1D[0]', 1)
	pm.setAttr(lt_foot_invert_percent+ '.input1D[1]', 1)
	pm.connectAttr(lt_footBtoS_percent+ '.outValueX', lt_foot_invert_percent+ '.input1D[1]')
	pm.setAttr(lt_foot_invert_percent+ '.operation', 2)

	pm.connectAttr(lt_ball_0toB_percent+ '.outValueX', lt_ball_percent_mult+ '.input1X')
	pm.connectAttr(lt_foot_invert_percent+ '.output1D', lt_ball_percent_mult+ '.input2X')

	pm.connectAttr(lt_ball_percent_mult+ '.outputX', lt_ball_roll_mult+ '.input1X')
	pm.connectAttr(lt_foot_icon+ '.roll', lt_ball_roll_mult+ '.input2X')
	pm.connectAttr(lt_ball_roll_mult+ '.outputX', lt_ball_loc+ '.rotateX')

	pm.parent(lt_ankle_ikh, lt_ball_loc)
	pm.parent(lt_leg_ikh, lt_ankle_loc)

	'''
	Lean
	'''
	pm.connectAttr('lt_foot_icon.lean', lt_ball_loc + '.rz')

	'''
	Toe Spin
	'''
	pm.connectAttr('lt_foot_icon.toeSpin', lt_toe_loc + '.ry')

	'''
	Parent the heel loc under the foot icon
	'''
	pm.parent(lt_heel_loc, lt_foot_icon)

	pm.parent(lt_noFlip_local, lt_ankle_loc)

	lt_heel_loc.v.set(0)

def rt_rflPrep(*args):
	global rt_leg_root, rt_leg_joint_2, rt_leg_joint_3, rt_leg_joint_4, rt_leg_joint_5
	global rt_heel_loc, rt_outerBank_loc, rt_innerBank_loc, rt_toe_loc, rt_ball_loc, rt_ankle_loc
	'''
	Create the locators
	'''
	rt_heel_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 1:', rt_heel_loc

	rt_outerBank_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 2:', rt_outerBank_loc
	pm.xform(rt_outerBank_loc, t=[-3, 0, 10])

	rt_innerBank_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 3:', rt_innerBank_loc
	pm.xform(rt_innerBank_loc, t=[3, 0, 10])
	
	rt_toe_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 4:', rt_toe_loc
	pm.xform(rt_toe_loc, t=[0, 0, 14])

	rt_ball_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 5:', rt_ball_loc 
	pm.xform(rt_ball_loc, t=[0, 0, 10])

	rt_ankle_loc = pm.spaceLocator(p=(0, 0, 0))
	# print 'Locator 6:', rt_ankle_loc 
	pm.xform(rt_ankle_loc, t=[0, 7, 2])

	locs = pm.select(rt_heel_loc, rt_outerBank_loc, rt_innerBank_loc, rt_toe_loc, rt_ball_loc, rt_ankle_loc)
	freezeTransform(locs)

	pm.parent(rt_outerBank_loc, rt_heel_loc)
	pm.parent(rt_innerBank_loc, rt_outerBank_loc)
	pm.parent(rt_toe_loc, rt_innerBank_loc)
	pm.parent(rt_ball_loc, rt_toe_loc)
	pm.parent(rt_ankle_loc, rt_ball_loc)

	'''
	Rename the locs
	'''
	loc_name = rt_leg_root.replace('leg_01_bind', 'heel_loc')
	rt_heel_loc.rename(loc_name)
	loc_name = rt_heel_loc.replace('heel', 'innerBank')
	rt_outerBank_loc.rename(loc_name)
	loc_name = rt_outerBank_loc.replace('inner', 'outer')
	rt_innerBank_loc.rename(loc_name)
	loc_name = rt_heel_loc.replace('heel', 'toe')
	rt_toe_loc.rename(loc_name)
	loc_name = rt_toe_loc.replace('toe', 'ball')
	rt_ball_loc.rename(loc_name)
	loc_name = rt_ball_loc.replace('ball', 'ankle')
	rt_ankle_loc.rename(loc_name)

def rt_rflSetup(*args):
	global rt_heel_rot_clamp, rt_ball_rot_clamp, rt_footBtoS_clamp, rt_footBtoS_percent, rt_foot_roll_mult, rt_toeTap_invert_mult 
	global rt_ball_0toB_percent, rt_foot_invert_percent, rt_ball_percent_mult, rt_ball_roll_mult, rt_ball_rot_clamp
	pm.select(rt_heel_loc)
	freezeTransform()
	
	'''
	Create and rename the heel rot clamp
	'''
	rt_heel_rot_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = rt_heel_loc.replace('loc', 'rot_clamp')
	rt_heel_rot_clamp.rename(clamp_name)
	# print 'Heel rot clamp:', rt_heel_rot_clamp

	rt_ball_rot_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = rt_heel_rot_clamp.replace('heel', 'ball')
	rt_ball_rot_clamp.rename(clamp_name)
	# print 'Ball rot clamp:', rt_ball_rot_clamp

	rt_footBtoS_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = rt_heel_rot_clamp.replace('rt_heel_rot', 'rt_footBtoS')
	rt_footBtoS_clamp.rename(clamp_name)
	# print 'Foot BtoS clamp:', rt_footBtoS_clamp

	rt_footBtoS_percent = pm.shadingNode('setRange', asUtility=1)
	clamp_name = rt_footBtoS_clamp.replace('clamp', 'percent')
	rt_footBtoS_percent.rename(clamp_name)
	# print 'Foot BtoS perect:', rt_footBtoS_percent

	rt_foot_roll_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = rt_foot_icon.replace('icon', 'roll_mult')
	rt_foot_roll_mult.rename(clamp_name)
	# print 'Foot roll mult:', rt_foot_roll_mult

	rt_toeTap_invert_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = rt_foot_icon.replace('rt_foot_icon', 'rt_toeTap_invert_mult')
	rt_toeTap_invert_mult.rename(clamp_name)

	pm.connectAttr(rt_foot_icon + '.roll', rt_heel_rot_clamp + '.inputR')
	rt_heel_rot_clamp.minR.set(-90)
	pm.connectAttr(rt_heel_rot_clamp + '.outputR', rt_heel_loc + '.rotateX')
	pm.connectAttr(rt_foot_icon + '.roll', rt_ball_rot_clamp + '.inputR')
	rt_ball_rot_clamp.maxR.set(90)
	pm.connectAttr(rt_ball_rot_clamp + '.outputR', rt_ball_loc + '.rotateX')

	pm.connectAttr(rt_foot_icon + '.toeStraightAngle', rt_footBtoS_clamp + '.maxR')
	pm.connectAttr(rt_foot_icon + '.bendLimitAngle', rt_footBtoS_clamp + '.minR')
	pm.connectAttr(rt_foot_icon + '.roll', rt_footBtoS_clamp + '.inputR')

	pm.connectAttr(rt_footBtoS_clamp + '.maxR', rt_footBtoS_percent + '.oldMaxX')
	pm.connectAttr(rt_footBtoS_clamp + '.minR', rt_footBtoS_percent + '.oldMinX')
	pm.setAttr(rt_footBtoS_percent + '.maxX', 1)
	pm.connectAttr(rt_footBtoS_clamp + '.inputR', rt_footBtoS_percent + '.valueX')

	pm.connectAttr(rt_footBtoS_percent + '.outValueX', rt_foot_roll_mult + '.input1X')
	pm.connectAttr(rt_footBtoS_clamp + '.inputR', rt_foot_roll_mult + '.input2X')
	pm.connectAttr(rt_foot_roll_mult + '.outputX', rt_toe_loc + '.rotateX')

	pm.disconnectAttr(rt_ball_rot_clamp + '.outputR', rt_ball_loc + '.rotateX')

	pm.connectAttr(rt_foot_icon + '.bendLimitAngle', rt_ball_rot_clamp + '.maxR')

	pm.setDrivenKeyframe(rt_innerBank_loc + '.rotateZ', currentDriver=rt_foot_icon + '.tilt')
	pm.setDrivenKeyframe(rt_outerBank_loc + '.rotateZ', currentDriver=rt_foot_icon + '.tilt')
	rt_foot_icon.tilt.set(-90)
	rt_outerBank_loc.rz.set(90)
	# pm.setAttr("rt_foot_icon.tilt", -90)
	# pm.setAttr("rt_innerBank_loc.rotateZ", 90)
	pm.setDrivenKeyframe(rt_outerBank_loc + '.rotateZ', currentDriver=rt_foot_icon + '.tilt')
	rt_foot_icon.tilt.set(90)
	rt_innerBank_loc.rz.set(-90)
	pm.setDrivenKeyframe(rt_innerBank_loc + '.rotateZ', currentDriver=rt_foot_icon + '.tilt')
	rt_foot_icon.tilt.set(0)

	'''
	Toe Tap Setup
	'''
	rt_toeTap_pivot = pm.group(empty=1, n='rt_toeTap_pivot')
	temp_constraint = pm.parentConstraint(rt_leg_joint_4, rt_toeTap_pivot)
	pm.delete(temp_constraint)
	pm.makeIdentity(rt_toeTap_pivot, apply=1, t=1, r=1, s=1, n=0, pn=1)
	pm.parent(rt_toe_ikh, rt_toeTap_pivot)
	pm.parent(rt_toeTap_pivot, rt_toe_loc)
	pm.setAttr(rt_toeTap_invert_mult + '.input2X', -1)
	pm.connectAttr(rt_foot_icon + '.toeTap', rt_toeTap_invert_mult + '.input1X')
	pm.connectAttr(rt_toeTap_invert_mult + '.input1X', rt_toeTap_pivot + '.rotateX')

	rt_ball_0toB_percent = pm.shadingNode('setRange', asUtility=1)
	clamp_name = rt_footBtoS_percent.replace('rt_footBtoS', 'rt_ball_0toB')
	rt_ball_0toB_percent.rename(clamp_name)
	# print 'Ball ball 0toB percent:', rt_ball_0toB_percent

	rt_foot_invert_percent = pm.shadingNode('plusMinusAverage', asUtility=1)
	clamp_name = rt_foot_icon.replace('icon', 'invert_percent')
	rt_foot_invert_percent.rename(clamp_name)
	# print 'Foot invert percent:', rt_foot_invert_percent

	rt_ball_percent_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = rt_foot_roll_mult.replace('rt_foot_roll', 'rt_ball_percent' )
	rt_ball_percent_mult.rename(clamp_name)
	# print 'ball percent mult:', rt_ball_percent_mult

	clamp_name = rt_heel_rot_clamp.replace('rt_heel_rot', 'rt_ball_0toB')
	rt_ball_rot_clamp.rename(clamp_name)
	# print 'Ball rot clamp:', rt_ball_rot_clamp

	rt_ball_roll_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = rt_ball_percent_mult.replace('percent', 'roll')
	rt_ball_roll_mult.rename(clamp_name)
	# print 'ball roll mult:', rt_ball_roll_mult

	pm.connectAttr(rt_ball_rot_clamp+ '.maxR', rt_ball_0toB_percent+ '.oldMaxX')
	pm.connectAttr(rt_ball_rot_clamp+ '.minR', rt_ball_0toB_percent+ '.oldMinX')
	pm.setAttr(rt_ball_0toB_percent+ '.maxX', 1)
	pm.connectAttr(rt_ball_rot_clamp+ '.inputR', rt_ball_0toB_percent+ '.valueX')

	pm.setAttr(rt_foot_invert_percent+ '.input1D[0]', 1)
	pm.setAttr(rt_foot_invert_percent+ '.input1D[1]', 1)
	pm.connectAttr(rt_footBtoS_percent+ '.outValueX', rt_foot_invert_percent+ '.input1D[1]')
	pm.setAttr(rt_foot_invert_percent+ '.operation', 2)

	pm.connectAttr(rt_ball_0toB_percent+ '.outValueX', rt_ball_percent_mult+ '.input1X')
	pm.connectAttr(rt_foot_invert_percent+ '.output1D', rt_ball_percent_mult+ '.input2X')

	pm.connectAttr(rt_ball_percent_mult+ '.outputX', rt_ball_roll_mult+ '.input1X')
	pm.connectAttr(rt_foot_icon+ '.roll', rt_ball_roll_mult+ '.input2X')
	pm.connectAttr(rt_ball_roll_mult+ '.outputX', rt_ball_loc+ '.rotateX')

	pm.parent(rt_ankle_ikh, rt_ball_loc)
	pm.parent(rt_leg_ikh, rt_ankle_loc)

	'''
	Lean
	'''
	pm.connectAttr('rt_foot_icon.lean', rt_ball_loc + '.rz')

	'''
	Toe Spin
	'''
	pm.connectAttr('rt_foot_icon.toeSpin', rt_toe_loc + '.ry')

	'''
	Parent the heel loc under the foot icon
	'''
	pm.parent(rt_heel_loc, rt_foot_icon)

	pm.parent(rt_noFlip_local, rt_ankle_loc)

	rt_heel_loc.v.set(0)

def rflPrep(*args):
	lt_rflPrep()
	rt_rflPrep()

def rflSetup(*args):
	lt_rflSetup()
	rt_rflSetup()

def rflPrepSystem(*args):
	ori_selection_type = pm.radioButtonGrp('rfl_orientationOption', q=1, sl=1) 
	print 'Orientation Selection:', ori_selection_type

	if ori_selection_type == 1:
		lt_rflPrep()	 
	if ori_selection_type == 2:
		rt_rflPrep()
	if ori_selection_type == 3:
		rflPrep()

def rflSystem(*args):
	ori_selection_type = pm.radioButtonGrp('rfl_orientationOption', q=1, sl=1) 
	print 'Orientation Selection:', ori_selection_type

	if ori_selection_type == 1:
		lt_rflSetup()	 
	if ori_selection_type == 2:
		rt_rflSetup()
	if ori_selection_type == 3:
		rflSetup()

def rflVis(*args):
	if pm.objExists('lt_leg_ikh'):
		ori_selection_type = pm.radioButtonGrp('rfl_orientationOption', q=1, sl=1, vis=1)
	else:
		ori_selection_type = pm.radioButtonGrp('rfl_orientationOption', q=1, sl=1, vis=0)

def bodyGeo_selection(*args):
	global body_geo
	selection = pm.ls(sl=1)
	body_geo = selection[0]
	print 'Body Geo selected:', body_geo

	body_geo_textChange = pm.textField('body_geo_selection', e=1, text=body_geo)

def lt_eyeGeo_selection(*args):
	global lt_eye_geo
	selection = pm.ls(sl=1)
	lt_eye_geo = selection[0]
	print 'Body Geo selected:', lt_eye_geo

	lt_eye_geo_textChange = pm.textField('lt_eye_geo_selection', e=1, text=lt_eye_geo)

def rt_eyeGeo_selection(*args):
	global rt_eye_geo
	selection = pm.ls(sl=1)
	rt_eye_geo = selection[0]
	print 'Body Geo selected:', rt_eye_geo

	rt_eye_geo_textChange = pm.textField('rt_eye_geo_selection', e=1, text=rt_eye_geo)

def bodyBind(*args):
	pm.select('*bind', body_geo)
	cmds.bindSkin(bcp=1, tsb=1, cj=0, dnd=1)

def eyeBind(*args):
	pm.select('*Bind', lt_eye_geo, rt_eye_geo)
	cmds.bindSkin(bcp=1, tsb=1, cj=0, dnd=1)

def windowResize(*args):
	if pm.window('ByrdRigs_Biped_Body_Auto_Rigger', q=1, exists=1):
		pm.window('ByrdRigs_Biped_Body_Auto_Rigger', e=1, wh=(240, 110), rtf=1)
	else:
		pm.warning('ByrdRigs_Biped_Body_Auto_Rigger does not exist')

def deleteUI(*args):
	pm.deleteUI('ByrdRigs_Biped_Body_Auto_Rigger')



