def split(*args):	
	import pymel.core as pm
	if pm.window('beJsWindow', exists=1):
		pm.deleteUI('beJsWindow')
		"""This file downloaded from Highend3d.com
		'  
		'  Highend3d.com File Information:
		'  
		'    Script Name: Joint Splitter
		'    Author:  
		'    Last Updated: Mar 13, 2007
		'    Update/Change this file at:
		'    http://Highend3d.com/maya/downloads/mel_scripts/character/3711.html
		'  
		'  Please do not alter any information above this line
		'  it is generated dynamically by Highend3d.com and will
		'  be changed automatically on any updates.
		"""
		"""***************************************************************************
		Name: Smart JointSpit
		Version: 1.0.1
		Purpose: Adds additional joint between a joint chain. Joint Quanity slider
		        allows between 1-10 joints. Fieled limit is 50. The joints can be
		        splitted with and without an interface. The interface allows
		        joints to be positioned using sliders. Source to run.
		Issues: Undo while interface is open is not supported. Solution is reload
		        start joint and re-create interface.
		History: 
		Version 1.0.1 March 13, 2007: Adjusted script to work in 8.5
		Version 1.0 Aug 30, 2005
		Created by: Brian Escribano
		Contact: brian@meljunky.com
		Visit: meljunky.com
		
		****************************************************************************"""
		
	pm.window('beJsWindow', t="Joint Splitter")
	pm.columnLayout()
	pm.rowColumnLayout('beJsRCL', nr=6, rh=[(1, 18), (3, 40), (5, 20), (6, 100)])
	pm.radioButtonGrp('beJsParentRBG', nrb=2, la2=("Auto-Parent", "Independent"), sl=1)
	pm.button(c=lambda *args: pm.mel.beJsSelStartJnt(), l="Select Start Joint")
	pm.rowColumnLayout(nc=2, cw=[(1, 115), (2, 115)])
	pm.text("            Start Joint")
	pm.text("             End Joint")
	pm.textField('beJsStartJnt', ed=0)
	pm.textField('beJsEndJnt', ed=0)
	pm.setParent('..')
	pm.intSliderGrp('beJsJntQty', fieldMinValue=1, 
		cw3=(49, 25, 20), 
		fieldMaxValue=50, maxValue=10, value=1, minValue=1, 
		field=True, label=" Jnt Qty:", cl3=("left", "left", "left"))
	pm.frameLayout('beJsSplitJntFL', cll=1, en=1, cl=1, 
		cc=lambda *args: [pm.rowColumnLayout('beJsRCL', rh=(5, 20), e=1), pm.window('beJsWindow', e=1, wh=(245, 190))], 
		h=200, l="Joint Slider Control", 
		ec=lambda *args: [pm.rowColumnLayout('beJsRCL', rh=(5, 120), e=1), pm.window('beJsWindow', e=1, wh=(245, 290))], 
		fn="plainLabelFont")
	pm.scrollLayout('beJsSplitJntSL', h=200, horizontalScrollBarThickness=0)
	pm.columnLayout('beJsSplitJntCL', h=200, columnAttach=("left", 5))
	#Sliders Created Here
	pm.setParent('..')
	pm.setParent('..')
	pm.setParent('..')
	pm.rowColumnLayout(nc=2, cw=[(1, 115), (2, 115)])
	pm.button('beJsBN', c=lambda *args: pm.mel.beJsBeginSplit(1), en=0, l="Split Joints")
	pm.button('beJsCiBN', c=lambda *args: pm.mel.beJsBeginSplit(2), en=0, l="Create Interface")
	#These fields are hidden from the viewer used to pass arrays through buttom command
	pm.textScrollList('beJsJntListTSL', h=50, vis=0)
	pm.setParent('..')
	pm.setParent('..')
	pm.setParent('..')
	pm.scriptJob(uid=('beJsWindow', 'beJsRemoveNodes'))
	pm.window('beJsWindow', e=1, wh=(245, 190))
	pm.showWindow('beJsWindow')

	def beJsBeginSplit(type):
		
		pm.button('beJsBN', c=lambda *args: pm.mel.beJsBeginSplit(1), e=1)
		pm.mel.beJsRemoveNodes()
		error=0
		start=str(pm.textField('beJsStartJnt', q=1, tx=1))
		end=str(pm.textField('beJsEndJnt', q=1, tx=1))
		if start == "":
			pm.pm.mel.error("Please select start joint.")
			error=1
			
		
		else:
			child=pm.listRelatives(start)
			if end != child[0]:
				pm.pm.mel.error(end + " is no longer child of " + start + ". Please select start joint.")
				error=1
				
			if end == "":
				pm.pm.mel.error("No end joint selected")
				error=1
				
			if error == 0:
				if type == 1:
					pm.mel.beJsCreateJoints()
					
				
				else:
					pm.mel.beJsCreateInterface()
					
				
			
		


	def beJsSelStartJnt():
		"""end proc
		urpose: Populates Start joint and End Joint Field"""
		

		child = []
		sel=pm.ls(type='joint', sl=1)
		if sel[0] == "":
			pm.pm.mel.error("Please select start joint.")
			
		
		else:
			child=pm.listRelatives(sel[0], type='joint')
			if pm.nodeType(child[0]) == "joint":
				pm.textField('beJsStartJnt', e=1, tx=sel[0])
				pm.textField('beJsEndJnt', e=1, tx=child[0])
				pm.button('beJsCiBN', en=1, e=1)
				pm.button('beJsBN', en=1, e=1)
				
			
			else:
				pm.pm.mel.error("Child of start joint is not a joint")
				
			
		


	def beJsCreateJoints():
		"""joint Spit Now"""
		

		locList = []
		jntList = []
		firstJnt = 0
		k = 0
		locList=pm.mel.beJsCreateLoc(1)
		#Creates Locators Only
		jntList=pm.mel.beJsAddJoints(locList)
		#Add Joints Only
		pm.mel.beJsParentJnt(jntList, pm.radioButtonGrp('beJsParentRBG', q=1, sl=1))
		#PArents Joints Only
		pm.mel.beJsCleanUp()
		#Cleans up nodes
		


	def beJsCreateInterface():
		"""end proc
		ater"""
		

		locList = []
		jntList = []
		attrName = []
		textName = []
		locList=pm.mel.beJsCreateLoc(2)
		#Creates Locators Only
		jntList=pm.mel.beJsAddJoints(locList)
		#Add Joints Only                                      
		textName=pm.columnLayout('beJsSplitJntCL', q=1, ca=1)
		#Name takes off "." need label name
		for i in range(0,len(textName)):
			attrName[i]=str(pm.text(textName[i], q=1, l=1))
			
		pm.deleteUI(textName)
		#Make room for sliders
		for i in range(0,len(locList)):
			pm.textScrollList('beJsJntListTSL', a=jntList[i], e=1)
			pm.mel.beJsCreateSlider(jntList[i], attrName[i])
			
		pm.frameLayout('beJsSplitJntFL', e=1, cl=0)
		pm.rowColumnLayout('beJsRCL', rh=(5, 120), e=1)
		pm.window('beJsWindow', e=1, wh=(245, 290))
		pm.button('beJsCiBN', en=0, e=1)
		pm.button('beJsBN', c=lambda *args: [pm.mel.beJsParentJnt(pm.textScrollList('beJsJntListTSL', q=1, ai=1), pm.radioButtonGrp('beJsParentRBG', q=1, sl=1)), pm.mel.beJsCleanUp()], e=1)
		


	def beJsCreateSlider(jntList, attrName):
		
		pm.setParent('beJsSplitJntCL')
		pm.attrFieldSliderGrp(pre=3, 
			min=0, max=1, l=jntList, 
			at=attrName, cal=[(1, 'left'), (2, 'left'), (3, 'left')], cw=[(1, 65), (2, 40), (3, 100)])
		


	def beJsParentJnt(jntList, type):
		
		if type == 1:
			start=str(pm.textField('beJsStartJnt', q=1, tx=1))
			end=str(pm.textField('beJsEndJnt', q=1, tx=1))
			firstJnt=len(jntList) - 1
			for i in range(1,len(jntList)):
				k=int(i - 1)
				pm.parent(jntList[k], jntList[i])
				
			pm.parent(jntList[firstJnt], start)
			pm.parent(end, jntList[0])
			
		
		else:
			for eval in jntList:
				pm.parent(eval, w=1)
				
			
		


	def beJsCreateLoc(type):
		"""end else
		oints have not been created"""
		

		qty=int(pm.intSliderGrp('beJsJntQty', q=1, v=1))
		start=str(pm.textField('beJsStartJnt', q=1, tx=1))
		end=str(pm.textField('beJsEndJnt', q=1, tx=1))
		i = 0.0
		sWeight = 0.0
		eWeight = 0.0
		pointName = []
		locList = []
		for i in range(float(1),qty+1):
			locName=pm.spaceLocator(p=(0, 0, 0), n=("beJsTempLoc" + str(i)))
			locList.append(str(locName[0]))
			pm.orientConstraint(start, locName, weight=1, offset=(0, 0, 0))
			sWeight=i / (qty + 1)
			eWeight=float(1 - sWeight)
			pointName=pm.pointConstraint(start, locName, weight=sWeight, offset=(0, 0, 0))
			pm.pointConstraint(end, locName, weight=eWeight, offset=(0, 0, 0))
			if type == 2:
				pm.mel.beCreateSubstractConnect(pointName[0], start, end)
				#create math connection
				
			
		return locList
		#end if
		#end for
		


	def beJsAddJoints(locList):
		"""end proc"""
		

		start=str(pm.textField('beJsStartJnt', q=1, tx=1))
		end=str(pm.textField('beJsEndJnt', q=1, tx=1))
		jntName = []
		jntTempName = []
		j = 0
		radius=float((pm.getAttr(start + ".radius") + pm.getAttr(end + ".radius")) / 2)
		pm.parent(end, w=1)
		#Jnt is dulpicated without parent
		for i in range(float(0),len(locList)):
			j=int(i + 1)
			jntTempName=pm.duplicate(start, n=("split" + str(j) + "_JNT"), rc=1)
			jntName[i]=jntTempName[0]
			pm.parent(jntName[i], locList[i])
			pm.setAttr((jntName[i] + ".translateX"), 
				0)
			pm.setAttr((jntName[i] + ".translateY"), 
				0)
			pm.setAttr((jntName[i] + ".translateZ"), 
				0)
			pm.setAttr((jntName[i] + ".jointOrientX"), 
				0)
			pm.setAttr((jntName[i] + ".jointOrientY"), 
				0)
			pm.setAttr((jntName[i] + ".jointOrientZ"), 
				0)
			
		pm.parent(end, start)
		#for
		return jntName
		


	def beCreateSubstractConnect(pointName, start, end):
		"""end proc"""
		

		minusNode = ""
		minusNode=str(pm.shadingNode('plusMinusAverage', asUtility=1, n=(pointName + "_beJsMinus")))
		pm.setAttr((minusNode + ".operation"), 
			2)
		pm.addAttr(minusNode, ln='startPoint', dv=1, at='double')
		pm.connectAttr((pointName + "." + start + "W0"), (minusNode + ".input1D[1]"), 
			f=1)
		pm.connectAttr((minusNode + ".startPoint"), (minusNode + ".input1D[0]"), 
			f=1)
		pm.connectAttr((minusNode + ".output1D"), (pointName + "." + end + "W1"), 
			f=1)
		pm.setParent('beJsSplitJntCL')
		pm.text((pointName + "." + start + "W0"), 
			l=(pointName + "." + start + "W0"))
		


	def beJsCleanUp():
		
		pm.rowColumnLayout('beJsRCL', rh=(5, 20), e=1)
		pm.window('beJsWindow', e=1, wh=(245, 190))
		pm.frameLayout('beJsSplitJntFL', e=1, cl=1)
		pm.textScrollList('beJsJntListTSL', e=1, ra=1)
		pm.mel.beJsRemoveNodes()
		pm.button('beJsBN', c=lambda *args: pm.mel.beJsBeginSplit(1), e=1)
		pm.button('beJsCiBN', en=1, e=1)
		


	def beJsRemoveNodes():
		
		if pm.columnLayout('beJsSplitJntCL', q=1, ex=1):
			delListUI=pm.columnLayout('beJsSplitJntCL', q=1, ca=1)
			#Deletes any sliders that are left over
			for delUI in delListUI:
				pm.deleteUI(delUI)
				
			
		delSubNode=pm.ls("beJsTempLoc*", type='plusMinusAverage')
		#Deletes any minus nodes that are left over
		for delSub in delSubNode:
			pm.delete(delSub)
			
		delLocNode=pm.ls("beJsTempLoc*", type='locator')
		#Deletes any locators that are left over 
		for delLoc in delLocNode:
			pm.delete(pm.listRelatives(delLoc, p=1, s=1))
			
		

