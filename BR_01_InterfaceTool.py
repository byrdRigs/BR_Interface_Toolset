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

tab_bgc=(0.472, 0.136, 239)
subTab_bgc = (0.492, 0.323, 241)
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
	if pm.window('ByrdRigs_interface_toolset', q=1, exists=1):
		pm.deleteUI('ByrdRigs_interface_toolset')
		#ByrdRigs_interface_toolset

	win_width = 240
	window_object = pm.window('ByrdRigs_interface_toolset', title="ByrdRigs' Toolset", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()


	'''
	Clean Up Geo and Controls

	'''
	pm.frameLayout(w=win_width, l='Clean Up', bgc=color_1, cl=1, cll=1, ann='Clean Up', cc=windowResize)
	pm.rowColumnLayout(w=win_width)
	pm.iconTextButton('delete_histroy', w=166, st='iconAndTextHorizontal', image1='DeleteHistory.png',l='Delete History', c=deleteHistory)
	pm.iconTextButton(w=166, st='iconAndTextHorizontal', image1='CenterPivot.png',l='Center Pivot', c=centerPivot)
	pm.iconTextButton(w=166, st='iconAndTextHorizontal', image1='FreezeTransform.png',l='Freeze Transforms', c=freezeTransform)

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_1, st='in')

	'''
	Visibility
	'''
	pm.frameLayout(w=win_width, l='Visibility', bgc=color_2, cl=1, cll=1, ann='Change Visibility', cc=windowResize)
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(l='Show')
	pm.button(l='All', c=showAll)
	pm.button(l='None', c=showNone)
	pm.text(l='Poly Vis')
	pm.button(l='On', c=polyOn)
	pm.button(l='Off', c=polyOff)
	pm.text(l='Poly Only Vis')
	pm.button(l='On', c=polyOnlyOn)
	pm.button(l='Off', c=polyOnlyOff)
	pm.text(l='Joints')
	pm.button(l='On', c=jointsOn)
	pm.button(l='Off', c=jointsOff)
	pm.text(l='X-Ray Joints')
	pm.button(l='On', c=xRayOn)
	pm.button(l='Off', c=xRayOff)
	pm.text(l='Wire Shaded')
	pm.button(l='On', c=wireOn)
	pm.button(l='Off', c=wireOff)
	pm.text(l='NURBS Curves')
	pm.button(l='On', c=curvesOn)
	pm.button(l='Off', c=curvesOff)
	pm.text(l='NURBS Surfaces')
	pm.button(l='On', c=surfacesOn)
	pm.button(l='Off', c=surfacesOff)
	pm.text(l='DAG')
	pm.button(l='On', c=dagOn)
	pm.button(l='Off', c=dagOff)

	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_2, st='in')

	'''
	Tools
	'''
	pm.frameLayout(w=win_width, l='Tools', bgc=color_3, cl=1, cll=1, ann='Different Tools', cc=windowResize)
	pm.columnLayout()
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinJoint.png', l='Create Joint Tool', c=jointTool)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='menuIconDisplay.png', l='Joint Size', c=jointSize)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='kinInsert.png', l='Insert Joint', c=insertJoint)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='menuIconDisplay.png', l='IK Handle Size', c=IkSize)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='BR_icons/BR_diagram.png', l='Select Hierarchy', c=hierarchy)
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='BR_icons/BR_renamerIcon.svg', l='Renamer', c=renamerWindow)
	
	pm.iconTextButton(w=win_width, st='iconAndTextHorizontal', image1='circle.png', l='Curve Tool Window', c=curveWindow)
	pm.separator(w=win_width, bgc=color_3, st='in')
	pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	pm.text(l='Mirror Joints')
	pm.button(l='B' , c=mirrorToolB)
	pm.button(l='Ori', c=mirrorToolO)
	pm.text(l='IK Handle Tool')
	pm.button(l='RP', c=RP_IkHandle)
	pm.button(l='SC', c=SC_IkHandle)
	pm.text(l='Padding')
	pm.button(l='Jnt' , c=jointPadding)
	pm.button(l='Ctrl', c=ctrlPadding)
	pm.button(l='Mirror Ctrl' , c=mirrorIcon)


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_3, st='in')
	
	'''
	Constraints
	'''
	pm.frameLayout(w=win_width, l='Constraints', bgc=color_4, cl=1, cll=1, ann='Constraints', cc=windowResize)
	pm.rowColumnLayout(nc=4, cw=[[1, win_width*.25], [2, win_width*.25],[3, win_width*.25], [4, win_width*.25]])
	pm.text(l='Parent MO')
	pm.button(l='On', c=parentConstraint_on)
	pm.button(l='Off', c=parentConstraint_off)
	pm.button(l='Temp', c=parentConstraint_temp)
	pm.text(l='Point MO')
	pm.button(l='On', c=pointConstraint_on)
	pm.button(l='Off', c=pointConstraint_off)
	pm.button(l='Temp', c=pointConstraint_temp)
	pm.text(l='Orient MO')
	pm.button(l='On', c=orientConstraint_on)
	pm.button(l='Off', c=orientConstraint_off)
	pm.button(l='Temp', c=orientConstraint_temp)
	pm.button(w=win_width, l='Pole Vector', c=poleVector)
	
	
	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_4, st='in')


	'''
	Bipeds
	'''
	pm.frameLayout(w=win_width, l='Bipeds', bgc=color_5, cl=1, cll=1, ann='Biped Tools', cc=windowResize)
	biped_layout = pm.columnLayout(w=win_width)
	pm.text(l="This is a biped auto rigger, it doesn't do weight painting. It is only a body rigger, there is no facial rigging done", ww=1, w=win_width)
	pm.button(l='Auto-Rig Window', bgc=color_6, w=win_width, c=autoRig)


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_5, st='in')
	'''
	Quadrupeds
	'''
	quad_layout = pm.frameLayout(w=win_width, l='Quadrupeds', bgc=color_6, cl=1, cll=1, ann='Quadruped Tools', cc=windowResize )
	pm.setParent(quad_layout)
	pm.text(l='Coming Soon - In Testing', w=win_width)
	# pm.frameLayout(w=win_width, l='Hind Legs', bgc=(color_7), cl=1, cll=1, cc=windowResize)
	# pm.text(l='orientation_h(Leg, LegIK, then LegFK)', w=win_width, al='center')
	# pm.button(l='Hind IK/FK/Helper Joints',w=win_width, ann='Creates leg ik/fk/helper joint chains', c=quad_hLeg_joints)
	# pm.text(l='Select the bind, ik, helper, and fk joints', w=win_width)
	# pm.button(l='hLeg IK/FK System', w=win_width,  ann='Sets up the hind leg IK/FK systems', c=quad_hIKFK_system)
	# pm.rowColumnLayout(nc=3, cw=[[1, win_width*.5], [2, win_width*.25],[3, win_width*.25]])
	# pm.text(l='Leg SDKs')
	# pm.button(l='lt', c=lt_hLeg_SDKs)
	# pm.button(l='rt', c=rt_hLeg_SDKs)
	


	pm.setParent(main_layout)
	pm.separator(w=win_width, bgc=color_6, st='in')

	'''
	Zero Out Attributes
	'''
	pm.frameLayout(w=win_width, l='Zero Out', bgc=color_7, cl=1, cll=1, ann='Zero Out the Attributes to defaults', cc=windowResize)
	pm.columnLayout()
	pm.button(l='Human Foot Attributes', w=win_width, c=setZeroHumanFoot, ann='Sets Custom Foot Attributes back to defaults')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.button(l='Human Hand Attributes', w=win_width, c=setZeroHumanHand, ann='Sets Custom Hand Attributes back to defaults')
	pm.separator(w=win_width, bgc=(tab_bgc), st='in')
	pm.rowColumnLayout(nc=3, cw=[[1, 80], [2, 80],[3, 80]])
	pm.button(l='Translate', c=setZeroTr)
	pm.button(l='Rotate', c=setZeroRo)
	pm.button(l='Scale', c=setZeroSc)


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

