# Projeto 2 - Prevendo o Retorno Financeiro de Investimentos em Títulos Públicos

# Parte 2 - Desenvolvimento do Modelo Sem Uso de Framework

# Imports
from os import getcwd
from math import sqrt
from csv import reader, writer

# Obtém o caminho do diretório atual
path = getcwd()

# Função para o cálculo da média
def mean(values):
	return sum(values) / float(len(values))

# Função para o cálculo da covariância
# Em teoria da probabilidade e na estatística, a covariância, ou variância conjunta, é uma medida do grau de interdependência (ou inter-relação) 
# numérica entre duas variáveis aleatórias. Assim, variáveis independentes têm covariância zero.
# A covariância ou variância conjunta é um momento conjunto de primeira ordem das variáveis aleatórias X e Y, centrados nas respectivas médias. 
# É a média do grau de interdependência ou inter-relação numérica linear entre elas.
# A covariância é por vezes chamada de medida de dependência linear entre as duas variáveis aleatórias.
# A covariância entre duas variáveis pode ser obtida de dados de variância.
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

# Função para o cálculo da variância
# Na teoria da probabilidade e na estatística, a variância de uma variável aleatória ou processo estocástico é uma medida da sua dispersão estatística, indicando 
# "o quão longe" em geral os seus valores se encontram do valor esperado.
def variance(list, mean):
	return sum([(x - mean)**2 for x in list])

# Função para o cálculo dos coeficientes
def coefficient(covar, var, mean_x, mean_y):
	b1 = covar / var
	b0 = mean_y - (b1 * mean_x)
	return b1, b0

# Função para carregar o dataset
def carrega_dados(dataset):
	init = 0
	x = list()
	y = list()
	with open(dataset) as file:
		content = reader(file)
		for row in content:
			if init == 0:
				init = 1
			else:
				x.append(row[0])
				y.append(row[1])
	return x, y

# Função para divisão dos dados
def split_dataset(x, y):

	x_treino = list()
	y_treino = list()
	x_teste = list()
	y_teste = list()

	training_size = int(.8 * len(x))

	x_treino, x_teste = x[0:training_size], x[training_size::]
	y_treino, y_teste = y[0:training_size], y[training_size::]

	return x_treino, y_treino, x_teste, y_teste

# Função para calcular a equação (y = B1 * x + B0) 
def predict(b0, b1, teste_x):
	predicted_y = list()
	for i in teste_x:
		predicted_y.append(b0 + b1 * i)
	return predicted_y

# Função para calcular o RMSE
def rmse(predicted_y, test_y):
	error = 0.0
	for i in range(len(predicted_y)):
		sum_error = (predicted_y[i] - test_y[i]) ** 2
	return sqrt(sum_error / float(len(test_y)))

# Bloco principal de execução
def main():
	try:

		# Carrega o dataset
		dataset = path + "/dados/dataset.csv"
		x, y = carrega_dados(dataset)

		# Prepara os dados
		x = [float(i) for i in x]
		y = [float(i) for i in y]	

		# Calcula os valores médios de x e y, covariância e variância	
		mean_x = mean(x)
		mean_y = mean(y)
		covar = covariance(x, mean_x, y, mean_y)
		var = variance(x, mean_x)

		# Divide os dados em x e y
		x_treino, y_treino, x_teste, y_teste = split_dataset(x, y)			

		# Calcula os coeficentes (treinamento do modelo)
		b1, b0 = coefficient(covar, var, mean_x, mean_y)
		
		# Imprimindo os coeficientes B1 e B0 
		print("\nCoeficientes")
		print('B1:', b1)
		print('B0:', b0)

		# Previsões com o modelo (coeficentes)
		predicted_y = predict(b0, b1, x_teste)

		# Erro do modelo
		root_mean = rmse(predicted_y, y_teste)

		# Print
		print("\nModelo de Regressão Linear Sem o Uso de Framework")
		print("Erro Médio do Modelo: {}\n".format(root_mean))

		# Novos dados
		novo_x = int(input("Digite o Valor do Investimento: "))

		# Previsões
		novo_y = b0 + b1 * novo_x
		print("\nRetorno Previsto: {}".format(novo_y))
		print("\n")
		
	except Exception as a:
		print(a)

# Execução do bloco main
main()

# Fim


	
