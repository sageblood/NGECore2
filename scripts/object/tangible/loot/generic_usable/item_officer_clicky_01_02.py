import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'object/usable')
	object.setStfFilename('static_item_n')
	object.setStfName('item_officer_clicky_01_02')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_officer_clicky_01_02')
	object.setIntAttribute('no_trade', 1)
	object.setStringAttribute('class_required', 'Officer')
	return

def use(core, actor, object):
	core.buffService.addBuffToCreature(actor, 'roadmapOfficerClicky', actor)
	return