def polyOnlyOn(*args):
	pm.modelEditor(panel_1, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_1, panel_1, "modelPanel1", "Playblast Display")

	pm.modelEditor(panel_2, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_2, panel_2, "modelPanel2", "Playblast Display")

	pm.modelEditor(panel_3, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_3, panel_3, "modelPanel3", "Playblast Display")

	pm.modelEditor(panel_4, allObjects=0, e=1)
	pm.mel.updateShowMenu(show_4, panel_4, "modelPanel4", "Playblast Display")	

	pm.modelEditor(panel_1, e=1, polymeshes=1)
	pm.modelEditor(panel_1, e=1, hos=1)
	pm.modelEditor(panel_2, e=1, polymeshes=1)
	pm.modelEditor(panel_2, e=1, hos=1)
	pm.modelEditor(panel_3, e=1, polymeshes=1)
	pm.modelEditor(panel_3, e=1, hos=1)
	pm.modelEditor(panel_4, e=1, polymeshes=1)
	pm.modelEditor(panel_4, e=1, hos=1)

def polyOnlyOff(*args):
	pm.modelEditor(panel_1, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_1, panel_1, "modelPanel1", "Playblast Display")

	pm.modelEditor(panel_2, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_2, panel_2, "modelPanel2", "Playblast Display")

	pm.modelEditor(panel_3, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_3, panel_3, "modelPanel3", "Playblast Display")

	pm.modelEditor(panel_4, allObjects=1, e=1)
	pm.mel.updateShowMenu(show_4, panel_4, "modelPanel4", "Playblast Display")

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
	pm.modelEditor( panel_1, e=1, controllers=1 )
	pm.modelEditor( panel_2, e=1, controllers=1 )
	pm.modelEditor( panel_3, e=1, controllers=1 )
	pm.modelEditor( panel_4, e=1, controllers=1 )

