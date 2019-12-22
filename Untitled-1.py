import pandas as pd
import csv
#url = "https://www.nseindia.com/archives/equities/mto/MTO_18122019.DAT"
#url = "https://www.nseindia.com/archives/equities/mto/MTO_17122019.DAT"
#print(url)
filepath=r"D:\nse\NSEdaily\New folder\Chrome_MTO_17122019DAT.csv"
df = pd.read_csv(filepath)
for i in df.index:
 name=df['Name of Security'][i]+".csv"
 with open(name,'w') as csvfile:
    fieldnames = ['Record Type', 'Quantity Traded']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([{'Record Type': df['Record Type'][i],'Quantity Traded':df['Quantity Traded'][i]}])
     
print("Writing complete")
