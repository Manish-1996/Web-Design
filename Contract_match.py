import pandas as pd 
import numpy as np 
import os
import filecmp
import shutil
file_names = []
folder_path= "/home/manish/40"
#destination = '/home/manish/Desktop/Manish'
directory = "Extracted Contract"
parent_dir = '/home/manish/Desktop/'
path = os.path.join(parent_dir, directory) 
os.mkdir(path)
print("Directory '% s' created" % directory)

df=pd.read_csv('/home/manish/Downloads/Contracts.csv')
# print(df)
df.head

X=df['Contract ID']
Y=df['Unique Contracts'].tolist()
Z=df['File Name']
# print(Y)
Unique_contract= [x for x in Y if str(x) != 'nan']
for i in Unique_contract :
    new_file=df.loc[df['Contract ID'] == i][:1]['File Name'].tolist()[0]
    file_names.append(new_file)
      

for r, d,f in os.walk(folder_path):
	for i in f:
		if ".pdf" in i:
			for file in file_names:
				if file == i:
					 print(i)
					 shutil.copy(r+'/'+i, path)
