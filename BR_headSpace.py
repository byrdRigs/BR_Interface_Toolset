'''
Head space window
'''

'''
How to run:
import BR_Interface_Toolset.BR_headSpace as BR_headSpace
reload(BR_headSpace)
BR_headSpace.gui()
'''

import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel

tab_bgc=(0.4718592, 0.13568, 239)
subTab_bgc = (0.4915200, 0.32256, 241)
window_bgc = (.2,.2,.2)


def gui():
	if pm.window('ByrdRigs_Head_Space', q=1, exists=1):
		pm.deleteUI('ByrdRigs_Head_Space')
		#ByrdRigs_Head_Space

	win_width = 240
	window_object = pm.window('ByrdRigs_Head_Space', title="ByrdRigs_Head_Space", w=win_width, bgc=window_bgc)
	main_layout = pm.columnLayout()

	pm.rowColumnLayout(nc=2, cw=(125,125))
	head_bind = pm.button(label='Head bind joint', c=headBindSelection)


	# pm.text(label='Select the head_01_bind, neck_04_waste, and headNeck_space_loc', w=win_width, ww=1)
	pm.button(label='Neck Space', w=win_width, c=neckSpace)


	pm.window('ByrdRigs_Head_Space', e=1, wh=(240, 110), rtf=1)
	pm.showWindow(window_object)


def freezeTransform(*args):
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
	# print 'Transform Frozen'


def deleteHistory(*args):
	pm.delete(ch=True)
	# print 'History Deleted'


