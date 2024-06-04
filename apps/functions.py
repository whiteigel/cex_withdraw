import ccxt


def get_okx_tokens() -> list:
    """
    Получение списка торговых пар с биржи OKX
    :return: список торговых пар
    """
    okx = ccxt.okx()
    try:
        data = okx.fetch_markets()
        pairs = [data['symbol'] for data in data]
        return pairs
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
        pairs = [data['symbol'] for data in data]
        return pairs
    except ccxt.AuthenticationError as e:
        print("Authentication Error:", e)
    except Exception as e:
        print("An error occurred:", e)


def get_balance(apikey: str, secretkey: str, password: str) -> None:
    """
    Получение баланса с биржи OKX
    :param apikey: ваш api ключ
    :param secretkey: ваш secret ключ
    :param password: ваш пароль
    :return: вывод баланса
    """
    params = {
        'type': 'funding'
    }

    okx = ccxt.okx({
        'apiKey': apikey,
        'secret': secretkey,
        'password': password
    })
    try:
        balance = okx.fetch_balance(params=params)
        for key, value in balance['total'].items():
            if value > 0:
                print(f'Ваш баланс {key}: {value}')
    except ccxt.AuthenticationError as e:
        print("Authentication Error:", e)
    except Exception as e:
        print("An error occurred:", e)
