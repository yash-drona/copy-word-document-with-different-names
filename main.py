import pandas as pd
import shutil

df = pd.read_csv('test.csv')

names_list = df['Name'].to_list()
print(names_list)

for fileName in names_list:
  new_fileName = fileName.replace('/', '-')
  destination = f'./output/{new_fileName}.docx'
  
  try:
    shutil.copy('test.docx', destination)
  except FileNotFoundError:
    print("File Not Found")
  
