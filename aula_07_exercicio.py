# Import dataset
import pandas as pd
fato_funcionarios = pd.read_csv("/content/fato_funcionarios_dataset.csv")

# Exercise 1
# Data Understanding
fato_funcionarios.head(20)
fato_funcionarios.info() # this function .info() give us the not only the amount of entries but also Data Type
'''or .shape[0] function -> fato_funcionarios.shape[0]
 or len(df) function -> len(fato_funcionarios)'''
# Data types - these info can be also checked on .info() function
fato_funcionarios.dtypes
# Brief Data Preparation
fato_funcionarios["Departamento"]=fato_funcionarios["Departamento"].str.strip() # remover empty spaces
fato_funcionarios["Cargo"]=fato_funcionarios["Cargo"].str.title() # Title format

# Exercise 2 -  Counting employees by department
# Using groupby, display how many employees are in each department
    # 'Departamento' / count 'FuncionarioID'
fun_depart=fato_funcionarios.groupby('Departamento')['FuncionarioID'].count().sort_values(ascending=False).reset_index()
fun_depart.head()
'''NOTE: .nunique() -> return the count of unique values !!'''
#fun_depart=fato_funcionarios.groupby('Departamento')['FuncionarioID'].nunique().sort_values(ascending=False).reset_index()

# Exercise 3 - Total Cost per Month (Time Period Analysis)
# Group the data by Year and Month, calculate - Sum of Total Cost
# Create a line graph showing the monthly evolution
    # Group 'Ano' and 'Mes' and calculate 'Custo_Total' - sum
group_ano_mes=fato_funcionarios.groupby(['Ano','Mes'])['Custo_Total'].sum().reset_index()
group_ano_mes.head()
    # to plot 'Custo_Total' each 'Mes' of each 'Ano' need to convert 'Ano' and 'Mes' into date
    # concatenate 'Ano' + 'Mes' and then turn into Data Time -> pd.to_datetime function
group_ano_mes['Data']=pd.to_datetime(group_ano_mes["Ano"].astype(str) + "-" + group_ano_mes["Mes"].astype(str))
group_ano_mes.head(25)
    # import libraries
import numpy as np # Import Numpy - Numerical Python adding Array capabilities
import matplotlib as mpl # Import Matplotlib library
import matplotlib.pyplot as plt # Import Matplotlib submodule Pyplot
import matplotlib.dates as mdates # Import the dates module to support more detailed graph on x-axis
 # plot line graph
plt.figure(figsize=(10,5))
''' NOTE: marker to see data points for clarity: '.';'o';'x'
- add colour to the graph: color='darkblue'
- add colour to the dot's fill: markerfacecolor='yellow'
- add colour to the dot's outline: markeredgecolor='red'
- line thickness:  linewidth=3 '''
plt.plot(group_ano_mes['Data'],group_ano_mes['Custo_Total'], marker='.', color='darkblue', linewidth=3, markerfacecolor='r',markeredgecolor='y')
    # Get the current axis
ax = plt.gca()
    # Set the locator to show every month (interval=1 means every 1 month)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    # %Y = Year (2023), %m = Month number, %b = Month name (Jan)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
    # Rotate the dates so they don't overlap
plt.xticks(rotation=45)
'''NOTE:Adding graph annotations - values. In line graph there's no quick options (only for loops) neither on Matlplotlib nor Seaborn (only for Bar charts)'''
plt.title("Custo Total Mes/Ano")
plt.xlabel("Mes")
plt.ylabel("Custo_Total")
plt.show()

# Exercise 4 - Average Salary by Department
# Calculate the average salary in each department.
# Bar chart illustrating the comparison.
    # 'Departamento' / average 'Salario'
sal_medios=fato_funcionarios.groupby('Departamento')['Salario'].mean().sort_values(ascending=False).reset_index()
sal_medios.head()
    # Using Matplotlib
plt.figure(figsize=(10,5))
'''NOTE: add colour to the graph: color='darkblue'
- add colour to the edge: edgecolor='g'
- define border line thickness: linewidth=2
- define bar thickness: width=8 NOTE: there's no such thing of spacing in bar charts, only bar width if you want bars touching (meaning no gap) width=1'''
bar_ant=plt.bar(sal_medios['Departamento'],sal_medios['Salario'], color='darkblue', edgecolor='g', linewidth=4, width=0.8)
    # get axes to labels
ax = plt.gca()
    # adding data annotations
ax.bar_label(bar_ant, fmt='%.2f', padding=1)
    # Zoom in on the bar chart to better identify differences in values
plt.ylim(8200, 10000)
plt.title("Salario Medio / Departamento")
plt.show()

    # Using Seaborn - leveraging other library
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
    # The Plotting - Seaborn handles the DataFrame mapping
ax = sns.barplot(data=sal_medios, x='Departamento', y='Salario', color='darkblue', edgecolor='green', linewidth=4, width=1)
    # The Labelx - grab the "container" from the axis (Slightly different in Seaborn)
ax.bar_label(ax.containers[0], fmt='%.2f', padding=1)
    # The Settings - Standard Matplotlib
plt.ylim(8200, 10000)
plt.title("Salario Medio / Departamento")
plt.show()

# Exercise 5 - Analysis of the impact of bonuses by area
# Calculate: Average bonuses per department; Sum of bonuses per department
# Comparing bar chart.
    # average 'Bonus' / 'Departamento'
bonus_dep_mean=fato_funcionarios.groupby('Departamento')['Bonus'].mean().sort_values(ascending=False).reset_index()
bonus_dep_mean.head()
    # sum 'Bonus' / 'Departamento'
