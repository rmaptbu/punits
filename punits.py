class punit(object):
	def __init__(self,coeff,unit=0):
		self.coeff=coeff
		if unit !=0:
			self.unit=unit
			self.import_config()
			self.unit_conversion()
		else: self.unit={}

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
		self.unit=self.unit.split(',') #split string into tokens
		unit_dict={}
		for token in self.unit:
			unit=re.match(r'\w*', token)
			exponent=re.search(r'\(([+-]?[0-9]+)\)',token)
			if not exponent: exponent = 1
			else: exponent = float(exponent.group(1))
			unit_dict[unit.group()]=exponent #fill dictionary with SI units and exponents
		self.unit=unit_dict

	def __eq__(self,other):
		if type(other)==punit:
			if self.coeff==other.coeff and self.unit==other.unit:
				return True
			else: return False
		else: raise ValueError("can only compare punit with punit")

	def __mul__(self,other):
		if type(other)!=punit:
			other=punit(other)
		result=punit(1)
		#define sets of units of input to add together the dictionaries
		first_units=set(self.unit.keys())
		second_units=set(other.unit.keys())
		all_units=first_units.union(second_units)
		common_units=first_units.intersection(second_units)
		for key in all_units:
			if key in common_units:
				result.unit[key]=self.unit[key]+other.unit[key]
			elif key in self.unit.keys():
				result.unit[key]=self.unit[key]
			elif key in other.unit.keys():
				result.unit[key]=other.unit[key]
		result.coeff=self.coeff*other.coeff
		return result
		
	def __add__(self,other):
		if type(other)!=punit:
			other=punit(other)
		if set(self.unit.keys()) == set(other.unit.keys()):
			result=self
			result.coeff=self.coeff+other.coeff
		else: raise ValueError("can not add different units together")
		return result
		
a=punit(2,'joules')
b=punit(3,'seconds')
print b.unit
print a*b