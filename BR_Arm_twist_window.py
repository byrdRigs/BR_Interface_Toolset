'''
Arm Twist Setup
'''
import pymel.core as pm

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
	if pm.window('Arm_twist_window', q=1, exists=1):
		pm.deleteUI('Arm_twist_window')
		#Arm_twist_window
		

	win_width = 450
	window_object = pm.window('Arm_twist_window', title="Arm_twist_window", w=win_width, bgc=window_bgc, mxb=False)
	main_layout = pm.columnLayout()

	pm.frameLayout(label='Step 1', bgc=(color_1), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Select the arm bind', w=win_width)
	pm.button(label='Twist Start', w=win_width, c=twistStartCreation)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 2', bgc=(color_2), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Split "01_twist" into 4', w=win_width, h=20)
	pm.text(label='"01_twist" = start joint, after you change the qty to 4, hit Create Interface. Split the joints evenly and make the split1_JNT 0.000. When joints are even hit Split Joints', w=win_width, ww=True)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 3', bgc=(color_3), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Select the "01_twist"', w=win_width, h=20)
	pm.button(label='Mid Creation', w=win_width, c=twistMidCreation)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 4', bgc=(color_4), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Split "06_twist" into 4', w=win_width, h=20)
	pm.text(label='Repeat the splitting process with "06_twist" being the start joint and split1_JNT being 0.000', w=win_width, ww=True)
	pm.button(label='End Creation', w=win_width, c=twistEndCreation)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 5', bgc=(color_5), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Select the "06_twist"', w=win_width, h=20)
	pm.button(label='Twist Rename', w=win_width, c=twistResult)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 6', bgc=(color_6), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Select "01_twist"', w=win_width, h=20)
	pm.button(label='Upper arm twist', w=win_width, c=firstSplineIk)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 7', bgc=(color_7), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Step 7: Select "06_twist"', w=win_width, h=20)
	pm.button(label='Forearm Twist', w=win_width, c=secondSplineIk)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 8', bgc=(color_8), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Select "02_twistBind", "03_twistBind", and "02_twistCrv"', w=win_width, ww=True)
	pm.button(label='Curve Binding', w=win_width, c=bind)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 9', bgc=(color_9), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Group all of the new curves, joints, and ikHandles.', w=win_width, ww=True)
	pm.text(label="Name the group based on the arm's orientation with twist_grp being the suffix", w=win_width, ww=True)
	pm.setParent(main_layout)
	pm.frameLayout(label='Step 10', bgc=(color_10), w=win_width, cl=True, cll=True, cc=windowResize)
	pm.text(label='Finish setting up the advanced twist settings', w=win_width, ww=True)
	pm.text(label='Input the "01_twistBind" into World UP Object on the "01_twist_ikh", and the "02_twistBind" into World Up Object 2. Then input "02_twistBind" into World Up Object on the "02_twist_ikh" and the "03_twistBind" into the World Up Object 2', w=win_width, ww=True)
	pm.setParent(main_layout)
	pm.window('Arm_twist_window', e=1, wh=(450, 110), rtf=True)
	pm.showWindow(window_object)
	print('Window Created:', window_object)



def twistStartCreation(*args):
	import armSetup
	reload (armSetup)
	armSetup.twistStartCreation()

def twistMidCreation(*args):
	import armSetup
	reload (armSetup)
	armSetup.twistMidCreation()	

def twistEndCreation(*args):
	import armSetup
	reload (armSetup)
	armSetup.twistEndCreation()

def twistResult(*args):
	import armSetup
	reload (armSetup)
	armSetup.twistResult()

def firstSplineIk(*args):
	import armSetup
	reload (armSetup)
	armSetup.firstSplineIk()

def secondSplineIk(*args):
	import armSetup
	reload (armSetup)
	armSetup.secondSplineIk()

def bind(*args):
	import armSetup
	reload (armSetup)
	armSetup.bind()

def windowResize(*args):
	if pm.window('Arm_twist_window', q=1, exists=1):
		pm.window('Arm_twist_window', e=1, wh=(450, 110), rtf=True)
	