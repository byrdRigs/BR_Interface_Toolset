'''
ByrdRigs Interface tool

import BR_Interface_Toolset.BR_01_InterfaceTool as BR_InterfaceTool
reload (BR_InterfaceTool)
BR_InterfaceTool.gui()

'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

# Still needs the control tab with the icons 
# Working on the quad and biped setups

tab_bgc=(0.4718592, 0.13568, 239)
subTab_bgc = (0.4915200, 0.32256, 241)
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
color_10 = (.529, .078, .678)


def gui():
	if pm.window('ByrdRigs_interface_toolset', q=1, exists=1):
		pm.deleteUI('ByrdRigs_interface_toolset')
		#ByrdRigs_interface_toolset

	win_width = 240
	window_object = pm.window('ByrdRigs_interface_toolset', title="ByrdRigs_interface_toolset", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()


	'''
	Clean Up Geo and Controls

	'''
	pm.frameLayout(w=win_width, label='Clean Up', bgc=color_1, cl=1, cll=1, ann='Clean Up', cc=windowResize)
	pm.rowColumnLayout(w=win_width)
	pm.iconTextButton('delete_histroy', w=166, st='iconAndTextHorizontal', image1='DeleteHistory.png',label='Delete History', c=deleteHistory)
	pm.iconTextButton(w=166, st='iconAndTextHorizontal', image1='CenterPivot.png',label='Center Pivot', c=centerPivot)
	pm.iconTextButton(w=166, st='iconAndTextHorizontal', image1='FreezeTransform.png',label='Freeze Transforms', c=freezeTransform)

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_1, st='in')

	'''
	Visibility
	'''
	pm.frameLayout(w=win_width, label='Visibility', bgc=color_2, cl=1, cll=1, ann='Change Visibility', cc=windowResize)
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(label='Show')
	pm.button(label='All', c=showAll)
	pm.button(label='None', c=showNone)
	pm.text(label='Poly Vis')
	pm.button(label='On', c=polyOn)
	pm.button(label='Off', c=polyOff)
	pm.text(label='Joints')
	pm.button(label='On', c=jointsOn)
	pm.button(label='Off', c=jointsOff)
	pm.text(label='X-Ray Joints')
	pm.button(label='On', c=xRayOn)
	pm.button(label='Off', c=xRayOff)
	pm.text(label='Wire Shaded')
	pm.button(label='On', c=wireOn)
	pm.button(label='Off', c=wireOff)
	pm.text(label='NURBS Curves')
	pm.button(label='On', c=curvesOn)
	pm.button(label='Off', c=curvesOff)
	pm.text(label='NURBS Surfaces')
	pm.button(label='On', c=surfacesOn)
	pm.button(label='Off', c=surfacesOff)

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_2, st='in')

	'''
	Tools
	'''
	pm.frameLayout(w=win_width, label='Tools', bgc=color_3, cl=1, cll=1, ann='Different Tools', cc=windowResize)
	pm.columnLayout()
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinJoint.png', label='Create Joint Tool', c=jointTool)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinMirrorJoint_S.png', label='Mirror Joint Tool-Behavior', c=mirrorToolB)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinMirrorJoint_S.png', label='Mirror Joint Tool-Orientation', c=mirrorToolO)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='menuIconDisplay.png', label='Joint Size', c=jointSize)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinInsert.png', label='Insert Joint', c=insertJoint)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='menuIconDisplay.png', label='IK Handle Size', c=IkSize)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='BR_icons/BR_diagram.png', label='Select Hierarchy', c=hierarchy)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='BR_icons/BR_renamerIcon.svg', label='Renamer', c=renamerWindow)
	
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='circle.png', label='Curve Tool Window', c=curveWindow)
	pm.separator(w=win_width, bgc=color_3, st='in')
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(label='IK Handle Tool')
	pm.button(label='RP', c=RP_IkHandle)
	pm.button(label='SC', c=SC_IkHandle)
	pm.text(label='Padding')
	pm.button(label='Jnt' , c=jointPadding)
	pm.button(label='Ctrl', c=ctrlPadding)
	# pm.text('Renamer')
	# pm.button(label='Jnt', c=jointRenamer)
	# pm.button(label='Ctrl',c=ctrlRenamer, ann='For control chains')

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_3, st='in')
	
	'''
	Constraints
	'''
	pm.frameLayout(w=win_width, label='Constraints', bgc=color_4, cl=1, cll=1, ann='Constraints', cc=windowResize)
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(label='Parent MO')
	pm.button(label='On', c=parentConstraint_on)
	pm.button(label='Off', c=parentConstraint_off)
	pm.text(label='Point MO')
	pm.button(label='On', c=pointConstraint_on)
	pm.button(label='Off', c=pointConstraint_off)
	pm.text(label='Orient MO')
	pm.button(label='On', c=orientConstraint_on)
	pm.button(label='Off', c=orientConstraint_off)
	pm.button(w=win_width, label='Pole Vector', c=poleVector)
	
	
	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_4, st='in')


	'''
	Bipeds
	'''
	pm.frameLayout(w=win_width, label='Bipeds', bgc=color_5, cl=0, cll=1, ann='Biped Tools', cc=windowResize)
	biped_layout = pm.columnLayout(w=win_width)


	pm.frameLayout(w=win_width, label='Head/Eyes/Jaws', bgc=color_6, cl=0, cll=1, cc=windowResize)
	pm.text(label='Select the head bind joints', w=win_width)
	pm.button(label='Head Space locator and icon', w=win_width, c=headSetup)

	pm.setParent(biped_layout)
	pm.separator(w=win_width, bgc=color_6, st='in')



	pm.frameLayout(w=win_width, label='Neck (Based on 4 joints)', bgc=color_7, cl=1, cll=1, cc=windowResize)
	pm.text(label='Select the neck bind joints', w=win_width)
	pm.button(label='Ik/Fk System', w=win_width, c=neckSetup)

	pm.setParent(biped_layout)
	pm.separator(w=win_width, bgc=color_7, st='in')


	pm.frameLayout(w=win_width, label='Shoulders/Arms', bgc=color_8, cl=1, cll=1, cc=windowResize)
	pm.text(label='Select the clav and arm bind', w=win_width)
	pm.button(label='Create shoulder system', w=win_width, c=shoulderSetup)
	pm.text(label='Select the arm bind', w=win_width)
	pm.button(label='IK/FK System', w=win_width, c=bipedArm_system)

	
	pm.setParent(biped_layout)
	pm.separator(w=win_width, bgc=color_8, st='in')



	pm.frameLayout(w=win_width, label='Back (Based on 7 joints)', bgc=color_9, cl=1, cll=1, cc=windowResize)
	pm.text(label='Select the back bind joints')
	pm.button(label='Setup', w=win_width, c=backSetup)
	
	pm.setParent(biped_layout)
	pm.separator(w=win_width, bgc=color_9, st='in')



	pm.frameLayout(w=win_width, label='Root/Hips', bgc=color_10, cl=1, cll=1, cc=windowResize)
	pm.text(label='Select the main root joint', w=win_width)
	pm.button(label='Space Locator', w=win_width, c=rootLoc)
	
	pm.text(label='Select the main hip joint', w=win_width)
	pm.button(label='Space Locator', w=win_width, c=hipLoc)
	
	pm.setParent(biped_layout)
	pm.separator(w=win_width, bgc=color_10, st='in')



	pm.frameLayout(w=win_width, label='Legs', bgc=color_1, cl=1, cll=1, cc=windowResize)
	pm.button(label='Leg IK/FK Joints', w=win_width, ann='Creates Leg ik/fk joints', c=bipedLeg_joints)
	pm.text(label='Select the bind, ik, and fk joints', w=win_width)
	pm.button(label='IK/FK System', w=win_width, c=bipedLeg_system)	

	pm.setParent(biped_layout)
	pm.separator(w=win_width, bgc=color_1, st='in')



	pm.frameLayout(w=win_width, label='Feet', bgc=color_2, cl=1, cll=1, cc=windowResize)
	pm.text(label='RFL Prep - Move the locators', w=win_width)
	pm.button(label='Create Locators - Select the bind', w=win_width, c=rflPrep)
	pm.text(label='Select the foot icon and the heel locator', w=win_width)
	pm.button(label='RFL System', w=win_width, c=rflSystem)

	pm.setParent(biped_layout)
	pm.separator(w=win_width, bgc=color_2, st='in')

	pm.frameLayout(w=win_width, label='Connections', bgc=color_2, cl=1, cll=1, cc=windowResize)
	pm.text(label='Select the shoulderSpace_loc, ik_cons_grp, twist_cons_grp, arm_01_fk_local, and the IkFk_switch', w=win_width, ww=1, ann='The shoulderSpace_loc is under the clav_02_waste, the arm_01_fk_local is under the gimbal_core_icon, and the cons_grps are under the clav_DO____NOT____TOUCH_grp')
	pm.button(label='Arm to Shoulder', w=win_width, c=armConnection_1)


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_5, st='in')
	'''
	Quadrupeds
	'''
	quad_layout = pm.frameLayout(w=win_width, label='Quadrupeds', bgc=color_6, cl=1, cll=1, ann='Quadruped Tools', cc=windowResize )
	pm.setParent(quad_layout)
	pm.frameLayout(w=win_width, label='Hind Legs', bgc=(color_7), cl=1, cll=1, cc=windowResize)
	pm.text(label='orientation_h(Leg, LegIK, then LegFK)', w=win_width, al='center')
	pm.button(label='Hind IK/FK/Helper Joints',w=win_width, ann='Creates leg ik/fk/helper joint chains', c=quad_hLeg_joints)
	pm.text(label='Select the bind, ik, helper, and fk joints', w=win_width)
	pm.button(label='hLeg IK/FK System', w=win_width,  ann='Sets up the hind leg IK/FK systems', c=quad_hIKFK_system)
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(label='Leg SDKs')
	pm.button(label='lt', c=lt_hLeg_SDKs)
	pm.button(label='rt', c=rt_hLeg_SDKs)
	


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_6, st='in')

	'''
	Zero Out Attributes
	'''
	pm.frameLayout(w=win_width, label='Zero Out', bgc=color_7, cl=1, cll=1, ann='Zero Out the Attributes to defaults', cc=windowResize)
	pm.columnLayout()
	pm.button(label='Human Foot Attributes', w=win_width, c=setZeroHumanFoot, ann='Sets Custom Foot Attributes back to defaults')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.button(label='Human Hand Attributes', w=win_width, c=setZeroHumanHand, ann='Sets Custom Hand Attributes back to defaults')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.rowColumnLayout(nc=3, cw=[[1, 80], [2, 80],[3, 80]])
	pm.button(label='Translate', c=setZeroTr)
	pm.button(label='Rotate', c=setZeroRo)
	pm.button(label='Scale', c=setZeroSc)


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_7, st='in') 

	pm.window('ByrdRigs_interface_toolset', e=1, wh=(240, 110), rtf=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)

def deleteHistory(*args):
	pm.delete(ch=1)
	# print 'History Deleted'

def centerPivot(*args):
	pm.xform(cpc=1)
	# print 'Selected pivot centered.'

def freezeTransform(*agrs):
	pm.makeIdentity(apply=1, t=1, r=1, s=1, n=0, pn=1)
	# print 'Transform Frozen'

panel_1 = 'modelPanel1' 
panel_2 =  'modelPanel2' 
panel_3 = 'modelPanel3' 
panel_4 = 'modelPanel4'

show_1 = 'MainPane|viewPanes|modelPanel1|modelPanel1|menu14'
show_2 = 'MainPane|viewPanes|modelPanel2|modelPanel2|menu18'
show_3 = 'MainPane|viewPanes|modelPanel3|modelPanel3|menu22'
show_4 = 'MainPane|viewPanes|modelPanel4|modelPanel4|menu26'


def showAll(*args):
	print 'Show All'
	pm.modelEditor(panel_1, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_1, panel_1, "modelPanel1", "Playblast Display")

	pm.modelEditor(panel_2, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_2, panel_2, "modelPanel2", "Playblast Display")

	pm.modelEditor(panel_3, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_3, panel_3, "modelPanel3", "Playblast Display")

	pm.modelEditor(panel_4, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_4, panel_4, "modelPanel4", "Playblast Display")

def showNone(*args):
	print 'Show None'
	pm.modelEditor(panel_1, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_1, panel_1, "modelPanel1", "Playblast Display")

	pm.modelEditor(panel_2, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_2, panel_2, "modelPanel2", "Playblast Display")

	pm.modelEditor(panel_3, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_3, panel_3, "modelPanel3", "Playblast Display")

	pm.modelEditor(panel_4, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_4, panel_4, "modelPanel4", "Playblast Display")

def polyOn(*args):
	print 'Polygons visible'
	pm.modelEditor(panel_1, e=1, polymeshes=1)
	pm.modelEditor(panel_1, e=1, hos=1)
	pm.modelEditor(panel_2, e=1, polymeshes=1)
	pm.modelEditor(panel_2, e=1, hos=1)
	pm.modelEditor(panel_3, e=1, polymeshes=1)
	pm.modelEditor(panel_3, e=1, hos=1)
	pm.modelEditor(panel_4, e=1, polymeshes=1)
	pm.modelEditor(panel_4, e=1, hos=1)

def polyOff(*args):
	print 'Polygons hidden'
	pm.modelEditor(panel_1, e=1, polymeshes=0)
	pm.modelEditor(panel_1, e=1, hos=0)
	pm.modelEditor(panel_2, e=1, polymeshes=0)
	pm.modelEditor(panel_2, e=1, hos=0)
	pm.modelEditor(panel_3, e=1, polymeshes=0)
	pm.modelEditor(panel_3, e=1, hos=0)
	pm.modelEditor(panel_4, e=1, polymeshes=0)
	pm.modelEditor(panel_4, e=1, hos=0)

def jointsOn(*args):
	print 'Joints visible'
	pm.modelEditor(panel_1, e=1, joints = 1)
	pm.modelEditor(panel_1, e=1, hos = 1)
	pm.modelEditor(panel_2, e=1, joints = 1)
	pm.modelEditor(panel_2, e=1, hos = 1)
	pm.modelEditor(panel_3, e=1, joints = 1)
	pm.modelEditor(panel_3, e=1, hos = 1)
	pm.modelEditor(panel_4, e=1, joints = 1)
	pm.modelEditor(panel_4, e=1, hos = 1)

def jointsOff(*args):
	print 'Joints hidden'
	pm.modelEditor(panel_1, e=1, joints = 0)
	pm.modelEditor(panel_1, e=1, hos = 0)
	pm.modelEditor(panel_2, e=1, joints = 0)
	pm.modelEditor(panel_2, e=1, hos = 0)
	pm.modelEditor(panel_3, e=1, joints = 0)
	pm.modelEditor(panel_3, e=1, hos = 0)
	pm.modelEditor(panel_4, e=1, joints = 0)
	pm.modelEditor(panel_4, e=1, hos = 0)

def xRayOn(*args):
	print 'X-Ray Joints visible'
	pm.modelEditor(panel_1, e=1, jointXray = 1)
	pm.modelEditor(panel_1, e=1, hos = 1)
	pm.modelEditor(panel_2, e=1, jointXray = 1)
	pm.modelEditor(panel_2, e=1, hos = 1)
	pm.modelEditor(panel_3, e=1, jointXray = 1)
	pm.modelEditor(panel_3, e=1, hos = 1)
	pm.modelEditor(panel_4, e=1, jointXray = 1)
	pm.modelEditor(panel_4, e=1, hos = 1)

def xRayOff(*args):
	print 'X-Ray Joints hidden'
	pm.modelEditor(panel_1, e=1, jointXray = 0)
	pm.modelEditor(panel_1, e=1, hos = 0)
	pm.modelEditor(panel_2, e=1, jointXray = 0)
	pm.modelEditor(panel_2, e=1, hos = 0)
	pm.modelEditor(panel_3, e=1, jointXray = 0)
	pm.modelEditor(panel_3, e=1, hos = 0)
	pm.modelEditor(panel_4, e=1, jointXray = 0)
	pm.modelEditor(panel_4, e=1, hos = 0)

def wireOn(*args):
	print 'Wireframe on Shaded On'
	pm.mel.setWireframeOnShadedOption(1, panel_1)
	pm.mel.setWireframeOnShadedOption(1, panel_2)
	pm.mel.setWireframeOnShadedOption(1, panel_3)
	pm.mel.setWireframeOnShadedOption(1, panel_4)

def wireOff(*args):
	print 'Wireframe On Shaded Off'
	pm.mel.setWireframeOnShadedOption(0, panel_1)
	pm.mel.setWireframeOnShadedOption(0, panel_2)
	pm.mel.setWireframeOnShadedOption(0, panel_3)
	pm.mel.setWireframeOnShadedOption(0, panel_4)

def curvesOn(*args):
	print 'NURBS Curves visible'
	pm.modelEditor(panel_1, e=1, nurbsCurves=1)
	pm.modelEditor(panel_2, e=1, nurbsCurves=1)
	pm.modelEditor(panel_3, e=1, nurbsCurves=1)
	pm.modelEditor(panel_4, e=1, nurbsCurves=1)

def curvesOff(*args):
	print 'NURBS Curves hidden'
	pm.modelEditor(panel_1, e=1, nurbsCurves=0)
	pm.modelEditor(panel_2, e=1, nurbsCurves=0)
	pm.modelEditor(panel_3, e=1, nurbsCurves=0)
	pm.modelEditor(panel_4, e=1, nurbsCurves=0)

def surfacesOn(*args):
	print 'NURBS Surfaces visible'
	pm.modelEditor(panel_1, e=1, nurbsSurfaces=1)
	pm.modelEditor(panel_2, e=1, nurbsSurfaces=1)
	pm.modelEditor(panel_3, e=1, nurbsSurfaces=1)
	pm.modelEditor(panel_4, e=1, nurbsSurfaces=1)

def surfacesOff(*args):
	print 'NURBS Surfaces hidden'
	pm.modelEditor(panel_1, e=1, nurbsSurfaces=0)
	pm.modelEditor(panel_2, e=1, nurbsSurfaces=0)
	pm.modelEditor(panel_3, e=1, nurbsSurfaces=0)
	pm.modelEditor(panel_4, e=1, nurbsSurfaces=0)

def jointTool(*args):
	print 'Joint Tool Active.'
	pm.mel.JointTool()

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

def jointSize(*args):
	print 'Changing Joint Size.'
	pm.mel.jdsWin()

def insertJoint(*args):
	print 'Joint Tool Active.'
	pm.mel.InsertJointTool()

def hierarchy(*args):
	print 'Hierarchy Selected'
	pm.mel.SelectHierarchy()

def renamerWindow(*args):
	mel.eval("source Quick_rename_tool;")
	mel.eval("Quick_rename_tool;")

	# Not my script, I downloaded it from highend3d.com I changed the colors though.

def curveWindow(*args):
	import BR_curve_tool
	reload (BR_curve_tool)
	BR_curve_tool.windowCreation()

def RP_IkHandle(*args):
	print 'RP IK Handle Tool.'
	pm.ikHandle()

def SC_IkHandle(*args):
	print 'SC IK Handle Tool.'
	pm.ikHandle(sol='ikSCsolver')

def IkSize(*args):
	print 'Changing IK Handle Size'
	pm.mel.ikHdsWin()

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


def headSetup(*args):
	joints = pm.ls(sl=1, dag=1)
	head_bind = joints[0]
	head_waste = joints[1]


	head_pad = pm.group(empty=1)
	temp_comnstraint = pm.parentConstraint(head_bind, head_pad, mo=0)
	pm.delete(temp_comnstraint)
	freezeTransform(head_pad)

	local_name = head_bind.replace('01_bind', '00_pad')
	head_pad.rename(local_name)
	pm.parent(head_bind, head_pad)

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

	temp_constraint = pm.parentConstraint(head_bind, head_icon, mo=0)
	pm.delete(temp_constraint)
	temp_constraint = pm.pointConstraint(head_waste, head_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()
	bind_pivots = head_bind.getTranslation(ws=1)
	# print bind_pivots
	head_icon.setPivots(bind_pivots)

	icon_name = head_bind.replace('bind', 'icon')
	head_icon.rename(icon_name)

	pm.parentConstraint(head_icon, head_pad, mo=0)

	head_icon.overrideEnabled.set(1)
	head_icon.overrideColor.set(17)

def eyeSetup(*args):
	



def rootLoc(*args):
	selection = pm.ls(sl=1)
	root_joint = selection[0]

	loc_1 = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.parentConstraint(root_joint, loc_1, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_1)

	loc_name = root_joint.replace('_01_waste', '_space_loc')
	loc_1.rename(loc_name)
	pm.parent(loc_1, root_joint)

def hipLoc(*args):
	selection = pm.ls(sl=1)
	hip_joint = selection[0]

	loc_2 = pm.spaceLocator(p=(0, 0, 0))

	temp_constraint = pm.parentConstraint(hip_joint, loc_2, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_2)

	loc_name = hip_joint.replace('_01_bind', '_space_loc')
	loc_2.rename(loc_name)
	pm.parent(loc_2, hip_joint)

def backSetup(*args):
	import BR_7Joint_backSetup
	reload (BR_7Joint_backSetup)
	BR_7Joint_backSetup.back()

def neckSetup(*args):
	import BR_4Joint_neckSetup
	reload (BR_4Joint_neckSetup)
	BR_4Joint_neckSetup.setup()

def bipedArm_system(*args):
	import BR_armSetup
	reload (BR_armSetup)
	BR_armSetup.armSetup()

def shoulderSetup(*args):
	joint_system = pm.ls(sl=1)
	clav_system = joint_system[0]
	arm_system = joint_system[1] 

	bJoints = pm.ls(clav_system, sl=1, dag=1)
	bRoot_joint = bJoints[0]
	bJoint_2 = bJoints[1]
	print 'Clav root joint:', bRoot_joint
	print 'Clav waste joint:', bJoint_2

	armJoints = pm.ls(arm_system, sl=1, dag=1)
	aRoot_joint = armJoints[0]
	aJoint_2 = armJoints[1]
	aJoint_3 = armJoints[2]
	print 'Arm root joint:', aRoot_joint
	print 'Arm joint 2:', aJoint_2
	print 'Arm joint 3:', aJoint_3

	pm.select(bRoot_joint, bJoint_2)
	ikh = pm.ikHandle(sol='ikSCsolver')[0]

	ik_name = bRoot_joint.replace('bind', 'ikh')
	ikh.rename(ik_name)

	loc_1 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.pointConstraint(aRoot_joint, loc_1, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_1)

	loc_name = ikh.replace('ikh', 'loc')
	loc_1.rename(loc_name)
	pm.parent(ikh, loc_1)

	loc_2 =	pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(bRoot_joint, loc_2, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(loc_2)
	loc_name = loc_1.replace('loc', 'startLoc')
	loc_2.rename(loc_name)

	loc_3 =	pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(bJoint_2, loc_3, mo=0)
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
	temp_constraint = pm.parentConstraint(bRoot_joint, transform, mo=0)
	pm.delete(temp_constraint)

	pm.connectAttr(loc_2 + '.worldPosition', clav_dist + '.startPoint')
	pm.connectAttr(loc_3 + '.worldPosition', clav_dist + '.endPoint')

	pm.parent(loc_3, loc_1)

	driver = clav_dist + '.distance'
	length = pm.getAttr(bJoint_2 + '.tx')


	pm.setDrivenKeyframe(bJoint_2 + '.tx', currentDriver=driver, driverValue=length, value=length)

	pm.setDrivenKeyframe(bJoint_2 + '.tx', currentDriver=driver, driverValue=(2 * length), value=(2 * length))
	pm.keyTangent(bJoint_2, itt='clamped', ott='clamped')
	pm.setInfinity(bJoint_2, poi='linear')

	shoulder_icon = pm.curve(d=1, p=[(0, 1.003235, 0),(0.668823, 0, 0),(0.334412, 0, 0),(0.334412, -0.167206, 0),(0.334412, -0.501617, 0),(0.334412, -1.003235, 0),(-0.334412, -1.003235, 0),(-0.334412, -0.501617, 0),(-0.334412, -0.167206, 0),(-0.334412, 0, 0),(-0.668823, 0, 0),(0, 1.003235, 0),(0, 0, -0.668823),(0, 0, -0.334412),(0, -0.167206, -0.334412),(0, -0.501617, -0.334412),(0, -1.003235, -0.334412),(0, -1.003235, 0.334412),(0, -0.501617, 0.334412),(0, -0.167206, 0.334412),(0, 0, 0.334412),(0, 0, 0.668823),(0, 1.003235, 0)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
	shoulder_icon.rx.set(180)
	temp_constraint = pm.pointConstraint(bJoint_2, shoulder_icon, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(shoulder_icon)
	shoulder_icon.ty.set(3)
	freezeTransform(shoulder_icon)

	icon_name = bRoot_joint.replace('clav_01_bind', 'shoulder_icon')
	shoulder_icon.rename(icon_name)
	pm.parent(loc_1, shoulder_icon)

	dnt_grp = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(bRoot_joint, dnt_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(dnt_grp)

	grp_name = bRoot_joint.replace('01_bind', 'DO____NOT____TOUCH_grp')
	dnt_grp.rename(grp_name)

	pm.parent(transform, loc_2, dnt_grp)

	global_grp = pm.group(empty=1)
	temp_constraint = pm.pointConstraint(bRoot_joint, global_grp, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(global_grp)

	grp_name = bRoot_joint.replace('01_bind', 'global_grp')
	global_grp.rename(grp_name)

	pad = pm.group(empty=1)
	temp_constraint= pm.pointConstraint(bRoot_joint, pad, mo=0)
	pm.delete(temp_constraint)
	freezeTransform(pad)

	pad_name = bRoot_joint.replace('01_bind', '00_pad')
	pad.rename(pad_name)

	pm.parent(bRoot_joint, pad)

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
		grp_name = bRoot_joint.replace('lt_clav_01_bind', 'joint_grp')
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

	loc_4 = pm.spaceLocator(p=(0, 0, 0))
	temp_constraint = pm.parentConstraint(bJoint_2, loc_4)
	pm.delete(temp_constraint)
	freezeTransform(loc_4)

	loc_name = shoulder_icon.replace('_icon', '_space_loc')
	loc_4.rename(loc_name)

	pm.parent(loc_4, bJoint_2)
	freezeTransform(loc_4)

def armConnection_1(*args):
	selection = pm.ls(sl=1)

	space_loc = selection[0]
	ik_main_grp = selection[1]
	twist_main_grp = selection[2]
	fk_icons = selection[3]
	switch = selection[4]
	# print 'Space loc:', space_loc
	# print 'Ik cons grp:', ik_main_grp 
	# print 'Twist cons grp:', twist_main_grp
	# print 'Fk icon grp:', fk_icons
	# print "IkFk switch:", switch

	constraint_1 = pm.pointConstraint(space_loc, ik_main_grp, mo=1)
	const_target_1 = constraint_1.getWeightAliasList()[0]
	print const_target_1
	switch.IkFk.set(1)
	const_target_1.set(0)
	pm.setDrivenKeyframe(const_target_1, currentDriver=switch + '.IkFk')
	switch.IkFk.set(0)
	const_target_1.set(1)
	pm.setDrivenKeyframe(const_target_1, currentDriver=switch + '.IkFk')

	constraint_2 = pm.pointConstraint(space_loc, twist_main_grp, mo=1)
	const_target_2 = constraint_2.getWeightAliasList()[0]
	print const_target_2
	switch.IkFk.set(1)
	const_target_2.set(0)
	pm.setDrivenKeyframe(const_target_2, currentDriver=switch + '.IkFk')
	switch.IkFk.set(0)
	const_target_2.set(1)
	pm.setDrivenKeyframe(const_target_2, currentDriver=switch + '.IkFk')

	pm.pointConstraint(space_loc, fk_icons, mo=1)

def twistWindow(*args):
	import BR_Arm_twist_window
	reload (BR_Arm_twist_window)
	BR_Arm_twist_window.gui()

def bipedLeg_joints(*args):
	joint_system = pm.ls(selection=1, dag=1)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	joint_4 = joint_system[3]
	joint_5 = joint_system[4]
	# print 'Root Joint:', root_joint
	# print 'Joint 2:', joint_2
	# print 'Joint 3:', joint_3
	# print 'Joint 4:', joint_4
	# print 'Joint 5:', joint_5
	pm.duplicate(root_joint)
	ik_joints = pm.ls(selection=1, dag=1)
	ik_root_joint = ik_joints[0]
	ik_joint_2 = ik_joints[1]
	ik_joint_3 = ik_joints[2]
	ik_joint_4 = ik_joints[3]
	ik_joint_5 = ik_joints[4]
	# print 'Ik Root Joint:', ik_root_joint
	# print 'Ik Joint 2:', ik_joint_2
	# print 'Ik Joint 3:', ik_joint_3
	# print 'Ik Joint 4:', ik_joint_4
	# print 'Ik Joint 5:', ik_joint_5

	ik_joint_name = root_joint.replace('bind', 'ik')
	ik_root_joint.rename(ik_joint_name)

	ik_joint_name = joint_2.replace('bind', 'ik')
	ik_joint_2.rename(ik_joint_name)

	ik_joint_name = joint_3.replace('bind', 'ik')
	ik_joint_3.rename(ik_joint_name)

	ik_joint_name = joint_4.replace('bind', 'ik')
	ik_joint_4.rename(ik_joint_name)

	ik_joint_name = joint_5.replace('waste', 'ik')
	ik_joint_5.rename(ik_joint_name)

	pm.duplicate(ik_root_joint)
	fk_joints = pm.ls(selection=1, dag=1)
	fk_root_joint = fk_joints[0]
	fk_joint_2 = fk_joints[1]
	fk_joint_3 = fk_joints[2]
	fk_joint_4 = fk_joints[3]
	fk_joint_5 = fk_joints[4]
	# print 'Ik Root Joint:', fk_root_joint
	# print 'Ik Joint 2:', fk_joint_2
	# print 'Ik Joint 3:', fk_joint_3
	# print 'Ik Joint 4:', fk_joint_4
	# print 'Ik Joint 5:', fk_joint_5

	fk_joint_name = root_joint.replace('bind', 'fk')
	fk_root_joint.rename(fk_joint_name)

	fk_joint_name = joint_2.replace('bind', 'fk')
	fk_joint_2.rename(fk_joint_name)

	fk_joint_name = joint_3.replace('bind', 'fk')
	fk_joint_3.rename(fk_joint_name)

	fk_joint_name = joint_4.replace('bind', 'fk')
	fk_joint_4.rename(fk_joint_name)

	fk_joint_name = joint_5.replace('waste', 'fk')
	fk_joint_5.rename(fk_joint_name)

def bipedLeg_system(*args):
	joint_systems = pm.ls(selection=1)
	
	leg_root = joint_systems[0]
	ik_root = joint_systems[1]
	fk_root = joint_systems[2]

	leg_joints = pm.ls(leg_root, dag=1)
	ik_joints = pm.ls(ik_root, dag=1)
	fk_joints = pm.ls(fk_root, dag=1)

	print 'Leg System:', leg_joints
	print 'IK System:', ik_joints
	print 'FK Systems:', fk_joints

	leg_root_joint = pm.ls(leg_joints[0])
	leg_joint_2 = pm.ls(leg_joints[1])
	leg_joint_3 = pm.ls(leg_joints[2])
	leg_joint_4 = pm.ls(leg_joints[3])
	leg_joint_5 = pm.ls(leg_joints[4])
	# print 'Leg root joint:', leg_root_joint
	# print '2nd leg joint:', leg_joint_2 
	# print '3rd leg joint:', leg_joint_3
	# print '4th leg joint:', leg_joint_4
	# print '5th leg joint:', leg_joint_5
	ik_root_joint = pm.ls(ik_joints[0])
	ik_joint_2 = pm.ls(ik_joints[1])
	ik_joint_3 = pm.ls(ik_joints[2])
	ik_joint_4 = pm.ls(ik_joints[3])
	ik_joint_5 = pm.ls(ik_joints[4])
	# print 'Leg root joint:', ik_root_joint
	# print '2nd ik joint:', ik_joint_2 
	# print '3rd ik joint:', ik_joint_3
	# print '4th ik joint:', ik_joint_4
	# print '5th ik joint:', ik_joint_5
	fk_root_joint = pm.ls(fk_joints[0])
	fk_joint_2 = pm.ls(fk_joints[1])
	fk_joint_3 = pm.ls(fk_joints[2])
	fk_joint_4 = pm.ls(fk_joints[3])
	fk_joint_5 = pm.ls(fk_joints[4])
	# print 'Leg root joint:', fk_root_joint
	# print '2nd fk joint:', fk_joint_2 
	# print '3rd fk joint:', fk_joint_3
	# print '4th fk joint:', fk_joint_4
	# print '5th fk joint:', fk_joint_5

	orient_blend_1 = pm.orientConstraint(ik_root_joint, fk_root_joint, leg_root_joint)
	orient_blend_2 = pm.orientConstraint(ik_joint_2, fk_joint_2, leg_joint_2)
	orient_blend_3 = pm.orientConstraint(ik_joint_3, fk_joint_3, leg_joint_3)
	orient_blend_4 = pm.orientConstraint(ik_joint_4, fk_joint_4, leg_joint_4)

	'''
	Create the ik handles
	'''

	pm.select(ik_root_joint, ik_joint_3)
	ikh_1 = pm.ikHandle()[0]
	pm.select(ik_joint_3, ik_joint_4)
	ikh_2 = pm.ikHandle(sol='ikSCsolver')[0]
	pm.select(ik_joint_4, ik_joint_5)
	ikh_3 =pm.ikHandle(sol='ikSCsolver')[0]

	'''
	Remane the ikh 
	'''
	ikh_name_1 = ik_root.replace('01_ik', 'ikh')
	ikh_1.rename(ikh_name_1)
	ikh_name_2 = ikh_1.replace('leg', 'ball')
	ikh_2.rename(ikh_name_2)
	ikh_name_3 = ikh_2.replace('ball', 'toe')
	ikh_3.rename(ikh_name_3)

	'''
	Create the foot icon
	'''
	footCurve_1 = pm.curve(p=[(-1.67422e-06, 0, 2.182925), (-0.13416, 0, 2.16342), (-0.266779, 0, 2.095529), (-0.395472, 0, 1.99807), (-0.518993, 0, 1.858632), (-0.636496, 0, 1.679268), (-0.737632, 0, 1.452024), (-0.819474, 0, 1.166445), (-0.846144, 0, 0.821387), (-0.824602, 0, 0.556128), (-0.749206, 0, 0.167213), (-0.673656, 0, -0.127237), (-0.597808, 0, -0.419587), (-0.545054, 0, -0.746104), (-0.544891, 0, -1.097217), (-0.571904, 0, -1.448294), (-0.512279, 0, -1.753435), (-0.393271, 0, -1.92306), (-0.266839, 0, -2.035747), (-0.133965, 0, -2.097731), (0, 0, -2.120128), (0.133965, 0, -2.097731), (0.266839, 0, -2.035747), (0.393271, 0, -1.92306), (0.512279, 0, -1.753435), (0.571904, 0, -1.448294), (0.544891, 0, -1.097217), (0.545054, 0, -0.746104), (0.597807, 0, -0.419586), (0.673656, 0, -0.127237), (0.749207, 0, 0.167214), (0.824602, 0, 0.556128), (0.846144, 0, 0.82139), (0.819474, 0, 1.166447), (0.737631, 0, 1.452029), (0.636486, 0, 1.679267), (0.519008, 0, 1.858641), (0.395504, 0, 1.9981), (0.266596, 0, 2.09545), (0.134293, 0, 2.163449), (-1.67422e-06, 0, 2.182925)], k=[0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 38], d=3)
	footCurve_2 = pm.curve(p=[(-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (-0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217), (0.544891, 0, -1.097217)], k=[0, 0, 0, 1, 2, 3, 3, 3], d=3)

	foot_icon = pm.group(empty=1)

	pm.select(footCurve_1, footCurve_2, foot_icon)
	foot_shapes = pm.ls(sl=1, dag=1)
	curveShape_1 = foot_shapes[1]
	curveShape_2 = foot_shapes[3]
	foot_icon_grp = foot_shapes[4]
	pm.parent(curveShape_1, curveShape_2, foot_icon, s=1, r=1)
	pm.delete(footCurve_1, footCurve_2)
	pm.xform(foot_icon, scale= [3.5, 3.5, 3.5])
	pm.select(foot_icon)
	freezeTransform()

	'''
	Move the foot icon
	'''
	temp_constraint = pm.pointConstraint(ik_joint_3, foot_icon)
	pm.delete(temp_constraint)
	foot_icon.ty.set(0)
	foot_icon.tz.set(6)
	pm.select(foot_icon)
	freezeTransform()
	

	'''
	Rename the foot icon
	'''
	foot_icon_name = leg_root.replace('leg_01_bind', 'foot_icon')
	foot_icon.rename(foot_icon_name)

	'''
	Add foot attrs
	'''
	pm.select(foot_icon)
	bipedFootAttrs()

	'''
	Parent the ikhs under the foot icon
	'''
	pm.parent(ikh_1, ikh_2, ikh_3, foot_icon)

	'''
	Move the pivot of the foot icon
	'''
	pm.select(leg_joint_3, foot_icon)
	selection = pm.ls(sl=1)
	driver_pivot = selection[0]
	driven_pivot = selection[1]
	driver_translation = driver_pivot.getTranslation(ws=1)
	driven_pivot.setPivots(driver_translation, ws=1)

	'''
	Create the knee icon.
	'''

	knee_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
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
	
	pm.select(knee_icon)
	centerPivot(knee_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the knee icon.
	'''
	temp_constraint = pm.pointConstraint(leg_joint_2, knee_icon)
	pm.delete(temp_constraint)
	freezeTransform(knee_icon)
	pm.xform(knee_icon, t=[0,0,15], scale=[.5, .5, .5], ro=[-90, 0, 0])
	freezeTransform()

	'''
	Pole vector constraint.
	'''
	pm.poleVectorConstraint(knee_icon, ikh_1)

	'''
	Rename the knee icon
	'''
	knee_name = leg_root.replace('leg_01_bind', 'knee_icon')
	knee_icon.rename(knee_name)

	'''
	FK Setup
	'''

	'''
	Create fk icons
	'''
	fk_icon_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=2, tol=.01, nr=(1, 0, 0))[0]
	print 'Fk icon 1:', fk_icon_1
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_icon_1)
	pm.delete(temp_constraint)
	fk_pad_1 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_pad_1)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_1, fk_pad_1)
	pm.select(fk_icon_1)
	freezeTransform()


	fk_icon_2 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	print 'Fk icon 2:', fk_icon_2
	temp_constraint = pm.parentConstraint(fk_joint_2, fk_icon_2)
	pm.delete(temp_constraint)
	fk_pad_2 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(fk_joint_2, fk_pad_2)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_2, fk_pad_2)
	pm.select(fk_icon_2)
	freezeTransform()
	pm.parent(fk_pad_2, fk_icon_1)

	fk_icon_3 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	print 'Fk icon 3:', fk_icon_3
	temp_constraint = pm.parentConstraint(fk_joint_3, fk_icon_3)
	pm.delete(temp_constraint)
	fk_pad_3 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(fk_joint_3, fk_pad_3)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_3, fk_pad_3)
	pm.select(fk_icon_3)
	freezeTransform()
	pm.parent(fk_pad_3, fk_icon_2)
	
	fk_icon_4 = pm.circle(c=(0, 0, 0), ch=2, d=3, ut=0, sw=360, s=8, r=2, tol=.02, nr=(2, 0, 0))[0]
	print 'Fk icon 4:', fk_icon_4
	temp_constraint = pm.parentConstraint(fk_joint_4, fk_icon_4)
	pm.delete(temp_constraint)
	fk_pad_4 = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(fk_joint_4, fk_pad_4)
	pm.delete(temp_constraint)
	pm.parent(fk_icon_4, fk_pad_4)
	pm.select(fk_icon_4)
	freezeTransform()
	pm.parent(fk_pad_4, fk_icon_3)

	'''
	Rename the icons and the pads
	'''
	fk_icon1_name = fk_root.replace('fk', 'fk_icon')
	fk_icon_1.rename(fk_icon1_name)

	fk_icon2_name = fk_icon_1.replace('01', '02')
	fk_icon_2.rename(fk_icon2_name)

	fk_icon3_name = fk_icon_2.replace('02', '03')
	fk_icon_3.rename(fk_icon3_name)
	
	fk_icon4_name = fk_icon_3.replace('03', '04')
	fk_icon_4.rename(fk_icon4_name)

	fk_pad1_name = fk_icon_1.replace('icon', 'local')
	fk_pad_1.rename(fk_pad1_name)

	fk_pad2_name = fk_icon_2.replace('icon', 'local')
	fk_pad_2.rename(fk_pad2_name)

	fk_pad3_name = fk_icon_3.replace('icon', 'local')
	fk_pad_3.rename(fk_pad3_name)

	fk_pad4_name = fk_icon_4.replace('icon', 'local')
	fk_pad_4.rename(fk_pad4_name)

	'''
	Orient constrain the icons to the joints
	'''
	pm.orientConstraint(fk_icon_1, fk_root_joint)
	pm.orientConstraint(fk_icon_2, fk_joint_2)
	pm.orientConstraint(fk_icon_3, fk_joint_3)
	pm.orientConstraint(fk_icon_4, fk_joint_4)

	'''
	Create the IKFK switch 
	'''

	ikfk_shape_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	ikfk_shape_2 = pm.curve(p=[(0, 0, -1), (0, 0, 1)], k=[0, 1], d=1)
	ikfk_shape_3 = pm.curve(p=[(-1, 0, 0), (1, 0, 0)], k=[0, 1], d=1)
	ikfk_shape_4 = pm.curve(p=[(0, 0, 1), (0, 0, 3)], k=[0, 1], d=1)

	shape_name_1 = leg_root.replace('leg_01_bind', 'ikfk_curve1') 
	# print 'Shape 1 Name:', shape_name_1
	ikfk_shape_1.rename(shape_name_1)
	
	shape_name_2 = leg_root.replace('leg_01_bind', 'ikfk_curve2') 
	# print 'Shape 2 Name:', shape_name_2
	ikfk_shape_2.rename(shape_name_2)

	shape_name_3 = leg_root.replace('leg_01_bind', 'ikfk_curve3') 
	# print 'Shape 3 Name:', shape_name_3
	ikfk_shape_3.rename(shape_name_3)
	
	shape_name_4 = leg_root.replace('leg_01_bind', 'ikfk_curve4') 
	# print 'Shape 4 Name:', shape_name_4
	ikfk_shape_4.rename(shape_name_4)

	leg_switch = pm.group(empty=1)
	pm.select(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4, leg_switch)
	shapes = pm.ls(selection=1, dag=1)
	curveShape_1 = shapes[1]
	curveShape_2 = shapes[3]
	curveShape_3 = shapes[5]
	curveShape_4 = shapes[7]
	leg_switch_grp = shapes[8]
	# print 'Curve Shape 1:', curveShape_1
	# print 'Curve Shape 2:', curveShape_2
	# print 'Curve Shape 3:', curveShape_3
	# print 'Curve Shape 4:', curveShape_4
	# print 'Switch:', leg_switch_grp
	pm.select(ikfk_shape_2, ikfk_shape_3)

	pm.cmds.scale(0.768, 0.768, 0.768)
	freezeTransform()

	pm.parent(curveShape_1, curveShape_2, curveShape_3, curveShape_4, leg_switch, s=1, r=1)
	pm.delete(ikfk_shape_1, ikfk_shape_2, ikfk_shape_3, ikfk_shape_4)
	pm.cmds.move(0, 0, 3, leg_switch + '.scalePivot', leg_switch + '.rotatePivot', rpr=1)

	pm.xform(leg_switch, ro=[0,0,90], scale=[1.5,1.5,1.5])
	freezeTransform(leg_switch)
	temp_constraint = pm.pointConstraint(leg_joint_3, leg_switch, mo=0, w=1)
	pm.delete(temp_constraint)
	freezeTransform()
	switch_name = leg_root.replace('01_bind', 'IkFk_switch')
	leg_switch.rename(switch_name)
	pm.pointConstraint(leg_joint_3, leg_switch, mo=0, w=1)
	deleteHistory()

	'''
	Add IkFk attribute
	'''
	pm.addAttr(leg_switch, ln="IkFk", max=1, dv=0, at='double', min=0)
	leg_switch.IkFk.set(e=1, keyable=1)

	leg_switch.tx.set(lock=1, channelBox=0, keyable=0)
	leg_switch.ty.set(lock=1, channelBox=0, keyable=0)
	leg_switch.tz.set(lock=1, channelBox=0, keyable=0)
	leg_switch.rx.set(lock=1, channelBox=0, keyable=0)
	leg_switch.ry.set(lock=1, channelBox=0, keyable=0)
	leg_switch.rz.set(lock=1, channelBox=0, keyable=0)
	leg_switch.sx.set(lock=1, channelBox=0, keyable=0)
	leg_switch.sy.set(lock=1, channelBox=0, keyable=0)
	leg_switch.sz.set(lock=1, channelBox=0, keyable=0)
 	leg_switch.v.set(lock=1, channelBox=0, keyable=0)
 	ik_root.v.set(0)
 	fk_root.v.set(0)

 	
	'''
 	Lt SDKs
 	'''
 	if pm.objExists('lt_leg_01_bind_orientConstraint1.lt_leg_01_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_1 + '.lt_leg_01_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_leg_01_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_leg_01_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_1 + '.lt_leg_01_fkW1', 1)
		pm.setAttr(orient_blend_1 + '.lt_leg_01_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_leg_01_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.lt_leg_01_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
		foot_icon.v.set(1)
		fk_pad_1.v.set(0)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		foot_icon.v.set(0)
		fk_pad_1.v.set(1)
		knee_icon.v.set(0)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0.01)
		foot_icon.v.set(1)
		fk_pad_1.v.set(1)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0.99)
		foot_icon.v.set(1)
		fk_pad_1.v.set(1)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
	else:
		print 'The left leg is not done'
	if pm.objExists('lt_leg_02_bind_orientConstraint1.lt_leg_02_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_2 + '.lt_leg_02_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_leg_02_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_leg_02_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_2 + '.lt_leg_02_fkW1', 1)
		pm.setAttr(orient_blend_2 + '.lt_leg_02_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_leg_02_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.lt_leg_02_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The left leg is not done'

	if pm.objExists('lt_leg_03_bind_orientConstraint1.lt_leg_03_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_3 + '.lt_leg_03_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_3 + '.lt_leg_03_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_3 + '.lt_leg_03_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_3 + '.lt_leg_03_fkW1', 1)
		pm.setAttr(orient_blend_3 + '.lt_leg_03_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_3 + '.lt_leg_03_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_3 + '.lt_leg_03_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The left leg is not done'

	if pm.objExists('lt_leg_04_bind_orientConstraint1.lt_leg_04_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_4 + '.lt_leg_04_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_4 + '.lt_leg_04_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_4 + '.lt_leg_04_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_4 + '.lt_leg_04_fkW1', 1)
		pm.setAttr(orient_blend_4 + '.lt_leg_04_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_4 + '.lt_leg_04_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_4 + '.lt_leg_04_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The left leg is not done'

	'''
 	Rt SDKs
 	'''
 	if pm.objExists('rt_leg_01_bind_orientConstraint1.rt_leg_01_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_1 + '.rt_leg_01_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_leg_01_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_leg_01_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_1 + '.rt_leg_01_fkW1', 1)
		pm.setAttr(orient_blend_1 + '.rt_leg_01_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_leg_01_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_1 + '.rt_leg_01_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
		foot_icon.v.set(1)
		fk_pad_1.v.set(0)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		foot_icon.v.set(0)
		fk_pad_1.v.set(1)
		knee_icon.v.set(0)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0.01)
		foot_icon.v.set(1)
		fk_pad_1.v.set(1)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0.99)
		foot_icon.v.set(1)
		fk_pad_1.v.set(1)
		knee_icon.v.set(1)
		pm.setDrivenKeyframe(foot_icon + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(fk_pad_1 + '.v', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(knee_icon + '.v', currentDriver= leg_switch + '.IkFk')
	else:
		print 'The right leg is not done'
	if pm.objExists('rt_leg_02_bind_orientConstraint1.rt_leg_02_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_2 + '.rt_leg_02_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_leg_02_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_leg_02_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_2 + '.rt_leg_02_fkW1', 1)
		pm.setAttr(orient_blend_2 + '.rt_leg_02_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_leg_02_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_2 + '.rt_leg_02_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The right leg is not done'

	if pm.objExists('rt_leg_03_bind_orientConstraint1.rt_leg_03_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_3 + '.rt_leg_03_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_3 + '.rt_leg_03_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_3 + '.rt_leg_03_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_3 + '.rt_leg_03_fkW1', 1)
		pm.setAttr(orient_blend_3 + '.rt_leg_03_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_3 + '.rt_leg_03_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_3 + '.rt_leg_03_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The right leg is not done'

	if pm.objExists('rt_leg_04_bind_orientConstraint1.rt_leg_04_fkW1'):
		leg_switch.IkFk.set(0)
		pm.setAttr(orient_blend_4 + '.rt_leg_04_fkW1', 0)
		pm.setDrivenKeyframe(orient_blend_4 + '.rt_leg_04_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_4 + '.rt_leg_04_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(1)
		pm.setAttr(orient_blend_4 + '.rt_leg_04_fkW1', 1)
		pm.setAttr(orient_blend_4 + '.rt_leg_04_ikW0', 0)
		pm.setDrivenKeyframe(orient_blend_4 + '.rt_leg_04_ikW0', currentDriver= leg_switch + '.IkFk')
		pm.setDrivenKeyframe(orient_blend_4 + '.rt_leg_04_fkW1', currentDriver= leg_switch + '.IkFk')
		leg_switch.IkFk.set(0)
	else:
		print 'The right leg is not done'

def rflPrep(*args):
	name_selection = pm.ls(sl=1, dag=1)
	root_joint = name_selection[0]
	joint_2 = name_selection[1]
	joint_3 = name_selection[2]
	joint_4 = name_selection[3]
	joint_5 = name_selection[4]
	'''
	Create the locators
	'''
	loc1 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 1:', loc1

	loc2 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 2:', loc2
	pm.xform(loc2, t=[-3, 0, 10])

	loc3 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 3:', loc3
	pm.xform(loc3, t=[3, 0, 10])
	
	loc4 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 4:', loc4
	pm.xform(loc4, t=[0, 0, 14])

	loc5 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 5:', loc5 
	pm.xform(loc5, t=[0, 0, 10])

	loc6 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 6:', loc6 
	pm.xform(loc6, t=[0, 7, 2])

	locs = pm.select(loc1, loc2, loc3, loc4, loc5, loc6)
	freezeTransform(locs)

	pm.parent(loc2, loc1)
	pm.parent(loc3, loc2)
	pm.parent(loc4, loc3)
	pm.parent(loc5, loc4)
	pm.parent(loc6, loc5)

	'''
	Rename the locs
	'''
	loc_name = root_joint.replace('leg_01_bind', 'heel_loc')
	loc1.rename(loc_name)
	loc_name = loc1.replace('heel', 'innerBank')
	loc2.rename(loc_name)
	loc_name = loc2.replace('inner', 'outer')
	loc3.rename(loc_name)
	loc_name = loc1.replace('heel', 'toe')
	loc4.rename(loc_name)
	loc_name = loc4.replace('toe', 'ball')
	loc5.rename(loc_name)
	loc_name = loc5.replace('ball', 'ankle')
	loc6.rename(loc_name)

def rflSystem(*args):
	rflSelection = pm.ls(sl=1)
	selection_1 = rflSelection[0]
	selection_2 = rflSelection[1]
	# print 'rfl selection', rflSelection
	# print 'selection 1', selection_1
	# print 'selection 2', selection_2

	foot_icon = pm.ls(selection_1, dag=1)
	locs = pm.ls(selection_2, dag=1)

	ikh_1 = foot_icon[3]
	ikh_2 = foot_icon[5]
	ikh_3 = foot_icon[6]
	# print 'ikh 1', ikh_1
	# print 'ikh 2', ikh_2
	# print 'ikh 3', ikh_3

	loc1 = locs[0]
	loc2 = locs[2]
	loc3 = locs[4]
	loc4 = locs[6]
	loc5 = locs[8]
	loc6 = locs[10]
	# print 'loc 1', loc1
	# print 'loc 2', loc2
	# print 'loc 3', loc3
	# print 'loc 4', loc4
	# print 'loc 5', loc5
	# print 'loc 6', loc6
	pm.select(loc1)
	freezeTransform()
	
	'''
	Create and rename the heel rot clamp
	'''
	heel_rot_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = loc1.replace('loc', 'rot_clamp')
	heel_rot_clamp.rename(clamp_name)
	print 'Heel rot clamp:', heel_rot_clamp

	ball_rot_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = heel_rot_clamp.replace('heel', 'ball')
	ball_rot_clamp.rename(clamp_name)
	print 'Ball rot clamp:', ball_rot_clamp

	footBtoS_clamp = pm.shadingNode('clamp', asUtility=1)
	clamp_name = heel_rot_clamp.replace('heel_rot', 'footBtoS')
	footBtoS_clamp.rename(clamp_name)
	print 'Foot BtoS clamp:', footBtoS_clamp

	footBtoS_percent = pm.shadingNode('setRange', asUtility=1)
	clamp_name = footBtoS_clamp.replace('clamp', 'percent')
	footBtoS_percent.rename(clamp_name)
	print 'Foot BtoS perect:', footBtoS_percent

	foot_roll_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = selection_1.replace('icon', 'roll_mult')
	foot_roll_mult.rename(clamp_name)
	print 'Foot roll mult:', foot_roll_mult

	toeTap_invert_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = selection_1.replace('foot_icon', 'toeTap_invert_mult')
	toeTap_invert_mult.rename(clamp_name)

	rflSetupPartA()

	ball_0toB_percent = pm.shadingNode('setRange', asUtility=1)
	clamp_name = footBtoS_percent.replace('footBtoS', 'ball_0toB')
	ball_0toB_percent.rename(clamp_name)
	print 'Ball ball 0toB percent:', ball_0toB_percent

	foot_invert_percent = pm.shadingNode('plusMinusAverage', asUtility=1)
	clamp_name = selection_1.replace('icon', 'invert_percent')
	foot_invert_percent.rename(clamp_name)
	print 'Foot invert percent:', foot_invert_percent

	ball_percent_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = foot_roll_mult.replace('foot_roll', 'ball_percent' )
	ball_percent_mult.rename(clamp_name)
	print 'ball percent mult:', ball_percent_mult

	clamp_name = heel_rot_clamp.replace('heel_rot', 'ball_0toB')
	ball_rot_clamp.rename(clamp_name)
	print 'Ball rot clamp:', ball_rot_clamp

	ball_roll_mult = pm.shadingNode('multiplyDivide', asUtility=1)
	clamp_name = ball_percent_mult.replace('percent', 'roll')
	ball_roll_mult.rename(clamp_name)
	print 'ball roll mult:', ball_roll_mult

	rflSetupPartB()

	pm.parent(ikh_2, loc5)
	pm.parent(ikh_1, loc6)

	'''
	Lean
	'''
	pm.connectAttr('lt_foot_icon.lean', loc5 + '.rz', f=1)

	'''
	Toe Spin
	'''
	pm.connectAttr('lt_foot_icon.toeSpin', loc4 + '.ry', f=1)

def bipedFootAttrs(*args):
	if pm.objExists('lt_foot_icon'):
		pm.addAttr('|lt_foot_icon', ln="roll", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.roll', e=1, keyable=1)
		pm.addAttr('|lt_foot_icon', ln="bendLimitAngle", dv=45, at='double')
		pm.setAttr('|lt_foot_icon.bendLimitAngle', e=1, keyable=1)
		pm.addAttr('|lt_foot_icon', ln="toeStraightAngle", dv=75, at='double')
		pm.setAttr('|lt_foot_icon.toeStraightAngle', e=1, keyable=1)
		pm.addAttr('|lt_foot_icon', ln="tilt", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.tilt', e=1, keyable=1)
		pm.addAttr('|lt_foot_icon', ln="lean", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.lean', e=1, keyable=1)
		pm.addAttr('|lt_foot_icon', ln="toeSpin", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.toeSpin', e=1, keyable=1)
		pm.addAttr('|lt_foot_icon', ln="toeTap", dv=0, at='double')
		pm.setAttr('|lt_foot_icon.toeTap', e=1, keyable=1)

	else:
		print "Lt foot icon donesn't exists"

	if pm.objExists('rt_foot_icon'):
		pm.addAttr('|rt_foot_icon', ln="roll", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.roll', e=1, keyable=1)
		pm.addAttr('|rt_foot_icon', ln="bendLimitAngle", dv=45, at='double')
		pm.setAttr('|rt_foot_icon.bendLimitAngle', e=1, keyable=1)
		pm.addAttr('|rt_foot_icon', ln="toeStraightAngle", dv=75, at='double')
		pm.setAttr('|rt_foot_icon.toeStraightAngle', e=1, keyable=1)
		pm.addAttr('|rt_foot_icon', ln="tirt", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.tirt', e=1, keyable=1)
		pm.addAttr('|rt_foot_icon', ln="lean", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.lean', e=1, keyable=1)
		pm.addAttr('|rt_foot_icon', ln="toeSpin", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.toeSpin', e=1, keyable=1)
		pm.addAttr('|rt_foot_icon', ln="toeTap", dv=0, at='double')
		pm.setAttr('|rt_foot_icon.toeTap', e=1, keyable=1)

	else:
		print "Rt foot icon donesn't exists"

def rflSetupPartA(*args):
	if pm.objExists('lt_heel_rot_clamp'):
		pm.connectAttr('lt_foot_icon.roll', 'lt_heel_rot_clamp.inputR', f=1)
		pm.setAttr("lt_heel_rot_clamp.minR", -90)
		pm.connectAttr('lt_heel_rot_clamp.outputR', 'lt_heel_loc.rotateX', f=1)
		pm.connectAttr('lt_foot_icon.roll', 'lt_ball_rot_clamp.inputR', f=1)
		pm.setAttr("lt_ball_rot_clamp.maxR", 90)
		pm.connectAttr('lt_ball_rot_clamp.outputR', 'lt_ball_loc.rotateX', f=1)

		pm.connectAttr('lt_foot_icon.toeStraightAngle', 'lt_footBtoS_clamp.maxR', f=1)
		pm.connectAttr('lt_foot_icon.bendLimitAngle', 'lt_footBtoS_clamp.minR', f=1)
		pm.connectAttr('lt_foot_icon.roll', 'lt_footBtoS_clamp.inputR', f=1)

		pm.connectAttr('lt_footBtoS_clamp.maxR', 'lt_footBtoS_percent.oldMaxX', f=1)
		pm.connectAttr('lt_footBtoS_clamp.minR', 'lt_footBtoS_percent.oldMinX', f=1)
		pm.setAttr("lt_footBtoS_percent.maxX", 1)
		pm.connectAttr('lt_footBtoS_clamp.inputR', 'lt_footBtoS_percent.valueX', f=1)

		pm.connectAttr('lt_footBtoS_percent.outValueX', 'lt_foot_roll_mult.input1X', f=1)
		pm.connectAttr('lt_footBtoS_clamp.inputR', 'lt_foot_roll_mult.input2X', f=1)
		pm.connectAttr('lt_foot_roll_mult.outputX', 'lt_toe_loc.rotateX', f=1)

		pm.mel.CBdeleteConnection("lt_ball_loc.rx")

		pm.connectAttr('lt_foot_icon.bendLimitAngle', 'lt_ball_rot_clamp.maxR', f=1)

		pm.setDrivenKeyframe('lt_innerBank_loc.rotateZ', currentDriver='lt_foot_icon.tilt')
		pm.setDrivenKeyframe('lt_outerBank_loc.rotateZ', currentDriver='lt_foot_icon.tilt')
		pm.setAttr("lt_foot_icon.tilt", -90)
		pm.setAttr("lt_innerBank_loc.rotateZ", 90)
		pm.setDrivenKeyframe('lt_innerBank_loc.rotateZ', currentDriver='lt_foot_icon.tilt')
		pm.setAttr("lt_foot_icon.tilt", 90)
		pm.setAttr("lt_outerBank_loc.rotateZ", -90)
		pm.setDrivenKeyframe('lt_outerBank_loc.rotateZ', currentDriver='lt_foot_icon.tilt')
		pm.setAttr("lt_foot_icon.tilt", 0)

		'''
		Toe Tap Setup
		'''
		toeTap_pad = pm.group(empty=1, n='lt_toeTap_pivot')
		temp_constraint = pm.parentConstraint('lt_leg_04_bind', toeTap_pad)
		pm.delete(temp_constraint)
		pm.makeIdentity(toeTap_pad, apply=1, t=1, r=1, s=1, n=0, pn=1)
		pm.parent('lt_toe_ikh', toeTap_pad)
		pm.parent(toeTap_pad, 'lt_toe_loc')
		pm.setAttr('lt_toeTap_invert_mult.input2X', -1)
		pm.connectAttr('lt_foot_icon.toeTap', 'lt_toeTap_invert_mult.input1X', f=1)
		pm.connectAttr('lt_toeTap_invert_mult.input1X', 'lt_toeTap_pivot.rotateX', f=1)

			
	else:
		print 'RFL not set up'

def rflSetupPartB(*agrs):
	if  pm.objExists('lt_ball_0toB_percent'):
		pm.connectAttr('lt_ball_0toB_clamp.maxR', 'lt_ball_0toB_percent.oldMaxX', f=1)
		pm.connectAttr('lt_ball_0toB_clamp.minR', 'lt_ball_0toB_percent.oldMinX', f=1)
		pm.setAttr("lt_ball_0toB_percent.maxX", 1)
		pm.connectAttr('lt_ball_0toB_clamp.inputR', 'lt_ball_0toB_percent.valueX', f=1)

		pm.setAttr('lt_foot_invert_percent.input1D[0]', 1)
		pm.setAttr('lt_foot_invert_percent.input1D[1]', 1)
		pm.connectAttr('lt_footBtoS_percent.outValueX', 'lt_foot_invert_percent.input1D[1]', f=1)
		pm.setAttr("lt_foot_invert_percent.operation", 2)

		pm.connectAttr('lt_ball_0toB_percent.outValueX', 'lt_ball_percent_mult.input1X', f=1)
		pm.connectAttr('lt_foot_invert_percent.output1D', 'lt_ball_percent_mult.input2X', f=1)

		pm.connectAttr('lt_ball_percent_mult.outputX', 'lt_ball_roll_mult.input1X', f=1)
		pm.connectAttr('lt_foot_icon.roll', 'lt_ball_roll_mult.input2X', f=1)
		pm.connectAttr('lt_ball_roll_mult.outputX', 'lt_ball_loc.rotateX', f=1)
	else:
		print 'RFL not set up'

def quadHind_fkLeg_icons():
	'''
	Input
	What are we working on?
	The root joint of the hind fk leg
	'''

	joint_systems = pm.ls(selection=1)

	leg_root = joint_systems[0]
	ik_root = joint_systems[1]
	helper_root = joint_systems[2]
	fk_root = joint_systems[3]

	leg_joints = pm.ls(leg_root, dag=1)
	ik_joints = pm.ls(ik_root, dag=1)
	helper_joints = pm.ls(helper_root, dag=1)
	fk_joints = pm.ls(fk_root, dag=1)

	print 'Leg System:', leg_joints
	print 'IK System:', ik_joints
	print 'Helper System:', helper_joints
	print 'FK Systems:', fk_joints

	leg_root_joint = pm.ls(leg_joints[0])
	leg_joint_2 = pm.ls(leg_joints[1])
	leg_joint_3 = pm.ls(leg_joints[2])
	leg_joint_4 = pm.ls(leg_joints[3])
	leg_joint_5 = pm.ls(leg_joints[4])
	leg_joint_6 = pm.ls(leg_joints[5])
	# print 'Leg root joint:', leg_root_joint
	# print '2nd leg joint:', leg_joint_2 
	# print '3rd leg joint:', leg_joint_3
	# print '4th leg joint:', leg_joint_4
	# print '5th leg joint:', leg_joint_5
	# print '6th leg joint:', leg_joint_6

	ik_root_joint = pm.ls(ik_joints[0])
	ik_joint_2 = pm.ls(ik_joints[1])
	ik_joint_3 = pm.ls(ik_joints[2])
	ik_joint_4 = pm.ls(ik_joints[3])
	ik_joint_5 = pm.ls(ik_joints[4])
	ik_joint_6 = pm.ls(ik_joints[5])
	# print 'Leg root joint:', ik_root_joint
	# print '2nd ik joint:', ik_joint_2 
	# print '3rd ik joint:', ik_joint_3
	# print '4th ik joint:', ik_joint_4
	# print '5th ik joint:', ik_joint_5
	# print '6th ik joint:', ik_joint_6

	helper_root_joint = pm.ls(helper_joints[0])
	helper_joint_2 = pm.ls(helper_joints[1])
	helper_joint_3 = pm.ls(helper_joints[2])
	helper_joint_4 = pm.ls(helper_joints[3])
	# print 'Leg root joint:', helper_root_joint
	# print '2nd helper joint:', helper_joint_2 
	# print '3rd helper joint:', helper_joint_3
	# print '4th helper joint:', helper_joint_4


	fk_root_joint = pm.ls(fk_joints[0])
	fk_joint_2 = pm.ls(fk_joints[1])
	fk_joint_3 = pm.ls(fk_joints[2])
	fk_joint_4 = pm.ls(fk_joints[3])
	fk_joint_5 = pm.ls(fk_joints[4])
	fk_joint_6 = pm.ls(fk_joints[5])
	# print 'Leg root joint:', fk_root_joint
	# print '2nd fk joint:', fk_joint_2 
	# print '3rd fk joint:', fk_joint_3
	# print '4th fk joint:', fk_joint_4
	# print '5th fk joint:', fk_joint_5
	# print '6th fk joint:', fk_joint_6

	'''
	Local Controls 
	'''

	'''
	Control 1 - root_joint
	'''
	# Create a control


	# Custom Orb Icon
	orbCurve_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	orbCurve_2 = pm.duplicate(rr=1)[0]
	orbCurve_2.rx.set(45)
	orbCurve_3 = pm.duplicate(rr=1)[0]
	orbCurve_3.rx.set(90)
	orbCurve_4 = pm.duplicate(rr=1)[0]
	orbCurve_4.ry.set(45)
	orbCurve_5 = pm.duplicate(rr=1)[0]
	orbCurve_5.ry.set(-45)
	pm.makeIdentity(orbCurve_1, orbCurve_2, orbCurve_3, orbCurve_4, orbCurve_5, n=0,s=1,r=1,t=1, apply=1,pn=1)
	orbIcon = pm.group(empty=1)
	temp_grp = pm.group(orbCurve_1, orbCurve_2, orbCurve_3, orbCurve_4, orbCurve_5)

	orbShapes = pm.ls(sl=1, dag=1)
	shape_1 = orbShapes[2]
	shape_2 = orbShapes[4]
	shape_3 = orbShapes[6]
	shape_4 = orbShapes[8]
	shape_5 = orbShapes[10]
	#print 'Shape 1:', shape_1

	pm.parent(shape_1, shape_2, shape_3, shape_4, shape_5, orbIcon, s=1, r=1)
	pm.delete(temp_grp)

	icon_name = leg_root.replace('bind', 'fk_icon')
	orbIcon.rename(icon_name)


	#  Create a group
	# Grouping control during the process.
	local_pad_1 = pm.group()

	# Output control and pad
	print 'Orb Created', orbIcon
	print 'Local Pad 1 Created', local_pad_1
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_root_joint, local_pad_1)
	pm.delete(temp_constraint)

	# Orient constrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(orbIcon, leg_root_joint)




	print 'Orb 1 Renamed', orbIcon

	# Renaming Pad
	pad_1 = local_pad_1
	pad_1_name = fk_root.replace('01_fk', '01_fk_local')
	pad_1.rename(pad_1_name)

	print 'Local Pad 1 Renamed', local_pad_1

	pm.parent(orbIcon, local_pad_1)

	'''
	Control 2
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad
	print 'Control 2 Created', control_icon_2
	print 'Local Pad 2 Created', local_pad_2
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(control_icon_2, fk_joint_2)

	# Renaming Icon
	# control_icon_2
	icon_2 = control_icon_2
	icon_2_name = fk_root.replace('01_fk', '02_fk_icon')
	icon_2.rename(icon_2_name)

	print 'Icon 2 Renamed', control_icon_2

	# Renaming Pad
	pad_2 = local_pad_2
	pad_2_name = fk_root.replace('01_fk', '02_fk_local')
	pad_2.rename(pad_2_name)

	print 'Local Pad 2 Renamed', local_pad_2

	''' 
	Parent controls together
	'''
	# Pad 2 -> control 1
	pm.parent(local_pad_2, orbIcon)

	'''
	Control 3
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad
	print 'Control 3 Created', control_icon_3
	print 'Local Pad 3 Created', local_pad_3
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_3, local_pad_3)
	pm.delete(temp_constraint)




	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(control_icon_3, fk_joint_3)

	# Renaming Icon
	# control_icon_3
	icon_3 = control_icon_3
	icon_3_name = fk_root.replace('01_fk', '03_fk_icon')
	icon_3.rename(icon_3_name)

	print 'Icon 3 Renamed', control_icon_3

	# Renaming Pad
	pad_3 = local_pad_3
	pad_3_name = fk_root.replace('01_fk', '03_fk_local')
	pad_3.rename(pad_3_name)

	print 'Local Pad 3 Renamed', local_pad_3


	''' 
	Parent controls together
	'''
	# Pad 3 -> control 1
	pm.parent(local_pad_3, control_icon_2)

def quad_hLeg_joints(*args):
	joint_system = pm.ls(selection=1, dag=1)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	joint_4 = joint_system[3]
	joint_5 = joint_system[4]
	joint_6 = joint_system[5]
	

	pm.duplicate(rr=1)
	ik_hJointRenamer()
	pm.duplicate(rr=1)
	fk_hJointRenamer()
	pm.duplicate(rr=1)
	helper_hJointRenamer()

def helper_hJointRenamer():
	'''
	Get Selected
	'''
	joint_chain = pm.ls(selection=1, dag=1)

	'''
	Figure out naming convention
	'''

	ori = raw_input()
	system_name = raw_input()
	count = 0
	suffix = 'helper'

	'''
	Loop through the joint chain.
	'''
	for current_joint in joint_chain:
		count = count + 1
		new_name = '{0},{1},0{2};{3}'.format(ori, system_name, count, suffix)
		#  Rename joints
		current_joint.rename(new_name)
	new_name = '{0},{1},0{2};{3}'.format(ori,system_name,count, 'helper')

	joint_system = pm.ls(selection=1, dag=1)

	root_joint = joint_system[0]
	joint_2 = joint_system[1]
	joint_3 = joint_system[2]
	joint_4 = joint_system[3]
	joint_5 = joint_system[4]
	joint_6 = joint_system[5]
	pm.delete(joint_5)

def quad_hIKFK_system(*args):
	joint_systems = pm.ls(selection=1)
	
	leg_root = joint_systems[0]
	ik_root = joint_systems[1]
	helper_root = joint_systems[2]
	fk_root = joint_systems[3]

	leg_joints = pm.ls(leg_root, dag=1)
	ik_joints = pm.ls(ik_root, dag=1)
	helper_joints = pm.ls(helper_root, dag=1)
	fk_joints = pm.ls(fk_root, dag=1)

	print 'Leg System:', leg_joints
	print 'IK System:', ik_joints
	print 'Helper System:', helper_joints
	print 'FK Systems:', fk_joints

	leg_root_joint = pm.ls(leg_joints[0])
	leg_joint_2 = pm.ls(leg_joints[1])
	leg_joint_3 = pm.ls(leg_joints[2])
	leg_joint_4 = pm.ls(leg_joints[3])
	leg_joint_5 = pm.ls(leg_joints[4])
	leg_joint_6 = pm.ls(leg_joints[5])
	# print 'Leg root joint:', leg_root_joint
	# print '2nd leg joint:', leg_joint_2 
	# print '3rd leg joint:', leg_joint_3
	# print '4th leg joint:', leg_joint_4
	# print '5th leg joint:', leg_joint_5
	# print '6th leg joint:', leg_joint_6

	ik_root_joint = pm.ls(ik_joints[0])
	ik_joint_2 = pm.ls(ik_joints[1])
	ik_joint_3 = pm.ls(ik_joints[2])
	ik_joint_4 = pm.ls(ik_joints[3])
	ik_joint_5 = pm.ls(ik_joints[4])
	ik_joint_6 = pm.ls(ik_joints[5])
	# print 'Leg root joint:', ik_root_joint
	# print '2nd ik joint:', ik_joint_2 
	# print '3rd ik joint:', ik_joint_3
	# print '4th ik joint:', ik_joint_4
	# print '5th ik joint:', ik_joint_5
	# print '6th ik joint:', ik_joint_6

	helper_root_joint = pm.ls(helper_joints[0])
	helper_joint_2 = pm.ls(helper_joints[1])
	helper_joint_3 = pm.ls(helper_joints[2])
	helper_joint_4 = pm.ls(helper_joints[3])
	# print 'Leg root joint:', helper_root_joint
	# print '2nd helper joint:', helper_joint_2 
	# print '3rd helper joint:', helper_joint_3
	# print '4th helper joint:', helper_joint_4


	fk_root_joint = pm.ls(fk_joints[0])
	fk_joint_2 = pm.ls(fk_joints[1])
	fk_joint_3 = pm.ls(fk_joints[2])
	fk_joint_4 = pm.ls(fk_joints[3])
	fk_joint_5 = pm.ls(fk_joints[4])
	fk_joint_6 = pm.ls(fk_joints[5])
	# print 'Leg root joint:', fk_root_joint
	# print '2nd fk joint:', fk_joint_2 
	# print '3rd fk joint:', fk_joint_3
	# print '4th fk joint:', fk_joint_4
	# print '5th fk joint:', fk_joint_5
	# print '6th fk joint:', fk_joint_6

	'''
	Orient constraint the IK/FK system with the bind.
	'''
	pm.orientConstraint(ik_root_joint, fk_root_joint, leg_root_joint, mo=0, w=1)
	pm.orientConstraint(ik_joint_2, fk_joint_2, leg_joint_2, mo=0, w=1)
	pm.orientConstraint(ik_joint_3, fk_joint_3, leg_joint_3, mo=0, w=1)
	pm.orientConstraint(ik_joint_4, fk_joint_4, leg_joint_4, mo=0, w=1)
	pm.orientConstraint(ik_joint_5, fk_joint_5, leg_joint_5, mo=0, w=1)

	'''
	Create the ikHandles
	'''
	pm.select(ik_root_joint, ik_joint_3)
	ikh_1 = pm.ikHandle(n='leg_ikh')[0]
	pm.select(ik_joint_3, ik_joint_4)
	ikh_2 = pm.ikHandle(sol='ikSCsolver', n='ankle_ikh')[0]
	pm.select(ik_joint_4, ik_joint_5)
	ikh_3 = pm.ikHandle(sol='ikSCsolver', n='ball_ikh')[0]
	pm.select(ik_joint_5, ik_joint_6)
	ikh_4 = pm.ikHandle(sol='ikSCsolver', n='toe_ikh')[0]
	pm.select(helper_root, helper_joint_4)
	ikh_5 = pm.ikHandle(n='helper_ikh')[0]

	'''
	Create the foot icon
	'''
	foot_icon = pm.curve(p=[(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
	pm.xform(scale=[2,0,4])
	temp_constraint = pm.pointConstraint(leg_joint_4, 'curve1')
	pm.delete(temp_constraint)
	freezeTransform()
	deleteHistory()

	'''
	Rename the foot icon
	'''
	foot_name = leg_root.replace('hLeg_01_bind', 'hFoot_icon')
	foot_icon.rename(foot_name)

	'''
	Parent the ikHandles under the foot icon.
	'''

	pm.parent(ikh_1, ikh_2, ikh_3, ikh_4, ikh_5, foot_icon)

	ikh_5.twist.set(180)


	'''
	Create the knee icon.
	'''

	knee_icon = pm.curve(p=[(2, 0, -2), (4, 0, -2), (4, 0, -3), (6, 0, -1), (4, 0, 1), (4, 0, 0), (2, 0, 0), (2, 0, 2), (3, 0, 2), (1, 0, 4), (-1, 0, 2), (0, 0, 2), (0, 0, 0), (-2, 0, 0), (-2, 0, 1), (-4, 0, -1), (-2, 0, -3), (-2, 0, -2), (0, 0, -2), (0, 0, -4), (-1, 0, -4), (1, 0, -6), (3, 0, -4), (2, 0, -4), (2, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], d=1)
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
	
	
	centerPivot(knee_icon)
	freezeTransform()
	deleteHistory()

	'''
	Move the knee icon.
	'''
	temp_constraint = pm.pointConstraint(leg_joint_3, knee_icon)
	pm.delete(temp_constraint)
	freezeTransform(knee_icon)
	pm.xform(knee_icon, t=[0,0,-30], scale=[3, 3, 3], ro=[90, 0, 0])
	freezeTransform(knee_icon)

	'''
	Pole vector constraint. 
	'''

	
	pm.poleVectorConstraint(knee_icon, ikh_1)
	pm.poleVectorConstraint(knee_icon, ikh_5)

	'''
	Rename the knee
	'''
	knee_name = leg_root.replace('hLeg_01_bind', 'knee_icon')
	knee_icon.rename(knee_name)
	'''
	Thigh Icon
	'''
	'''
	Create orb icon
	'''
	# Custom Orb Icon
	orbCurve2_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	orbCurve2_2 = pm.duplicate(rr=1)[0]
	orbCurve2_2.rx.set(45)
	orbCurve2_3 = pm.duplicate(rr=1)[0]
	orbCurve2_3.rx.set(90)
	orbCurve2_4 = pm.duplicate(rr=1)[0]
	orbCurve2_4.ry.set(45)
	orbCurve2_5 = pm.duplicate(rr=1)[0]
	orbCurve2_5.ry.set(-45)
	pm.makeIdentity(orbCurve2_1, orbCurve2_2, orbCurve2_3, orbCurve2_4, orbCurve2_5, n=0,s=1,r=1,t=1, apply=1,pn=1)
	ik_thigh_icon = pm.group(empty=1)
	temp_grp = pm.group(orbCurve2_1, orbCurve2_2, orbCurve2_3, orbCurve2_4, orbCurve2_5)

	orb2Shapes = pm.ls(sl=1, dag=1)
	shape2_1 = orb2Shapes[2]
	shape2_2 = orb2Shapes[4]
	shape2_3 = orb2Shapes[6]
	shape2_4 = orb2Shapes[8]
	shape2_5 = orb2Shapes[10]
	#print 'Shape 1:', shape_1

	pm.parent(shape2_1, shape2_2, shape2_3, shape2_4, shape2_5, ik_thigh_icon, s=1, r=1)
	pm.delete(temp_grp)

	'''
	Move the icon
	'''
	temp_constraint = pm.parentConstraint(ik_root_joint, ik_thigh_icon)
	pm.delete(temp_constraint)
	freezeTransform(ik_thigh_icon)
	# pm.xform(ik_thigh_icon, t=[0, 0, -10], scale=[3, 3, 3])



	'''
	Pad the icon
	'''

	ik_thigh_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(ik_root_joint, ik_thigh_pad)
	pm.delete(temp_constraint)
	pm.parent(ik_thigh_icon, ik_thigh_pad)
	freezeTransform()

	# Rename Icon
	ik_thigh_icon_name = leg_root.replace('hLeg_01_bind', 'thigh_icon')
	ik_thigh_icon.rename(ik_thigh_icon_name)

	# Renaming Pad
	ik_thigh_pad_name = ik_thigh_icon.replace('icon', 'local')
	ik_thigh_pad.rename(ik_thigh_pad_name)

	'''
	Create the IK/FK switch
	'''
	pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))

	pm.curve(p=[(0, 0, -1), (0, 0, 1)], k=[0, 1], d=1)

	pm.curve(p=[(-1, 0, 0), (1, 0, 0)], k=[0, 1], d=1)

	pm.curve(p=[(0, 0, 1), (0, 0, 3)], k=[0, 1], d=1)


	pm.rename('nurbsCircle1', 'ikfk_curve1')
	pm.rename('curve1', 'ikfk_curve2')
	pm.rename('curve2', 'ikfk_curve3')
	pm.rename('curve3', 'ikfk_curve4')

	shape_1 = 'ikfk_curveShape1'
	shape_2 = 'ikfk_curveShape2'
	shape_3 = 'ikfk_curveShape3'
	shape_4 = 'ikfk_curveShape4'
	switch = pm.group(empty=1)
	print 'Shape 1:', shape_1
	print 'Switch:', switch


	pm.select(shape_2, shape_3)

	pm.cmds.scale(0.768552, 0.768552, 0.768552)
	pm.makeIdentity(n=0, s=1, r=1, t=1, apply=1, pn=1)



	pm.parent(shape_1, shape_2, shape_3, shape_4, switch, s=1, r=1)

	pm.makeIdentity(n=0, s=1, r=1, t=1, apply=1, pn=1)
	shape_1 = 'ikfk_curve1'
	shape_2 = 'ikfk_curve2'
	shape_3 = 'ikfk_curve3'
	shape_4 = 'ikfk_curve4'
	pm.delete(shape_1, shape_2, shape_3, shape_4)

	pm.select(switch, r=1)
	pm.cmds.move(0, 0, 3, switch + '.scalePivot', switch + '.rotatePivot', rpr=1)

	pm.xform(switch, ro=[0,0,90], scale=[2,2,2])
	freezeTransform(switch)
	temp_constraint = pm.pointConstraint(leg_joint_4, switch, mo=0, w=1)
	pm.delete(temp_constraint)
	freezeTransform()
	pm.pointConstraint(leg_joint_4, switch, mo=0, w=1)
	deleteHistory()

	'''
	Add IkFk attribute
	'''
	pm.addAttr(switch, ln="IkFk", max=10, dv=0, at='double', min=0)
	switch.IkFk.set(e=1, keyable=1)

	switch.tx.set(lock=1, channelBox=0, keyable=0)
	switch.ty.set(lock=1, channelBox=0, keyable=0)
	switch.tz.set(lock=1, channelBox=0, keyable=0)
	switch.rx.set(lock=1, channelBox=0, keyable=0)
	switch.ry.set(lock=1, channelBox=0, keyable=0)
	switch.rz.set(lock=1, channelBox=0, keyable=0)
	switch.sx.set(lock=1, channelBox=0, keyable=0)
	switch.sy.set(lock=1, channelBox=0, keyable=0)
	switch.sz.set(lock=1, channelBox=0, keyable=0)
 	switch.v.set(lock=1, channelBox=0, keyable=0)

	'''
	Fk set up
	'''
	
	'''

	Create a hierarchy based upon given system

	Select root joint and execute function.

	# import fk_hQ_legSetUp
	# reload(fk_hQ_legSetUp)
	# fk_hQ_legSetUp.fk_hQ_leg()
	'''

	# print 'Hierarchy Selected'

	'''
	Local Controls 
	'''

	'''
	Control 1 - root_joint
	'''
	'''
	Create orb icon
	'''
	# Custom Orb Icon
	orbCurve_1 = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]
	orbCurve_2 = pm.duplicate(rr=1)[0]
	orbCurve_2.rx.set(45)
	orbCurve_3 = pm.duplicate(rr=1)[0]
	orbCurve_3.rx.set(90)
	orbCurve_4 = pm.duplicate(rr=1)[0]
	orbCurve_4.ry.set(45)
	orbCurve_5 = pm.duplicate(rr=1)[0]
	orbCurve_5.ry.set(-45)
	pm.makeIdentity(orbCurve_1, orbCurve_2, orbCurve_3, orbCurve_4, orbCurve_5, n=0,s=1,r=1,t=1, apply=1,pn=1)
	fk_thigh_icon = pm.group(empty=1)
	temp_grp = pm.group(orbCurve_1, orbCurve_2, orbCurve_3, orbCurve_4, orbCurve_5)

	orbShapes = pm.ls(sl=1, dag=1)
	shape_1 = orbShapes[2]
	shape_2 = orbShapes[4]
	shape_3 = orbShapes[6]
	shape_4 = orbShapes[8]
	shape_5 = orbShapes[10]
	#print 'Shape 1:', shape_1

	pm.parent(shape_1, shape_2, shape_3, shape_4, shape_5, fk_thigh_icon, s=1, r=1)
	pm.delete(temp_grp)

	icon_name = leg_root.replace('bind', 'fk_icon')
	fk_thigh_icon.rename(icon_name)


	'''
	Move the icon
	'''
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_thigh_icon)
	pm.delete(temp_constraint)
	pm.makeIdentity(fk_thigh_icon, n=0,s=1,r=1,t=1, apply=1,pn=1)

	'''
	Pad the icon
	'''

	fk_thigh_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(fk_root_joint, fk_thigh_pad)
	pm.delete(temp_constraint)
	pm.parent(fk_thigh_icon, fk_thigh_pad)
	freezeTransform()

	# Renaming Pad

	fk_thigh_pad_name = fk_thigh_icon.replace('icon', 'local')
	fk_thigh_pad.rename(fk_thigh_pad_name)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(fk_thigh_icon, fk_root_joint)


	'''
	Control 2
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_2 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_2 = pm.group()

	# Output control and pad
	print 'Control 2 Created', control_icon_2
	print 'Local Pad 2 Created', local_pad_2
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_2, local_pad_2)
	pm.delete(temp_constraint)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(control_icon_2, fk_joint_2)

	# Renaming Icon
	# control_icon_2
	icon_2 = control_icon_2
	icon_2_name = fk_thigh_icon.replace('01', '02')
	icon_2.rename(icon_2_name)

	print 'Icon 2 Renamed', control_icon_2

	# Renaming Pad
	pad_2 = local_pad_2
	pad_2_name = control_icon_2.replace('icon', 'local')
	pad_2.rename(pad_2_name)

	print 'Local Pad 2 Renamed', local_pad_2

	''' 
	Parent controls together
	'''
	# Pad 2 -> control 1
	pm.parent(local_pad_2, fk_thigh_icon)

	'''
	Control 3
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_3 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_3 = pm.group()

	# Output control and pad
	print 'Control 3 Created', control_icon_3
	print 'Local Pad 3 Created', local_pad_3
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_3, local_pad_3)
	pm.delete(temp_constraint)


	# Orient constgrain the joint to the control
	# Driver -> Driven
	# Control -> Joint
	pm.orientConstraint(control_icon_3, fk_joint_3)

	# Renaming Icon
	control_icon_3
	icon_3 = control_icon_3
	icon_3_name = control_icon_2.replace('02', '03')
	icon_3.rename(icon_3_name)

	print 'Icon 3 Renamed', control_icon_3

	# Renaming Pad
	pad_3 = local_pad_3
	pad_3_name = control_icon_3.replace('icon', 'local')
	pad_3.rename(pad_3_name)

	print 'Local Pad 3 Renamed', local_pad_3


	''' 
	Parent controls together
	'''
	# Pad 3 -> control 1
	pm.parent(local_pad_3, control_icon_2)

	'''
	Control 4
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_4 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_4 = pm.group()

	# Output control and pad
	print 'Control 4 Created', control_icon_4
	print 'Local Pad 4 Created', local_pad_4
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_4, local_pad_4)
	pm.delete(temp_constraint)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	pm.orientConstraint(control_icon_4, fk_joint_4)

	# Renaming Icon
	# control_icon_4
	icon_4 = control_icon_4
	icon_4_name = control_icon_3.replace('03', '04')
	icon_4.rename(icon_4_name)

	# print 'Icon 4 Renamed', control_icon_4

	# Renaming Pad
	pad_4 = local_pad_4
	pad_4_name = control_icon_4.replace('icon', 'local')
	pad_4.rename(pad_4_name)

	# print 'Local Pad 4 Renamed', local_pad_4


	''' 
	Parent controls together
	'''
	# Pad 4 -> control 1
	pm.parent(local_pad_4, control_icon_3)


	'''
	Control 5
	'''
	# Create a control
	# normal = [1, 0, 0], radius=2
	control_icon_5 = pm.circle(normal=[1, 0, 0], radius=2)[0]

	#  Create a group
	# Grouping control during the process.
	local_pad_5 = pm.group()

	# Output control and pad
	print 'Control 5 Created', control_icon_5
	print 'Local Pad 5 Created', local_pad_5
	# Move group over to the target joint
	# Delete constraint when finished snapping
	temp_constraint = pm.parentConstraint(fk_joint_5, local_pad_5)
	pm.delete(temp_constraint)

	# Orient constgrain the joint to the control
	# Driver -> Driven
	#  Control -> Joint
	temp_constraint = pm.orientConstraint(control_icon_5, fk_joint_5)


	# Renaming Icon
	# control_icon_5
	icon_5 = control_icon_5
	icon_5_name = control_icon_4.replace('04', '05')
	icon_5.rename(icon_5_name)

	print 'Icon 5 Renamed', control_icon_5

	# Renaming Pad
	pad_5 = local_pad_5
	pad_5_name = control_icon_5.replace('icon', 'local')
	pad_5.rename(pad_5_name)

	print 'Local Pad 5 Renamed', local_pad_5


	''' 
	Parent controls together
	'''
	# Pad 5 (Last) -> control 1
	pm.parent(local_pad_5, control_icon_4)

	pm.setAttr("lt_hLeg_01_ik.visibility", 0)
	pm.setAttr("lt_leg_01_helper.visibility", 0)
	pm.setAttr("lt_hLeg_01_fk.visibility", 0)

	'''
	Create the locators
	'''
	# pm.CreateLocator()
	loc1 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 1:', loc1

	# pm.CreateLocator()
	loc2 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 2:', loc2

	# pm.CreateLocator()
	loc3 = pm.spaceLocator(p=(0, 0, 0))
	print 'Locator 3:', loc3

	'''
	Point constraint the locs to the joints.
	'''

	temp_constraint = pm.pointConstraint(leg_joint_4, loc1)
	pm.delete(temp_constraint)
	freezeTransform(loc1)

	temp_constraint = pm.pointConstraint(leg_joint_5, loc2)
	pm.delete(temp_constraint)
	freezeTransform(loc2)

	temp_constraint = pm.pointConstraint(leg_joint_6, loc3)
	pm.delete(temp_constraint)
	freezeTransform(loc3)

	'''
	Parent the locs under the foot icon.
	'''
	pm.parent(loc1, loc2, loc3, foot_icon)

	'''
	Create the flex pivot and offset.
	'''

	flex_pivot = pm.group(empty=1)
	flex_offset = pm.group(empty=1)

	flex_pivot_name = leg_root.replace('hLeg_01_bind', 'flex_pivot')
	flex_pivot.rename(flex_pivot_name)

	flex_offset_name = flex_pivot.replace('pivot', 'offset')
	flex_offset.rename(flex_offset_name)


	temp_constraint = pm.pointConstraint(loc1, flex_pivot)
	pm.delete(temp_constraint)
	pm.makeIdentity(flex_pivot, n=0, s=1, r=1, t=1, apply=1, pn=1)


	temp_constraint = pm.pointConstraint(loc1, flex_offset)
	pm.delete(temp_constraint)
	freezeTransform(flex_offset)

	pm.parent(ikh_1, ikh_2, flex_pivot)
	pm.parent(flex_pivot, flex_offset)

	'''
	Create the toeTap pivot.
	'''

	toeTap_pivot = pm.group(empty=1)

	temp_constraint = pm.pointConstraint(loc2, toeTap_pivot)
	pm.delete(temp_constraint)
	freezeTransform(toeTap_pivot)

	toeTap_name = flex_pivot.replace('flex', 'toeTap')
	toeTap_pivot.rename(toeTap_name)

	pm.parent(ikh_4, toeTap_pivot)

	pm.parentConstraint(helper_joint_4, flex_offset, mo=1, w=1)

	'''
	Add custom attributes.
	'''
	pm.addAttr(foot_icon, ln="flex", dv=0, at='double')
	foot_icon.flex.set(e=1, keyable=1)
	pm.addAttr(foot_icon, ln="swivel", dv=0, at='double')
	foot_icon.swivel.set(e=1, keyable=1)
	pm.addAttr(foot_icon, ln="toeTap", dv=0, at='double')
	foot_icon.toeTap.set(e=1, keyable=1)
	pm.addAttr(foot_icon, ln="toeTip", dv=0, at='double')
	foot_icon.toeTip.set(e=1, keyable=1)

	'''
	Connect the flex attribute
	'''
	pm.connectAttr(foot_icon + '.flex', flex_pivot.rx, f=1)

	'''
	Connect the toeTap attribute.
	'''
	pm.connectAttr(foot_icon + '.toeTap', toeTap_pivot.rx, f=1)

	'''
	Parent the pivots under the foot icon.
	'''
	pm.parent(toeTap_pivot, flex_offset, foot_icon )

	ikfk_name = foot_icon.replace('hFoot_icon', 'IkFk_switch')
	switch.rename(ikfk_name)

def lt_hLeg_SDKs(*args):
	switch = 'lt_IkFk_switch'
	foot_icon = 'lt_hFoot_icon'
	pm.setAttr("lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_fkW1", 0)
	pm.setDrivenKeyframe('lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 10)
	pm.setAttr("lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_fkW1", 1)
	pm.setAttr("lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_01_bind_orientConstraint1.lt_hLeg_01_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_fkW1", 1)
	pm.setAttr("lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_02_bind_orientConstraint1.lt_hLeg_02_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_fkW1", 1)
	pm.setAttr("lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_03_bind_orientConstraint1.lt_hLeg_03_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_fkW1", 1)
	pm.setAttr("lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_04_bind_orientConstraint1.lt_hLeg_04_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_fkW1", 1)
	pm.setAttr("lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_ikW0", 0)
	pm.setDrivenKeyframe('lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hLeg_05_bind_orientConstraint1.lt_hLeg_05_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 0)
	pm.setAttr('lt_hLeg_01_fk_local.visibility', 0)
	pm.setDrivenKeyframe('lt_hLeg_01_fk_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_thigh_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hFoot_icon.visibility', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 10)	
	pm.setAttr("lt_hLeg_01_fk_local.visibility", 1)
	pm.setAttr("lt_thigh_local.visibility", 0)
	pm.setAttr("lt_hFoot_icon.visibility", 0)
	pm.setDrivenKeyframe('lt_hLeg_01_fk_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_thigh_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('lt_hFoot_icon.visibility', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 0)

def rt_hLeg_SDKs(*args):
	switch = 'rt_IkFk_switch'
	foot_icon = 'rt_hFoot_icon'
	pm.setAttr("rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_fkW1", 0)
	pm.setDrivenKeyframe('rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 10)
	pm.setAttr("rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_fkW1", 1)
	pm.setAttr("rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_01_bind_orientConstraint1.rt_hLeg_01_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_fkW1", 1)
	pm.setAttr("rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_02_bind_orientConstraint1.rt_hLeg_02_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_fkW1", 1)
	pm.setAttr("rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_03_bind_orientConstraint1.rt_hLeg_03_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_fkW1", 1)
	pm.setAttr("rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_04_bind_orientConstraint1.rt_hLeg_04_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr("rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_fkW1", 1)
	pm.setAttr("rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_ikW0", 0)
	pm.setDrivenKeyframe('rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_ikW0', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hLeg_05_bind_orientConstraint1.rt_hLeg_05_fkW1', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 0)
	pm.setAttr('rt_hLeg_01_fk_local.visibility', 0)
	pm.setDrivenKeyframe('rt_hLeg_01_fk_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_thigh_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hFoot_icon.visibility', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 10)	
	pm.setAttr("rt_hLeg_01_fk_local.visibility", 1)
	pm.setAttr("rt_thigh_local.visibility", 0)
	pm.setAttr("rt_hFoot_icon.visibility", 0)
	pm.setDrivenKeyframe('rt_hLeg_01_fk_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_thigh_local.visibility', currentDriver=switch + '.IkFk')
	pm.setDrivenKeyframe('rt_hFoot_icon.visibility', currentDriver=switch + '.IkFk')
	pm.setAttr(switch + '.IkFk', 0)

def setZeroHumanFoot(*args):
	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".roll"), lock=0)
		pm.setAttr((str(current) + ".roll"), 0)
		pm.setAttr((str(current) + ".bendLimitAngle"), lock=0)
		pm.setAttr((str(current) + ".bendLimitAngle"), 45)
		pm.setAttr((str(current) + ".toeStraightAngle"), lock=0)
		pm.setAttr((str(current) + ".toeStraightAngle"), 75)
		pm.setAttr((str(current) + ".tilt"), lock=0)
		pm.setAttr((str(current) + ".tilt"), 0)
		pm.setAttr((str(current) + ".lean"), lock=0)
		pm.setAttr((str(current) + ".lean"), 0)
		pm.setAttr((str(current) + ".toeSpin"), lock=0)
		pm.setAttr((str(current) + ".toeSpin"), 0)
		pm.setAttr((str(current) + ".toeTap"), lock=0)
		pm.setAttr((str(current) + ".toeTap"), 0)

def setZeroHumanHand(*args):

	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".All_Curl"), lock=0)
		pm.setAttr((str(current) + ".All_Curl"), 0)
		pm.setAttr((str(current) + ".All_Spread"), lock=0)
		pm.setAttr((str(current) + ".All_Spread"), 0)
		pm.setAttr((str(current) + ".Thumb_Drop"), lock=0)
		pm.setAttr((str(current) + ".Thumb_Drop"), 0)
		pm.setAttr((str(current) + ".Thumb_Root"), lock=0)
		pm.setAttr((str(current) + ".Thumb_Root"), 0)
		pm.setAttr((str(current) + ".Thumb_Mid"), lock=0)
		pm.setAttr((str(current) + ".Thumb_Mid"), 0)
		pm.setAttr((str(current) + ".Thumb_End"), lock=0)
		pm.setAttr((str(current) + ".Thumb_End"), 0)
		pm.setAttr((str(current) + ".Index_Root"), lock=0)
		pm.setAttr((str(current) + ".Index_Root"), 0)
		pm.setAttr((str(current) + ".Index_Mid"), lock=0)
		pm.setAttr((str(current) + ".Index_Mid"), 0)
		pm.setAttr((str(current) + ".Index_End"), lock=0)
		pm.setAttr((str(current) + ".Index_End"), 0)
		pm.setAttr((str(current) + ".Mid_Root"), lock=0)
		pm.setAttr((str(current) + ".Mid_Root"), 0)
		pm.setAttr((str(current) + ".Mid_Mid"), lock=0)
		pm.setAttr((str(current) + ".Mid_Mid"), 0)
		pm.setAttr((str(current) + ".Mid_End"), lock=0)
		pm.setAttr((str(current) + ".Mid_End"), 0)
		pm.setAttr((str(current) + ".Ring_Root"), lock=0)
		pm.setAttr((str(current) + ".Ring_Root"), 0)
		pm.setAttr((str(current) + ".Ring_Mid"), lock=0)
		pm.setAttr((str(current) + ".Ring_Mid"), 0)
		pm.setAttr((str(current) + ".Ring_End"), lock=0)
		pm.setAttr((str(current) + ".Ring_End"), 0)
		pm.setAttr((str(current) + ".Pinky_Root"), lock=0)
		pm.setAttr((str(current) + ".Pinky_Root"), 0)
		pm.setAttr((str(current) + ".Pinky_Mid"), lock=0)
		pm.setAttr((str(current) + ".Pinky_Mid"), 0)
		pm.setAttr((str(current) + ".Pinky_End"), lock=0)
		pm.setAttr((str(current) + ".Pinky_End"), 0)
		pm.setAttr((str(current) + ".Thumb_Spread"), lock=0)
		pm.setAttr((str(current) + ".Thumb_Spread"), 0)
		pm.setAttr((str(current) + ".Index_Spread"), lock=0)
		pm.setAttr((str(current) + ".Index_Spread"), 0)
		pm.setAttr((str(current) + ".Middle_Spread"), lock=0)
		pm.setAttr((str(current) + ".Middle_Spread"), 0)
		pm.setAttr((str(current) + ".Ring_Spread"), lock=0)
		pm.setAttr((str(current) + ".Ring_Spread"), 0)
		pm.setAttr((str(current) + ".Pinky_Spread"), lock=0)
		pm.setAttr((str(current) + ".Pinky_Spread"), 0)

def setZeroTr(*args):
	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".translateX"), lock=0)
		pm.setAttr((str(current) + ".translateX"), 0)
		pm.setAttr((str(current) + ".translateY"), lock=0)
		pm.setAttr((str(current) + ".translateY"), 0)
		pm.setAttr((str(current) + ".translateZ"), lock=0)
		pm.setAttr((str(current) + ".translateZ"), 0)

def setZeroRo(*args):
	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".rotateX"), lock=0)
		pm.setAttr((str(current) + ".rotateX"), 0)
		pm.setAttr((str(current) + ".rotateY"), lock=0)
		pm.setAttr((str(current) + ".rotateY"), 0)
		pm.setAttr((str(current) + ".rotateZ"), lock=0)
		pm.setAttr((str(current) + ".rotateZ"), 0)

def setZeroSc(*args):
	selList=pm.ls(sl=1)
	for current in selList:
		pm.setAttr((str(current) + ".scaleX"), lock=0)
		pm.setAttr((str(current) + ".scaleX"), 1)
		pm.setAttr((str(current) + ".scaleY"), lock=0)
		pm.setAttr((str(current) + ".scaleY"), 1)
		pm.setAttr((str(current) + ".scaleZ"), lock=0)
		pm.setAttr((str(current) + ".scaleZ"), 1)

def windowResize(*args):
	if pm.window('ByrdRigs_interface_toolset', q=1, exists=1):
		pm.window('ByrdRigs_interface_toolset', e=1, wh=(240, 110), rtf=1)
	else:
		pm.warming('ByrdRigs_interface_toolset does not exist')
