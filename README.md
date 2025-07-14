# 📈 Previsão de Retorno Financeiro em Títulos Públicos

Um projeto de machine learning para prever retornos financeiros de investimentos em títulos públicos brasileiros usando regressão linear.

## 🎯 Objetivo

Este projeto implementa um modelo de regressão linear para prever o retorno financeiro de investimentos em títulos públicos com base no valor investido. O sistema oferece duas abordagens distintas: uma usando a biblioteca scikit-learn e outra implementada do zero para fins educacionais.

## 🗂️ Estrutura do Projeto

```
financial-returns-in-government-bonds/
├── README.md                    # Documentação do projeto
├── parte1.py                    # Modelo usando scikit-learn
├── parte2.py                    # Modelo implementado do zero
├── dados/
│   └── dataset.csv             # Dataset com dados históricos
└── imagens/                    # Gráficos e visualizações geradas
    ├── parte1-grafico1.png
    ├── parte1-regressionLine.png
    └── parte1-actualvspredicted.png
```

## 🔧 Tecnologias Utilizadas

**Parte 1 - Framework:**
- Python 3.x
- scikit-learn
- pandas
- numpy
- matplotlib

**Parte 2 - Implementação Manual:**
- Python (apenas bibliotecas nativas)
- csv
- math
- os

## 📊 Funcionalidades

### Parte 1 (parte1.py) - Usando scikit-learn
- ✅ Carregamento e visualização dos dados
- ✅ Divisão treino/teste (70/30)
- ✅ Treinamento do modelo de regressão linear
- ✅ Visualização da linha de regressão
- ✅ Avaliação completa do modelo (MAE, MSE, RMSE, R²)
- ✅ Comparação valores reais vs preditos
- ✅ Predição para novos investimentos

### Parte 2 (parte2.py) - Implementação Manual
- ✅ Cálculo manual de média, covariância e variância
- ✅ Implementação dos coeficientes de regressão (B0, B1)
- ✅ Divisão dos dados (80/20)
- ✅ Predição usando equação linear manual
- ✅ Cálculo do RMSE
- ✅ Predição para novos valores

## 🚀 Como Executar

### Pré-requisitos

1. Python 3.7 ou superior instalado
2. Para a Parte 1, instale as dependências:
```bash
pip install scikit-learn pandas numpy matplotlib
```

### Executando o Projeto

**Parte 1 - Com Framework:**
```bash
python parte1.py
```

**Parte 2 - Sem Framework:**
```bash
python parte2.py
```

## 📋 Dataset

O arquivo `dados/dataset.csv` contém duas colunas:
- **Investimento**: Valor investido em títulos públicos
- **Retorno**: Retorno financeiro obtido

**Formato esperado:**
```csv
Investimento,Retorno
1000,1050
2000,2100
3000,3150
...
```

## 📈 Métricas de Avaliação

O projeto avalia o modelo usando as seguintes métricas:

- **MAE (Mean Absolute Error)**: Erro médio absoluto
- **MSE (Mean Squared Error)**: Erro quadrático médio
- **RMSE (Root Mean Squared Error)**: Raiz do erro quadrático médio
- **R² Score**: Coeficiente de determinação

## 🎨 Visualizações

O sistema gera automaticamente:

1. **Gráfico de dispersão**: Investimento vs Retorno
2. **Linha de regressão**: Visualização do modelo ajustado
3. **Comparação**: Valores reais vs valores preditos

## 💡 Conceitos Implementados

### Regressão Linear
O modelo usa a equação: **y = B1 × x + B0**

Onde:
- **y**: Retorno previsto
- **x**: Valor do investimento  
- **B1**: Coeficiente angular (inclinação)
- **B0**: Intercepto (ponto onde a reta cruza o eixo y)

### Implementação Manual (Parte 2)
- **Covariância**: Medida de dependência linear entre variáveis
- **Variância**: Medida de dispersão dos dados
- **Coeficientes**: Calculados usando fórmulas estatísticas

## 🔮 Fazendo Predições

Ambas as implementações permitem inserir um novo valor de investimento e obter uma predição do retorno esperado:

```
Digite o valor do investimento: 5000
Retorno Previsto: 5250.45
```

## 📚 Propósito Educacional

Este projeto foi desenvolvido para demonstrar:
- Implementação de ML com e sem frameworks
- Conceitos fundamentais de regressão linear
- Avaliação de modelos de machine learning
- Visualização de dados e resultados
- Boas práticas em ciência de dados

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Melhorar a documentação
- Adicionar novos algoritmos
- Otimizar o código existente
- Implementar novas visualizações

## 📄 Licença

Este projeto é de código aberto para fins educacionais.

---

**Nota**: Este é um projeto educacional. Para investimentos reais, consulte sempre um profissional qualificado.
