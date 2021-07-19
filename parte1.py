# Projeto 2 - Prevendo o Retorno Financeiro de Investimentos em Títulos Públicos

# Parte 1 - Desenvolvimento do Modelo Usando Framework

# Imports
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings
warnings.filterwarnings("ignore")

# Carregando o dataset
df = pd.read_csv('dados/dataset.csv')
print("\n")
print('Dados Carregados com Sucesso!')
print('Shape:', df.shape)
print(df.head())

# Visualizando dados
df.plot(x = 'Investimento', y = 'Retorno', style = 'o')
plt.title('Invetimento x Retorno')
plt.xlabel('Investimento')
plt.ylabel('Retorno')
plt.savefig('imagens/parte1-grafico1.png')
plt.show()

# Preparando os dados
X = df.iloc[:, :-1].values    
y = df.iloc[:, 1].values

# Divisão em dados de treino e teste (70/30)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Ajusta o shape e tipo de dados de entrada de treino
X_treino = X_treino.reshape(-1, 1).astype(np.float32)

# Construção do Modelo

# Modelo de regressão linear
modelo = LinearRegression()    

# Treinamento do modelo
modelo.fit(X_treino, y_treino)
print("\n")
print('Modelo Treinado com Sucesso!')

# Imprimindo os coeficientes B0 e B1
print("\n")
print('B1 (coef_) :', modelo.coef_)
print('B0 (intercept_) :', modelo.intercept_)

# Plot da linha de regressão linear
# y =  B1 * X + B0
regression_line = modelo.coef_ * X + modelo.intercept_
plt.scatter(X, y)
plt.title('Invetimento x Retorno')
plt.xlabel('Investimento')
plt.ylabel('Retorno Previsto')
plt.plot(X, regression_line, color = 'red')
plt.savefig('imagens/parte1-regressionLine.png')
plt.show()

# Previsões com dados de teste
y_pred = modelo.predict(X_teste)

# Real x Previsto
df_valores = pd.DataFrame({'Valor Real': y_teste, 'Valor Previsto': y_pred})
print("\n")
print(df_valores)

# Plot
fig, ax = plt.subplots()
index = np.arange(len(X_teste))
bar_width = 0.35
actual = plt.bar(index, df_valores['Valor Real'], bar_width, label = 'Valor Real')
predicted = plt.bar(index + bar_width, df_valores['Valor Previsto'], bar_width, label = 'Valor Previsto')
plt.xlabel('Investimento')
plt.ylabel('Retorno Previsto')
plt.title('Valor Real x Valor Previsto')
plt.xticks(index + bar_width, X_teste)
plt.legend()
plt.savefig('imagens/parte1-actualvspredicted.png')
plt.show()

# Avaliação do modelo
print("\n")
print('MAE (Mean Absolute Error):', mean_absolute_error(y_teste, y_pred))
print('MSE (Mean Squared Error):', mean_squared_error(y_teste, y_pred))
print('RMSE (Root Mean Squared Error):', math.sqrt(mean_squared_error(y_teste, y_pred)))
print('R2 Score:', r2_score(y_teste, y_pred))

# Prevendo retorno para o investimento com novos dados

# Recebendo input via terminal e aplicando aos dados as mesmas transformações aplicadas aos dados de treino
print("\n")
input_inv = input('\nDigite o valor do investimento: ')
input_inv = float(input_inv)
inv = np.array([input_inv])
inv = inv.reshape(-1, 1)

# Previsões
pred_score = modelo.predict(inv)

print("\n")
print("Investimento Realizado = ", input_inv)
print("Retorno Previsto = {:.4}".format(pred_score[0]))
print("\n")

# Fim




