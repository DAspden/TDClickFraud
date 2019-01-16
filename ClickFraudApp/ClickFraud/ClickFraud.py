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
		self.df = pd.read_csv(self.train_data, nrows=nrows)

	def get_data_summary(self):
		print('Summary of Data')


	def test(self):
		print(self.train_data)
		print(self.test_data)
		self.load_data(10)
		print(self.df.head(20))
		print(self)

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

if __name__ == '__main__': 
	print('Hello, welcome to the Dataloader for this project. This program requires that the test and training data be in unzipped csv format.')
	test_csv_name = 'test_test.csv'
	train_csv_name ='train_sample.csv'
	my_dataloader = Dataloader(train_csv_name , test_csv_name)
	my_dataloader.test()

	# wu's shoes
	# zoo for shoes
	# sneaker heaven
	# girl got sole
	# 