def curvesOff(*args):
	print 'NURBS Curves hidden'
	pm.modelEditor(panel_1, e=1, nurbsCurves=0)
	pm.modelEditor(panel_2, e=1, nurbsCurves=0)
	pm.modelEditor(panel_3, e=1, nurbsCurves=0)
	pm.modelEditor(panel_4, e=1, nurbsCurves=0)
	pm.modelEditor( panel_1, e=1, controllers=0 )
	pm.modelEditor( panel_2, e=1, controllers=0 )
	pm.modelEditor( panel_3, e=1, controllers=0 )
	pm.modelEditor( panel_4, e=1, controllers=0 )

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

def dagOn(*args):
	# print('Showing DAG objects')
	pm.outlinerEditor('outlinerPanel3', showDagOnly=1, e=1)

def dagOff(*args):
	# print('Hiding DAG objects')
	pm.outlinerEditor('outlinerPanel3', showDagOnly=0, e=1)

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

def mirrorIcon(*args):
	# Get all the icons
	pm.select( 'lt*_icon', 'lt*_switch' )

	lt_icons = pm.ls( sl=1 )
	# print(lt_icons)

	tempGrp = pm.group( em=1, n='temp_grp' )

	pm.parent( lt_icons, tempGrp )

	mirrorGrp = pm.duplicate( tempGrp, n='mirror_grp' )[0]

	mirrorGrp.sx.set( -1 )

	pm.select(mirrorGrp)
	freezeTransform()

	pm.parent( lt_icons, w=1 )
	pm.delete(tempGrp)

	rt_icons = pm.ls( mirrorGrp, dag=1 )
	print(rt_icons)

	pm.select( lt_icons[0] )
	icon = pm.ls( sl=1 )[0]


	search= 'lt'
	replace= 'rt'
	pm.select( rt_icons )
	pm.mel.searchReplaceNames(search, replace, "hierarchy")

	pm.select( rt_icons )
	pm.parent( w=1 )
	pm.delete( mirrorGrp )
		
	
	

		


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
	pm.mel.source("Quick_rename_tool.mel")
	pm.mel.Quick_rename_tool()

def curveWindow(*args):
	import BR_Interface_Toolset.BR_curveTool as BR_curveTool
	reload(BR_curveTool)
	BR_curveTool.curve_gui()

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

def parentConstraint_temp(*args):
	selection = pm.ls(sl=1)
	driver = selection[0]
	driven= selection[1]

	temp_constraint = pm.parentConstraint(driver, driven, mo=0)
	pm.delete(temp_constraint)

def pointConstraint_temp(*args):
	selection = pm.ls(sl=1)
	driver = selection[0]
	driven= selection[1]

	temp_constraint = pm.pointConstraint(driver, driven, mo=0)
	pm.delete(temp_constraint)

def orientConstraint_temp(*args):
	selection = pm.ls(sl=1)
	driver = selection[0]
	driven= selection[1]

	temp_constraint = pm.orientConstraint(driver, driven, mo=0)
	pm.delete(temp_constraint)

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

def autoRig(*args):
	import BR_Interface_Toolset.BR_biped_AutoRig_setup as BR_biped_setup
	reload (BR_biped_setup)
	BR_biped_setup.gui()

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
	selection=pm.ls(sl=1)
	for each in selection:
		if pm.getAttr(each + '.kneeTwist', lock=0):
			pm.setAttr(each + '.kneeTwist', 0)
		if pm.getAttr(each + '.roll', lock=0):
			pm.setAttr(each + '.roll', 0)
		if pm.getAttr(each + '.bendLimitAngle', lock=0):
			pm.setAttr(each + '.bendLimitAngle', 45)
		if pm.getAttr(each + '.toeStraightAngle', lock=0):
			pm.setAttr(each + '.toeStraightAngle', 75)
		if pm.getAttr(each + '.tilt', lock=0):
			pm.setAttr(each + '.tilt', 0)
		if pm.getAttr(each + '.lean', lock=0):
			pm.setAttr(each + '.lean', 0)
		if pm.getAttr(each + '.toeSpin', lock=0):
			pm.setAttr(each + '.toeSpin', 0)
		if pm.getAttr(each + '.toeTap', lock=0):
			pm.setAttr(each + '.toeTap', 0)

