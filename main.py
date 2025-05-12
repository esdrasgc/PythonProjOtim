import numpy as np
from functools import partial
from multiprocessing import Pool
from itertools import combinations

from libs.create_simulation.sharpes import calcular_n_sharpes_da_carteira
from libs.load_data.dow_jones import download_dow_jones_data
from libs.matrix_manipulation.create import calculate_matrix_of_percentual_change, calculate_matrix_of_volatility
from libs.utils.timer import timer_func

@timer_func
def test():
    # Carregar os dados
    tickers = [
        "UNH", "GS", "MSFT", "HD", "V", "SHW", "MCD", "CAT", "AMGN", "AXP",
        "TRV", "CRM", "IBM", "JPM", "AAPL", "HON", "AMZN", "PG", "BA", "JNJ",
        "CVX", "MMM", "NVDA", "WMT", "DIS", "MRK", "KO", "CSCO", "NKE", "VZ"
    ]
    df = download_dow_jones_data(start_date="2024-08-01", end_date="2024-12-31")

    # Calcular a matriz de retornos percentuais e a matriz de volatilidade
    r = calculate_matrix_of_percentual_change(df)
    sigma = calculate_matrix_of_volatility(r)

    ## sample teste
    indices_teste = [np.random.choice(r.shape[1], size=25, replace=False) for _ in range(1000)]
    calcular_n_sharpes_dos_indices = partial(calcular_n_sharpes_da_carteira, r=r, sigma=sigma)
    print("Iniciando as simulações em paralelo do sharpe ratio otimizado...")
    result = Pool().map(calcular_n_sharpes_dos_indices, indices_teste)

    ## calcular sharpe final e retornar as informações da carteira e dos pesos usados
    max_sharpe = max(result, key=lambda x: x[0])
    max_index = result.index(max_sharpe)
    print(f"Max Sharpe Ratio: {max_sharpe[0]}")
    print(f"Carteiras: {[tickers[i] for i in indices_teste[max_index]]}")
    print(f"Pesos correspondentes: {result[max_index][1]}")

@timer_func
def main():
    tickers = [
        "UNH", "GS", "MSFT", "HD", "V", "SHW", "MCD", "CAT", "AMGN", "AXP",
        "TRV", "CRM", "IBM", "JPM", "AAPL", "HON", "AMZN", "PG", "BA", "JNJ",
        "CVX", "MMM", "NVDA", "WMT", "DIS", "MRK", "KO", "CSCO", "NKE", "VZ"
    ]
    # Carregar os dados
    df = download_dow_jones_data(start_date="2024-08-01", end_date="2024-12-31")

    # Calcular a matriz de retornos percentuais e a matriz de volatilidade
    r = calculate_matrix_of_percentual_change(df)
    sigma = calculate_matrix_of_volatility(r)

    ## sample teste
    indices_carteiras = list(combinations(range(r.shape[1]), 25))
    calcular_n_sharpes_dos_indices = partial(calcular_n_sharpes_da_carteira, r=r, sigma=sigma)

    print("Iniciando as simulações em paralelo do sharpe ratio otimizado...")
    result = Pool().map(calcular_n_sharpes_dos_indices, indices_carteiras)

    ## calcular sharpe final e retornar as informações da carteira e dos pesos usados
    max_sharpe = max(result, key=lambda x: x[0])
    max_index = result.index(max_sharpe)

    print(f"Max Sharpe Ratio: {max_sharpe[0]}")
    print(f"Carteiras: {[tickers[i] for i in indices_carteiras[max_index]]}")
    print(f"Pesos correspondentes: {result[max_index][1]}")
    with open("resultados_simulacao.txt", "w") as f:
        print(f"Max Sharpe Ratio: {max_sharpe[0]}")
        print(f"Carteiras: {[tickers[i] for i in indices_carteiras[max_index]]}")
        print(f"Pesos correspondentes: {result[max_index][1]}")
if __name__ == "__main__":
    test()