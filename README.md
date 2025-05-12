# Otimização de Carteira de Investimentos

Este projeto implementa um sistema de otimização de carteira de investimentos utilizando o índice Sharpe para encontrar a melhor combinação de ativos do Dow Jones.

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd PythonProjOtim
```

2. Crie um ambiente virtual Python:
```bash
python3.12 -m venv env
source env/bin/activate  # No Windows: env\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Executar

Execute o script principal para iniciar a simulação de otimização:

```bash
python main.py
```

O script irá:
1. Baixar dados históricos das ações do Dow Jones
2. Calcular matrizes de retorno percentual e volatilidade
3. Simular diferentes combinações de carteiras com 25 ativos
4. Calcular o índice Sharpe para cada combinação
5. Encontrar a carteira com o melhor índice Sharpe
6. Salvar os resultados em `resultados_simulacao.txt`

## Requisitos e Dependências

- Python 3.12.9
- Principais bibliotecas:
  - numpy: Operações com matrizes e cálculos numéricos
  - pandas: Manipulação de dados e séries temporais
  - yfinance: Download de dados históricos de ações
  - multiprocessing: Processamento paralelo para otimização

Para a lista completa de dependências, consulte o arquivo `requirements.txt`.

## Resultados Esperados

Após a execução, o programa gera um arquivo `resultados_simulacao.txt` contendo:

- Valor máximo do índice Sharpe encontrado
- Índice da carteira ótima
- Quais ativos compõem a carteira ótima (por índices)
- Os pesos ótimos para cada ativo na carteira

### Exemplo de Resultado

```
Max Sharpe Ratio: 2.9131323567925227
Carteiras: ['AMZN', 'PG', 'CAT', 'MRK', 'AXP', 'HON', 'MCD', 'CSCO', 'UNH', 'AMGN', 'VZ', 'CRM', 'NKE', 'HD', 'JNJ', 'NVDA', 'IBM', 'SHW', 'MSFT', 'V', 'JPM', 'BA', 'WMT', 'AAPL', 'TRV']
Pesos correspondentes: [0.02759261 0.02857444 0.07629749 0.05379341 0.045389   0.06555456
 0.0834639  0.06953114 0.07264235 0.01287522 0.06229837 0.01324291
 0.04508432 0.03556664 0.00949264 0.04126969 0.02482889 0.04280196
 0.05672892 0.0174913  0.00904574 0.02721361 0.06575692 0.00731567
 0.00614831]
```

### Desempenho

A execução completa do script levou aproximadamente 8 minutos (473.92 segundos) para processar todas as combinações possíveis e encontrar a carteira ótima, utilizando um ryzen 7 2700X. O tempo pode variar dependendo do hardware utilizado.

## Observações

- O projeto realiza otimização de carteira considerando as restrições de que nenhum ativo pode ter peso superior a 20%
- A simulação utiliza processamento paralelo para otimizar o tempo de execução
- O índice Sharpe é calculado usando a taxa livre de risco padrão de 0
- Os dados são obtidos do Yahoo Finance para o período especificado
