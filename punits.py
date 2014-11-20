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
		for unit_type in self.units_dict:
			for unit in self.units_dict[unit_type]:
				exact_match += self.unit == unit
				if exact_match:
					self.coeff*=self.units_dict[unit_type][unit]
					self.unit=unit_type
		if not exact_match:
			raise ValueError("Unit not found")
		
a=punit(1,'hour')
