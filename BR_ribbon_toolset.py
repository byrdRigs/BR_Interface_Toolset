'''
Title: BR_ribbon_toolset.py
Description
	This file contains: Ribbon tool
	
How to run:
	import BR_Interface_Toolset.BR_ribbon_toolset as BR_ribbon
	reload (BR_ribbon)
	BR_ribbon.gui()
'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import os.path


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
	if pm.window('BR_ribbon_toolset', q=1, exists=1):
		pm.deleteUI('BR_ribbon_toolset')
		#BR_ribbon_toolset

	if(pm.dockControl('dockWindows', q=1, exists=1)):
		pm.deleteUI('dockWindows')

	global window_object, win_width

	win_width = 300
	window_object = pm.window( 'BR_ribbon_toolset', title="Byrd Rig's Ribbon Toolset", w=win_width, bgc=window_bgc )
	main_layout = pm.columnLayout()
	# DockButton = pm.button(l='dock UI', c=dockWindow, w=win_width)

	controllerCreationLayout = pm.frameLayout( l='Create Controllers', cl=1, cll=1, w=win_width, cc=windowResize)
	controllerSubLayout = pm.rowColumnLayout( nc = 3, columnWidth =[(1, 125), (2, 85), (3, 85)] )

	
	pm.text(l = 'Chose controller type: ', al = 'right')
	controllerShapeSelection = pm.radioCollection()
	circleShape = pm.radioButton(l = 'Circle', sl = 1)
	sphereShape = pm.radioButton(l = 'Sphere')
	pm.text(l = 'Controller Radius:', al = 'right')
	controllerRadiusField = pm.floatField(v = 1)
	pm.separator(st = 'none', h = 10)
	GroupJntsOnlyCB = pm.checkBox(l = 'Grp joints Only', v = 0)
	pm.separator(st = 'none', h = 10)
	pm.separator(st = 'none', h = 10)

	# Probably don't need
	ControlMethodRC = pm.radioCollection()
	ParentJntRB = pm.radioButton('Parent',l='Parent', sl=1)
	ConstraintJntsOnlyRB = pm.radioButton('Constraint',l='Constraint', sl=0, onc='constraintOn()', ofc='ConstraintOff()')
	ConnectJntRB = pm.radioButton('Connect', l='connect', sl=0, onc='ConnectOn()', ofc='ConnectOff()')


	pm.setParent(controllerCreationLayout)
	ConstraintSelection = pm.rowColumnLayout(nc = 4)
	pm.setParent(controllerCreationLayout)
	pm.rowColumnLayout(nc=2, cw=[(1, 150), (2, 150)])
	createControllerButton = pm.button(l='Create', c='createControlButtonCommand()')
	createJntBtn = pm.button(l ='Create Jnt', c='createJntUnderSelection()')
	pm.setParent(controllerCreationLayout)
	pm.text(l='Select Controllers and then Skin: ')
	pm.rowColumnLayout(nc=2, cw=[(1, 90), (2, 210)])
	FollowSkinOrientationCB = pm.checkBox(l='Orientation', v=False)
	FollowSkinCtrlButton = pm.button(l='Make Follow Skin', c='attachControllersToSkin()', w = 200)


	#create jnt along crv section UI
	pm.setParent(main_layout)
	ContJntAlongCrvLayout = pm.frameLayout(l='Create Joints Along Curve', cl=1, cll=True, w=win_width, cc=windowResize)
	pm.rowColumnLayout(nc=4, columnWidth=[(1, 70), (2, 70), (3, 90), (4, 70)])
	pm.text(l ='Joint name:')
	jointNameTextField = pm.textField()
	pm.text(l='Joint amount: ')
	jointAmountIntField = pm.intField(v=3)
	pm.text(l='Joint radius: ')
	jointRadiusFloatField = pm.floatField(v=1.0)
	pm.text(l='Locator size: ')
	locatorSizeFloatField = pm.floatField(v=1.0)

	pm.setParent(ContJntAlongCrvLayout)
	# pm.text(l='Use the Naming Convention under the Create Controllers')
	createJointAlongCrvBtn = pm.button(l='Create Joints', c='createJnt()')


	#create ribbon based on curve selected section UI
	pm.setParent(main_layout)
	RibbonUILayout = pm.frameLayout(l='Create Ribbon', cl=1, cll=True, w=win_width, cc=windowResize)
	pm.text(l='select curve or nothing: ')
	pm.rowColumnLayout(nc=4)
	pm.text(l='bind joint count: ')
	bindJntCountIntField = pm.intField(w=50, v=6)
	pm.text(l='control joint count: ')
	ctrlJntCountIntField = pm.intField(w=50, v=3)
	pm.text(l='ribbon width: ')
	RibbonWidthFloatField = pm.floatField(v=0.5, w=20)
	pm.setParent(RibbonUILayout)
	pm.rowColumnLayout(nc=2)
	pm.text(l='ribbon name base: ')
	RibbonNameField = pm.textField(w=200)
	pm.setParent(RibbonUILayout)
	pm.rowLayout(nc=6)
	pm.text(l='Direction: ')
	ribbonDirectionRC = pm.radioCollection()
	pm.radioButton('X')
	pm.radioButton('Y', sl=True)
	pm.radioButton('Z')
	usingNurbsCB = pm.checkBox( l='use nurbs', v=False)
	pm.setParent(RibbonUILayout)
	pm.rowColumnLayout(nc=3)
	CreateCtrlCB = pm.checkBox(l='Create Controllers', v=True)
	ParentToHierachyCB = pm.checkBox(l='Parent To Hierachy', v=False, onc='ParentToHierachyCBOnCmd()', ofc='ParentToHierachyCBOffCmd()')
	pm.setParent(RibbonUILayout)
	pm.rowColumnLayout(nc=3)
	parentJntText = pm.text(l='Parent Joint:', vis=1)
	parentJntTextField = pm.textField(vis=1, ed=False, w=200)
	parentJntAssignTextFieldBtn = pm.button(l='<<<', vis=1, c='assignTextField(parentJntTextField)')
	#useNurbs = pm.checkBox(l='use nurbs', v=False)
	pm.setParent(RibbonUILayout)
	createRibbonBtn = pm.button(l='Create Ribbon', c='createRibbonBtnCmd()')






	pm.window('BR_ribbon_toolset', e=1, wh=(300, 60), rtf=1, nde=1)
	pm.showWindow(window_object)

	print('Window Created:', window_object)

#Data and Object Types:
class ControllerTypes:
    Circle = 1
    Sphere = 2
    
class globalMem:
    ControllerList = []
    curentController = 0

def dockWindow(*args):
    allowedAreas = ['right', 'left']
    if pm.dockControl( 'dockWindows', q=1, exists=1 ):
        return
    pm.dockControl( 'dockWindows', l='BR_ribbon_toolset', area='left', content=window_object, allowedArea=allowedAreas, mov=1, w=win_width, h=win_height)
    
def GetSelectedAttribute(*args):
    selectedObj = pm.ls(sl = True)[0]
    Attr = pm.channelBox("mainChannelBox", q=True, sma=True)[0]
    selectedObjAttr = selectedObj + "." + Attr
    return selectedObjAttr

def setTextField(content, textFieldToSet):
    pm.textField(textFieldToSet, e=True, tx=content)
      
def getText(textFieldToGet):
    return pm.textField(textFieldToGet, q=True, tx=True)

def createClamp(name, clampPos):
    if not pm.objExists(name):
        pm.createNode('clamp', asUtility=1, n = name)
        if clampPos:
            pm.setAttr(name + '.maxR', 10000)
            pm.setAttr(name + '.maxG', 10000)
            pm.setAttr(name + '.maxB', 10000)        
        else:
            pm.setAttr(name + '.minR', -10000)
            pm.setAttr(name + '.minG', -10000)
            pm.setAttr(name + '.minB', -10000)

def createInvertMD(name):
    if not pm.objExists(name):
        pm.createNode('multiplyDivide', asUtility=1, n = name)
        pm.setAttr(name + '.input2X', -1)
        pm.setAttr(name + '.input2Y', -1)
        pm.setAttr(name + '.input2Z', -1)

def createScaleMD(name, factor):
    if not pm.objExists(name):
        pm.createNode('multiplyDivide', asUtility=1, n = name)
    pm.setAttr(name + '.input2X', factor)
    pm.setAttr(name + '.input2Y', factor)
    pm.setAttr(name + '.input2Z', factor)

def windowResize(*args):
	if pm.window('BR_ribbon_toolset', q=1, exists=1):
		pm.window('BR_ribbon_toolset', e=1, wh=(300, 60), rtf=1)
	else:
		pm.warning('BR_ribbon_toolset does not exist')

def deleteUI(*args):
	# print('Closing UI')
	pm.deleteUI('BR_ribbon_toolset')















