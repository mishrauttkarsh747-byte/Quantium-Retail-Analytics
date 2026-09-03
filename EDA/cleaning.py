import pandas as pd
import numpy as np
import seaborn as sns

transaction_data = pd.read_excel(
    r"C:\Users\lenovo\Desktop\quantrium projet\QVI_transaction_data.xlsx"
)

print(transaction_data.head(10))
customer_data= pd.read_csv(r"C:\Users\lenovo\Downloads\QVI_purchase_behaviour.csv")
print(customer_data.head(10))
print(customer_data.head(2))
print(transaction_data.describe())
print(transaction_data.isnull().sum())
data_type=transaction_data.dtypes
print(data_type)
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.displot(transaction_data["TOT_SALES"], kde=True)
plt.show()
numericdata =transaction_data.select_dtypes(['float','int'])
print(numericdata.head())
x= numericdata[numericdata['TOT_SALES']<8.000]
sns.displot(x.TOT_SALES,kde=True)
plt.show()
sns.boxplot(x.TOT_SALES)
plt.show()