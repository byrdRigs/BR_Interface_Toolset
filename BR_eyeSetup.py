'''
Eye Setup

How to run:
import BR_Interface_Toolset.BR_eyeSetup as BR_eyeSetup
reload(BR_eyeSetup)
BR_eyeSetup.setup()
'''
import pymel.core as pm
def freezeTransform(*args):
	selection = pm.ls(sl=1, dag=1)
	pm.makeIdentity(selection, apply=True, t=1, r=1, s=1, n=0, pn=1)
	# print 'Transform Frozen'

def deleteHistory(*args):
	pm.delete(ch=1)
	# print 'History Deleted'

def setup(*args):
	selection = pm.ls(sl=1)
	lt_eye_joints = selection[0]
	rt_eye_joints = selection[1]
	head_joints=selection[2]
	print 'Selection:', selection
	print 'Lt eye joints:', lt_eye_joints
	print 'Rt eye joints:', rt_eye_joints
	print 'Head joints:', head_joints

	lt_eye = pm.ls(lt_eye_joints, sl=1, dag=1)
	lt_root = lt_eye[0]
	lt_joint_2 = lt_eye[1]
	print 'Lt eye:', lt_eye
	print 'Lt root:', lt_root
	print 'Lt joint 2:', lt_joint_2

	rt_eye = pm.ls(rt_eye_joints, sl=1, dag=1)
	rt_root = rt_eye[0]
	rt_joint_2  = rt_eye[1]
	print 'Rt eye:', rt_eye
	print 'Rt root:', rt_root
	print 'Rt joint 2:', rt_joint_2



	ct_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]

	rt_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]

	lt_icon = pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]

	icon_name = lt_root.replace('01_bind', 'icon')
	lt_icon.rename(icon_name)
	icon_name = rt_root.replace('01_bind', 'icon')
	rt_icon.rename(icon_name)
	icon_name = lt_icon.replace('lt', 'ct')
	ct_icon.rename(icon_name)

	ct_icon.sx.set(5.8)
	ct_icon.sy.set(5.8)
	ct_icon.sz.set(5.8)
	pm.select(ct_icon)
	freezeTransform()


	pm.select(ct_icon + '.cv[5]',
			  ct_icon + '.cv[1]')
	pm.cmds.scale(1, 1, 0.05, p=(0, 0, 0), r=1)

	ct_icon.overrideEnabled.set(1)
	ct_icon.overrideColor.set(17)
	rt_icon.overrideEnabled.set(1)
	rt_icon.overrideColor.set(13)
	lt_icon.overrideEnabled.set(1)
	lt_icon.overrideColor.set(6)

	lt_icon.tx.set(-3.5)

	rt_icon.tx.set(3.5)

	icon_scale = 2.03
	lt_icon.sx.set(icon_scale)
	lt_icon.sy.set(icon_scale)
	lt_icon.sz.set(icon_scale)


	rt_icon.sx.set(icon_scale)
	rt_icon.sy.set(icon_scale)
	rt_icon.sz.set(icon_scale)

	pm.parent(lt_icon, rt_icon, ct_icon)

	ct_icon.rx.set(90)
	pm.select(ct_icon)
	freezeTransform()
	pm.addAttr(ct_icon, ln="followHead", at='bool')
	ct_icon.followHead.set(e=1, keyable=1)

	temp_constraint = pm.pointConstraint(lt_eye, ct_icon, skip=['x', 'z'], w=1, mo=0)
	pm.delete(temp_constraint)
	ct_icon.tz.set(20)

	temp_constraint = pm.pointConstraint(lt_root, lt_icon, skip=['y', 'z'], w=1, mo=0)
	pm.delete(temp_constraint)

	temp_constraint = pm.pointConstraint(rt_root, rt_icon, skip=['y', 'z'], w=1, mo=0)
	pm.delete(temp_constraint)

	pm.select(ct_icon)
	freezeTransform()

	pm.aimConstraint(lt_icon, lt_root, w=1, upVector=(0, 1, 0), worldUpType="vector", mo=0, aimVector=(1, 0, 0), worldUpVector=(0, 1, 0))

	pm.aimConstraint(rt_icon, rt_root, w=1, upVector=(0, 1, 0), worldUpType="vector", mo=0, aimVector=(1, 0, 0), worldUpVector=(0, 1, 0))


	icon_pad = pm.group(empty=1)
	temp_constraint = pm.parentConstraint(ct_icon, icon_pad, mo=0)
	pm.delete(temp_constraint)
	pm.select(icon_pad)
	freezeTransform()

	pad_name = ct_icon.replace('icon', 'local')
	icon_pad.rename(pad_name)

	pm.parent(ct_icon, icon_pad)

	follow_const = pm.parentConstraint(head_joints, icon_pad, mo=1, w=0)
	print 'Follow constraint:', follow_const
	const_targets = follow_const.getWeightAliasList()[0]

	pm.setDrivenKeyframe(const_targets, currentDriver=ct_icon + '.followHead')
	ct_icon.followHead.set(1)
	const_targets.set(1)
	pm.setDrivenKeyframe(const_targets, currentDriver=ct_icon + '.followHead')
	ct_icon.followHead.set(0)


	pm.parent(lt_root, rt_root, head_joints)
	pm.select(icon_pad)
	deleteHistory()


