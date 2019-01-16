from ClickFraud.ClickFraud import Dataloader

print('hello world')
_test = r'C:\Users\slin2\Documents\GitHub\TDClickFraud\data\test_test.csv'
_train = r'C:\Users\slin2\Documents\GitHub\TDClickFraud\data\train_sample.csv'
print(_train)

dl = Dataloader(_train, _test)
df = dl.load_data()
print('hi')
print(df.head())
dl.get_data_spread_counts()