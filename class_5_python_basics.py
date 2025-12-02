import pandas as pd

# Upload dataset
vendas = pd.read_excel("/content/vendas_portugal.xlsx")
vendas.head()

# Brief analysis of the data set
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
- na
'''

# Dataset

"""#Exercicio 3 - Preparação dos Dados"""

#Trata NaN em preco_unitario e quantidade
vendas["quantidade"]=vendas["quantidade"].fillna(vendas['valor_total']/vendas['preco_unitario']) # tirando partido dos valores de outras colunas e mantendo o float
vendas["preco_unitario"]=vendas["preco_unitario"].fillna(vendas['valor_total']/vendas['quantidade']) # tirando partido dos valores de outras colunas e mantendo o float
'''NOTA: opçao + correta seria criar novas colunas com os dados tratados em vez de alterar diretamente as colunas 'quantidade' e 'perco_unitario' '''
#Corrige nomes
vendas["cliente"]=vendas["cliente"].str.strip() # remover espaços no inicio/fim
vendas["cliente"]=vendas["cliente"].str.title() # deixar no formato título
#Corrige cidades
vendas["cidade"]=vendas["cidade"].str.strip() # remover espaços no inicio/fim
vendas["cidade"]=vendas["cidade"].str.title() # deixar no formato título

vendas.info() # para testar/validar improvement
vendas.head() # para testar/validar improvement

#Calcula uma coluna receita = preco_unitario * quantidade * (1 - desconto_percent)
vendas["receita"] = vendas["preco_unitario"] * vendas["quantidade"] * (1 - vendas["desconto_percent"])
#Converte data_venda para datetime
vendas["data_venda"]= pd.to_datetime(vendas["data_venda"])
vendas.head(10)

"""#Exercicio 4 - Modelagem (Análise Exploratória)

"""

#Identificar quantos produtos são e distribuição de valores
produto_count=vendas['produto'].value_counts()
print(produto_count)
#Mostra o top 5 produtos em faturamento total
vendas_top5 = vendas.groupby(["produto"])["receita"].sum().sort_values(ascending=False).reset_index()
vendas_top5.head()

#Cria um gráfico de barras com faturamento por canal de venda - receita por canal de vendas
vendas_canal=vendas.groupby(["canal_venda"])["receita"].sum().reset_index().sort_values("receita", ascending=False)
vendas_canal.head()

vendas_canal.plot(title='Receita por canal de vendas')
vendas_canal.plot.bar()

#identificar quantas cidades e sua distribuição
cidade_count=vendas['cidade'].value_counts()
print(cidade_count)
#Calcula o ticket médio por cidade (receita média por venda)
vendas_cidade_average=vendas.groupby(["cidade"])["receita"].mean().sort_values(ascending=False).reset_index()
vendas_cidade_average.round(2).head(7)

"""#Exercicio 5 - Avaliação

- Qual canal é mais lucrativo?  Online - ver venda_canal.plot em cima
- Há diferenças entre cidades? - Sim, ver valores médios de receita em cada cidade min - Aveiro, max - Coimbra, ver desvios em baixo (.describe)
- O desconto médio afeta a receita? Não, ver matroz de correlação em baixo

"""

#Há diferenças entre cidades?
vendas_cidade_average.describe()

#O desconto medio afeta a receita?
vendas['desconto_medio']=vendas['desconto_percent']/len(vendas['desconto_medio']) # calculo serie desconto medio == mean desconto_percent on vendas.describe()
corr_matrix=vendas[['receita','desconto_medio']].corr() # calculo da matrix de correlação entre Receita e Desconto Medio
corr_matrix.head()

# 0.075 é desprezivel assim não ha correlação

"""# Exercicio 6 - Implantação"""

#satisfacao_cliente é relativo a quê?! produto/cidade/canal venda ?!
#avg_satisfaction cidade:
  #avg_satisfaction=vendas.groupby('cidade')['avaliacao_cliente'].mean().sort_values(ascending=False)
#avg_satisfaction canal venda:
  #avg_satisfaction=vendas.groupby('canal_venda')['avaliacao_cliente'].mean().sort_values(ascending=False)
#avg_satisfaction produto:
  #avg_satisfaction=vendas.groupby('produto')['avaliacao_cliente'].mean().sort_values(ascending=False)

from numpy._core.defchararray import count
#Cria um resumo em DataFrame com: Cidade, Canal mais usado, Faturamento total e Avaliação média dos clientes
#cidade -> already in vendas df
#canal de venda mais usado por cidade (count por cidade)
'''esta metrica tbm pode ser obtida atraves de .mode() -->
  cidade_canal_vendas=vendas.groupby('cidade')['canal_venda'].apply(lambda x: x.mode()).reset_index().drop(columns=['level_1'])'''
cidade_canal_vendas=vendas.groupby('cidade')['canal_venda'].apply(lambda x: x.value_counts().idxmax()).reset_index()
cidade_canal_vendas.head(7)

#receita total por cidade (todos canais)
cidade_receita=vendas.groupby('cidade')['receita'].sum().sort_values(ascending=False).reset_index()
cidade_receita.head(7)

#avaliação media dos clientes (por cidade?!)
avg_city_satisfaction=vendas.groupby('cidade')['avaliacao_cliente'].mean().sort_values(ascending=False).reset_index()
avg_city_satisfaction.head(7)

vendas_resumo=pd.merge(cidade_canal_vendas,cidade_receita, how='inner', on='cidade')
vendas_resumo.head(7)

# Dataframe final
vendas_resumo_final=pd.merge(vendas_resumo,avg_city_satisfaction, how='inner', on='cidade')
vendas_resumo_final.head(7)

# Exportação do ficheito
vendas_resumo_final.to_excel('resumo_vendas__final_portugal.xlsx', index=False)
