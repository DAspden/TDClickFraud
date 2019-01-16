#more PlaceHoldermd
import os
import pandas as pd

class Dataloader(object):
	"""docstring for Dataloader"""
	def __init__(self, train_data_file_name, test_data_file_name):
		# create path
		app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
		# print(app_path)
		if not train_data_file_name.endswith('.csv'): train_data_file_name += '.csv'
		self.train_data = os.path.join(app_path,'data',train_data_file_name)
		if not test_data_file_name.endswith('.csv'): test_data_file_name += '.csv'
		self.test_data = os.path.join(app_path,'data',test_data_file_name)

	
	def load_data(self,nrows):
		self.df = pd.read_csv(self.test_data, nrows=nrows)

	def test(self):
		print(self.train_data)
		print(self.test_data)
		self.load_data(10)
		print(self.df.head(20))

if __name__ == '__main__': 
	print('Hello, welcome to the Dataloader for this project. This program requires that the test and training data be in unzipped csv format.')
	test_csv_name = 'test.csv'
	train_csv_name ='train.csv'
	my_dataloader = Dataloader(train_csv_name , test_csv_name)
	my_dataloader.test()


	# wu's shoes
	# zoo for shoes
	# sneaker heaven
	# girl got sole
	# 