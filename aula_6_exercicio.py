# Import Pandas and CSVs
import pandas as pd
dim_cliente = pd.read_csv("/content/dim_cliente.csv")
dim_hub = pd.read_csv("/content/dim_hub.csv")
dim_produto = pd.read_csv("/content/dim_produto.csv")
dim_tempo = pd.read_csv("/content/dim_tempo.csv")
fac_venda = pd.read_csv("/content/fato_envios.csv")

# Data Understanding
'''.describe() dataframes to check data info'''
dim_cliente.describe()
dim_hub.describe()
dim_produto.describe()
dim_tempo.describe()
fac_venda.describe()
 '''.info() dataframes to check data types'''
dim_cliente.info()
dim_hub.info()
dim_produto.info()
dim_tempo.info()
fac_venda.info()
 '''.head() to quickly visualize data'''
dim_cliente.head(10)
dim_hub.head(10)
dim_produto.head(10)
dim_tempo.head(10)
fac_venda.head(10)

# Exercise 1 - Total amount sent per hub
 # Merge 'fac_venda' and 'dim_hub' to link 'hub_id' and 'hub_nome'
info_hub_produto=pd.merge(fac_venda,dim_hub,how='inner',on='hub_id')
 # Groupby 'hub' and 'quantidade', identifying total sum
info_total = info_hub_produto.groupby(["hub_id", "hub_nome"])["quantidade"].sum().reset_index().sort_values("quantidade", ascending=False)
info_total.head(10)

# Exercise 2 - Which product (or category) had the highest total volume shipped?
 # Merge 'dim_produto' and 'fac_venda' to link product and sales info
info_produto_peso=pd.merge(fac_venda,dim_produto, how="inner", on="produto_id")
 # Identify Total Weight
info_produto_peso['peso_total']= info_produto_peso["peso_medio_kg"]*info_produto_peso["quantidade"]
 # Groupby product info and total weight - 'peso_total'
produto_mais_vendido = info_produto_peso.groupby(['produto_id', 'produto', 'categoria'])['peso_total'].sum().reset_index().sort_values("peso_total", ascending=False)
 # Identify Max value
produto_mais_vendido.max()

# Exercise 3 - Average shipping time by product category
 # Merge 'fac_venda' and 'dim_produto' to link product info 'categoria' and sales info 'tempo_transporte_h'
product_avg = pd.merge(fac_venda, dim_produto, how="left", on="produto_id")
 # Groupby product info and 'categoria', identifying average lead time of transport 'tempo_transporte_h'
tempo_medio = product_avg.groupby(['produto_id','produto', 'categoria'])['tempo_transporte_h'].mean().reset_index().sort_values('tempo_transporte_h', ascending=False)
tempo_medio.head()

# Exercise 4 - Determine the total number of shipments made to customers: 'Grossistas' and 'Retalho'
 # Merge 'fac_vendas' and 'dim_cliente' to link relacionar 'envio_id' and 'cliente_id' with 'tipo_cliente'
tipo_cliente=pd.merge(fac_venda, dim_cliente, how="left", on="cliente_id")
 # Groupby 'tipo_cliente' and 'envio_id', identifying number of shipments made
envios_cliente= tipo_cliente.groupby("tipo_cliente")["envio_id"].count().reset_index().sort_values('envio_id', ascending=False)
envios_cliente.head()

# Exercise 5 - Find the hub with the highest average lead time - show the hub name and cost.
 # Merge 'fac_venda' and 'dim_hub' to link 'hub_nome' and 'tempo_transporte_h'
tempo_hub=pd.merge(fac_venda,dim_hub, how="left", on="hub_id")
 # Groupby produto, identifying average lead time of transport 'tempo_transporte_h'
hub_tempo_medio= tempo_hub.groupby('hub_nome')['tempo_transporte_h'].mean().reset_index()
 # Fetching max value
hub_tempo_medio.max()

# Exercise 6 - Perform 3 different merges between 'fato_envios' and 'dim_cliente' using: how="inner"; how="left"; how="outer"
 # Merge with how='inner'
merge=pd.merge(fac_venda, dim_cliente, how='inner', on='cliente_id')
merge.head(10)
 # Merge with how='left'
merge2=pd.merge(fac_venda, dim_cliente, how='left', on='cliente_id')
merge2.head(10)
 # Merge with how='outer'
merge3=pd.merge(fac_venda, dim_cliente, how='outer', on='cliente_id')
merge3.head(10)
 # Note: different merge options with different outcomes in the dataframes

# Exercise 7 - After combining the necessary tables, calculate the total quantity shipped per region.
 # Merge 'fac_venda' and 'dim_cliente' to link hub info 'regiao' and sales 'quantidade'
info_regiao=pd.merge(fac_venda, dim_cliente, how='left', on='cliente_id')
info_regiao.head()
 # Groupby produto 'regiao', identifying the total sum of volume shipped per 'regiao'
quantidade_regiao=info_regiao.groupby('regiao')['quantidade'].sum().reset_index().sort_values("quantidade", ascending=False)
quantidade_regiao.head()

# Exercise 8 - Capacity vs. Hubs Usage, for each hub: Get your daily capacity; Calculate the total volume shipped; Create a column: percentage_used = volume / capacity * 100
# Showcase which hubs are above 50% usage
 # Merge 'dim_produto' and 'fac_venda' to link product and sales info
info_produto_peso=pd.merge(fac_venda,dim_produto, how="inner", on="produto_id")
 # Identify total weight - 'peso_total'
info_produto_peso['peso_total']= info_produto_peso["peso_medio_kg"]*info_produto_peso["quantidade"]
 # Merge info_produto_peso 'dim_hub' to link fac_vendas and dim_produto with dim_hub
hub_capacidade=pd.merge(info_produto_peso,dim_hub, how='inner', on='hub_id')
 # Aggregate only relevant keys and identify sum 'peso_total'
hub_cap_group=hub_capacidade.groupby(['hub_id','hub_nome','capacidade_diaria','data_id'])['peso_total'].sum().reset_index()
 # Calculate and add 'percentual_utilizado'
hub_cap_group['percentual_utilizado']=((hub_cap_group['peso_total']/hub_cap_group['capacidade_diaria'])*100).round(2)
 # Showcase only hubs with percentual_utilizado over 50%
hub_cap_50=hub_cap_group[hub_cap_group['percentual_utilizado']>50].sort_values('percentual_utilizado', ascending=False)
hub_cap_50.head()

# Exercise 9 - Most Shipped Product by Region.
# For each region - South, North, Central. Determine which product category is shipped most by volume.
 # Merge info_produto_peso and dim_cliente
cliente_peso=pd.merge(info_produto_peso, dim_cliente, how='inner', on='cliente_id')
 # Groupby 'regiao', 'categoria' and 'peso_total'
regiao_cat_peso=cliente_peso.groupby(['regiao','categoria'])['peso_total'].sum().reset_index()
 # Identify max value
max=regiao_cat_peso.groupby(['regiao'])['peso_total'].idxmax()
 # Showcase only max
cat_max=regiao_cat_peso.loc[max]
cat_max.head()

# Exercise 10 - Day with Highest Logistics Activity
# Find out which date had the highest total number of shipments (quantity).
 # Merge fac_venda and dim_tempo to relate data_id
data_quantidade=pd.merge(fac_venda, dim_tempo, how='inner', on='data_id')
 # Aggregate 'data' and sum of 'quantidade'
data_quantidade=data_quantidade.groupby('data')['quantidade'].sum().reset_index()
 # Identify max value
data_quantidade.max()
