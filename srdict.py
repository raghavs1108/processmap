
from tdict import TDict 

class SRDict:
	def __init__ (self, strainRate =  None, tdict = None) :
		self.dictionary = dict();
		if strainRate:
			self.dictionary[strainRate] = tdict;

	def insert(self, strainRate, tdict) :
		try:
			self.dictionary[strainRate] = tdict;
		except KeyError, e:
			print ("No such Strain Rate.")
		else:
			pass
		finally:
			pass


	def delete(self, strainRate) :
		try:
			del(self.dictionary[strainRate]);
		except KeyError, e:
			print ("No such Strain Rate.")
		else:
			pass
		finally:
			pass
		

	def stressVal(self, strainRate, temperature):
		try:
			return  self.dictionary[strainRate].stressVal(temperature);
		except KeyError, e:
			print ("No such Strain Rate or temperature.")
		else:
			pass
		finally:
			pass

	def temperatureArray (self, strainRate) :
		try:
			return self.dictionary[strainRate]
		except KeyError, e:
			print("No such Strain Rate.");
		else:
			pass
		finally:
			pass


if __name__ == '__main__' :
	
	d = TDict(200, 50);
	d.insert(500, 100)
	
	k = SRDict();
	k.insert(12, d);
	print k.stressVal(12, 200);