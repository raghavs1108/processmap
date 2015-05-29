'''

accept input in any format
convert it into the dictionary:

DICT (strain, DICT(strainRate, DICT(temperature, stress) ) )

'''

'''
Create APIs to create new dictionaries at the last two levels that allow for easy insertions and easy deletions.
'''

class TDict:
	def __init__ (self, temperature =  None, stress = None) :
		self.dictionary = dict();
		if temperature:
			self.dictionary[temperature] = stress;

	def insert(self, temperature, stress) :
		try:
			self.dictionary[temperature] = stress;
		except KeyError, e:
			print ("No such temperature.")
		else:
			pass
		finally:
			pass


	def delete(self, temperature) :
		try:
			del(self.dictionary[temperature]);
		except KeyError, e:
			print ("No such temperature.")
		else:
			pass
		finally:
			pass
		

	def stressVal(self, temperature):
		try:
			return self.dictionary[temperature];
		except KeyError, e:
			print ("No such temperature.")
		else:
			pass
		finally:
			pass


if __name__ == '__main__' :
	
	d = TDict(200, 50);
	d.insert(500, 100)
	d.delete(500)
	print d.stressVal(500);