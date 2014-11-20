class punit(object):
	def __init__(self,coeff,unit=0):
		self.coeff=coeff
		self.import_config()
		if unit !=0:
			self.unit=unit
			self.unit_conversion()
			
	def import_config(self):
		#import dictionary of prefixes and units
		import yaml
		self.prefixes_dict=yaml.load(open('config.yml'))['prefix']
		self.units_dict=yaml.load(open('config.yml'))['units']

	def unit_conversion(self):
		import re
		for unit_type in self.units_dict:
			for unit in self.units_dict[unit_type]:
				match=re.search(self.unit, unit)
				print match, unit, unit_type
		
a=punit(1,'meter')