def setZeroHumanHand(*args):

	selection=pm.ls(sl=1)
	for each in selection:
		if pm.getAttr(each + '.Ik_Fk_Switch', lock=0):
			pm.setAttr(each + '.Ik_Fk_Switch', 0)
		if pm.getAttr(each + '.All_Curl', lock=0):
			pm.setAttr(each + '.All_Curl', 0)
		if pm.getAttr(each + '.All_Spread', lock=0):
			pm.setAttr(each + '.All_Spread', 0)
		if pm.getAttr(each + '.thumbDrop', lock=0):
			pm.setAttr(each + '.thumbDrop', 0)
		if pm.getAttr(each + '.thumbRoot', lock=0):
			pm.setAttr(each + '.thumbRoot', 0)
		if pm.getAttr(each + '.thumbMid', lock=0):
			pm.setAttr(each + '.thumbMid', 0)
		if pm.getAttr(each + '.thumbEnd', lock=0):
			pm.setAttr(each + '.thumbEnd', 0)
		if pm.getAttr(each + '.indexRoot', lock=0):
			pm.setAttr(each + '.indexRoot', 0)
		if pm.getAttr(each + '.indexMid', lock=0):
			pm.setAttr(each + '.indexMid', 0)
		if pm.getAttr(each + '.indexEnd', lock=0):
			pm.setAttr(each + '.indexEnd', 0)
		if pm.getAttr(each + '.middleRoot', lock=0):
			pm.setAttr(each + '.middleRoot', 0)
		if pm.getAttr(each + '.middleMid', lock=0):
			pm.setAttr(each + '.middleMid', 0)
		if pm.getAttr(each + '.middleEnd', lock=0):
			pm.setAttr(each + '.middleEnd', 0)
		if pm.getAttr(each + '.ringRoot', lock=0):
			pm.setAttr(each + '.ringRoot', 0)
		if pm.getAttr(each + '.ringMid', lock=0):
			pm.setAttr(each + '.ringMid', 0)
		if pm.getAttr(each + '.ringEnd', lock=0):
			pm.setAttr(each + '.ringEnd', 0)
		if pm.getAttr(each + '.pinkyRoot', lock=0):
			pm.setAttr(each + '.pinkyRoot', 0)
		if pm.getAttr(each + '.pinkyMid', lock=0):
			pm.setAttr(each + '.pinkyMid', 0)
		if pm.getAttr(each + '.pinkyEnd', lock=0):
			pm.setAttr(each + '.pinkyEnd', 0)
		if pm.getAttr(each + '.thumbSpread', lock=0):
			pm.setAttr(each + '.thumbSpread', 0)
		if pm.getAttr(each + '.indexSpread', lock=0):
			pm.setAttr(each + '.indexSpread', 0)
		if pm.getAttr(each + '.middleSpread', lock=0):
			pm.setAttr(each + '.middleSpread', 0)
		if pm.getAttr(each + '.ringSpread', lock=0):
			pm.setAttr(each + '.ringSpread', 0)
		if pm.getAttr(each + '.pinkySpread', lock=0):
			pm.setAttr(each + '.pinkySpread', 0)

def setZeroTr(*args):
	selection = pm.ls(sl=1)
	for each in selection:
		if pm.getAttr(each + '.tx', lock=0):
			pm.setAttr(each + '.tx', 0)

		if pm.getAttr(each + '.ty', lock=0):
			pm.setAttr(each + '.ty', 0)

		if pm.getAttr(each + '.tz', lock=0):
			pm.setAttr(each + '.tz', 0)

def setZeroRo(*args):
	selection = pm.ls(sl=1)
	for each in selection:
		if pm.getAttr(each + '.rx', lock=0):
			pm.setAttr(each + '.rx', 0)

		if pm.getAttr(each + '.ry', lock=0):
			pm.setAttr(each + '.ry', 0)

		if pm.getAttr(each + '.rz', lock=0):
			pm.setAttr(each + '.rz', 0)	

def setZeroSc(*args):
	selection = pm.ls(sl=1)
	for each in selection:
		if pm.getAttr(each + '.scaleX', lock=0):
			pm.setAttr(each + '.scaleX', 1)

		if pm.getAttr(each + '.scaleY', lock=0):
			pm.setAttr(each + '.scaleY', 1)

		if pm.getAttr(each + '.scaleZ', lock=0):
			pm.setAttr(each + '.scaleZ', 1)	

def windowResize(*args):
	if pm.window('ByrdRigs_interface_toolset', q=1, exists=1):
		pm.window('ByrdRigs_interface_toolset', e=1, wh=(240, 110), rtf=1)
	else:
		pm.warning('ByrdRigs_interface_toolset does not exist')
