'''
ByrdRigs- Curve Interface

Author: Cheyenne Byrd
Date Modified: 

Description:
    This is a main tool comprised of smaller, sub-scripts.
    The Curves Tool script contains commonly used features such as:
    - Control icon creation
	- Colorizing options
	- Preset and custom attribut creation
	- Control clean up options

How to run:
import BR_curve_tool
reload (BR_curve_tool)
'''

import pymel.core as pm
import maya.cmds as cmds
from functools import partial

win_width = 325
height = 10
tab_bgc = (0.4718592, 0.13568, 239)
window_bgc = (.2,.2,.2)
element_bgc = (.45,.45,.45)
title_color = (0.4915200, 0.32256, 241)
curveCreation_width = 290
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


def windowCreation():

	if pm.window('ByrdRigs_Curve_Tool', q=1, exists=1):
		pm.deleteUI('ByrdRigs_Curve_Tool')
		#ByrdRigs_Curve_Tool

	window_object = pm.window('ByrdRigs_Curve_Tool', title="ByrdRigs_Curve_Tool", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()
	gui()



	pm.window('ByrdRigs_Curve_Tool', e=1, wh=(240, 81), rtf=True)
	pm.showWindow(window_object)

	print('Window Created:', window_object)

def gui():
	main_layout = pm.columnLayout()

	# Creation
	pm.frameLayout('Creation', label='Creation', w=win_width, bgc=color_1, cl=True, cll=True, cc=windowResize)
	# global main, naming_form, grouping_form, grouping_options_frame
	# main = pm.columnLayout()

	# naming_form = pm.formLayout()
	# naming_title = title_creation('Control Naming', naming_form)
	# rename_col = rename_gui()
	# ctrl_options_col = control_options_gui()

	# pm.formLayout(naming_form, e=True,
	# attachForm=[(ctrl_options_col, 'right', 5), (ctrl_options_col, 'left', 5), (rename_col, 'right', 5), (rename_col, 'left', 5), (naming_title, 'right', 5), (naming_title, 'left', 5), (naming_title, 'top', 5)],
	# attachControl=[(ctrl_options_col, 'top', 5, rename_col), (rename_col, 'top', 5, naming_title)])
	# pm.setParent(main)


	# pm.columnLayout(co=('left', 5))
	# grouping_options_frame = pm.frameLayout(l='Grouping', en=False, w=curveCreation_width, cl=True, cll=True, bgc=tab_bgc, cc=pm.Callback(window_resize, -200))
	# pm.setParent(main)

	# grouping_form = pm.formLayout(p=grouping_options_frame)
	# grouping_title = title_creation('Group Naming', grouping_form)
	# group_naming_col = group_naming_gui()
	# grouping_instructions_title = title_creation('Grouping Options', grouping_form)
	# grouping_instructions_col = group_instructions_gui()
	# grouping_options_col = grouping_options_gui()
	# pm.setParent(main)

	# pm.formLayout(grouping_form, e=True,
	# attachForm=[(grouping_options_col, 'left', 0), (grouping_options_col, 'right', 0),(grouping_instructions_col, 'left', 0), (grouping_instructions_col, 'right', 0),(grouping_instructions_title, 'left', 0), (grouping_instructions_title, 'right', 0),(group_naming_col, 'left', 0), (group_naming_col, 'right', 0),(grouping_title, 'left', 0), (grouping_title, 'right', 0), (grouping_title, 'top', 5), ],
	# attachControl=[(grouping_options_col, 'top', 5, grouping_instructions_col), (grouping_instructions_col, 'top', 5, grouping_instructions_title), (grouping_instructions_title, 'top', 5, group_naming_col), (group_naming_col, 'top', 5, grouping_title)])

	# pm.setParent(main)
	# control_buttons_gui()
	pm.setParent(main_layout)


	# Coloring
	pm.frameLayout('Coloring', label='Coloring', w=win_width, bgc=color_2, cl=True, cll=True, cc=windowResize)
	pm.setParent(main_layout)

	# Attributes
	pm.frameLayout('Attributes', label='Attributes', w=win_width, bgc=color_3, cl=True, cll=True, cc=windowResize)

	main = pm.columnLayout(w=win_width)
	main_form = pm.formLayout(nd=100, w=win_width)

	preset_options_column = pm.columnLayout(w=win_width)
	# attr_title_creation('Preset Options')
	preset_options()
	pm.setParent(main_form)

	custom_options_column = pm.columnLayout(w=win_width)
	# attr_title_creation('Custom Options')
	custom_options()
	pm.setParent(main_form)

	pm.formLayout(main_form, e=True,
	attachForm=[(custom_options_column, 'left', 5), (custom_options_column, 'right', 5), (custom_options_column, 'bottom', 5), (preset_options_column, 'left', 5), (preset_options_column, 'right', 5), (preset_options_column, 'top', 5)],
	attachControl=[(custom_options_column, 'top', 2, preset_options_column)])

	pm.setParent(main_layout)

	# Lock and Hide
	pm.frameLayout('Lock and Hide', label='Lock and Hide', w=win_width, bgc=color_4, cl=True, cll=True)
	pm.setParent(main_layout)


'''
Curve Creation

Description:
    A custom GUI to easily create commonly used control icons for rig construction.
	- Includes 2D, 3D, and text based curves.
	
    Provides features for:
	- Priming controls based on a selected transform node, or a heirarchy of nodes.
	- Naming control icons
	- Naming priming groups
	- Constraining selected transform node
	    ~ Parent or orient constraint options

    The curve must be selected first, then the transform node. This selection order was
    choosen because it replicates actual parenting inside of Maya.
'''














'''
Add Attributes Tool

Description:
    A custom GUI to easily add common attributes to objects.
    
    Allows for additonal, custom attributes, to be added to objects
    without having to navigate to other windows.
'''
def title_creation(title):
    pm.columnLayout(w=win_width)
    pm.separator(w=win_width-15, h=5)
    pm.text(l=title, w=win_width-15, bgc=title_color)
    pm.separator(w=win_width-15, h=5)
     
def preset_options():
    main = pm.columnLayout(w=win_width)
    
    pm.rowColumnLayout(nc=2, w=win_width)
    pm.button(w=141, bgc=element_bgc, l='Ik Foot', c=add_ikFootAttrs)
    pm.button(w=141, bgc=element_bgc, l='Foot Switch', c=add_footSwitchAttrs)
    pm.button(w=141, bgc=element_bgc, l='Ik Hand', c=add_ikHandAttrs)
    pm.button(w=141, bgc=element_bgc, l='Hand Switch', c=add_handSwitchAttrs)
    pm.setParent(main)
    
    pm.rowColumnLayout(nc=3, w=win_width)
    pm.button(w=94, bgc=element_bgc, l='Cog', c=add_cogAttrs)
    pm.button(w=94, bgc=element_bgc, l='Head', c=add_headAttrs)
    pm.button(w=94, bgc=element_bgc, l='Eye', c=add_eyeAttrs)
    pm.setParent(main)
    
def custom_options():
    global attributeType_radioGrp, attribute_nameField, attribute_minField, attribute_maxField
    main = pm.columnLayout()
    attributeType_radioGrp = pm.radioButtonGrp(cc=field_display, sl=1, nrb=4, cw4=(75,75,75,75), la4=('Float', 'Integer', 'Boolean', 'Sep'))
    
    pm.separator(w=win_width-15, h=10)
    pm.rowColumnLayout(nc=4, w=win_width)
    attribute_nameField = pm.textField(w=71, ann = 'Attribute Name', tx='Name')
    attribute_minField = pm.floatField(w=71, ann='Attribute Min', v=-360, pre=1)
    attribute_maxField = pm.floatField(w=71, ann='Attribute Max', v=360, pre=1)
    pm.button(l='Create', bgc=element_bgc, w=71, c=create_attr)
    pm.setParent(main)

def field_display(*args):
    attr_value = attributeType_radioGrp.getSelect()
    
    if attr_value == 1:
	attribute_minField.setEnable(True)
	attribute_maxField.setEnable(True)
	
    elif attr_value == 2:
	attribute_minField.setEnable(True)
	attribute_maxField.setEnable(True)
	
    elif attr_value == 3:
	attribute_minField.setEnable(False)
	attribute_maxField.setEnable(False)
	
    else:
	attribute_minField.setEnable(False)
	attribute_maxField.setEnable(False)

# Work Functions
def add_cogAttrs(*args):
    selection = pm.ls(sl=True)
	
    for individual_object in selection:
	create_separatorAttr(individual_object, 'Adv_Back')
	pm.addAttr(individual_object, ln='Back_Ctrls', at='enum', en='Fk_Ctrls:Ik_Ctrls:Both:None', k=True)
	
	create_separatorAttr(individual_object, 'Other')
	pm.addAttr(individual_object, ln='Res', at='enum', en='Low:Proxy:High', k=True)
	create_boolAttr(individual_object, 'Auto_Hips')

def add_eyeAttrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	create_separatorAttr(individual_object, 'Control_Visibility')
	create_boolAttr(individual_object, 'Indiv_Ctrls')

def add_headAttrs(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
	create_separatorAttr(individual_object, 'Control_Visibility')
	create_boolAttr(individual_object, 'Face_Ctrls')
	create_boolAttr(individual_object, 'Eye_Ctrls')

def add_ikFootAttrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	create_separatorAttr(individual_object, 'Foot_SDKs')

	create_floatAttr(individual_object, 'Foot_Roll', -10, 10)
	create_floatAttr(individual_object, 'Bank', -100, 100)
	
	create_curlAttrs(individual_object, foot_raiseAttrs)
	
	create_separatorAttr(individual_object, 'Grinds')
	create_floatAttr(individual_object, 'Heel_Grind', -100, 100)
	create_floatAttr(individual_object, 'Toe_Grind', -100, 100)

	create_separatorAttr(individual_object, 'Knee_Pv')
	create_floatAttr(individual_object, 'Knee', -100, 100)
	create_floatAttr(individual_object, 'Offset', -100, 100)

	create_separatorAttr(individual_object, 'Space_Switching')
	create_floatAttr(individual_object, 'Cog', -100, 100)
	create_floatAttr(individual_object, 'Locator', -100, 100)

def add_ikHandAttrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	create_separatorAttr(individual_object, 'Space_Switching')
	create_floatAttr(individual_object, 'Head', 0, 10)
	create_floatAttr(individual_object, 'Back', 0, 10)
	create_floatAttr(individual_object, 'Hips', 0, 10)
	create_floatAttr(individual_object, 'Locator', 0, 10)

def add_footSwitchAttrs(*args):
    selection = pm.ls(sl=True)

    for individual_object in selection:
	create_separatorAttr(individual_object, 'Foot_SDKs')
	create_floatAttr(individual_object, 'Ik_Fk_Switch', 0 , 10)
	create_boolAttr(individual_object, 'Indiv_Ctrls')
	create_floatAttr(individual_object, 'All_Curl', -10 , 10)
	create_floatAttr(individual_object, 'All_Spread', -10 , 10)

	create_curlAttrs(individual_object, big_curlAttrs)
	create_curlAttrs(individual_object, index_curlAttrs)
	create_curlAttrs(individual_object, mid_curlAttrs)
	create_curlAttrs(individual_object, fourth_curlAttrs)
	create_curlAttrs(individual_object, pinky_curlAttrs)
	
	create_spreadAttrs(individual_object, toe_spreadAttrs)

def add_handSwitchAttrs(*args):
    selection = pm.ls(sl=True)
    
    for individual_object in selection:
	create_separatorAttr(individual_object, 'Hand_SDKs')
	create_floatAttr(individual_object, 'Ik_Fk_Switch', 0 , 10)
	create_boolAttr(individual_object, 'Indiv_Ctrls')
	create_floatAttr(individual_object, 'All_Curl', -10 , 10)
	create_floatAttr(individual_object, 'All_Spread', -10 , 10)
	
	
	create_dropAttrs(individual_object, finger_dropAttrs)
	
	create_curlAttrs(individual_object, thumb_curlAttrs)
	create_curlAttrs(individual_object, index_curlAttrs)
	create_curlAttrs(individual_object, mid_curlAttrs)
	create_curlAttrs(individual_object, ring_curlAttrs)
	create_curlAttrs(individual_object, pinky_curlAttrs)
	
	create_spreadAttrs(individual_object, finger_spreadAttrs)

def create_dropAttrs(individual_object, attr_list):
    create_separatorAttr(individual_object, attr_list[0])
    create_floatAttr(individual_object, attr_list[1], -100 , 100)
    create_floatAttr(individual_object, attr_list[2], -100 , 100)

def create_curlAttrs(individual_object, attr_list):
    create_separatorAttr(individual_object, attr_list[0])
    create_floatAttr(individual_object, attr_list[1], -100 , 100)
    create_floatAttr(individual_object, attr_list[2], -100 , 100)
    create_floatAttr(individual_object, attr_list[3], -100 , 100)

def create_spreadAttrs(individual_object, attr_list):
    create_separatorAttr(individual_object, attr_list[0])
    create_floatAttr(individual_object, attr_list[1], -100 , 100)
    create_floatAttr(individual_object, attr_list[2], -100 , 100)
    create_floatAttr(individual_object, attr_list[3], -100 , 100)
    create_floatAttr(individual_object, attr_list[4], -100 , 100)
    create_floatAttr(individual_object, attr_list[5], -100 , 100)
    
def create_attr(*args):
    attr_value = attributeType_radioGrp.getSelect()
    name = attribute_nameField.getText()
    min_value = attribute_minField.getValue()
    max_value = attribute_maxField.getValue()

    selection = pm.ls(sl=True)

    for individual_object in selection:
	if attr_value == 1:
	    create_floatAttr(individual_object, name, min_value, max_value)
	    
	elif attr_value == 2:
	    create_intAttr(individual_object, name, min_value, max_value)

	elif attr_value == 3:
	    create_boolAttr(individual_object, name)
	    
	else:
	    create_separatorAttr(individual_object, attr_name)
	
    print "Custom attribute '" + name + "' has been added to selected objects."
     
def create_boolAttr(control, attr_name):
    pm.addAttr(control, ln=attr_name, at='bool', dv=1, k=True)
    # print 'boolAttr:'

def create_separatorAttr(control, attr_name):
    pm.addAttr(control, ln=attr_name, at='enum', en='----------------')
    pm.setAttr(control + '.' + attr_name, cb=True)

def create_floatAttr(control, attr_name, min_value, max_value):
    pm.addAttr(control, ln=attr_name, at='double', min=min_value, max=max_value, k=True)
    # print 'floatAttr'

def create_intAttr(control, attr_name, min_value, max_value):
    pm.addAttr(control, ln=attr_name, at='long', min=min_value, max=max_value, k=True)




finger_dropAttrs = ('Finger_Drops', 'Thumb_Drop', 'Pinky_Drop')
finger_spreadAttrs = ('Spreads', 'Thumb_Spread', 'Index_Spread', 'Middle_Spread', 'Ring_Spread', 'Pinky_Spread')
thumb_curlAttrs = ('Thumb_Curl', 'Thumb_Root', 'Thumb_Mid', 'Thumb_End')
index_curlAttrs = ('Index_Curl', 'Index_Root', 'Index_Mid', 'Index_End')
mid_curlAttrs = ('Mid_Curl', 'Mid_Root', 'Mid_Mid', 'Mid_End')
ring_curlAttrs = ('Ring_Curl', 'Ring_Root', 'Ring_Mid', 'Ring_End')
pinky_curlAttrs = ('Pinky_Curl', 'Pinky_Root', 'Pinky_Mid', 'Pinky_End')

toe_spreadAttrs = ('Spreads', 'Big_Spread', 'Index_Spread', 'Middle_Spread', 'Fourth_Spread', 'Pinky_Spread')
big_curlAttrs = ('Big_Curl', 'Big_Root', 'Big_Mid', 'Big_End')
fourth_curlAttrs = ('Fourth_Curl', 'Fourth_Root', 'Fourth_Mid', 'Fourth_End')

foot_raiseAttrs = ('Raises', 'Heel_Raise', 'Ball_Raise', 'Toe_Raise')

def windowResize(*args):
	if pm.window('ByrdRigs_Curve_Tool', q=1, exists=1):
		pm.window('ByrdRigs_Curve_Tool', e=1, wh=(240, 81), rtf=True)