def headBindSelection(*args):
	'''
	head_bind_input = cmds.promptDialog(
						title='Head Bind Joint',
						message=('Enter the name of the first head joint'),
						button=('Enter', 'Cancel'),
						defaultButton='Enter',
						cancelButton='Cancel',
						dismissString='Cancel')

	if head_bind_input == 'Enter':
		head_bind = cmds.promptDialog(q=1, text=1)
	'''
	head_bind = 'ct_head_01_bind'
	print 'Head bind joint:', head_bind
	pm.select(head_bind)
	head_joints = pm.ls(sl=1, dag=1)
	print 'Head joints:', head_joints
	'''
	else:
		pm.warning('The head bind joint is needed to continue')
	'''


	'''
	headNeck_loc_input = cmds.promptDialog(
						title='Enter the Neck Space Locator',
						message=('i.e "ct_headNeck_space_loc"'),
						button=('Enter', 'Cancel'),
						defaultButton='Enter',
						cancelButton='Cancel',
						dismissString='Cancel')

	if headNeck_loc_input == 'Enter':
		neck_loc = cmds.promptDialog(q=1, text=1)
	'''
	
	neck_loc = 'ct_headNeck_space_loc'
	pm.select(neck_loc)
	neck_loc = pm.ls(sl=1)
	print 'Neck Space Locator:', neck_loc
	
	'''
	else:
		pm.warning('The neck locator is needed to continue')
	'''



	'''
	headBody_loc_input = cmds.promptDialog(
						title='Enter the Body Space Locator',
						message=('i.e "ct_headBody_space_loc"'),
						button=('Enter', 'Cancel'),
						defaultButton='Enter',
						cancelButton='Cancel',
						dismissString='Cancel')

	if headBody_loc_input == 'Enter':
		back_loc = cmds.promptDialog(q=1, text=1)
	'''
	
	back_loc = 'ct_headBody_space_loc'
	pm.select(back_loc)
	back_loc = pm.ls(sl=1)
	print 'Body Space Locator:', back_loc
	
	'''
	else:
		pm.warning('The body locator is needed to continue')
	'''


	'''
	root_loc_input = cmds.promptDialog(
						title='Enter the Root Space Locator',
						message=('i.e "ct_root_space_loc"'),
						button=('Enter', 'Cancel'),
						defaultButton='Enter',
						cancelButton='Cancel',
						dismissString='Cancel')

	if root_loc_input == 'Enter':
		root_loc = cmds.promptDialog(q=1, text=1)
	'''
	
	root_loc = 'ct_root_space_loc'
	pm.select(root_loc)
	root_loc = pm.ls(sl=1)
	print 'Root Space Locator:', root_loc
	
	'''
	else:
		pm.warning('The root locator is needed to continue')
	'''



	'''
	hip_loc_input = cmds.promptDialog(
						title='Enter the Hips Space Locator',
						message=('i.e "ct_hip_space_loc"'),
						button=('Enter', 'Cancel'),
						defaultButton='Enter',
						cancelButton='Cancel',
						dismissString='Cancel')

	if hp_loc_input == 'Enter':
		hip_loc = cmds.promptDialog(q=1, text=1)
	'''
	
	hip_loc = 'ct_hip_space_loc'
	pm.select(hip_loc)
	root_loc = pm.ls(sl=1)
	print 'Hip Space Locator:', hip_loc
	
	'''
	else:
		pm.warning('The hip locator is needed to continue')
	'''


	'''
	lt_shoulder_loc_input = cmds.promptDialog(
						title='Enter the left shoulder Space Locator',
						message=('i.e "lt_shoulder_space_loc"'),
						button=('Enter', 'Cancel'),
						defaultButton='Enter',
						cancelButton='Cancel',
						dismissString='Cancel')

	if lt_shoulder_loc_input == 'Enter':
		shoulder_loc = cmds.promptDialog(q=1, text=1)
	'''
	
	lt_shoulder_loc = 'lt_shoulder_space_loc'
	pm.select(lt_shoulder_loc)
	lt_shoulder_loc = pm.ls(sl=1)
	print 'Left Shoulder Space Locator:', lt_shoulder_loc
	
	'''
	else:
		pm.warning('The left shoulder locator is needed to continue')
	'''

	'''
	rt_shoulder_loc_input = cmds.promptDialog(
						title='Enter the right shoulder Space Locator',
						message=('i.e "rt_shoulder_space_loc"'),
						button=('Enter', 'Cancel'),
						defaultButton='Enter',
						cancelButton='Cancel',
						dismissString='Cancel')

	if rt_shoulder_loc_input == 'Enter':
		shoulder_loc = cmds.promptDialog(q=1, text=1)
	'''
	
	rt_shoulder_loc = 'rt_shoulder_space_loc'
	pm.select(rt_shoulder_loc)
	rt_shoulder_loc = pm.ls(sl=1)
	print 'Right Shoulder Space Locator:', rt_shoulder_loc
	
	'''
	else:
		pm.warning('The right shoulder locator is needed to continue')
	'''

	'''
	pad_input = cmds.promptDialog(
						title='Enter the head pad',
						message=('i.e "ct_head_00_pad'),
						button=('Enter', 'Cancel'),
						defaultButton='Enter',
						cancelButton='Cancel',
						dismissString='Cancel')

	if pad_input == 'Enter':
		head_pad = cmds.promptDialog(q=1, text=1)
	'''
	
	head_pad = 'ct_head_00_pad'
	pm.select(head_pad)
	head_pad = pm.ls(sl=1)
	print 'Head Pad:', head_pad
	
	'''
	else:
		pm.warning('The head pad is needed to continue')
	'''

	pm.orientConstraint(neck_loc, back_loc, hip_loc, root_loc, head_pad, mo=1)


def neckSpace(*args):
	'''
	Head bind and neck loc selection
	'''
	print 'hi'

	# selection = pm.ls(sl=1, dag=1)
	# root_joint = selection[0]
	# joint_2 = selection[1]
	# neck_waste = selection[2]
	# neck_loc = selection[3]
	# # print 'Selection:', selection
	# # print 'Root Joint:', root_joint
	# # print '2nd Joint:', joint_2
	# # print 'Neck Waste:', neck_waste
	# # print 'Neck Loc:', neck_loc

	# pm.parent(neck_loc, neck_waste)

	