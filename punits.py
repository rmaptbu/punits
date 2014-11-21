class punit(object):
	def __init__(self,coeff,unit=0):
		self.coeff=coeff
		if unit !=0:
			self.unit=unit
			self.import_config()
			self.unit_conversion()
			
	def import_config(self):
		#import dictionary of prefixes and units
		import yaml
		self.prefixes_dict=yaml.load(open('config.yml'))['prefix']
		self.units_dict=yaml.load(open('config.yml'))['units']

	def unit_conversion(self):
		#scan for prefixes, adjust coefficient and remove prefix
		for key in self.prefixes_dict.keys():
			if key in self.unit:
				self.coeff*=self.prefixes_dict[key]
				self.unit=self.unit.replace(key,'')
				break
				
		#scan if unit is in unit dict, rename unit (SI) and adjust coefficient
		found_match=False
		for unit_type in self.units_dict:
			for unit in self.units_dict[unit_type]:
				if self.unit == unit:
					self.coeff*=self.units_dict[unit_type][unit]
					self.unit=unit_type
					found_match=True				
		if not found_match:
			raise ValueError("Unit not found")
			
		#transform string of self.unit into dictionary {SI:exponent}
		import re
		self.unit=self.unit.split(',')
		for token in self.unit:
			unit=re.match(r'\w*', token)
			exponent=re.search(r'[\(([+-]?[0-9]+)\)]?',token)
			print token
			if exponent:
				print unit.group(), 'abc', exponent.group(1)
			
	def __eq__(self,other):
		if type(other)==punit:
			if self.coeff==other.coeff and self.unit==other.unit:
				return True
			else: return False
		else: raise ValueError("can only compare punit with punit")
		
a=punit(1,'joule')
