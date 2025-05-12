import yfinance as yf
import pathlib
import numpy as np

def download_dow_jones_data(start_date: str = "2024-08-01", end_date:str = "2024-12-31") -> np.ndarray:
    tickers = [
        "UNH", "GS", "MSFT", "HD", "V", "SHW", "MCD", "CAT", "AMGN", "AXP",
        "TRV", "CRM", "IBM", "JPM", "AAPL", "HON", "AMZN", "PG", "BA", "JNJ",
        "CVX", "MMM", "NVDA", "WMT", "DIS", "MRK", "KO", "CSCO", "NKE", "VZ"
    ]

    # Baixa todos os dados
    raw_data = yf.download(tickers, start=start_date, end=end_date)

    # Filtra apenas a parte "Close"
    return raw_data["Close"].copy()