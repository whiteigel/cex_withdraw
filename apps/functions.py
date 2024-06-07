import ccxt


def get_okx_tokens() -> list:
    """
    Получение списка торговых пар с биржи OKX
    :return: список торговых пар
    """
    okx = ccxt.okx()
    try:
        data = okx.fetch_markets()
        pairs = [pair['symbol'] for pair in data]
        return pairs
        # for pair in data:
        #     print(pair['symbol'])
    except ccxt.AuthenticationError as e:
        print("Authentication Error:", e)
    except Exception as e:
        print("An error occurred:", e)


def get_binance_tokens() -> list:
    """
    Получение списка торговых пар с биржи Binance
    :return: список торговых пар
    """
    binance = ccxt.binance()
    try:
        data = binance.fetch_markets()
        pairs = [pair['symbol'] for pair in data]
        return pairs
        # for pair in data:
        #     print(pair['symbol'])
    except ccxt.AuthenticationError as e:
        print("Authentication Error:", e)
    except Exception as e:
        print("An error occurred:", e)


def get_balance_okx(exchange: ccxt.Exchange, token: str) -> None:
    """
    Получение баланса с биржи OKX
    :param apikey: ваш api ключ
    :param secretkey: ваш secret ключ
    :param password: ваш пароль
    :param token: токен для вывода баланса, 'all'-вывод всех балансов токенов
    :return: вывод баланса
    """
    try:
        balance = exchange.fetch_balance(params={'type': 'funding'})
        for key, value in balance['total'].items():
            if key.casefold() == token.casefold() and value > 0:
                print(f'Ваш баланс {key}: {value}')
                return value
            elif token == 'all' and value > 0:
                print(f'Ваш баланс {key}: {value}')
    except ccxt.AuthenticationError as e:
        print("Authentication Error:", e)
    except Exception as e:
        print("An error occurred:", e)


def get_balance(exchange: ccxt.Exchange) -> dict:
    balance = {}

    if exchange.name == 'OKX':
        try:
            balance['funding'] = exchange.fetch_balance(params={'type': 'funding'})
            balance['spot'] = exchange.fetch_balance(params={'type': 'spot'})
        except ccxt.AuthenticationError as e:
            print("Authentication Error:", e)
        except Exception as e:
            print("An error occurred:", e)
    elif exchange.name == 'Bybit':
        try:
            balance['spot'] = exchange.fetch_balance(params={'type': 'spot'})
            balance['FUND'] = exchange.fetch_balance(params={'type': 'FUND'})
        except ccxt.AuthenticationError as e:
            print("Authentication Error:", e)
        except Exception as e:
            print("An error occurred:", e)
    return balance
