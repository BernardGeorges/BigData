import pandas as pd

# Read the data from the CSV files
ds1 = pd.read_excel('efeito_estufa.xlsx')
ds2 = pd.read_excel('emissoes_gases.xlsx')
ds3 = pd.read_excel('intensidade_carbonica.xlsx')
ds4 = pd.read_excel('PIBcrescimento.xlsx')
ds5 = pd.read_excel('PIBdespesas.xlsx')
ds6 = pd.read_excel('PIBproducao.xlsx')
ds7 = pd.read_excel('PIBrendimento.xlsx')

# Merge the data
dsAmbiente = pd.merge(pd.merge(ds1, ds2, on='Anos'), ds3, on='Anos')
dsPIB = pd.merge(pd.merge(ds4, ds5, on='Anos'), pd.merge(ds6, ds7, on='Anos'), on='Anos')

# verify joined datasets
dsPIB.dropna(inplace=True)
# drop repeated columns total, total_x and total_y are all the same values
dsPIB.drop(columns=['Total_x', 'Total_y'], inplace=True)

dsAmbiente.dropna(inplace=True)

ds = pd.merge(dsAmbiente, dsPIB, on='Anos')
print(ds.head())