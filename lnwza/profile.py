# profile.py

class Profile:
	'''
	Example:

	my = Profile('mane')
	my.show_name() 

	'''
	def __init__(self,name):
		self.name = name
		

	def show_name(self):
		print(self.name)



if __name__ == '__main__':
	my = Profile('mane')



