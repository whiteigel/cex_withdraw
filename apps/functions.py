import ccxt


def get_okx_tokens() -> list:
    okx = ccxt.okx()
    data = okx.fetch_markets()
    pairs = [data['symbol'] for data in data]
    return pairs


def get_binance_tokens() -> list:
    binance = ccxt.binance()
    data = binance.fetch_markets()
    pairs = [data['symbol'] for data in data]
    return pairs
