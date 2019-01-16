#more PlaceHoldermd
import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

class Dataloader():
	"""docstring for Dataloader"""
	def __init__(self, train_data_file_name, test_data_file_name, nrows=None, local=False):
		# create path
		path = 1
		if local:
			app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
			print(app_path)
			if not train_data_file_name.endswith('.csv'): train_data_file_name += '.csv'
			self.train_data = os.path.join(app_path,'data',train_data_file_name)
			if not test_data_file_name.endswith('.csv'): test_data_file_name += '.csv'
			self.test_data = os.path.join(app_path,'data',test_data_file_name)
		else:
			self.train_data = train_data_file_name
			self.test_data = test_data_file_name
		self.df = self.load_data(nrows)


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
		return self.df


	def get_data_summary(self):
		s = 'Summary of Data\n\n'
		s += 'Index: \n' + str(self.df.index) + '\n\n'
		s += 'Columns: \n' + str(self.df.columns) + '\n\n'
		s += 'Description: \n' + str(self.df.describe()) + '\n\n'
		s += 'Histogram: \n' + ' ' + '\n\n'
		self.df.hist()
		s += 'dan test! histograms should be above, but they wont be!\n\n' 
		s += 'box plot time'
		sns.boxplot(x=self.df['os'])
		#sns.boxplot(x=self.df['channel'])
		#df[df['os']<400].hist(column='os',bins=100)
		#df1 = df[df['os'].isin([13,19])]
		#self.df.boxplot()

		print('Information about the category os\n\n')
		print('Let\'s look at all of the different operating systems in the os column using df[\'os\'].value_counts() ')
		self.df.value_counts()
		print('\n\nGreat, now let\'s look at the distribution of those counts ')
		sns.boxplot(x=self.df['os'].value_counts())
		print('\n\nWe see that there are two massive outliers. These must be the most popular operating systems.')
		return s

	def get_data_spread_counts(self):
		df = self.df
		print('The dataframe has the following columns\n\n')
		print(df.columns)
		print('\n\n'+'Here are the plots for each feature')
		for i, col in enumerate(df.columns):
			#print('Summary stats for ',col)
			plt.figure(i*2)
			sns.boxplot(x=df[col].value_counts()).set_title('spread of '+ str(col))
			plt.figure(i*2+1)
			sns.countplot(x=df[col].value_counts()).set_title('counts of ' + str(col))
		return 1

	def test2(self):
		self.load_data()
		print(get_data_spread_counts())
        #print(self.get_data_summary())
		#print(self.df.hist())
       
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
	my_dataloader = Dataloader(train_csv_name , test_csv_name, local=True)
	my_dataloader.test1()

	# wu's shoes
	# zoo for shoes
	# sneaker heaven
	# girl got sole
	# 