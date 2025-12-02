import pandas as pd

# Upload Dataset
vendas = pd.read_excel("/content/vendas_portugal.xlsx")
vendas.head()

#1 Data Understanding
vendas.info()
vendas.describe()
'''
Null values:
- x3 'cidade'
- x5 'preco_unitario'; 'quantidade'; 'desconto_percent'
Inconsistencies:
- 'quantidade'; 'portes' as float instead of integer
- 'cidade' and 'distrito' sometimes not matching
- 'produto' and 'categoria' sometimes not matching
Outliers:
- NA
'''

#2 Brief Data Preparation
  # Clean NaN on 'preco_unitario' and 'quantidade'
vendas["quantidade"]=vendas["quantidade"].fillna(vendas['valor_total']/vendas['preco_unitario']) 
vendas["preco_unitario"]=vendas["preco_unitario"].fillna(vendas['valor_total']/vendas['quantidade'])
'''NOTE: It would be wiser/better to create new columns, transforming existing columns to fill the gaps
and correct the dataset data quality '''
  # Correct/transform client names - 'client'
vendas["cliente"]=vendas["cliente"].str.strip()
vendas["cliente"]=vendas["cliente"].str.title()
  # Corret cities name - 'cidade'
vendas["cidade"]=vendas["cidade"].str.strip() # remover espaços no inicio/fim
vendas["cidade"]=vendas["cidade"].str.title() # deixar no formato título
  # Check corrections
vendas.info()
vendas.head()

# Identify sales aka 'receita' --> 'receita' = preco_unitario * unitario * (1-desconto_percent) 
vendas["receita"] = vendas["preco_unitario"] * vendas["quantidade"] * (1 - vendas["desconto_percent"])
# Convert 'data_venda' to datetime type
vendas["data_venda"]= pd.to_datetime(vendas["data_venda"])
vendas.head(10)

#3 Data Modelling
  # Identify how many different products exist in the dataset and respective distribution
produto_count=vendas['produto'].value_counts()
print(produto_count)

  # Showcase top 5 products in sales
vendas_top5 = vendas.groupby(["produto"])["receita"].sum().sort_values(ascending=False).reset_index()
vendas_top5.head()

  # Plot a bar chart with all sales per sales channel - 'receita' per 'canal_venda'
vendas_canal=vendas.groupby(["canal_venda"])["receita"].sum().reset_index().sort_values("receita", ascending=False)
vendas_canal.head() # just to check needed data
vendas_canal.plot(title='Receita por canal de vendas')
vendas_canal.plot.bar()

  # Identify how many different cities exist in the dataset and respective distribution
cidade_count=vendas['cidade'].value_counts()
print(cidade_count)

  # Identify the average amount per sale per city - aka mean 'receita' per 'cidade'
vendas_cidade_average=vendas.groupby(["cidade"])["receita"].mean().sort_values(ascending=False).reset_index()
vendas_cidade_average.round(2).head(7)

#4 Evaluation
'''
- Which channel is more profitable? Online - see sales_channel.plot (above)
- Are there differences in revenue between cities? - Yes, see average revenue values ​​in each city (min - Aveiro, max - Coimbra), see deviations below with .describe() function
- Does the average discount affect revenue? No, see the correlation matrix below
'''
  # Differences in revenue between cities
vendas_cidade_average.describe()

  # Average discount affect revenue?
vendas['desconto_medio']=vendas['desconto_percent']/len(vendas['desconto_medio']) # identify  average discount == mean 'desconto_percent' on vendas.describe()
corr_matrix=vendas[['receita','desconto_medio']].corr() # correlation da matrix between 'receita' and 'deconto_medio'
corr_matrix.head()
'''Note: correlation == 0.075, so we can say there's no correlation'''

#5 Deployment
  # Create a dataframe summary entailing: city; most used channel; total revenue; and average client satisfaction

from numpy._core.defchararray import count
  # Most used sales channel per city (count # of sales per channel)
cidade_canal_vendas=vendas.groupby('cidade')['canal_venda'].apply(lambda x: x.value_counts().idxmax()).reset_index()
cidade_canal_vendas.head(7)

  # Total revenue per city - total 'receita' per 'cidade' (all channels)
cidade_receita=vendas.groupby('cidade')['receita'].sum().sort_values(ascending=False).reset_index()
cidade_receita.head(7)

  # Average client satisfaction (per city)
avg_city_satisfaction=vendas.groupby('cidade')['avaliacao_cliente'].mean().sort_values(ascending=False).reset_index()
avg_city_satisfaction.head(7)

vendas_resumo=pd.merge(cidade_canal_vendas,cidade_receita, how='inner', on='cidade')
vendas_resumo.head(7)

  # Final Dataframe
vendas_resumo_final=pd.merge(vendas_resumo,avg_city_satisfaction, how='inner', on='cidade')
vendas_resumo_final.head(7)

  # File export as .xlsx
vendas_resumo_final.to_excel('resumo_vendas__final_portugal.xlsx', index=False)
