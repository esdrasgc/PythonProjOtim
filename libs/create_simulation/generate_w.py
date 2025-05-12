from functools import partial
import numpy as np

def gerar_vetores_aleatorios(n):
    return np.random.uniform(0, 0.2, n) ## impura

def gerar_w_valido(n: int = 25, max_tentativas: int = 1000):
    """
    Gera um vetor w válido, ou seja, que soma 1 e tem n elementos e nenhum ativo tem mais de 20% da carteira
    """
    gerar_vetores = partial(gerar_vetores_aleatorios, n)
    for _ in range(max_tentativas):
        valores = gerar_vetores() ## impura

        soma_atual = np.sum(valores)    
        valores_normalizados = valores * (1 / soma_atual)
        
        # Verificar se após normalização todos os valores ainda estão abaixo de 0.2
        if np.all(valores_normalizados <= 0.2):
            return valores_normalizados
