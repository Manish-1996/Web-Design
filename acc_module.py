import os
import pandas as pd
from pandas import DataFrame
csv_path = "/home/manish/Downloads/Exigent"
path_lst = []
for r,d,f in os.walk(csv_path):
	for i in f:
		path_lst.append(r + '/'+ i)
print(path_lst)
payment= {'Key name':[],
'Total correct': [],
'Total not correct':[],
'Total rows count':[],
'Accuracy':[]
}
for i in path_lst:
	df = pd.read_csv(i)
	# print(df)
	print("\n\n-------------------------------------------------\n\n")
	subsetDataFrame = df[df['Status'].isin(['yes', 'no'])]
	For_yes=subsetDataFrame['Status'] == 'yes'
	yesdf= subsetDataFrame[For_yes]
	# print(yesdf.head())
	yesdf['Status']
	yess=len(yesdf['Status'])
	# print(yess)
	Text=len(subsetDataFrame['text'])
	# print(Text)
	accu=(yess/Text)*100
	# print(accu)
	For_no=subsetDataFrame['Status'] == 'no'
	nodf= subsetDataFrame[For_no]
	len(nodf)
	noo=len(nodf)
	sum=(noo/Text)*100
	# print(sum)
	# payment= {'Key name':f,
	# 'Total correct': yess,
	# 'Total not correct':noo,
	# 'Total rows count':Text,
	# 'Accuracy':accu
	# }
	base = os.path.basename(i).split('.csv')

	payment['Key name'].append(base[0])
	payment['Total correct'].append(yess)
	payment['Total not correct'].append(noo)
	payment['Total rows count'].append(Text)
	payment['Accuracy'].append(accu)
	
pd.DataFrame(payment).to_csv('all in one.csv', index = False)