bonus_dep_sum=fato_funcionarios.groupby('Departamento')['Bonus'].sum().sort_values(ascending=False).reset_index()
bonus_dep_sum.head()
    # Ploting Bar chart
plt.figure(figsize=(12,6))
bar_sum=plt.bar(bonus_dep_sum['Departamento'],bonus_dep_sum['Bonus'], color='green', edgecolor='black', linewidth=1, width=0.8, label='Sum Bonus - Total') # blue series
bar_mean=plt.bar(bonus_dep_mean['Departamento'],bonus_dep_mean['Bonus'], color='darkblue', edgecolor='black', linewidth=1, width=0.8, label='Mean') # green series
ax = plt.gca()
ax.bar_label(bar_sum, fmt='%.2f', padding=1)
ax.bar_label(bar_mean, fmt='%.2f', padding=1)
plt.title("Bonus Medio/Bonus Total - Departamento")
plt.legend()
plt.show()

'''NOTE:Delta between data series too high'''
    # Try other variance of this exercise to have other view using Bonus Max value per Department
    # Max 'Bonus' / 'Departamento'
bonus_dep_max=fato_funcionarios.groupby('Departamento')['Bonus'].max().sort_values(ascending=False).reset_index()
bonus_dep_max.head()
    # Plot Bar Masx 'Bonus' / 'Departamento' -> add annotations to the bar series
plt.figure(figsize=(12,6))
bar_max=plt.bar(bonus_dep_max['Departamento'],bonus_dep_max['Bonus'], label='Max',  color='green', edgecolor='black', linewidth=1, width=0.8)
bar_mean=plt.bar(bonus_dep_mean['Departamento'],bonus_dep_mean['Bonus'], label='Mean',  color='darkblue', edgecolor='black', linewidth=1, width=0.8)
ax = plt.gca()
ax.bar_label(bar_max, fmt='%.2f', padding=2)
ax.bar_label(bar_mean, fmt='%.2f', padding=2)
plt.title("Bonus Medio / Bonus Max - Departamento")
plt.ylim(1500, 5200)
plt.legend()
plt.show()

# Exercise 6 — Create a histogram using matplotlib showing the absenteeism distribution.
    # Histogram
plt.figure(figsize=(10, 5))
    # Forcing showcasing all x-axis values
min_val = fato_funcionarios['Absenteismo'].min()
max_val = fato_funcionarios['Absenteismo'].max()
    # Using bins
bins = np.arange(min_val - 0.5, max_val + 1.5, 1)
plt.hist(fato_funcionarios['Absenteismo'], bins=bins, color='orange', edgecolor='black', width=1)
plt.xlabel('Number of Absence Days')
plt.ylabel('Frequency')
plt.title('Distribution of Absence Days')
    # Forcing min y-axis value 8 (to zoom in)
plt.ylim(8,)
plt.xticks(range(min_val, max_val + 1))
plt.show()

# Exercise 7 - Relationship between salary and bonus. Create a scatterplot: x-axis = Salary;  y-axis = Bonus
    # And answer whether there is any visual correlation.
plt.figure(figsize=(10,5))
plt.scatter(fato_funcionarios['Salario'],fato_funcionarios['Bonus'])
plt.title("Salario vs Bonus")
plt.xlabel("Salario")
plt.ylabel("Bonus")
plt.show()
    #there's no clear visual clustering, therefore we could say there's no visual correlation

# Exercise 8 — Month with the highest total cost.
# Using groupby, identify the month and year with the highest aggregate total cost. Show the value found.
    # group_ano_mes dataframe that aggregate 'Ano' and 'Mes'
max_index=group_ano_mes['Custo_Total'].idxmax()
max_total_cost=group_ano_mes.loc[max_index, 'Data']
valor_total=group_ano_mes['Custo_Total'].max()
print(f'A data com maior custo total é {max_total_cost} no valor de {valor_total}')
    # Visual confirmation through bar chart
plt.figure(figsize=(20,5))
bar_custo_total=sns.barplot(group_ano_mes, x="Data", y="Custo_Total")
bar_custo_total.bar_label(bar_custo_total.containers[0])
plt.xticks(rotation=45)
plt.show()

# Exercise 9 — Analysis of hours worked by department (boxplot).
# Create a boxplot with Matplotlib: x-axis = 'Departmento'; y-axis = 'Horas_Trabalhadas'
sns.boxplot(fato_funcionarios, x='Departamento', y='Horas_Trabalhadas')
plt.show()

# Exercise 10  — Final Report
# Based on your previous analyses, answer: Which area spends the most on personnel throughout the year? - use sum of 'Custo_Total' per 'Departamento'
# Write a short paragraph with the conclusion.
    # Identify which 'Departamento' spent more
dep_spent=fato_funcionarios.groupby('Departamento')['Custo_Total'].sum().sort_values(ascending=False).reset_index()
dep_spent.head(20)
dep_spent_year=fato_funcionarios.groupby(['Departamento','Ano'])['Custo_Total'].sum().sort_values(ascending=False).reset_index()
dep_spent_year.head(20)
    # Visual analysis on which 'Departamento' spent more
plt.figure(figsize=(10,5))
    # hue its necessary to split dataframe into years - 'Ano'
custo_dep=sns.barplot(data=dep_spent_year, x="Departamento", y="Custo_Total", hue="Ano", palette='dark:blue', edgecolor='black', linewidth=1, width=0.8)
    # Needed to add value annotations on both series - 2023 and 2024
for container in custo_dep.containers:
    custo_dep.bar_label(container, fmt='%.0f', padding=3)
plt.legend(title='Ano')
plt.ylim(150000,)
plt.show()
"""Department that spent the most:
- Marketing: 2023
- Finance: 2024"""
