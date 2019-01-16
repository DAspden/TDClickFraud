#more PlaceHoldermd
import os
import pandas as pd
import matplotlib

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



	def __repr__(self):
			s = '''Data fields\nEach row of the training data contains a click record, with the following features.
ip: ip address of click.
app: app id for marketing.\ndevice: device type id of user mobile phone (e.g., iphone 6 plus, iphone 7, huawei mate 7, etc.)
os: os version id of user mobile phone\nchannel: channel id of mobile ad publisher\nclick_time: timestamp of click (UTC)
attributed_time: if user download the app for after clicking an ad, this is the time of the app download
is_attributed: the target that is to be predicted, indicating the app was downloaded\nNote that ip, app, device, os, and channel are encoded.
The test data is similar, with the following differences:\nclick_id: reference for making predictions
is_attributed: not included'''
			return s

	# nrows is an optional argument, it is initially none, which would have read_csv operate as if no argument was passed
	def load_data(self,nrows=None):
		self.df = pd.read_csv(self.train_data, nrows=nrows)

	def get_data_summary(self):
		s = 'Summary of Data\n\n'
		s += 'Index: \n' + str(self.df.index) + '\n\n'
		s += 'Columns: \n' + str(self.df.columns) + '\n\n'
		s += 'Description: \n' + str(self.df.describe())

		self.df['app']
		return s

	def test2(self):
		self.load_data()
		print(self.get_data_summary())
		print(self.df.hist())
	def test1(self):
		print(self.train_data)
		print(self.test_data)
		self.load_data(10)
		print(self.df.head(20))
		print(self)


if __name__ == '__main__': 
	print('Hello, welcome to the Dataloader for this project. This program requires that the test and training data be in unzipped csv format.\n\n')
	test_csv_name = 'test_test.csv'
	train_csv_name ='train_sample.csv'
	my_dataloader = Dataloader(train_csv_name , test_csv_name)
	my_dataloader.test2()

	# wu's shoes
	# zoo for shoes
	# sneaker heaven
	# girl got sole
	# 